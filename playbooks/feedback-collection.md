# Playbook: Feedback Collection

> **Version:** 2.3.0 | **Audience:** Evaluators

---

## Purpose

This playbook guides evaluators through the complete feedback collection process — from session setup through submission. Follow these steps for every evaluation session.

---

## Pre-Session Setup (5-10 minutes)

### Step 1: Review Session Assignment
```
1. Open your assigned session in the evaluation dashboard
2. Note: Client ID, Model ID, Domain, Expected volume
3. Verify your calibration score is current (≥ 0.80)
```

### Step 2: Load Context
```
1. Review the client's evaluation guidelines (if custom)
2. Load active memory rules for:
   a. This client (MEM_CLIENT_PREF)
   b. This domain (MEM_DOMAIN_RULE)
   c. This model (MEM_MODEL_BEHAVIOR)
   d. Global safety rules (MEM_SAFETY_RULE)
3. Review the model profile in taxonomy/ai-model-profiles.yaml
4. Open relevant reference materials for the domain
```

### Step 3: Initialize Session
```
1. Create session record with session template
2. Start session timer
3. Confirm all pre-session checklist items
```

---

## Evaluation Process (Per Response)

### Step 4: First-Pass Read
```
1. Read the complete user query
2. Read the complete AI response WITHOUT annotating
3. Form an initial impression of overall quality
4. Note any immediate red flags (safety, hallucination)
```

> ⚠️ **If you detect a P0 issue during first-pass, STOP and escalate immediately per the Escalation Procedures playbook.**

### Step 5: Good Signal Pass (✅)
```
1. Re-read the response looking ONLY for positive behaviors
2. For each good signal found:
   a. Identify the category code (GOOD_REASONING, GOOD_FACTUAL, etc.)
   b. Write a specific description (≥10 characters)
   c. Quote exact evidence from the response
   d. Assign reinforcement value (0.0-1.0)
3. Aim for at least 1 good signal per response
   (if truly none exist, document why)
```

### Step 6: Bad Signal Pass (❌)
```
1. Re-read the response looking ONLY for issues and errors
2. For each bad signal found:
   a. Identify the category code
   b. Assign severity level (P0-P4)
   c. Write a specific description
   d. Quote exact evidence
   e. Analyze root cause (WHY did this happen?)
   f. Write remediation recommendation
3. Verify all claims before marking as BAD_FACTUAL or BAD_HALLUCINATION
```

### Step 7: Learning Capture Pass (📘)
```
1. Consider: Did this evaluation reveal anything NEW?
2. Ask yourself:
   - Is there a pattern I'm seeing across multiple responses?
   - Is there an edge case the model handled unusually?
   - Is there a capability boundary I discovered?
   - Is there a prompt sensitivity I noticed?
3. For each learning:
   a. Identify category code
   b. Document observation with context
   c. Provide supporting evidence
   d. Explain the implication
   e. Recommend an action
```

### Step 8: Memory Check Pass (🧠)
```
1. Check: Were all applicable memory rules followed?
   - If violated, note in bad signals
2. Check: Should any new memory rules be created?
   - Client preferences discovered?
   - Safety boundaries identified?
   - Domain-specific rules needed?
   - Model-specific behaviors noted?
3. For new rules:
   a. Select rule type
   b. Write clear, unambiguous rule text
   c. Define scope (global, client, domain, model)
   d. Set expiration (null for indefinite)
```

### Step 9: Score the Response
```
1. Assign component scores:
   - Good Signal Score (0-100)
   - Bad Signal Penalty (0 to -100)
   - Severity Impact (0 to -100)
   - Completeness Score (0-100)
   - Consistency Score (0-100)
2. Calculate composite score using formula:
   Composite = (Good × 0.25) + ((100 + BadPenalty) × 0.30) + 
               ((100 + SeverityImpact) × 0.20) + 
               (Completeness × 0.15) + (Consistency × 0.10)
3. Verify the composite score falls in the expected band
4. Cross-check: Does the score feel right given your overall impression?
```

### Step 10: Self-Review
```
Before submitting each entry, verify:
- [ ] All 4 pillars addressed (even if some are empty arrays)
- [ ] All descriptions are ≥10 characters and specific
- [ ] All entries have evidence citations
- [ ] Severity levels are calibrated correctly
- [ ] Memory rules were checked and applied
- [ ] Quality score is consistent with annotations
- [ ] No PII in any text fields
```

---

## Post-Session (10-15 minutes)

### Step 11: Generate Session Report
```
1. Review all entries for consistency across the session
2. Identify the top 3 issues (by frequency and severity)
3. Summarize key learnings
4. List new memory rules
5. Write 3-5 recommendations for the client
6. Submit the session report
```

### Step 12: Complete Post-Session Checklist
```
- [ ] All entries submitted and schema-validated
- [ ] Session report generated and submitted
- [ ] New memory rules submitted for review
- [ ] Any P0/P1 escalations completed
- [ ] Session timer stopped
- [ ] Session feedback form completed (self-assessment)
```

---

## Common Pitfalls

| Pitfall | How to Avoid |
|---|---|
| Forgetting to check memory rules | Always load memory rules in pre-session setup |
| Vague descriptions | Use the "specific enough to reproduce" test |
| Missing evidence citations | Treat evidence as mandatory, never optional |
| Severity inflation/deflation | Calibrate against the severity levels taxonomy |
| Skipping the learning pillar | Ask "what's new?" for every response |
| Score-annotation mismatch | Review score against annotations before submitting |
