# Trend Analysis

> **Version:** 2.3.0 | **Last Updated:** 2026-07-01

---

## Overview

Trend analysis detects quality patterns over time — regressions, improvements, seasonal variations, and emerging issues before they become critical.

---

## Trend Types

| Type | Detection Method | Alert Threshold |
|---|---|---|
| **Score Regression** | 7-day moving average drops >5 points | Alert when sustained >3 days |
| **Severity Escalation** | P0/P1 rate exceeds target for 3+ consecutive days | Immediate alert |
| **Category Concentration** | Single category exceeds 40% of all bad signals | Alert in weekly report |
| **Improvement Trend** | 30-day moving average increases >3 points | Highlight in monthly report |
| **Seasonal Pattern** | Year-over-year comparison for volume and quality | Quarterly analysis |
| **Model Regression** | Quality drop correlated with model version change | Alert within 48 hours |

---

## Analysis Windows

| Window | Use Case | Metrics |
|---|---|---|
| **Daily** | Real-time monitoring | Entry count, avg score, P0/P1 count |
| **Weekly** | Operational trends | Score distribution, category trends, evaluator consistency |
| **Monthly** | Strategic analysis | Client-level trends, learning capture rates, memory growth |
| **Quarterly** | Business intelligence | Cross-client patterns, model evolution, capacity planning |

---

## Regression Detection Algorithm

```python
def detect_regression(scores, window=7, threshold=5.0):
    """
    Detect quality regression using moving average comparison.
    
    Returns: List of regression alerts with start date and magnitude.
    """
    if len(scores) < window * 2:
        return []  # Not enough data
    
    alerts = []
    for i in range(window, len(scores)):
        current_avg = sum(scores[i-window:i]) / window
        previous_avg = sum(scores[i-window*2:i-window]) / window
        
        delta = current_avg - previous_avg
        if delta < -threshold:
            alerts.append({
                "type": "regression",
                "magnitude": abs(delta),
                "period_start": i - window,
                "current_avg": current_avg,
                "previous_avg": previous_avg,
            })
    
    return alerts
```

---

## Actionable Outputs

| Alert | Action | Owner |
|---|---|---|
| Score regression detected | Investigate root cause, check for model updates | Quality Lead |
| Severity escalation | Escalate per procedures, notify client | Account Manager |
| Category concentration | Review taxonomy, check for systematic issue | Methodology Lead |
| Model regression | Compare model versions, alert client engineering | Quality Lead |

---

> **See Also:** [Metrics & KPIs →](../docs/METRICS_AND_KPIs.md) | [Dashboard →](../reports/dashboard-metrics.md)
