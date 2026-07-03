# Data Handling Policy

> **Version:** 2.3.0 | **Last Updated:** 2026-07-01 | **Classification:** Internal — Shared with Clients

---

## Overview

This policy defines how the ASR Feedback Intelligence Platform handles, stores, processes, and disposes of client data throughout the feedback lifecycle.

---

## Data Classification

| Classification | Description | Examples | Handling |
|---|---|---|---|
| **Confidential** | Client AI responses, system prompts, proprietary data | AI responses, training data, model configurations | Encrypted, access-controlled, audit-logged |
| **Internal** | Feedback entries, quality scores, evaluator annotations | Feedback entries, session reports, quality scores | Encrypted, access-controlled |
| **Restricted** | PII, authentication credentials, security keys | User names, email addresses, API keys | Encrypted, redacted before evaluation, minimal retention |
| **Public** | Published documentation, methodology descriptions | This repository, anonymized case studies | Open access |

---

## Data Lifecycle

```
COLLECTION → VALIDATION → PROCESSING → STORAGE → ACCESS → ARCHIVAL → DELETION
```

### 1. Collection
- Data enters the platform via API, SDK, or batch upload
- TLS 1.3 encryption in transit for all data
- Input validation and schema enforcement at ingestion

### 2. Validation
- Schema validation against formal JSON schemas
- PII detection scan (pre-processing)
- Data integrity checks (checksums, format validation)

### 3. Processing
- Evaluators access data through secure evaluation interface
- PII is redacted before presentation to evaluators
- No data leaves the evaluation environment
- Processing is logged in the audit trail

### 4. Storage
- All data encrypted at rest using AES-256
- Database-level encryption with key management via cloud KMS
- Backups are encrypted and stored in a separate geographic region
- Storage complies with client-specified data residency requirements

### 5. Access
- Role-Based Access Control (RBAC) for all data access
- Principle of least privilege enforced
- All access logged in immutable audit trail
- Multi-factor authentication required for sensitive data access

### 6. Archival
- Data transitioned to cold storage after active retention period
- Archived data remains encrypted and access-controlled
- Archival event logged in audit trail

### 7. Deletion
- Data deleted upon client request or at end of retention period
- Deletion is cryptographic (key destruction) for encrypted stores
- Deletion verified and logged in audit trail
- Certificate of deletion available upon request

---

## Retention Policy

| Data Type | Active Retention | Archive Retention | Total |
|---|---|---|---|
| Feedback entries | 24 months | 12 months | 36 months |
| Session reports | 24 months | 12 months | 36 months |
| Quality scores | 24 months | 12 months | 36 months |
| Memory rules | Indefinite (while active) | 12 months after deprecation | — |
| Audit logs | 36 months | 48 months | 7 years |
| API access logs | 12 months | 24 months | 36 months |
| Raw AI responses | 6 months | Deleted | 6 months |

> **Note:** Clients may request custom retention periods. Shorter retention is always accommodated; longer retention requires separate agreement.

---

## Data Isolation

- Each client's data is logically isolated at the database level
- Client data is never co-mingled during processing
- Cross-client analytics use only anonymized, aggregated data
- Evaluators are assigned to specific clients and cannot access other clients' data

---

## Third-Party Data Sharing

**We do NOT share client data with any third party**, with the following documented exceptions:
1. Cloud infrastructure providers (encrypted storage only — they cannot read the data)
2. As required by law (with client notification unless legally prohibited)
3. Anonymized, aggregated analytics (no client identification possible)

---

## Client Rights

| Right | Process | Timeline |
|---|---|---|
| Data access | Request via API or account manager | Within 5 business days |
| Data export | Full export in JSON format | Within 10 business days |
| Data deletion | Request via account manager | Within 30 calendar days |
| Data portability | Export in standard formats (JSON, CSV) | Within 10 business days |
| Processing restriction | Temporary halt of evaluation | Immediate upon request |

---

> **See Also:** [Privacy Framework →](privacy-framework.md) | [Audit Trail →](audit-trail.md) | [SLA Definitions →](sla-definitions.md)
