# Contributing to ASR Feedback

Thank you for your interest in contributing to the ASR Feedback Intelligence Platform. This document provides guidelines and standards for contributing to this repository.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Workflow](#development-workflow)
- [Style Guidelines](#style-guidelines)
- [Commit Message Convention](#commit-message-convention)
- [Pull Request Process](#pull-request-process)
- [Review Standards](#review-standards)

---

## Code of Conduct

This project adheres to our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

---

## How Can I Contribute?

### 🐛 Reporting Issues

Before creating an issue, please check existing issues to avoid duplicates. When reporting:

1. Use the appropriate [issue template](.github/ISSUE_TEMPLATE/)
2. Include a clear, descriptive title
3. Provide detailed reproduction steps (for bugs)
4. Include relevant schema versions and environment details

### 📝 Improving Documentation

Documentation improvements are always welcome:

- Fix typos, grammar, or unclear explanations
- Add missing examples or edge cases
- Improve schema documentation
- Update the glossary with new terms

### 🔧 Schema Changes

Schema modifications require extra rigor:

1. All changes must be backward-compatible unless a major version bump is planned
2. New fields must include descriptions, types, and examples
3. Example payloads must be updated to reflect changes
4. The `FEEDBACK_SCHEMA.md` documentation must be synchronized

### 📊 Taxonomy Updates

When adding or modifying taxonomy entries:

1. Follow the existing YAML structure exactly
2. Include descriptive comments for new categories
3. Ensure severity levels are properly calibrated
4. Update the taxonomy README with any new entries

---

## Development Workflow

### Branch Naming Convention

```
<type>/<short-description>

Types:
  feat/     — New feature or capability
  fix/      — Bug fix or correction
  docs/     — Documentation changes only
  schema/   — Schema modifications
  taxonomy/ — Taxonomy updates
  playbook/ — Playbook or template changes
  ci/       — CI/CD pipeline changes
```

**Examples:**
```
feat/add-multimodal-feedback-category
fix/schema-validation-edge-case
docs/update-integration-guide
schema/add-confidence-score-field
taxonomy/new-domain-tags-healthcare
```

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/acadify-solutions/asr-feedback.git
   cd asr-feedback
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feat/your-feature-name
   ```

3. **Make your changes** following the style guidelines below

4. **Validate schemas** (if modified)
   ```bash
   # Install ajv-cli for JSON Schema validation
   npm install -g ajv-cli

   # Validate example against schema
   ajv validate -s schemas/feedback-entry.schema.json -d schemas/examples/feedback-entry.example.json
   ```

5. **Submit a pull request**

---

## Style Guidelines

### Markdown

- Use ATX-style headers (`#`, `##`, `###`)
- Include a table of contents for documents longer than 3 sections
- Use fenced code blocks with language identifiers
- Use tables for structured comparisons
- Include horizontal rules (`---`) between major sections
- Maximum line length: 120 characters (soft limit)

### JSON Schemas

- Use `draft-07` specification
- Include `title`, `description`, and `examples` for every property
- Use `$id` for schema identification
- Follow naming convention: `kebab-case` for file names, `camelCase` for property names
- Include `required` arrays at each object level

### YAML

- Use 2-space indentation
- Include comments for non-obvious entries
- Use quotes for strings containing special characters
- Sort entries alphabetically within sections when logical

### Mermaid Diagrams

- Use consistent node naming: `PascalCase` for nodes
- Include colors for visual hierarchy
- Add descriptive labels on edges
- Keep diagrams focused — split complex flows into multiple diagrams

---

## Commit Message Convention

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <subject>

[optional body]

[optional footer(s)]
```

### Types

| Type | Description |
|---|---|
| `feat` | New feature or capability |
| `fix` | Bug fix |
| `docs` | Documentation changes |
| `schema` | Schema changes |
| `taxonomy` | Taxonomy changes |
| `style` | Formatting, missing semi-colons, etc. |
| `refactor` | Code refactoring |
| `test` | Adding or updating tests |
| `ci` | CI/CD changes |
| `chore` | Maintenance tasks |

### Examples

```
feat(schema): add confidence_score field to feedback entry
docs(methodology): expand inter-rater reliability section
fix(taxonomy): correct severity level P2 description
schema(session): add optional metadata block to session report
```

---

## Pull Request Process

### Before Submitting

- [ ] All schema examples validate against their schemas
- [ ] Documentation changes are consistent across related files
- [ ] No broken links in markdown files
- [ ] CHANGELOG.md is updated for user-facing changes
- [ ] Commit messages follow the convention above

### PR Template

Use the [Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md) — it will be loaded automatically.

### Review Timeline

| Priority | Target Review Time |
|---|---|
| P0 — Critical | Within 2 hours |
| P1 — High | Within 4 hours |
| P2 — Medium | Within 1 business day |
| P3 — Low | Within 3 business days |

---

## Review Standards

### What Reviewers Check

1. **Correctness** — Are the changes technically accurate?
2. **Completeness** — Are all related files updated (schema, docs, examples)?
3. **Consistency** — Do changes follow existing patterns and conventions?
4. **Clarity** — Is the documentation clear and unambiguous?
5. **Backward Compatibility** — Do schema changes break existing integrations?

### Approval Requirements

| Change Type | Required Approvals |
|---|---|
| Documentation only | 1 reviewer |
| Schema changes | 2 reviewers (including schema owner) |
| Taxonomy changes | 2 reviewers |
| Playbook changes | 1 reviewer + operations lead |
| CI/CD changes | 1 reviewer + DevOps lead |

---

## Recognition

All contributors are recognized in our [CHANGELOG](CHANGELOG.md) and in release notes. Significant contributions are highlighted in team updates.

---

<p align="center">
  <strong>Thank you for helping us maintain the highest standards of AI feedback quality.</strong>
</p>
