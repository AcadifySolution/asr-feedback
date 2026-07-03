# Benchmark Framework

> **Version:** 2.3.0 | **Last Updated:** 2026-07-01

---

## Overview

The ASR Benchmark Framework provides a standardized methodology for comparing AI model quality across time, models, and domains.

---

## Benchmark Types

| Type | Purpose | Frequency |
|---|---|---|
| **Baseline Benchmark** | Establish initial quality metrics for a new client/model | At onboarding |
| **Progress Benchmark** | Measure quality improvement over time | Monthly |
| **Comparative Benchmark** | A/B comparison between models on identical tasks | On demand |
| **Domain Benchmark** | Quality standards by industry domain | Quarterly |

---

## Benchmark Dataset

Each benchmark uses a curated dataset of evaluation tasks:

| Category | Count | Difficulty Distribution |
|---|---|---|
| Question Answering | 50 | 15 Easy / 20 Medium / 15 Hard |
| Code Generation | 30 | 10 Easy / 10 Medium / 10 Hard |
| Summarization | 30 | 10 Easy / 10 Medium / 10 Hard |
| Creative Writing | 20 | 5 Easy / 10 Medium / 5 Hard |
| Reasoning | 30 | 5 Easy / 10 Medium / 15 Hard |
| Conversation (Multi-turn) | 20 | 5 Easy / 10 Medium / 5 Hard |
| **Total** | **180** | |

---

## Benchmark Scoring

```
Benchmark Score = Weighted Average of:
  - Composite Quality Score (50%)
  - Category-Level Accuracy (25%)
  - Safety Compliance Rate (15%)
  - Completeness Rate (10%)
```

### Benchmark Grades

| Grade | Score Range | Description |
|---|---|---|
| A+ | 95–100 | Exceptional — top-tier quality across all dimensions |
| A | 90–94 | Excellent — consistently high quality |
| B+ | 85–89 | Very Good — strong with minor gaps |
| B | 80–84 | Good — meets enterprise standards |
| C+ | 75–79 | Adequate — acceptable but room for improvement |
| C | 70–74 | Below Standard — needs focused improvement |
| D | 60–69 | Poor — significant quality gaps |
| F | <60 | Failing — fundamental issues requiring remediation |

---

## Running a Benchmark

1. Select benchmark dataset (standard or custom)
2. Generate responses from target model(s)
3. Evaluate all responses using standard 4-pillar methodology
4. Compute benchmark scores and grades
5. Generate comparative report
6. Store results for trend tracking

---

> **See Also:** [Model Comparison Playbook →](../playbooks/model-comparison.md) | [Scoring Algorithm →](scoring-algorithm.md)
