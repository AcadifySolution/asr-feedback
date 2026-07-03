# Scoring Algorithm

> **Version:** 2.3.0 | **Last Updated:** 2026-07-01

---

## Overview

The ASR Feedback composite quality score (0–100) is a weighted combination of five sub-scores that holistically assess the quality of an AI-generated response.

---

## Formula

```
CompositeScore = clamp(0, 100,
    GoodSignalScore       × W_good       +
    (100 + BadSignalPenalty) × W_bad      +
    (100 + SeverityImpact)  × W_severity  +
    CompletenessScore       × W_completeness +
    ConsistencyScore        × W_consistency
)
```

### Default Weights

| Component | Weight | Rationale |
|---|---|---|
| Good Signal Score | 0.25 | Positive behaviors should be recognized but not dominate |
| Bad Signal Penalty | 0.30 | Issues have the highest impact on overall quality |
| Severity Impact | 0.20 | Severity amplifies the bad signal penalty for critical issues |
| Completeness Score | 0.15 | Missing information is a distinct quality dimension |
| Consistency Score | 0.10 | Consistency with established patterns |

> **Note:** Weights are configurable per client. Financial services clients may increase the Bad Signal weight; educational clients may increase Completeness weight.

---

## Sub-Score Calculations

### Good Signal Score (0–100)

```python
def calculate_good_signal_score(good_signals):
    """
    Score based on the number and quality of positive behaviors identified.
    """
    if not good_signals:
        return 0
    
    category_weights = {
        "GOOD_REASONING": 1.5,
        "GOOD_FACTUAL": 1.5,
        "GOOD_CONTEXT": 1.2,
        "GOOD_CREATIVE": 1.2,
        "GOOD_STRUCTURE": 1.0,
        "GOOD_TONE": 1.0,
        "GOOD_SAFETY": 1.0,
        "GOOD_TOOL_USE": 1.0,
    }
    
    weighted_sum = sum(
        category_weights.get(signal.category_code, 1.0) * signal.reinforcement_value
        for signal in good_signals
    )
    
    # Normalize: max possible is ~5 high-value signals with max reinforcement
    max_possible = 5 * 1.5 * 1.0  # 7.5
    score = min(100, (weighted_sum / max_possible) * 100)
    return round(score, 1)
```

### Bad Signal Penalty (-100 to 0)

```python
def calculate_bad_signal_penalty(bad_signals):
    """
    Penalty based on the number and type of issues identified.
    Each issue reduces the score proportionally.
    """
    if not bad_signals:
        return 0  # No penalty
    
    # Each bad signal contributes a penalty proportional to its count
    penalty_per_signal = -8  # Base penalty per issue
    total_penalty = len(bad_signals) * penalty_per_signal
    
    return max(-100, total_penalty)
```

### Severity Impact (-100 to 0)

```python
def calculate_severity_impact(bad_signals):
    """
    Additional penalty based on the severity of issues.
    P0 issues dominate; P4 issues have minimal impact.
    """
    severity_multipliers = {
        0: -40,  # P0: Critical — single P0 has massive impact
        1: -15,  # P1: High
        2: -8,   # P2: Medium
        3: -3,   # P3: Low
        4: -1,   # P4: Trivial
    }
    
    total_impact = sum(
        severity_multipliers.get(signal.severity, -5)
        for signal in bad_signals
    )
    
    return max(-100, total_impact)
```

### Completeness Score (0–100)

Measures how thoroughly the AI response addressed the task:

| Criteria | Weight | Scoring |
|---|---|---|
| Core question answered | 0.40 | Full/Partial/Missing |
| Supporting details provided | 0.25 | Comprehensive/Adequate/Sparse |
| Edge cases addressed | 0.20 | Proactive/On-demand/Absent |
| Actionable next steps | 0.15 | Clear/Vague/Missing |

### Consistency Score (0–100)

Measures alignment with established quality patterns:

- Consistency with memory rules (weighted highest)
- Consistency with previous evaluations of similar responses
- Consistency with domain-specific quality standards

---

## Score Band Classification

```python
def classify_score(composite):
    """Classify a composite score into a quality band."""
    if composite >= 90:
        return "excellent"
    elif composite >= 75:
        return "good"
    elif composite >= 60:
        return "acceptable"
    elif composite >= 40:
        return "poor"
    else:
        return "critical"
```

---

## Example Calculation

Given a response with:
- 3 good signals (GOOD_FACTUAL: 0.9, GOOD_STRUCTURE: 0.8, GOOD_CONTEXT: 0.75)
- 1 bad signal (BAD_INCOMPLETE, P2)
- Completeness: 72/100
- Consistency: 91/100

```
Good Signal Score = ((1.5 × 0.9) + (1.0 × 0.8) + (1.2 × 0.75)) / 7.5 × 100 = 45.3
Bad Signal Penalty = 1 × (-8) = -8
Severity Impact = -8 (one P2 issue)

Composite = (45.3 × 0.25) + ((100 + (-8)) × 0.30) + ((100 + (-8)) × 0.20) + (72 × 0.15) + (91 × 0.10)
         = 11.33 + 27.60 + 18.40 + 10.80 + 9.10
         = 77.23

Band: "good"
```

---

> **See Also:** [Quality Framework →](../docs/QUALITY_FRAMEWORK.md) | [Feedback Schema →](../docs/FEEDBACK_SCHEMA.md)
