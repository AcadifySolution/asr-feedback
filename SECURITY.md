# Security Policy

## Reporting a Vulnerability

The ASR Feedback team takes security seriously. We appreciate your efforts to responsibly disclose your findings.

### How to Report

**DO NOT** create a public GitHub issue for security vulnerabilities.

Instead, please report security vulnerabilities via one of the following channels:

- **Email:** security@acadifysolutions.com
- **Subject Line Format:** `[ASR-SECURITY] Brief description of vulnerability`

### What to Include

Please include the following information in your report:

| Field | Description |
|---|---|
| **Description** | Clear description of the vulnerability |
| **Impact** | What data or systems could be affected |
| **Reproduction Steps** | Step-by-step instructions to reproduce the issue |
| **Affected Components** | Which schemas, APIs, or processes are involved |
| **Severity Estimate** | Your assessment of the severity (Critical/High/Medium/Low) |
| **Suggested Fix** | If you have a recommended remediation (optional) |

### Response Timeline

| Stage | Timeline |
|---|---|
| Acknowledgment | Within 24 hours |
| Initial Assessment | Within 48 hours |
| Status Update | Within 5 business days |
| Resolution Target | Within 30 days (critical), 90 days (non-critical) |

### Scope

The following are in scope for security reports:

- **Data Schema Vulnerabilities** — Schemas that could allow injection or malformed data
- **API Security Issues** — Authentication, authorization, or input validation flaws
- **Data Exposure Risks** — PII leakage, improper data handling, or access control gaps
- **Compliance Gaps** — Issues that could affect SOC 2, GDPR, or other compliance requirements
- **Infrastructure Misconfigurations** — CI/CD pipeline, secrets management, or access control issues

### Out of Scope

- Issues in third-party dependencies (report these to the respective maintainers)
- Social engineering attacks
- Denial of service attacks against development infrastructure
- Issues requiring physical access to hardware

## Supported Versions

| Version | Supported |
|---|---|
| 2.x.x | ✅ Active support |
| 1.x.x | ⚠️ Security patches only |
| < 1.0 | ❌ Not supported |

## Security Best Practices

All contributors and team members must follow these security practices:

### Data Handling
- Never commit real client data, API keys, or credentials to this repository
- Use example/synthetic data in all schema examples and documentation
- Follow the [Data Handling Policy](compliance/data-handling-policy.md) for all feedback data

### Access Control
- Use branch protection rules on `main` and `release/*` branches
- Require signed commits for all production changes
- Follow the principle of least privilege for repository access

### Review Requirements
- All changes affecting data handling must be reviewed by a security-aware reviewer
- Schema changes that affect data validation require security review
- Compliance document changes require legal/compliance team review

## Acknowledgments

We maintain a [Security Hall of Fame](#) to recognize individuals who have responsibly disclosed security issues. Your contribution to keeping ASR Feedback secure is valued and appreciated.

---

<p align="center">
  <em>Security is a shared responsibility. Thank you for helping us protect our clients' data.</em>
</p>
