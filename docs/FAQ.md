# Frequently Asked Questions

> **Document Version:** 2.3.0 | **Last Updated:** 2026-07-01

---

## Table of Contents

- [General](#general)
- [Methodology](#methodology)
- [Integration](#integration)
- [Quality & Reliability](#quality--reliability)
- [Data & Privacy](#data--privacy)
- [Pricing & Plans](#pricing--plans)

---

## General

### What is ASR Feedback?

ASR Feedback is an enterprise AI Response Quality Intelligence service operated by Acadify Solutions. We provide structured, multi-dimensional feedback on AI-generated responses using our proprietary 4-Pillar Methodology (Good, Bad, Learned, Remember). We help AI teams identify issues, reinforce strengths, capture novel insights, and build persistent institutional memory.

### Who is ASR Feedback for?

ASR Feedback is designed for organizations that build, deploy, or operate:
- Large Language Models (LLMs) — GPT, Claude, Gemini, Llama, etc.
- AI Agents — LangChain, AutoGen, CrewAI, custom agent frameworks
- Code Generation Tools — GitHub Copilot, Cursor, Codex, custom tools
- Conversational AI — Customer support bots, virtual assistants
- Domain-Specific AI — Medical, legal, financial, educational AI systems

### How is ASR Feedback different from traditional data labeling?

| Aspect | Traditional Data Labeling | ASR Feedback |
|---|---|---|
| **Depth** | Binary (correct/incorrect) or simple categories | 4-dimensional analysis with severity, root cause, and remediation |
| **Insight Capture** | Not captured | Dedicated Learning Capture pillar |
| **Institutional Memory** | None | Memory Persistence pillar with durable rules |
| **Quality Control** | Basic consensus voting | Calibrated evaluators with κ ≥ 0.80 |
| **Actionability** | Labels for training data | Actionable intelligence for improvement |

### What AI models do you evaluate?

We evaluate responses from any AI system, including GPT-4o/4.1, Claude Opus/Sonnet, Gemini 2.5 Pro/Flash, Llama 3.x, Mistral, DeepSeek, and custom fine-tuned models. We also evaluate agent frameworks (LangChain, AutoGen, CrewAI) and multimodal systems.

---

## Methodology

### What are the 4 Pillars?

1. **✅ Good Signal** — What the AI did well (reinforcement)
2. **❌ Bad Signal** — What the AI did poorly (correction + severity)
3. **📘 Learning Capture** — Novel insights discovered during evaluation
4. **🧠 Memory Persistence** — Durable rules that must be applied in future evaluations

See [Methodology](METHODOLOGY.md) for the complete deep dive.

### What does the quality score (0-100) mean?

| Range | Band | Meaning |
|---|---|---|
| 90–100 | Excellent | Exceptional quality, minimal issues |
| 75–89 | Good | Strong quality, minor issues only |
| 60–74 | Acceptable | Adequate, some issues needing attention |
| 40–59 | Poor | Below expectations, significant issues |
| 0–39 | Critical | Unacceptable, major remediation needed |

### How do severity levels work?

| Level | Name | Impact |
|---|---|---|
| P0 | Critical | User safety risk, data breach, harmful content |
| P1 | High | Major factual errors, significant hallucinations |
| P2 | Medium | Moderate quality issues, reasoning gaps |
| P3 | Low | Minor issues — tone, formatting, slight redundancy |
| P4 | Trivial | Cosmetic issues, marginal improvement suggestions |

### What happens to "Learned" insights?

Every insight captured through the Learning pillar goes through a review process:
1. Evaluated for novelty and significance
2. Tagged with domain and model context
3. Analyzed for cross-client patterns (anonymized)
4. Fed back to client as actionable recommendations
5. Used to refine evaluation criteria over time

### What happens to "Remember" rules?

Memory rules follow a lifecycle: Proposed → Reviewed → Active → Applied → Quarterly Review → Reconfirmed/Deprecated. Active rules are applied by all evaluators in every future session for the applicable scope (per-client, per-domain, or global).

---

## Integration

### How do I integrate with ASR Feedback?

Three options:
1. **REST API** — Direct HTTP integration for full control
2. **Python SDK** — `pip install asr-feedback-client`
3. **JavaScript SDK** — `npm install @asr-feedback/client`

See the [Integration Guide](INTEGRATION_GUIDE.md) for step-by-step instructions.

### How long does integration take?

| Integration Type | Typical Time |
|---|---|
| SDK integration | 2–4 hours |
| REST API integration | 1–2 days |
| Custom integration (webhook + batch) | 3–5 days |

### Can I submit historical data?

Yes. Use the Batch Upload API to submit historical AI responses for evaluation. This is commonly used during initial onboarding to establish a quality baseline.

### Do you support real-time evaluation?

Yes. Enterprise Critical tier clients receive evaluation turnaround within 2 hours. For sub-minute feedback, we offer a pre-screening API that provides automated initial assessment (note: human-in-the-loop deep evaluation follows).

---

## Quality & Reliability

### How do you ensure feedback consistency?

1. **Calibrated Evaluators** — All evaluators must achieve and maintain κ ≥ 0.80
2. **Dual Evaluation** — 10% of entries are independently evaluated by two evaluators
3. **Regular Audits** — 5% real-time audit, daily spot checks, weekly deep audits
4. **Gold Standard Calibration** — Monthly calibration against benchmark datasets
5. **Memory Rules** — Persistent rules ensure consistent treatment of recurring scenarios

See [Quality Framework](QUALITY_FRAMEWORK.md) for details.

### What is your inter-rater reliability?

Current Cohen's Kappa: **0.87** (target: ≥ 0.80). This means substantial agreement between independent evaluators, accounting for chance agreement.

### How do you handle evaluator disagreements?

When dual evaluations disagree beyond acceptable thresholds, a senior evaluator adjudicates. The adjudication rationale is documented and used to update calibration materials.

---

## Data & Privacy

### How do you handle client data?

- All data is encrypted at rest (AES-256) and in transit (TLS 1.3)
- PII is automatically detected and redacted before evaluation
- Client data is never shared across clients
- Full audit trail on all data access
- Data retention follows client-specific agreements (default: 24 months)

See [Privacy Framework](../compliance/privacy-framework.md) for details.

### Can I delete my data?

Yes. Clients can request data deletion at any time. We comply within 30 days per our data handling policy.

### Do you use our data to train models?

No. Client data is used exclusively for the contracted evaluation service. We do not use client data for model training, benchmarking, or any purpose beyond the agreed scope.

---

## Pricing & Plans

### What are the service tiers?

| Tier | Monthly Volume | Turnaround SLA | Features |
|---|---|---|---|
| **Standard** | Up to 500 entries | 24 hours | Core 4-pillar feedback |
| **Professional** | Up to 2,000 entries | 8 hours | + Analytics dashboard |
| **Enterprise Standard** | Up to 5,000 entries | 4 hours | + Custom taxonomy, SDK access |
| **Enterprise Critical** | Unlimited | 2 hours | + Priority queue, dedicated team |

### How is pricing structured?

Pricing is based on:
1. Monthly evaluation volume
2. Turnaround SLA tier
3. Number of AI models under evaluation
4. Custom requirements (domain-specific expertise, compliance, etc.)

Contact your account manager or email sales@acadifysolutions.com for a customized quote.

### Is there a free trial?

Yes. We offer a 2-week pilot program with 50 evaluation entries to demonstrate our methodology and impact. Contact us to get started.

---

> **See Also:**
> - [Methodology →](METHODOLOGY.md)
> - [Integration Guide →](INTEGRATION_GUIDE.md)
> - [Quality Framework →](QUALITY_FRAMEWORK.md)
> - [Glossary →](GLOSSARY.md)
