# Privacy Framework

> **Version:** 2.3.0 | **Last Updated:** 2026-07-01

---

## Overview

The ASR Feedback Privacy Framework ensures that personally identifiable information (PII) is detected, handled, and protected throughout the feedback lifecycle.

---

## PII Detection

### Automated PII Scanning

All incoming data is automatically scanned for PII patterns before evaluation:

| PII Type | Detection Method | Action |
|---|---|---|
| Email addresses | Regex pattern matching | Auto-redact |
| Phone numbers | Regex + format detection | Auto-redact |
| Social Security Numbers | Regex pattern matching | Auto-redact + alert |
| Credit card numbers | Luhn algorithm + regex | Auto-redact + alert |
| IP addresses | Regex pattern matching | Auto-redact |
| Physical addresses | NER + pattern matching | Flag for review |
| Personal names | Named Entity Recognition | Flag for review |
| Dates of birth | Date pattern + context analysis | Flag for review |
| Medical record numbers | Pattern matching | Auto-redact + alert |

### Redaction Format

```
Original:  "Call John Smith at john.smith@example.com or 555-123-4567"
Redacted:  "Call [REDACTED_NAME] at [REDACTED_EMAIL] or [REDACTED_PHONE]"
```

Redaction is applied before data reaches evaluators. Original data is stored in encrypted, access-restricted storage with strict audit requirements.

---

## Privacy by Design Principles

| Principle | Implementation |
|---|---|
| **Data Minimization** | Collect only data necessary for evaluation |
| **Purpose Limitation** | Data used exclusively for contracted evaluation service |
| **Storage Limitation** | Defined retention periods, automatic deletion |
| **Integrity** | Schema validation, checksums, audit trail |
| **Confidentiality** | Encryption, access controls, PII redaction |
| **Accountability** | Immutable audit logs, compliance monitoring |

---

## GDPR Compliance

| GDPR Article | Compliance Measure |
|---|---|
| Art. 5 — Principles | Data minimization, purpose limitation, storage limitation |
| Art. 6 — Lawful Basis | Legitimate interest (contracted service) + client consent |
| Art. 15 — Right of Access | Data export available within 5 business days |
| Art. 17 — Right to Erasure | Data deletion within 30 calendar days |
| Art. 20 — Data Portability | Export in JSON and CSV formats |
| Art. 25 — Privacy by Design | Automated PII detection, encryption at rest/transit |
| Art. 28 — Processor Requirements | DPA available, subprocessor disclosure |
| Art. 30 — Records of Processing | Maintained and available for inspection |
| Art. 32 — Security of Processing | AES-256, TLS 1.3, RBAC, audit logging |
| Art. 33 — Breach Notification | 72-hour notification commitment |

---

## Data Processing Agreement (DPA)

A formal DPA is available for all enterprise clients, covering:
- Nature and purpose of processing
- Types of personal data processed
- Data subject categories
- Subprocessor disclosure
- Security measures
- Breach notification procedures
- Data return and deletion terms

---

> **See Also:** [Data Handling Policy →](data-handling-policy.md) | [Audit Trail →](audit-trail.md)
