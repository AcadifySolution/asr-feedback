# Feedback Taxonomy

> **Version:** 2.3.0 | **Last Updated:** 2026-07-01

This directory contains the formal classification system used across the ASR Feedback Intelligence Platform.

## Files

| File | Purpose |
|---|---|
| [categories.yaml](categories.yaml) | Master feedback category definitions across all 4 pillars |
| [severity-levels.yaml](severity-levels.yaml) | P0–P4 severity classification with criteria and examples |
| [ai-model-profiles.yaml](ai-model-profiles.yaml) | Model-specific evaluation configurations and known behaviors |
| [domain-tags.yaml](domain-tags.yaml) | Industry and domain-specific tagging system |

## Usage

All feedback entries must reference valid taxonomy codes. The schemas enforce these codes via `enum` constraints — any feedback entry with an unrecognized code will fail validation.

## Adding New Entries

1. Propose the new entry via a pull request
2. Include the code, description, and at least 2 examples
3. Update the corresponding schema `enum` if adding a new code
4. Get approval from 2 reviewers (including taxonomy committee member)

---

> **See Also:** [Methodology →](../docs/METHODOLOGY.md) | [Feedback Schema →](../docs/FEEDBACK_SCHEMA.md)
