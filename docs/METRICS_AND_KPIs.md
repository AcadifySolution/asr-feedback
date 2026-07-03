# Metrics & KPIs

> **Document Version:** 2.3.0 | **Last Updated:** 2026-07-01 | **Audience:** Leads, Management, Stakeholders

---

## Table of Contents

- [Overview](#overview)
- [Operational Metrics](#operational-metrics)
- [Quality Metrics](#quality-metrics)
- [Client Impact Metrics](#client-impact-metrics)
- [Growth Metrics](#growth-metrics)
- [SLA Performance](#sla-performance)
- [Metric Definitions](#metric-definitions)

---

## Overview

This document defines the key performance indicators (KPIs) and operational metrics used to measure the effectiveness, quality, and impact of the ASR Feedback Intelligence Platform. All metrics are tracked in real-time dashboards and reported in weekly/monthly reviews.

---

## Operational Metrics

| Metric | Definition | Target | Current | Trend |
|---|---|---|---|---|
| Entries Processed (Monthly) | Total feedback entries completed | — | **12,847** | ↑ 8% |
| Sessions Completed (Monthly) | Total evaluation sessions | — | **534** | ↑ 12% |
| Avg. Entries per Session | Mean entries per evaluation session | 20–30 | **24.1** | → Stable |
| Evaluator Utilization | % of evaluator capacity used | 75–85% | **81%** | → Stable |
| Queue Depth (Peak) | Max pending entries at any time | < 200 | **142** | ↓ Improving |
| Queue Wait Time (P50) | Median time from submission to evaluation start | < 30 min | **18 min** | ↓ Improving |
| Queue Wait Time (P99) | 99th percentile wait time | < 2 hours | **1.4 hours** | ↓ Improving |

---

## Quality Metrics

| Metric | Definition | Target | Current | Trend |
|---|---|---|---|---|
| Inter-Rater Reliability (κ) | Cohen's Kappa across dual-evaluated entries | ≥ 0.80 | **0.87** | ↑ Improving |
| Severity Agreement Rate | % agreement on severity classification | ≥ 85% | **89%** | ↑ Improving |
| Schema Validation Rate | % of entries passing schema validation | 100% | **100%** | → Stable |
| Audit Pass Rate | % of audited entries meeting quality standards | ≥ 95% | **97.2%** | → Stable |
| Completeness Score | Avg. % of pillars addressed per entry | ≥ 95% | **98.4%** | → Stable |
| Evidence Citation Rate | % of entries with specific evidence quotes | ≥ 90% | **94.1%** | ↑ Improving |
| Memory Compliance Rate | % of applicable memory rules correctly applied | ≥ 95% | **96.8%** | → Stable |
| Avg. Composite Quality Score | Mean quality score across all evaluated responses | — | **73.6** | Baseline |

---

## Client Impact Metrics

| Metric | Definition | Measurement Period | Result |
|---|---|---|---|
| Hallucination Rate Reduction | Change in AI hallucination rate after ASR feedback integration | 6-month post-integration | **↓ 47%** |
| Response Accuracy Improvement | Change in factual accuracy scores | 6-month post-integration | **↑ 34%** |
| Critical Issue Reduction | Change in P0/P1 issue frequency | 3-month post-integration | **↓ 62%** |
| Model Iteration Speed | Change in time between identifying issue and deploying fix | Post-integration vs. pre | **3.2x faster** |
| Error Recurrence Reduction | Change in same-error repetition rate across sessions | Quarterly measurement | **↓ 71%** |
| Client Retention Rate | % of clients renewing after initial contract period | Annual | **89%** |
| Client Satisfaction (CSAT) | Average client satisfaction rating | Monthly survey | **4.7 / 5.0** |
| Net Promoter Score (NPS) | Client likelihood to recommend | Quarterly survey | **+62** |

---

## Growth Metrics

| Metric | Q1 2026 | Q2 2026 | Q3 2026 (Target) |
|---|---|---|---|
| Active Enterprise Clients | 6 | 8 | 11 |
| AI Models Under Evaluation | 18 | 23 | 30 |
| Domains Covered | 9 | 12 | 15 |
| Active Evaluators | 14 | 18 | 24 |
| Monthly Entry Volume | 9,200 | 12,847 | 18,000 |
| Unique Learning Entries (Cumulative) | 1,240 | 1,890 | 2,500 |
| Active Memory Rules | 312 | 487 | 650 |

---

## SLA Performance

### By Service Tier

| Tier | Turnaround SLA | Actual (P50) | Actual (P95) | Compliance |
|---|---|---|---|---|
| **Enterprise Critical** | 2 hours | 1.1 hours | 1.8 hours | **99.2%** |
| **Enterprise Standard** | 4 hours | 2.3 hours | 3.6 hours | **98.7%** |
| **Professional** | 8 hours | 4.1 hours | 6.8 hours | **99.5%** |
| **Standard** | 24 hours | 8.2 hours | 18.4 hours | **99.8%** |

### SLA Compliance Trend

```
Month     | Enterprise Critical | Enterprise Standard | Professional | Standard
----------|--------------------|--------------------|-------------|--------
Jan 2026  | 98.5%              | 97.8%              | 99.1%       | 99.9%
Feb 2026  | 98.9%              | 98.2%              | 99.3%       | 99.8%
Mar 2026  | 99.1%              | 98.4%              | 99.4%       | 99.9%
Apr 2026  | 99.0%              | 98.5%              | 99.5%       | 99.7%
May 2026  | 99.3%              | 98.9%              | 99.4%       | 99.8%
Jun 2026  | 99.2%              | 98.7%              | 99.5%       | 99.8%
```

---

## Metric Definitions

### Operational

| Metric | Formula | Data Source |
|---|---|---|
| Entries Processed | `COUNT(entries WHERE status = 'completed' AND month = current)` | Feedback Store |
| Queue Wait Time | `evaluation_start_time - submission_time` | Queue Manager |
| Evaluator Utilization | `(actual_entries / max_capacity) × 100` | Session Manager |

### Quality

| Metric | Formula | Data Source |
|---|---|---|
| Inter-Rater Reliability | `Cohen's κ = (P_o - P_e) / (1 - P_e)` | Dual-evaluation audit data |
| Audit Pass Rate | `(audits_passed / total_audits) × 100` | Audit system |
| Completeness Score | `(pillars_addressed / 4) × 100, averaged` | Feedback entries |

### Impact

| Metric | Formula | Data Source |
|---|---|---|
| Hallucination Rate Reduction | `((pre_rate - post_rate) / pre_rate) × 100` | Client telemetry |
| CSAT | `Σ(ratings) / count(ratings)` | Monthly survey |
| NPS | `% Promoters - % Detractors` | Quarterly survey |

---

> **See Also:**
> - [Quality Framework →](QUALITY_FRAMEWORK.md)
> - [SLA Definitions →](../compliance/sla-definitions.md)
> - [Dashboard Specification →](../reports/dashboard-metrics.md)
> - [Sample Reports →](../reports/)
