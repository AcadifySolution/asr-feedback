# Service Level Agreement (SLA) Definitions

> **Version:** 2.3.0 | **Last Updated:** 2026-07-01

---

## Overview

This document defines the service level agreements for the ASR Feedback Intelligence Platform. SLAs represent our contractual commitments to service quality, availability, and responsiveness.

---

## Service Tiers

| Tier | Monthly Volume | Turnaround SLA | Uptime SLA | Price Range |
|---|---|---|---|---|
| **Standard** | Up to 500 entries | 24 hours | 99.0% | $ |
| **Professional** | Up to 2,000 entries | 8 hours | 99.5% | $$ |
| **Enterprise Standard** | Up to 5,000 entries | 4 hours | 99.9% | $$$ |
| **Enterprise Critical** | Unlimited | 2 hours | 99.95% | $$$$ |

---

## Turnaround SLA

### Definition

**Turnaround time** = Time from response submission (API acknowledgment) to completed feedback entry delivery (webhook notification or status change to `completed`).

### Measurement

| Tier | P50 Target | P95 Target | P99 Target | Max |
|---|---|---|---|---|
| Standard | 8 hours | 18 hours | 22 hours | 24 hours |
| Professional | 4 hours | 7 hours | 7.5 hours | 8 hours |
| Enterprise Standard | 2 hours | 3.5 hours | 3.8 hours | 4 hours |
| Enterprise Critical | 1 hour | 1.5 hours | 1.8 hours | 2 hours |

### Exclusions

Turnaround SLA excludes:
- Planned maintenance windows (communicated 48 hours in advance)
- Force majeure events
- Client-side delays (e.g., insufficient context requiring clarification)
- Volume exceeding contracted tier by >20% without prior arrangement

---

## Uptime SLA

### Definition

**Uptime** = Percentage of time the API is available and responding to requests within acceptable latency thresholds.

### Measurement

| Component | Uptime Target | Measurement Window |
|---|---|---|
| API Gateway | Per tier (above) | Monthly |
| Dashboard | 99.5% | Monthly |
| Webhook Delivery | 99.9% | Monthly |
| SDK Availability | 99.9% | Monthly |

### Downtime Calculation

```
Uptime % = ((Total Minutes - Downtime Minutes) / Total Minutes) × 100

Example (99.9% in a 30-day month):
Total Minutes = 43,200
Max Downtime = 43.2 minutes = ~43 minutes
```

---

## Quality SLA

| Metric | Target | Measurement |
|---|---|---|
| Inter-Rater Reliability (κ) | ≥ 0.80 | Weekly, across all evaluators |
| Schema Validation Rate | 100% | Continuous |
| Audit Pass Rate | ≥ 95% | Weekly audit cycle |
| Evidence Citation Rate | ≥ 90% | Weekly audit cycle |
| Memory Compliance Rate | ≥ 95% | Weekly audit cycle |

---

## Incident Response SLA

| Severity | Response Time | Resolution Target | Communication |
|---|---|---|---|
| P0 (Critical) | 15 minutes | 4 hours | Real-time updates |
| P1 (High) | 30 minutes | 8 hours | Hourly updates |
| P2 (Medium) | 2 hours | 24 hours | Daily updates |
| P3 (Low) | 4 hours | 72 hours | On resolution |

---

## SLA Credits

If turnaround or uptime SLAs are not met, clients receive service credits:

| SLA Miss | Credit |
|---|---|
| Uptime < SLA target by ≤1% | 10% of monthly fee |
| Uptime < SLA target by 1-5% | 25% of monthly fee |
| Uptime < SLA target by >5% | 50% of monthly fee |
| Turnaround SLA missed for >5% of entries | 10% of monthly fee |
| Turnaround SLA missed for >10% of entries | 25% of monthly fee |

---

## Reporting

SLA performance is reported to clients:
- **Weekly:** Summary metrics in weekly quality report
- **Monthly:** Detailed SLA performance in monthly review
- **Real-time:** Dashboard access for Enterprise tier clients

---

> **See Also:** [Metrics & KPIs →](../docs/METRICS_AND_KPIs.md) | [Dashboard →](../reports/dashboard-metrics.md) | [Escalation Procedures →](../playbooks/escalation-procedures.md)
