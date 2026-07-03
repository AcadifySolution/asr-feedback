# Weekly Quality Report — Sample

> **Report Period:** Week of 2026-06-23 to 2026-06-29
> **Generated:** 2026-06-30 | **Author:** Quality Lead

---

## Executive Summary

Strong operational week with entry volume up 6% over the previous week. Inter-rater reliability remains well above target at κ = 0.88. One notable trend: a systematic increase in `BAD_INCOMPLETE` signals across HealthTech client evaluations, suggesting a model regression in completeness for medical QA. Two new memory rules created to address discovered patterns. SLA compliance at 99.1% across all tiers.

---

## Key Metrics

| Metric | Target | This Week | Last Week | Trend |
|---|---|---|---|---|
| Entries Processed | — | **3,247** | 3,061 | ↑ 6% |
| Sessions Completed | — | **138** | 127 | ↑ 9% |
| Avg Composite Score | — | **74.8** | 75.2 | ↓ 0.5% |
| Inter-Rater Reliability (κ) | ≥ 0.80 | **0.88** | 0.87 | ↑ Improving |
| Schema Validation Rate | 100% | **100%** | 100% | → Stable |
| Audit Pass Rate | ≥ 95% | **96.8%** | 97.1% | → Stable |
| SLA Compliance | ≥ 98% | **99.1%** | 98.9% | ↑ Improving |
| Memory Compliance Rate | ≥ 95% | **97.2%** | 96.5% | ↑ Improving |

---

## Score Distribution

| Band | Count | % | Change vs Last Week |
|---|---|---|---|
| Excellent (90-100) | 389 | 12.0% | ↑ 1.2% |
| Good (75-89) | 1,267 | 39.0% | → Stable |
| Acceptable (60-74) | 1,105 | 34.0% | ↑ 0.8% |
| Poor (40-59) | 421 | 13.0% | ↓ 1.5% |
| Critical (0-39) | 65 | 2.0% | ↓ 0.5% |

---

## Severity Distribution

| Level | Count | Rate per 1,000 | Target | Status |
|---|---|---|---|---|
| P0 (Critical) | 0 | 0.0 | < 1 | ✅ |
| P1 (High) | 12 | 3.7 | < 5 | ✅ |
| P2 (Medium) | 78 | 24.0 | < 30 | ✅ |
| P3 (Low) | 198 | 61.0 | < 80 | ✅ |
| P4 (Trivial) | 89 | 27.4 | — | — |

---

## Top Issues This Week

| Rank | Category | Occurrences | Severity | Client(s) Affected |
|---|---|---|---|---|
| 1 | BAD_INCOMPLETE | 34 | P2 | HealthTech, EdTech |
| 2 | BAD_CONTEXT | 21 | P2-P3 | FinServ |
| 3 | BAD_REDUNDANT | 19 | P3 | HealthTech, FinServ |
| 4 | BAD_HALLUCINATION | 8 | P1 | HealthTech |
| 5 | BAD_TONE | 7 | P3 | EdTech |

**Analysis:** The 34 `BAD_INCOMPLETE` signals represent a 42% increase over last week, concentrated in medical QA responses. Investigation reveals the model's most recent update (June 20 deployment) appears to have reduced completeness in symptom-listing responses. Recommending client-side A/B testing against the previous model version.

---

## Key Learnings Captured

1. **LEARN_DOMAIN (Healthcare):** Medical QA responses after the June 20 model update are 15% shorter on average, correlating with the increase in incompleteness issues — suggests a compression trade-off was applied
2. **LEARN_INTERACTION:** Multi-turn conversations in FinServ show context degradation specifically when users switch between account types (savings → credit → mortgage) within the same thread
3. **LEARN_PROMPT:** Adding "Be comprehensive but concise" to system prompts reduced BAD_REDUNDANT by 28% without increasing BAD_INCOMPLETE in EdTech evaluations

---

## New Memory Rules

| Rule ID | Type | Scope | Rule Summary |
|---|---|---|---|
| MEM-2026-0487 | MEM_DOMAIN_RULE | domain:healthcare | After June 20 model update, verify response completeness against ADA minimum symptom lists |
| MEM-2026-0488 | MEM_CLIENT_PREF | client:FINSERV-01 | When evaluating multi-product conversations, check for context retention at each product switch |

---

## Evaluator Performance

| Evaluator | Entries | Avg Score | κ | Audit Pass | Notes |
|---|---|---|---|---|---|
| EVAL-012 | 298 | 74.2 | 0.91 | 98% | Top performer |
| EVAL-023 | 312 | 75.8 | 0.87 | 97% | Consistent |
| EVAL-037 | 289 | 73.1 | 0.86 | 96% | — |
| EVAL-042 | 267 | 76.4 | 0.89 | 98% | — |
| EVAL-051 | 301 | 74.9 | 0.84 | 95% | — |
| EVAL-058 | 274 | 73.6 | 0.88 | 97% | New — completed calibration |
| EVAL-063 | 256 | 74.0 | 0.85 | 96% | — |
| EVAL-071 | 250 | 75.1 | 0.90 | 98% | — |

All evaluators above minimum κ threshold (0.80). ✅

---

## Client Highlights

### HealthTech (CLIENT-HEALTHTECH-01)
- Sessions: 42 | Entries: 1,008
- Avg Score: **72.1** (↓ from 75.8 — model update impact)
- Notable: Completeness regression detected post June 20 model update
- **Action:** Scheduled call with client engineering team for Thursday

### FinServ (CLIENT-FINSERV-01)
- Sessions: 38 | Entries: 912
- Avg Score: **76.4** (→ stable)
- Notable: Multi-product context switching is a new issue pattern
- **Action:** Added memory rule MEM-2026-0488

### EdTech (CLIENT-EDTECH-01)
- Sessions: 28 | Entries: 672
- Avg Score: **77.2** (↑ from 74.6)
- Notable: Prompt optimization recommendation from last week showing positive results
- **Action:** Document successful prompt pattern for cross-client sharing

---

## Action Items

| # | Action | Owner | Due Date | Priority |
|---|---|---|---|---|
| 1 | Investigate HealthTech completeness regression with client | Account Manager | Jul 3 | High |
| 2 | Expand FinServ multi-product context test cases | EVAL-042 | Jul 5 | Medium |
| 3 | Document EdTech prompt optimization as case study | Quality Lead | Jul 7 | Medium |
| 4 | Schedule EVAL-058 calibration review (first month complete) | Quality Lead | Jul 2 | Medium |
| 5 | Update medical QA rubric for post-update completeness standards | Methodology Lead | Jul 5 | High |

---

## Next Week Focus

- Monitor HealthTech completeness metrics after client engineering call
- Continue tracking FinServ multi-product context pattern
- Begin Q3 calibration exercise preparation
- Onboard 2 new evaluators (EVAL-075, EVAL-076) — start Phase 1 training
