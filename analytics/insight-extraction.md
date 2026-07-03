# Insight Extraction

> **Version:** 2.3.0 | **Last Updated:** 2026-07-01

---

## Overview

Insight extraction transforms raw feedback data into actionable intelligence by identifying patterns, correlations, and systemic issues that individual feedback entries cannot reveal in isolation.

---

## Extraction Pipeline

```
Raw Feedback Entries
    → Aggregation (by model, domain, client, time period)
    → Pattern Detection (clustering similar observations)
    → Correlation Analysis (linking causes to effects)
    → Significance Testing (is this pattern real or noise?)
    → Insight Generation (actionable recommendations)
    → Prioritization (impact × confidence ranking)
    → Delivery (reports, dashboards, notifications)
```

---

## Pattern Categories

| Pattern | Detection Method | Example |
|---|---|---|
| **Systematic Error** | Same BAD category across 10%+ of entries in a model/domain | "GPT-4o consistently omits disclaimers in medical responses" |
| **Capability Cliff** | Sharp quality drop at specific task complexity threshold | "Quality drops 40% when code generation exceeds 100 lines" |
| **Context Window Effect** | Quality degradation correlated with conversation length | "Accuracy drops 20% after turn 8 in multi-turn conversations" |
| **Prompt Sensitivity** | Quality variation correlated with prompt phrasing | "Adding 'step by step' improves reasoning scores by 30%" |
| **Domain Transfer Gap** | Model trained for domain A performs poorly in domain B | "Finance fine-tuned model scores 25% lower on healthcare tasks" |
| **Temporal Regression** | Quality decline correlated with model version change | "June 20 deployment reduced completeness by 15%" |

---

## Insight Quality Criteria

Every generated insight must meet these criteria:

| Criterion | Description |
|---|---|
| **Evidence-Based** | Supported by quantitative data from 10+ feedback entries |
| **Statistically Significant** | Not explainable by random variation (p < 0.05 or practical significance) |
| **Actionable** | Clear recommendation for what to do with the insight |
| **Scoped** | Clearly states which models, domains, and clients are affected |
| **Prioritized** | Ranked by potential impact × confidence |

---

## Delivery Channels

| Channel | Content | Frequency | Audience |
|---|---|---|---|
| Session Reports | Session-level insights | Per session | Evaluators, Quality leads |
| Weekly Intelligence | Top patterns and trends | Weekly | Operations, Management |
| Monthly Deep Dive | Cross-client analysis | Monthly | Leadership, Stakeholders |
| Quarterly Intelligence | Strategic patterns | Quarterly | C-level, Board-ready |
| Real-Time Alerts | P0/P1 patterns | Immediate | All relevant stakeholders |

---

## Cross-Client Intelligence

Insights are anonymized and aggregated across clients to identify industry-wide patterns. No client-specific data is shared. Anonymized patterns include:

- Model-level quality trends (e.g., "GPT-4o v2025.06.20 shows 12% regression in completeness across 4 clients")
- Domain-specific challenges (e.g., "Medical AI systems universally struggle with asymptomatic condition information")
- Effective improvement strategies (e.g., "Adding regulatory citations to system prompts improves compliance by 45% on average")

---

> **See Also:** [Trend Analysis →](trend-analysis.md) | [Case Studies →](../docs/CASE_STUDIES.md) | [Metrics & KPIs →](../docs/METRICS_AND_KPIs.md)
