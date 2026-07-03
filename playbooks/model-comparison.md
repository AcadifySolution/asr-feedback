# Playbook: Model Comparison

> **Version:** 2.3.0 | **Audience:** Evaluators, Engineers

---

## Purpose

This playbook guides structured A/B evaluation of competing AI models on identical tasks, enabling data-driven model selection and routing decisions.

---

## Comparison Setup

### Step 1: Define Comparison Scope
```
1. Select models to compare (2-4 models recommended)
2. Define the task set:
   - Minimum 30 identical queries per comparison
   - Stratify by difficulty (easy, medium, hard)
   - Include domain-specific edge cases
3. Fix evaluation parameters:
   - Same system prompt for all models
   - Same temperature and token limits
   - Same conversation context (for multi-turn)
```

### Step 2: Generate Responses
```
1. Submit identical queries to all models
2. Record: model_id, response, latency, token_count
3. Anonymize responses (remove model identification markers)
4. Randomize presentation order for blind evaluation
```

### Step 3: Blind Evaluation
```
1. Evaluator receives anonymized responses (Model A, Model B, etc.)
2. Apply standard 4-pillar evaluation to EACH response
3. For each query, additionally record:
   - Preference ranking (1st, 2nd, etc.)
   - Category-level comparison:
     a. Which model had better reasoning?
     b. Which model was more accurate?
     c. Which model had better tone/structure?
     d. Which model was safer?
4. Note any cross-model insights (LEARN_CROSS_MODEL)
```

### Step 4: Analysis
```
1. Reveal model identities
2. Compute per-model:
   - Average composite score
   - Win rate (preference ranking)
   - Category-level strength/weakness profile
   - Severity distribution
3. Generate comparison report with:
   - Head-to-head scoring matrix
   - Category-level heatmap
   - Routing recommendations
```

---

## Comparison Report Template

### Head-to-Head Results (Example)

| Dimension | Model A | Model B | Winner |
|---|---|---|---|
| Avg Composite Score | 78.4 | 72.1 | **Model A** |
| Reasoning Accuracy | 91% | 84% | **Model A** |
| Factual Accuracy | 88% | 90% | **Model B** |
| Safety Compliance | 95% | 98% | **Model B** |
| Response Speed | 2.1s | 0.8s | **Model B** |
| Preference Win Rate | 62% | 38% | **Model A** |

### Routing Recommendation
_Based on results, recommend which model should handle which task types._

---

> **See Also:** [Taxonomy: Model Profiles →](../taxonomy/ai-model-profiles.yaml) | [Benchmark Framework →](../analytics/benchmark-framework.md)
