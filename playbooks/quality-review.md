# Playbook: Quality Review

> **Version:** 2.3.0 | **Audience:** Quality Leads

---

## Purpose

This playbook defines the quality review process — how we audit our own evaluators' work to ensure consistency, accuracy, and completeness.

---

## Audit Types & Schedule

| Type | Volume | Frequency | Focus |
|---|---|---|---|
| **Real-Time Sampling** | 5% of entries | Continuous | Immediate quality gate |
| **Daily Spot Check** | 20 entries | Daily | Cross-evaluator consistency |
| **Weekly Deep Audit** | 50 entries | Weekly | Comprehensive quality analysis |
| **Monthly QA Review** | Full report | Monthly | Strategic quality assessment |

---

## Real-Time Sampling Procedure

### Trigger
Automated random selection of 5% of submitted entries.

### Process
```
1. Receive flagged entry for audit
2. Perform independent evaluation of the same AI response
3. Compare your evaluation against the evaluator's:
   a. Pillar-by-pillar category agreement
   b. Severity alignment (±1 level tolerance)
   c. Score agreement (±5 points tolerance)
4. Record results:
   - PASS: All checks within tolerance
   - REVIEW: 1 dimension outside tolerance
   - FAIL: 2+ dimensions outside tolerance or safety miss
5. For REVIEW/FAIL:
   a. Document specific disagreements
   b. Provide coaching feedback to evaluator
   c. If FAIL, trigger re-calibration procedure
```

---

## Daily Spot Check Procedure

```
1. Pull 20 random entries from yesterday's submissions
   - Stratify by evaluator (ensure coverage)
   - Include at least 2 entries from each active evaluator

2. For each entry, check:
   □ All 4 pillars addressed
   □ Descriptions are specific (not vague)
   □ Evidence citations present
   □ Severity levels appropriate
   □ Memory rules checked (note in metadata)
   □ Score consistent with annotations
   □ No PII in feedback text

3. Calculate quick metrics:
   - Pass rate (target: ≥ 95%)
   - Common issues identified
   - Evaluator-specific patterns

4. Generate daily quality brief (3-5 bullet points)
5. Send to quality team channel
```

---

## Weekly Deep Audit Procedure

```
1. Sample Selection (50 entries):
   - 10 per major client (top 3-5 clients)
   - Stratified by evaluator, model, and domain
   - Include 10 dual-evaluated entries for κ calculation

2. Full Audit Checklist (per entry):
   □ Category codes correctly applied
   □ Severity levels calibrated against taxonomy
   □ Good signals are genuinely positive (not generic praise)
   □ Bad signals include root cause + remediation
   □ Learnings are genuinely novel (not restating known issues)
   □ Memory rules checked and applied correctly
   □ Evidence is specific and verifiable
   □ Quality score matches formula output (±0.5)
   □ Schema validation passes

3. Compute Metrics:
   - Cohen's κ from dual-evaluated entries
   - Category usage distribution
   - Severity distribution vs. targets
   - Average composite score trends
   - Memory compliance rate

4. Generate Weekly Quality Report (use template)
5. Identify top 3 improvement actions
6. Conduct weekly quality team standup
```

---

## Handling Audit Failures

| Failure Type | Action | Timeline |
|---|---|---|
| Single minor miss | Coaching feedback via direct message | Same day |
| Pattern of minor misses | 1:1 review session with calibration exercises | Within 3 days |
| Major miss (wrong severity, missed P0) | Immediate pause + re-calibration | Same day |
| Systematic quality drop (κ < 0.80) | Formal re-training program | Within 1 week |

---

> **See Also:** [Quality Framework →](../docs/QUALITY_FRAMEWORK.md) | [Escalation Procedures →](escalation-procedures.md)
