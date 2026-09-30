# Contributing

## Workflow

1. Create a focused branch.
2. Keep schema, SDK, documentation, and operational changes separately testable.
3. Add regression coverage for behavior changes.
4. Run the repository quality checks before opening a pull request.
5. Use synthetic or approved anonymized evaluation data.
6. Never commit credentials, customer responses, private prompts, or production reports.

## Schema changes

Treat JSON schemas as public contracts. Update:

- the schema
- representative examples
- documentation
- SDK references, where applicable
- changelog entry for breaking changes

## SDK changes

Maintain compatibility for documented constructor and method behavior. Add tests or smoke checks for validation, authentication errors, rate limiting, and retry behavior when those paths change.

## Documentation changes

Keep claims evidence-based. Distinguish examples, targets, measured results, and production guarantees.

## Pull requests

Include the problem, approach, verification performed, compatibility impact, security/privacy impact, and any migration notes.
