# Case Studies

> **Document Version:** 2.3.0 | **Last Updated:** 2026-07-01 | **Note:** All case studies are anonymized to protect client confidentiality.

---

## Table of Contents

- [Case Study 1: HealthTech AI Diagnostics](#case-study-1-healthtech-ai-diagnostics)
- [Case Study 2: FinServ Customer Support Agent](#case-study-2-finserv-customer-support-agent)
- [Case Study 3: EdTech Adaptive Learning Platform](#case-study-3-edtech-adaptive-learning-platform)
- [Case Study 4: Enterprise Code Generation Tool](#case-study-4-enterprise-code-generation-tool)

---

## Case Study 1: HealthTech AI Diagnostics

### Client Profile

| Attribute | Details |
|---|---|
| **Industry** | Healthcare Technology |
| **AI Application** | Patient symptom analysis and triage recommendations |
| **Models Evaluated** | GPT-4o, Claude Sonnet, Gemini 2.5 Pro |
| **Engagement Duration** | 8 months (ongoing) |
| **Monthly Evaluation Volume** | ~2,400 responses |

### Challenge

The client's AI-powered triage system was producing recommendations that were technically accurate in isolation but failed to account for comorbidities, patient demographics, and regional healthcare access variations. Their internal QA team could catch factual errors but lacked the structured framework to capture the nuanced clinical judgment gaps.

### What ASR Feedback Delivered

**✅ Good Signal Insights:**
- Identified that the AI consistently excelled at recognizing acute symptoms (98% accuracy on P0 clinical indicators)
- Documented 23 specific reasoning patterns where the model outperformed clinical decision trees

**❌ Bad Signal Detection:**
- Detected a systematic "completeness gap" — the model omitted asymptomatic presentation information in 34% of responses
- Identified P1-severity hallucination patterns in drug interaction recommendations (12 instances across 2,400 evaluations)
- Found that triage urgency was over-estimated for low-acuity conditions, leading to unnecessary ER referrals

**📘 Learning Capture:**
- Discovered that the model's performance degraded significantly when handling multilingual symptom descriptions (22% accuracy drop for Hindi/Spanish inputs vs. English)
- Identified a novel interaction pattern: the model performed better when asked to "think step by step" about differential diagnoses but worse when asked to "be brief"

**🧠 Memory Persistence:**
- Established 47 persistent clinical rules specific to this client's use case
- Created region-specific evaluation criteria for 6 geographic markets

### Results

| Metric | Before ASR | After 6 Months | Change |
|---|---|---|---|
| Clinical accuracy | 78% | 91% | **↑ 13 pp** |
| Hallucination rate | 5.2% | 1.8% | **↓ 65%** |
| Completeness score | 64/100 | 84/100 | **↑ 31%** |
| P0/P1 issues per 1,000 | 18 | 4 | **↓ 78%** |
| Patient safety escalations | 3/month | 0/month | **↓ 100%** |

### Client Testimonial

> *"ASR Feedback transformed how we think about AI quality in healthcare. The Learning Capture pillar alone has generated more actionable insights than our entire internal QA team produced in the previous year. The persistent memory rules ensure that every lesson learned is applied in perpetuity."*
> — VP of Engineering, HealthTech Client

---

## Case Study 2: FinServ Customer Support Agent

### Client Profile

| Attribute | Details |
|---|---|
| **Industry** | Financial Services (Banking) |
| **AI Application** | Customer support chatbot for banking queries |
| **Models Evaluated** | GPT-4o, Custom fine-tuned Llama 3.1 |
| **Engagement Duration** | 12 months (ongoing) |
| **Monthly Evaluation Volume** | ~3,600 responses |

### Challenge

The client's AI chatbot handled 40,000+ customer interactions monthly. While response accuracy was generally acceptable, they were experiencing:
- Regulatory compliance violations in 2.3% of responses
- Inconsistent tone across different product categories
- A persistent inability to handle complex multi-step financial calculations

### What ASR Feedback Delivered

**✅ Good Signal Insights:**
- The custom fine-tuned Llama model outperformed GPT-4o on product-specific queries by 18%, validating their fine-tuning investment
- Identified 31 "golden response" patterns that became training examples for future fine-tuning

**❌ Bad Signal Detection:**
- Detected 89 regulatory compliance violations across 3 months (categorized by regulation: TILA, ECOA, FCRA)
- Found that the model consistently miscalculated APR for variable-rate products
- Identified tone inconsistencies: formal for credit cards, overly casual for mortgages

**📘 Learning Capture:**
- Discovered that the model's compliance rate improved 45% when system prompts included specific regulatory citations rather than general "be compliant" instructions
- Found that multi-step calculations failed primarily at the "accumulation" step — the model lost track of running totals

**🧠 Memory Persistence:**
- Established 112 regulatory compliance rules mapped to specific regulations
- Created product-specific tone guides for 8 financial product categories

### Results

| Metric | Before ASR | After 12 Months | Change |
|---|---|---|---|
| Compliance violations | 2.3% | 0.1% | **↓ 96%** |
| Customer satisfaction (CSAT) | 3.8/5.0 | 4.5/5.0 | **↑ 18%** |
| Escalation to human agent | 34% | 19% | **↓ 44%** |
| Calculation accuracy | 71% | 94% | **↑ 32%** |
| Fine-tuning dataset quality | — | Top 15% labeled "golden" | New capability |

---

## Case Study 3: EdTech Adaptive Learning Platform

### Client Profile

| Attribute | Details |
|---|---|
| **Industry** | Education Technology |
| **AI Application** | Adaptive tutoring system for K-12 mathematics |
| **Models Evaluated** | GPT-4o, Gemini 2.5 Flash |
| **Engagement Duration** | 6 months |
| **Monthly Evaluation Volume** | ~1,800 responses |

### Challenge

The client's AI tutor needed to adapt its explanations to student age, skill level, and learning style — a challenge that generic evaluation couldn't address because "correct" varied dramatically by student context.

### What ASR Feedback Delivered

**📘 Key Learning:**
- Discovered that the model's explanations for Grade 3 students used vocabulary at a Grade 6 reading level in 42% of cases
- Found that the model's step-by-step math breakdowns skipped intermediate steps that were obvious to adults but essential for young learners

**🧠 Key Memory Rules:**
- Established grade-specific vocabulary constraints
- Created 28 "explanation pattern" rules that map mathematical concepts to age-appropriate analogies

### Results

| Metric | Before ASR | After 6 Months | Change |
|---|---|---|---|
| Student comprehension rate | 61% | 82% | **↑ 34%** |
| Age-appropriate language score | 58/100 | 89/100 | **↑ 53%** |
| Student engagement (time on task) | 4.2 min | 7.8 min | **↑ 86%** |
| Teacher satisfaction | 3.2/5.0 | 4.6/5.0 | **↑ 44%** |

---

## Case Study 4: Enterprise Code Generation Tool

### Client Profile

| Attribute | Details |
|---|---|
| **Industry** | Developer Tools |
| **AI Application** | AI-powered code generation and review |
| **Models Evaluated** | GPT-4.1, Claude Opus, Codex, Custom Models |
| **Engagement Duration** | 4 months |
| **Monthly Evaluation Volume** | ~1,200 code responses |

### Challenge

The client's code generation tool was producing syntactically correct code that often had:
- Security vulnerabilities (SQL injection, XSS)
- Performance anti-patterns
- Inconsistent coding style
- Missing error handling

### What ASR Feedback Delivered

**❌ Critical Bad Signal Detection:**
- Identified 34 security vulnerability patterns across 4 models
- Categorized vulnerabilities by OWASP Top 10 classification
- Found that 67% of security issues were concentrated in database interaction code

**📘 Key Learning:**
- Discovered that providing the model with the project's existing code style guide in the system prompt reduced style violations by 73%
- Found that Claude Opus produced the most secure code but GPT-4.1 produced the most performant code — enabling the client to build a routing strategy

**🧠 Key Memory Rules:**
- Established 89 security-specific evaluation rules mapped to CWE identifiers
- Created language-specific (Python, JavaScript, Go) evaluation criteria

### Results

| Metric | Before ASR | After 4 Months | Change |
|---|---|---|---|
| Security vulnerabilities per 100 outputs | 8.7 | 1.2 | **↓ 86%** |
| Code review rejection rate | 41% | 12% | **↓ 71%** |
| Developer adoption rate | 34% | 67% | **↑ 97%** |
| Time to production-ready code | 45 min avg | 18 min avg | **↓ 60%** |

---

## Common Patterns Across Case Studies

```
┌────────────────────────────────────────────────────────────────────┐
│               PATTERNS ACROSS ALL ENGAGEMENTS                      │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  1. SYSTEMATIC GAPS > RANDOM ERRORS                                │
│     Most AI quality issues are systematic patterns,                │
│     not random failures. ASR's structured approach                 │
│     identifies these patterns in weeks, not months.                │
│                                                                    │
│  2. LEARNING CAPTURE IS THE HIGHEST-VALUE PILLAR                   │
│     Clients consistently report that the insights from             │
│     Pillar 3 (📘 Learned) drive more improvement than              │
│     the error detection from Pillar 2 (❌ Bad).                    │
│                                                                    │
│  3. MEMORY PERSISTENCE PREVENTS REGRESSION                         │
│     Without persistent rules, 40-60% of fixed issues              │
│     recur within 3 months. With memory rules, recurrence           │
│     drops to < 5%.                                                 │
│                                                                    │
│  4. MULTI-MODEL EVALUATION REVEALS STRATEGIC INSIGHTS              │
│     Evaluating the same tasks across multiple models               │
│     enables routing strategies that no single-model                │
│     evaluation can provide.                                        │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

---

> **See Also:**
> - [Methodology →](METHODOLOGY.md)
> - [Metrics & KPIs →](METRICS_AND_KPIs.md)
> - [Quality Framework →](QUALITY_FRAMEWORK.md)
