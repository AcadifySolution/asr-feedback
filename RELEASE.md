# Release Process

## Before release

Run the repository quality workflows and verify:

- JSON schemas and examples validate
- JavaScript SDK syntax/build checks pass
- Python SDK compiles
- documentation lint passes
- public examples contain no secrets or customer data
- changelog reflects user-visible changes

## Versioning

Use semantic versioning for public SDK and schema contracts:

- PATCH: backwards-compatible fixes
- MINOR: backwards-compatible functionality
- MAJOR: breaking API/schema/SDK changes

Document breaking schema changes with migration notes.

## Data integrity

Never publish real customer feedback, prompts, conversation history, or reports as examples. Use synthetic data or approved anonymized datasets.
