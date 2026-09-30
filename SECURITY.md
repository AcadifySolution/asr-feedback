# Security Policy

ASR Feedback contains schemas, SDKs, evaluation methodology, and operational guidance for AI-response quality workflows. Public repository content should never contain customer responses, production credentials, or confidential evaluation data.

## Data protection baseline

Treat submitted AI responses, prompts, conversation history, metadata, and feedback as potentially sensitive.

Production integrations should provide:

- authentication and authorization
- tenant/workspace isolation
- encryption in transit and at rest
- retention and deletion controls
- least-privilege API credentials
- webhook signature verification
- rate limiting and abuse protection
- audit logging
- PII detection/redaction
- access-controlled analytics exports

Do not rely on a schema or SDK alone to establish regulatory compliance.

## SDK handling

The SDKs may accept prompts, AI responses, conversation history, system prompts, and metadata. Callers should minimize sensitive fields and avoid logging raw payloads.

Secrets must be supplied at runtime and never committed to Git.

## Evaluation integrity

Keep production or customer evaluation datasets outside the public repository unless they are explicitly approved, synthetic, or appropriately anonymized.

## Vulnerability reporting

Report vulnerabilities privately through the repository's GitHub security reporting mechanism. Include the affected component, reproduction steps, impact, and mitigation where known. Do not include secrets or customer data.
