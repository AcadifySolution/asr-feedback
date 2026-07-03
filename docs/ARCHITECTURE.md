# System Architecture

> **Document Version:** 2.3.0 | **Last Updated:** 2026-07-01 | **Author:** ASR Engineering Team

---

## Table of Contents

- [Overview](#overview)
- [Design Principles](#design-principles)
- [High-Level Architecture](#high-level-architecture)
- [Component Deep Dive](#component-deep-dive)
- [Data Flow](#data-flow)
- [Integration Architecture](#integration-architecture)
- [Scalability & Performance](#scalability--performance)
- [Security Architecture](#security-architecture)
- [Technology Stack](#technology-stack)

---

## Overview

The ASR Feedback Intelligence Platform is designed as a **modular, event-driven system** that ingests AI-generated responses, orchestrates multi-dimensional evaluation through our 4-Pillar methodology, and produces structured intelligence outputs. The architecture prioritizes **auditability**, **schema integrity**, and **extensibility** — ensuring that every feedback entry is traceable, validated, and actionable.

---

## Design Principles

| Principle | Description |
|---|---|
| **Schema-First** | Every data entity is defined by a formal JSON Schema before any code is written. The schema is the contract. |
| **Immutable Audit Trail** | Every feedback entry, score, and decision is logged immutably. Nothing is silently overwritten. |
| **Separation of Concerns** | Ingestion, evaluation, scoring, storage, and reporting are independent, composable services. |
| **Backward Compatibility** | Schema changes are additive by default. Breaking changes trigger major version bumps with migration paths. |
| **Defense in Depth** | Security is layered — input validation, schema enforcement, access controls, PII detection, and audit logging. |
| **Human-in-the-Loop** | The system augments human evaluators, never replaces them. Every automated signal is reviewed by a calibrated analyst. |

---

## High-Level Architecture

```mermaid
graph TB
    subgraph "Client Integration Layer"
        direction LR
        CL1["Client AI System<br/>(LLM / Agent / AGI)"]
        CL2["Client Dashboard"]
        CL3["Client SDK<br/>(Python / JS)"]
    end

    subgraph "API Gateway"
        AG["API Gateway<br/>Rate Limiting · Auth · Routing"]
    end

    subgraph "Ingestion Service"
        IS1["Request Validator"]
        IS2["Schema Enforcer"]
        IS3["Response Queue<br/>(Priority-Based)"]
    end

    subgraph "Evaluation Engine"
        direction TB
        EE1["Session Manager"]
        EE2["Evaluator Assignment"]
        EE3["4-Pillar Analysis Module"]
        
        subgraph "4-Pillar Analysis"
            direction LR
            P1["✅ Good<br/>Signal Extractor"]
            P2["❌ Bad<br/>Signal Detector"]
            P3["📘 Learning<br/>Capture Engine"]
            P4["🧠 Memory<br/>Persistence Layer"]
        end
    end

    subgraph "Quality Assurance Layer"
        QA1["Quality Scoring Engine<br/>(Composite 0-100)"]
        QA2["Inter-Rater Calibration"]
        QA3["Anomaly Detector"]
    end

    subgraph "Data Store"
        DS1["Feedback Store<br/>(Schema-Validated)"]
        DS2["Session Store"]
        DS3["Memory Store<br/>(Persistent Rules)"]
        DS4["Audit Log<br/>(Immutable)"]
    end

    subgraph "Intelligence Layer"
        IL1["Trend Analyzer"]
        IL2["Pattern Detector"]
        IL3["Benchmark Engine"]
        IL4["Insight Extractor"]
    end

    subgraph "Reporting Service"
        RS1["Report Generator"]
        RS2["Dashboard API"]
        RS3["Export Engine"]
    end

    CL1 --> AG
    CL3 --> AG
    AG --> IS1
    IS1 --> IS2
    IS2 --> IS3
    IS3 --> EE1
    EE1 --> EE2
    EE2 --> EE3
    EE3 --> P1 & P2 & P3 & P4
    P1 & P2 & P3 & P4 --> QA1
    QA1 --> QA2
    QA2 --> QA3
    QA3 --> DS1
    EE1 --> DS2
    P4 --> DS3
    DS1 & DS2 & DS3 --> DS4
    DS1 --> IL1 & IL2 & IL3 & IL4
    IL1 & IL2 & IL3 & IL4 --> RS1
    RS1 --> RS2
    RS2 --> CL2
    RS1 --> RS3

    style CL1 fill:#4A90D9,stroke:#2C5F8A,color:#fff
    style AG fill:#95A5A6,stroke:#7F8C8D,color:#fff
    style EE3 fill:#7B68EE,stroke:#5B4ACE,color:#fff
    style QA1 fill:#E67E22,stroke:#C76B18,color:#fff
    style DS1 fill:#2ECC71,stroke:#1FA855,color:#fff
    style IL1 fill:#E74C3C,stroke:#C0392B,color:#fff
    style RS1 fill:#9B59B6,stroke:#8E44AD,color:#fff
```

---

## Component Deep Dive

### 1. Client Integration Layer

The entry point for all client interactions. Supports multiple integration patterns:

```mermaid
graph LR
    subgraph "Integration Patterns"
        A["REST API<br/>Direct HTTP"] --> GW["API Gateway"]
        B["Python SDK<br/>Typed Client"] --> GW
        C["JavaScript SDK<br/>Browser/Node"] --> GW
        D["Webhook<br/>Push-Based"] --> GW
        E["Batch Upload<br/>File-Based"] --> GW
    end
    
    style GW fill:#95A5A6,stroke:#7F8C8D,color:#fff
```

| Pattern | Use Case | Latency | Volume |
|---|---|---|---|
| REST API | Real-time, single-entry submission | < 200ms | Low-Medium |
| Python SDK | Programmatic integration, pipelines | < 200ms | Medium-High |
| JavaScript SDK | Browser dashboards, web apps | < 200ms | Low-Medium |
| Webhook | Event-driven, automated triggers | Async | Medium |
| Batch Upload | Historical data, bulk migration | Async | High |

---

### 2. Ingestion Service

Responsible for receiving, validating, and queuing AI responses for evaluation.

```mermaid
sequenceDiagram
    participant Client
    participant Gateway as API Gateway
    participant Validator as Request Validator
    participant Schema as Schema Enforcer
    participant Queue as Response Queue

    Client->>Gateway: POST /api/v2/responses
    Gateway->>Gateway: Authenticate & Rate Limit
    Gateway->>Validator: Forward Request
    Validator->>Validator: Validate Required Fields
    
    alt Validation Failed
        Validator-->>Client: 400 Bad Request + Error Details
    end
    
    Validator->>Schema: Validate Against JSON Schema
    Schema->>Schema: Enforce feedback-entry.schema.json
    
    alt Schema Validation Failed
        Schema-->>Client: 422 Unprocessable Entity + Schema Errors
    end
    
    Schema->>Queue: Enqueue (Priority-Based)
    Queue-->>Client: 202 Accepted + Entry ID
    
    Note over Queue: Priority based on:<br/>1. Client SLA tier<br/>2. Severity estimate<br/>3. FIFO within tier
```

**Key Design Decisions:**

- **Asynchronous Processing:** Responses are queued for evaluation, not processed synchronously. This decouples ingestion throughput from evaluation capacity.
- **Schema Enforcement at Ingestion:** Invalid data is rejected immediately — malformed entries never enter the evaluation pipeline.
- **Priority Queuing:** Enterprise clients with critical SLAs receive priority evaluation without starving standard-tier clients.

---

### 3. Evaluation Engine

The core of the platform — where AI responses are analyzed through our 4-Pillar methodology.

```mermaid
graph TB
    subgraph "Evaluation Engine"
        SM["Session Manager"]
        EA["Evaluator Assignment<br/>Skill Matching · Load Balancing"]
        
        subgraph "4-Pillar Analysis Module"
            direction TB
            
            subgraph "Pillar 1: Good Signal"
                G1["Identify Strengths"]
                G2["Classify Good Behaviors"]
                G3["Score Reinforcement Value"]
            end
            
            subgraph "Pillar 2: Bad Signal"
                B1["Detect Issues"]
                B2["Classify Failure Mode"]
                B3["Assign Severity (P0-P4)"]
            end
            
            subgraph "Pillar 3: Learning Capture"
                L1["Identify Novel Patterns"]
                L2["Extract Edge Cases"]
                L3["Document Insights"]
            end
            
            subgraph "Pillar 4: Memory Persistence"
                M1["Identify Persistent Rules"]
                M2["Check Existing Memory"]
                M3["Update/Create Memory Entry"]
            end
        end
    end
    
    SM --> EA
    EA --> G1 & B1 & L1 & M1
    G1 --> G2 --> G3
    B1 --> B2 --> B3
    L1 --> L2 --> L3
    M1 --> M2 --> M3

    style SM fill:#4A90D9,stroke:#2C5F8A,color:#fff
    style G1 fill:#2ECC71,stroke:#1FA855,color:#fff
    style B1 fill:#E74C3C,stroke:#C0392B,color:#fff
    style L1 fill:#3498DB,stroke:#2980B9,color:#fff
    style M1 fill:#9B59B6,stroke:#8E44AD,color:#fff
```

**Evaluator Assignment Algorithm:**

```
1. Incoming response arrives from queue
2. Extract: domain, model_type, language, complexity_estimate
3. Match available evaluators by:
   a. Domain expertise (required match)
   b. Model familiarity (preferred match)
   c. Current workload (load balancing)
   d. Calibration score (minimum threshold: 0.80)
4. Assign to best-fit evaluator
5. Start session timer (SLA tracking)
```

---

### 4. Quality Assurance Layer

Ensures consistency and accuracy across all evaluations.

```mermaid
graph LR
    subgraph "Quality Assurance Pipeline"
        FE["Feedback Entry"] --> CS["Composite Scoring<br/>(0-100)"]
        CS --> IRC["Inter-Rater<br/>Calibration Check"]
        IRC --> AD["Anomaly<br/>Detection"]
        AD --> VS["Validated<br/>& Stored"]
    end
    
    IRC -->|"κ < 0.80"| RC["Re-Calibration<br/>Triggered"]
    AD -->|"Anomaly Detected"| ESC["Escalation<br/>Triggered"]
    
    style CS fill:#E67E22,stroke:#C76B18,color:#fff
    style IRC fill:#3498DB,stroke:#2980B9,color:#fff
    style AD fill:#E74C3C,stroke:#C0392B,color:#fff
    style VS fill:#2ECC71,stroke:#1FA855,color:#fff
```

**Composite Score Calculation:**

```
CompositeScore = (
    GoodSignalScore × W_good +
    BadSignalPenalty × W_bad +
    SeverityImpact × W_severity +
    CompletenessScore × W_completeness +
    ConsistencyScore × W_consistency
)

Where:
  W_good         = 0.25  (configurable per client)
  W_bad          = 0.30
  W_severity     = 0.20
  W_completeness = 0.15
  W_consistency  = 0.10
```

---

### 5. Data Store

A multi-model storage layer optimized for different access patterns.

| Store | Purpose | Access Pattern | Retention |
|---|---|---|---|
| **Feedback Store** | Individual feedback entries | Write-heavy, read-by-session | 24 months |
| **Session Store** | Evaluation session metadata | Write-once, read-many | 36 months |
| **Memory Store** | Persistent rules & preferences | Read-heavy, write-on-change | Indefinite |
| **Audit Log** | Immutable activity trail | Append-only, read-for-compliance | 7 years |

---

### 6. Intelligence Layer

Transforms raw feedback data into actionable intelligence.

| Component | Input | Output | Frequency |
|---|---|---|---|
| **Trend Analyzer** | Feedback entries over time | Trend reports, regression alerts | Daily / Weekly |
| **Pattern Detector** | Clustered feedback entries | Common failure patterns, recurring strengths | Weekly |
| **Benchmark Engine** | Cross-model quality scores | Comparative benchmarks, rankings | Monthly |
| **Insight Extractor** | Learned + Remember entries | Institutional knowledge base | Continuous |

---

## Data Flow

### End-to-End Request Lifecycle

```mermaid
sequenceDiagram
    participant AI as Client AI System
    participant API as ASR API
    participant Queue as Evaluation Queue
    participant Eval as Evaluator
    participant QA as Quality Engine
    participant Store as Data Store
    participant Intel as Intelligence Layer
    participant Dash as Client Dashboard

    AI->>API: Submit AI Response for Evaluation
    API->>API: Authenticate · Validate · Schema Check
    API->>Queue: Enqueue (with priority)
    API-->>AI: 202 Accepted + Entry ID
    
    Queue->>Eval: Assign to Calibrated Evaluator
    
    Note over Eval: 4-Pillar Analysis<br/>✅ Good · ❌ Bad · 📘 Learned · 🧠 Remember
    
    Eval->>QA: Submit Feedback Entry
    QA->>QA: Compute Composite Score
    QA->>QA: Inter-Rater Calibration Check
    QA->>Store: Persist (Schema-Validated)
    Store->>Store: Write Audit Log Entry
    
    Store->>Intel: Trigger Analysis Pipeline
    Intel->>Intel: Update Trends · Detect Patterns
    Intel->>Dash: Publish Updated Intelligence
    
    Dash-->>AI: Webhook: New Insights Available
```

---

## Integration Architecture

### Supported Integration Models

```mermaid
graph TB
    subgraph "Push Model"
        P1["Client pushes responses<br/>via API / SDK"]
        P1 --> P2["ASR processes and<br/>returns feedback"]
    end
    
    subgraph "Pull Model"
        PL1["ASR connects to client's<br/>AI system via API"]
        PL1 --> PL2["ASR pulls responses<br/>for evaluation"]
    end
    
    subgraph "Hybrid Model"
        H1["Real-time push for<br/>critical responses"]
        H2["Batch pull for<br/>historical analysis"]
        H1 & H2 --> H3["Unified feedback<br/>pipeline"]
    end

    style P2 fill:#2ECC71,stroke:#1FA855,color:#fff
    style PL2 fill:#3498DB,stroke:#2980B9,color:#fff
    style H3 fill:#9B59B6,stroke:#8E44AD,color:#fff
```

---

## Scalability & Performance

### Capacity Targets

| Metric | Current | Target (2026 H2) |
|---|---|---|
| Entries/hour (sustained) | 500 | 2,000 |
| Entries/hour (burst) | 1,500 | 5,000 |
| P99 ingestion latency | 180ms | 100ms |
| Evaluation turnaround (P50) | 2.3 hours | 1.5 hours |
| Evaluation turnaround (P99) | 6 hours | 4 hours |
| Concurrent sessions | 50 | 200 |
| Storage (monthly growth) | 12 GB | 50 GB |

### Horizontal Scaling Strategy

```
Ingestion Service    → Stateless, scale by adding instances
Evaluation Engine    → Scale by adding evaluators (human + assisted)
Quality Engine       → Stateless computation, scale horizontally
Data Store           → Sharded by client_id, replicated for reads
Intelligence Layer   → Batch processing, scale by compute allocation
Reporting Service    → Cached results, scale by CDN/cache layer
```

---

## Security Architecture

```mermaid
graph TB
    subgraph "Perimeter"
        WAF["Web Application Firewall"]
        RL["Rate Limiter"]
    end
    
    subgraph "Authentication"
        AUTH["API Key + JWT"]
        RBAC["Role-Based Access Control"]
    end
    
    subgraph "Data Protection"
        PII["PII Detector & Redactor"]
        ENC["Encryption at Rest (AES-256)"]
        TLS["Encryption in Transit (TLS 1.3)"]
    end
    
    subgraph "Audit & Compliance"
        AL["Immutable Audit Log"]
        CM["Compliance Monitor"]
    end
    
    WAF --> RL --> AUTH --> RBAC
    RBAC --> PII --> ENC
    ENC --> AL
    PII --> TLS
    TLS --> CM
    
    style WAF fill:#E74C3C,stroke:#C0392B,color:#fff
    style AUTH fill:#E67E22,stroke:#C76B18,color:#fff
    style PII fill:#9B59B6,stroke:#8E44AD,color:#fff
    style AL fill:#2ECC71,stroke:#1FA855,color:#fff
```

---

## Technology Stack

| Layer | Technology | Rationale |
|---|---|---|
| **API Gateway** | Kong / AWS API Gateway | Rate limiting, auth, routing |
| **Backend Services** | Python (FastAPI) | Type safety, async support, ML ecosystem |
| **Queue** | Redis Streams / SQS | Priority queuing, reliability |
| **Primary Database** | PostgreSQL | ACID compliance, JSON support, mature ecosystem |
| **Document Store** | MongoDB | Flexible schema for feedback entries |
| **Cache** | Redis | Session caching, leaderboard computation |
| **Search** | Elasticsearch | Full-text search across feedback corpus |
| **Object Storage** | S3 / GCS | Attachments, exports, backups |
| **Monitoring** | Prometheus + Grafana | Metrics, alerting, dashboards |
| **CI/CD** | GitHub Actions | Schema validation, doc linting |
| **SDK Languages** | Python, JavaScript | Client library support |

---

> **See Also:**
> - [Methodology →](METHODOLOGY.md)
> - [Feedback Schema →](FEEDBACK_SCHEMA.md)
> - [Integration Guide →](INTEGRATION_GUIDE.md)
> - [Quality Framework →](QUALITY_FRAMEWORK.md)
