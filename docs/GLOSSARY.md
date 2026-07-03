# Glossary

> **Document Version:** 2.3.0 | **Last Updated:** 2026-07-01

---

This glossary defines key terms, concepts, and abbreviations used throughout the ASR Feedback Intelligence Platform documentation.

---

## A

**AGI (Artificial General Intelligence):** An AI system with the ability to understand, learn, and apply knowledge across a wide range of tasks at a human-equivalent level. ASR Feedback evaluates AGI-class systems alongside narrower AI tools.

**Annotation:** The act of attaching structured feedback to a specific AI response. In ASR's methodology, annotations are organized across four pillars: Good, Bad, Learned, and Remember.

**Audit Trail:** An immutable, chronological record of all actions taken on a feedback entry — from creation through review and any modifications. See [compliance/audit-trail.md](../compliance/audit-trail.md).

## B

**Bad Signal:** Pillar 2 of the ASR 4-Pillar Methodology. Captures what the AI response did poorly — errors, failures, and quality gaps requiring correction. See [METHODOLOGY.md](METHODOLOGY.md).

## C

**Calibration:** The process of ensuring evaluators apply consistent standards when scoring and annotating. New evaluators undergo a multi-phase calibration process, and ongoing calibration is maintained through monthly exercises.

**Calibration Score:** A numeric score (0.0–1.0) representing an evaluator's agreement with gold-standard annotations. Minimum threshold for independent evaluation: 0.80.

**Category Code:** A standardized identifier for a specific type of feedback (e.g., `GOOD_REASONING`, `BAD_HALLUCINATION`, `LEARN_EDGE_CASE`). Defined in the [taxonomy](../taxonomy/).

**Cohen's Kappa (κ):** A statistical measure of inter-rater reliability that accounts for chance agreement. ASR targets κ ≥ 0.80 across all evaluators.

**Composite Score:** The overall quality score (0–100) assigned to an AI response, calculated as a weighted combination of Good Signal Score, Bad Signal Penalty, Severity Impact, Completeness Score, and Consistency Score.

## D

**Domain Tag:** A classification label indicating the industry or subject area of an AI response (e.g., healthcare, finance, education). Defined in [taxonomy/domain-tags.yaml](../taxonomy/domain-tags.yaml).

**Dual Evaluation:** The process of having two independent evaluators assess the same AI response, used for 10% of all entries to measure inter-rater reliability.

## E

**Entry ID:** The unique identifier for a single feedback entry. Format: `FB-YYYY-NNNN-NNN` (e.g., `FB-2026-0547-001`).

**Evaluator:** A trained, calibrated human expert who performs 4-pillar analysis on AI responses. All evaluators must maintain a calibration score ≥ 0.80.

**Evidence:** Specific quotes, line numbers, or references from the AI response that support a feedback annotation. All annotations must include evidence.

## F

**Feedback Entry:** The atomic unit of the ASR Feedback system. A single, schema-validated annotation capturing observations across all four pillars for one AI response. See [FEEDBACK_SCHEMA.md](FEEDBACK_SCHEMA.md).

**Four Pillars:** The core framework of ASR's methodology: ✅ Good Signal, ❌ Bad Signal, 📘 Learning Capture, 🧠 Memory Persistence.

## G

**Gold Standard:** A set of pre-evaluated AI responses with "correct" annotations, used for calibration and inter-rater reliability measurement.

**Good Signal:** Pillar 1 of the ASR 4-Pillar Methodology. Captures what the AI response did well — behaviors, reasoning, and qualities to reinforce.

## H

**Hallucination:** An AI-generated claim that is factually incorrect, fabricated, or unsupported by any source. Classified as `BAD_HALLUCINATION` with typical severity P0–P1.

## I

**Inter-Rater Reliability (IRR):** The degree of agreement among independent evaluators. Measured using Cohen's Kappa (κ) and Krippendorff's Alpha.

## K

**Krippendorff's Alpha:** A reliability coefficient for measuring agreement among multiple raters, accommodating ordinal, nominal, and interval data. ASR targets α ≥ 0.80.

## L

**Learning Capture:** Pillar 3 of the ASR 4-Pillar Methodology. Records novel insights, edge cases, and discoveries that emerge during evaluation.

**LLM (Large Language Model):** A neural network trained on large text corpora to generate human-like text. Examples: GPT-4o, Claude, Gemini, Llama.

## M

**Memory Persistence:** Pillar 4 of the ASR 4-Pillar Methodology. Creates durable institutional memory — persistent rules, client preferences, and critical guardrails.

**Memory Rule:** A persistent evaluation rule stored in the Memory Store. Types include Client Preference, Safety Rule, Domain Rule, Model Behavior, Correction Pattern, and Quality Standard.

## N

**NPS (Net Promoter Score):** A client satisfaction metric calculated as `% Promoters - % Detractors`. Scale: -100 to +100.

## P

**P0 / P1 / P2 / P3 / P4:** Severity levels for Bad Signal classifications. P0 = Critical (safety risk), P4 = Trivial (cosmetic). See [taxonomy/severity-levels.yaml](../taxonomy/severity-levels.yaml).

**Pillar:** One of the four dimensions of ASR's feedback methodology. Each pillar captures a distinct type of signal from the evaluation.

## Q

**Quality Score:** See Composite Score.

## R

**Reinforcement Value:** A numeric score (0.0–1.0) assigned to Good Signal entries, indicating how strongly the positive behavior should be reinforced in training.

**Remediation:** A concrete recommendation for fixing an issue identified in a Bad Signal annotation.

**Root Cause:** The underlying reason why an AI response exhibited a particular bad behavior (e.g., "Training data may not include asymptomatic presentations").

## S

**Schema Validation:** The process of checking that a data payload conforms to its formal JSON Schema definition. All feedback entries must pass schema validation before storage.

**Session:** A bounded period during which an evaluator reviews multiple AI responses. Sessions have a start time, end time, and are associated with a specific client and model.

**Severity Level:** A P0–P4 classification indicating the impact of a Bad Signal. See [METHODOLOGY.md](METHODOLOGY.md).

**SLA (Service Level Agreement):** Contractual commitments for feedback turnaround time, quality standards, and availability. See [compliance/sla-definitions.md](../compliance/sla-definitions.md).

## T

**Taxonomy:** The hierarchical classification system for feedback categories, severity levels, model profiles, and domain tags. See [taxonomy/](../taxonomy/).

**Turnaround Time:** The elapsed time between an AI response being submitted for evaluation and the completed feedback being delivered to the client.

---

> **See Also:**
> - [Methodology →](METHODOLOGY.md)
> - [Feedback Schema →](FEEDBACK_SCHEMA.md)
> - [Taxonomy →](../taxonomy/)
> - [FAQ →](FAQ.md)
