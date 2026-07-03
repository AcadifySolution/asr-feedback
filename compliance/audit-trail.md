# Audit Trail Specification

> **Version:** 2.3.0 | **Last Updated:** 2026-07-01

---

## Overview

The ASR Feedback audit trail is an **immutable, chronological record** of all significant actions performed on the platform. It provides full traceability for compliance, quality assurance, and incident investigation.

---

## Design Principles

| Principle | Implementation |
|---|---|
| **Immutability** | Audit entries are append-only. No modification or deletion. |
| **Completeness** | Every data access, modification, and decision is logged |
| **Timeliness** | Events are logged within 1 second of occurrence |
| **Tamper-Evidence** | Cryptographic chaining (hash of previous entry included) |
| **Retention** | 7-year minimum retention period |

---

## Audited Events

| Event Category | Events | Severity |
|---|---|---|
| **Authentication** | Login, logout, failed login, API key usage | Medium |
| **Data Access** | Read feedback entry, view session report, export data | Low |
| **Data Modification** | Create entry, update score, modify memory rule | Medium |
| **Data Deletion** | Delete entry, purge client data | High |
| **Evaluation** | Start session, submit entry, complete session | Medium |
| **Quality** | Audit pass/fail, calibration event, escalation | Medium |
| **Configuration** | Webhook change, API key rotation, permission change | High |
| **Security** | PII detected, access denied, rate limit exceeded | High |

---

## Audit Entry Schema

```json
{
  "auditId": "AUD-2026-0701-000001",
  "timestamp": "2026-07-01T14:23:45.123Z",
  "eventType": "evaluation.entry_submitted",
  "actor": {
    "type": "evaluator",
    "id": "EVAL-042",
    "ip": "[REDACTED]"
  },
  "resource": {
    "type": "feedback_entry",
    "id": "FB-2026-0547-001"
  },
  "action": "create",
  "details": {
    "sessionId": "SES-2026-0547",
    "clientId": "CLIENT-HEALTHTECH-01",
    "compositeScore": 74
  },
  "previousHash": "sha256:a1b2c3d4...",
  "hash": "sha256:e5f6g7h8..."
}
```

---

## Access Controls

| Role | Read Audit | Export Audit | Admin |
|---|---|---|---|
| Evaluator | Own entries only | ❌ | ❌ |
| Quality Lead | All entries | By request | ❌ |
| Account Manager | Client-specific | By request | ❌ |
| Operations Director | All entries | ✅ | ❌ |
| Compliance Officer | All entries | ✅ | ✅ |

---

## Retention & Archival

| Period | Storage Tier | Access |
|---|---|---|
| 0–12 months | Hot storage (instant query) | Full search and filter |
| 12–36 months | Warm storage (query within minutes) | Search with delay |
| 36–84 months | Cold storage (retrieval within hours) | By request only |

---

> **See Also:** [Data Handling Policy →](data-handling-policy.md) | [Privacy Framework →](privacy-framework.md)
