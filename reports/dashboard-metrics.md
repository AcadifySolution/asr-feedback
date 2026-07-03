# Dashboard Metrics Specification

> **Version:** 2.3.0 | **Last Updated:** 2026-07-01

---

## Overview

This document specifies the dashboard panels, metrics, and data sources for the ASR Feedback operational dashboard.

---

## Dashboard Layout

### Panel 1: Real-Time Monitor
| Metric | Source | Refresh |
|---|---|---|
| Active evaluation sessions | Session Manager | 30s |
| Pending entries in queue | Queue Manager | 30s |
| SLA countdown (oldest entry) | Queue Manager | 30s |
| Active evaluators | Session Manager | 60s |
| Today's entry count | Feedback Store | 60s |

### Panel 2: Quality Overview
| Metric | Source | Refresh |
|---|---|---|
| Avg composite score (rolling 7 days) | Feedback Store | 5 min |
| Score distribution (band chart) | Feedback Store | 5 min |
| Severity distribution (stacked bar) | Feedback Store | 5 min |
| Top 5 issue categories (this week) | Feedback Store | 15 min |
| Inter-rater reliability trend (12 weeks) | Audit System | Daily |

### Panel 3: Evaluator Performance
| Metric | Source | Refresh |
|---|---|---|
| Per-evaluator composite score avg | Feedback Store | 15 min |
| Per-evaluator κ score | Audit System | Daily |
| Per-evaluator entry volume | Session Manager | 15 min |
| Audit pass rate by evaluator | Audit System | Daily |
| Calibration score trend | Calibration System | Weekly |

### Panel 4: Client View
| Metric | Source | Refresh |
|---|---|---|
| Per-client avg composite score | Feedback Store | 15 min |
| Per-client severity distribution | Feedback Store | 15 min |
| Per-client SLA compliance | SLA Monitor | 5 min |
| Per-client entry volume | Feedback Store | 15 min |
| Per-client memory rules (active/violated) | Memory Store | 15 min |

### Panel 5: Intelligence
| Metric | Source | Refresh |
|---|---|---|
| New learnings this week | Feedback Store | 15 min |
| New memory rules this week | Memory Store | 15 min |
| Memory rule compliance rate | Memory Store | 15 min |
| Category usage heatmap | Feedback Store | Daily |
| Trend alerts | Intelligence Layer | Hourly |

### Panel 6: SLA Monitor
| Metric | Source | Refresh |
|---|---|---|
| Per-tier compliance % | SLA Monitor | 5 min |
| Average turnaround by tier | SLA Monitor | 15 min |
| SLA breaches (count, details) | SLA Monitor | Real-time |
| Queue depth by priority | Queue Manager | 30s |

---

## Alert Thresholds

| Alert | Condition | Severity | Notification |
|---|---|---|---|
| SLA Breach Imminent | Entry approaching 80% of SLA time | Warning | Dashboard + Slack |
| SLA Breached | Entry exceeds SLA time | Critical | Dashboard + Slack + Email |
| κ Drop | Evaluator κ drops below 0.80 | High | Dashboard + Quality Lead |
| P0 Detected | P0 severity entry submitted | Critical | All channels |
| Queue Overload | Queue depth exceeds 200 entries | Warning | Dashboard + Operations Lead |
| Volume Spike | Entry volume exceeds 150% of daily average | Info | Dashboard |

---

> **See Also:** [Metrics & KPIs →](../docs/METRICS_AND_KPIs.md) | [Quality Framework →](../docs/QUALITY_FRAMEWORK.md)
