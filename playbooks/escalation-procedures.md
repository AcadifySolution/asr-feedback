# Playbook: Escalation Procedures

> **Version:** 2.3.0 | **Audience:** All Team Members

---

## Purpose

This playbook defines when, how, and to whom issues should be escalated. Quick and correct escalation protects our clients, our quality reputation, and end users.

---

## Escalation Decision Matrix

```
Is there a P0 (Critical) issue?
├── YES → IMMEDIATE ESCALATION (see Level 1 below)
│
└── NO → Is there a P1 (High) issue?
    ├── YES → Is it a safety concern?
    │   ├── YES → IMMEDIATE ESCALATION (Level 1)
    │   └── NO → PRIORITY ESCALATION (Level 2)
    │
    └── NO → Is there a pattern of P2 issues?
        ├── YES (3+ same P2 in one session) → STANDARD ESCALATION (Level 3)
        │
        └── NO → Is the evaluator's κ below threshold?
            ├── YES → QUALITY ESCALATION (Level 4)
            └── NO → No escalation needed. Document normally.
```

---

## Escalation Levels

### Level 1: Immediate Escalation (P0 / Safety)

| Step | Action | Timeline |
|---|---|---|
| 1 | **STOP** current evaluation | Immediately |
| 2 | Document the issue with full evidence | Within 5 minutes |
| 3 | Notify Quality Lead via emergency channel | Within 10 minutes |
| 4 | Quality Lead notifies Account Manager | Within 15 minutes |
| 5 | Account Manager notifies client's primary contact | Within 30 minutes |
| 6 | Create Incident Report (templates/incident-report.md) | Within 1 hour |
| 7 | Create MEM_SAFETY_RULE to prevent recurrence | Within 2 hours |

**Emergency Contact Chain:**
```
Evaluator → Quality Lead → Account Manager → Operations Director
```

### Level 2: Priority Escalation (P1 / Non-Safety)

| Step | Action | Timeline |
|---|---|---|
| 1 | Complete current entry evaluation | Normal |
| 2 | Flag entry as "P1 — Requires Review" | Immediately |
| 3 | Notify Quality Lead via standard channel | Within 30 minutes |
| 4 | Include in session report "Top Issues" section | End of session |
| 5 | Quality Lead reviews and determines if client notification needed | Within 4 hours |

### Level 3: Standard Escalation (Pattern Detection)

| Step | Action | Timeline |
|---|---|---|
| 1 | Document the pattern with evidence across entries | End of session |
| 2 | Include in session report with trend analysis | End of session |
| 3 | Flag for weekly quality review | Next weekly audit |
| 4 | Quality Lead determines if systematic action needed | Within 1 week |

### Level 4: Quality Escalation (Evaluator Performance)

| Step | Action | Timeline |
|---|---|---|
| 1 | Quality system automatically detects κ drop | Real-time |
| 2 | Evaluator notified of calibration concern | Same day |
| 3 | Quality Lead schedules re-calibration session | Within 48 hours |
| 4 | If κ < 0.70, evaluator removed from production | Immediately |

---

## Communication Templates

### Level 1 Emergency Notification
```
🚨 P0 ESCALATION — [Client Name]

Entry ID: FB-YYYY-NNNN-NNN
Model: [model-id]
Category: [BAD_SAFETY / BAD_HALLUCINATION]
Description: [1-2 sentence summary]
Evidence: [Brief quote]
Potential Impact: [Assessment]
Evaluator: EVAL-NNN

ACTION REQUIRED: Review within 15 minutes.
```

### Level 2 Priority Notification
```
⚠️ P1 FLAG — [Client Name]

Entry ID: FB-YYYY-NNNN-NNN
Category: [Category Code]
Severity: P1
Description: [1-2 sentence summary]
Action: Review before next client report delivery.
```

---

## De-Escalation Criteria

An escalation can be de-escalated when:
- The issue is confirmed to be a false positive after review
- The root cause is identified and mitigated
- The client has been informed and acknowledges the resolution
- Preventive measures (memory rules) are in place

---

> **See Also:** [Incident Report Template →](../templates/incident-report.md) | [Quality Framework →](../docs/QUALITY_FRAMEWORK.md)
