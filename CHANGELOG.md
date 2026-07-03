# Changelog

All notable changes to the ASR Feedback Intelligence Platform are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.3.0] — 2026-07-01

### Added
- **Multimodal Feedback Support** — Extended feedback schema to capture evaluations of image, audio, and video AI outputs alongside text
- **Model Comparison Playbook** — New operational playbook for structured A/B evaluation of competing AI models ([playbooks/model-comparison.md](playbooks/model-comparison.md))
- **Confidence Score Field** — Added `confidenceScore` (0.0–1.0) to feedback entries for reviewer certainty tracking
- **Domain Tags Taxonomy** — Introduced industry-specific tagging system with 12 domains ([taxonomy/domain-tags.yaml](taxonomy/domain-tags.yaml))
- **JavaScript SDK** — Client library for JavaScript/Node.js environments ([sdk/javascript/](sdk/javascript/))

### Changed
- **Quality Scoring Algorithm** — Updated composite score calculation to weight severity levels dynamically based on client risk profile
- **Session Report Schema** — Added optional `environmentMetadata` block for capturing model configuration details
- **Escalation Procedures** — Refined P0 escalation path to include real-time notification channel

### Fixed
- **Schema Validation** — Corrected `additionalProperties` handling in nested objects within `feedback-entry.schema.json`
- **Taxonomy Typos** — Fixed category descriptions in `categories.yaml` for clarity

---

## [2.2.0] — 2026-05-15

### Added
- **Benchmark Framework** — Comprehensive methodology for benchmarking AI model quality over time ([analytics/benchmark-framework.md](analytics/benchmark-framework.md))
- **Audit Trail Specification** — Formal specification for immutable audit logging ([compliance/audit-trail.md](compliance/audit-trail.md))
- **Client Onboarding Template** — Structured onboarding checklist for new client engagements ([templates/client-onboarding.md](templates/client-onboarding.md))
- **SLA Definitions** — Service level agreements with measurable targets ([compliance/sla-definitions.md](compliance/sla-definitions.md))

### Changed
- **Architecture Documentation** — Updated data flow diagrams to reflect new intelligence layer components
- **Python SDK** — Added retry logic and exponential backoff for API calls

### Security
- **PII Detection** — Enhanced privacy framework with automated PII pattern detection rules

---

## [2.1.0] — 2026-03-01

### Added
- **Trend Analysis Module** — Methodology for detecting quality trends across sessions and time periods ([analytics/trend-analysis.md](analytics/trend-analysis.md))
- **Incident Report Template** — Standardized template for documenting AI response incidents ([templates/incident-report.md](templates/incident-report.md))
- **FAQ Document** — Comprehensive FAQ addressing common client and stakeholder questions ([docs/FAQ.md](docs/FAQ.md))

### Changed
- **Methodology Documentation** — Expanded inter-rater reliability section with calibration procedures
- **Quality Framework** — Added continuous improvement feedback loops

### Fixed
- **Schema Example** — Corrected timestamp format in session-report example to ISO 8601

---

## [2.0.0] — 2025-12-01

### Added
- **4-Pillar Feedback Methodology** — Complete redesign of feedback framework introducing the Good/Bad/Learned/Remember paradigm
- **JSON Schema Validation** — Formal schemas for all data entities using JSON Schema Draft 7
- **Python SDK** — Client library for programmatic feedback submission and retrieval
- **Compliance Suite** — Data handling, privacy, and governance documentation
- **GitHub CI/CD** — Automated schema validation and documentation linting

### Changed
- **BREAKING:** Feedback entry structure redesigned — all v1.x integrations require migration
- **BREAKING:** API endpoints restructured for RESTful consistency
- **Quality Scoring** — Migrated from simple pass/fail to composite 0–100 scoring system

### Removed
- **Legacy Annotation Format** — Removed support for v1.x flat-file annotation format
- **Manual Validation Scripts** — Replaced by automated CI/CD schema validation

### Migration Guide
See [docs/INTEGRATION_GUIDE.md](docs/INTEGRATION_GUIDE.md) for v1.x → v2.x migration instructions.

---

## [1.2.0] — 2025-08-15

### Added
- Severity level classification (P0–P4)
- Weekly report template
- Basic quality scoring rubric

### Changed
- Expanded feedback categories from 8 to 24

---

## [1.1.0] — 2025-05-01

### Added
- Monthly review template
- Glossary of domain terms
- Initial case studies (anonymized)

### Fixed
- Documentation cross-reference links

---

## [1.0.0] — 2025-02-01

### Added
- Initial release of ASR Feedback platform
- Basic feedback schema (Good/Bad binary format)
- Core documentation (architecture, methodology)
- Simple annotation guidelines
- Internal playbooks for feedback collection

---

<p align="center">
  <em>For older versions, see the <a href="https://github.com/acadify-solutions/asr-feedback/releases">GitHub Releases</a> page.</em>
</p>
