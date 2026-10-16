# ASR Feedback — AI Response Evaluation Toolkit

Organize human feedback on LLM answers using JSON Schemas, example records,
Python and JavaScript SDK source, review templates, and quality playbooks.
Maintained by [Acadify Solution](https://github.com/AcadifySolution).

This repository provides reference materials and client source. It does not
include a hosted evaluation service or a complete server implementation. API
examples require a compatible backend that you operate or separately arrange.

## Start with a feedback record

1. Read the [four-pillar methodology](docs/METHODOLOGY.md): Good, Bad, Learned,
   and Remember.
2. Inspect the [feedback schema](schemas/feedback-entry.schema.json) and
   [example payloads](schemas/examples/).
3. Validate the included examples locally:

   ```bash
   git clone https://github.com/AcadifySolution/asr-feedback.git
   cd asr-feedback
   python -m pip install jsonschema
   python scripts/validate_schemas.py
   ```

4. Adapt the [feedback session template](templates/feedback-session.md) to your
   use case and run an independent review using the [quality playbook](playbooks/quality-review.md).

Keep real customer data, credentials, and sensitive prompts out of public issues
and sample records. See the [security policy](SECURITY.md).

## Find the right material

| Need                                      | Starting point                                                           |
| ----------------------------------------- | ------------------------------------------------------------------------ |
| Understand the proposed system            | [Architecture](docs/ARCHITECTURE.md)                                     |
| Structure feedback and session reports    | [Schemas](schemas/) and [schema guide](docs/FEEDBACK_SCHEMA.md)          |
| Integrate client source with your backend | [SDK source](sdk/) and [integration guide](docs/INTEGRATION_GUIDE.md)    |
| Define review criteria                    | [Quality framework](docs/QUALITY_FRAMEWORK.md) and [taxonomy](taxonomy/) |
| Run a review process                      | [Playbooks](playbooks/) and [templates](templates/)                      |
| Explore proposed reporting formats        | [Sample reports](reports/) and [analytics guidance](analytics/)          |
| Review data handling proposals            | [Governance documentation](compliance/)                                  |

Documentation describes proposed practices and illustrative examples. It is not
an independently audited record of client deployments, certifications, service
availability, or operational results. Review and validate each practice for your
own implementation before adoption.

## Measure quality with your own evidence

| Question                    | Evidence to collect                                                                 |
| --------------------------- | ----------------------------------------------------------------------------------- |
| Do reviewers agree?         | Independently rated samples, rubric version, and an agreement calculation           |
| Are feedback records valid? | Schema version and validation results for the actual dataset                        |
| Does a model change help?   | A held-out dataset, baseline and candidate versions, and comparable evaluation runs |
| How fast is review?         | Recorded submission and completion timestamps                                       |
| Which errors recur?         | Versioned severity labels and issue counts over comparable periods                  |

No measured client outcomes, adoption totals, or benchmark improvements are
claimed by this README. Examples in linked documents are reference material;
validate any quantitative claims against primary evidence before reusing them.

## Related projects and contributions

Use [AI Evals Framework](https://github.com/AcadifySolution/ai-evals-framework)
for automated dataset-based evaluation alongside human feedback.
The [organisation project directory](https://github.com/AcadifySolution) lists
related RAG, fine-tuning, and agent tools.

If this toolkit helps, star it to save it or fork it to adapt the schemas.
Contributions should include a reproducible example and validation results;
follow [CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md).

## License

[MIT](LICENSE).
