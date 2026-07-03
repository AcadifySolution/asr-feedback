# API Reference

> **Version:** 2.3.0 | **Base URL:** `https://api.asrfeedback.com/v2`

---

## Authentication

All API requests require authentication via Bearer token:

```http
Authorization: Bearer YOUR_API_KEY
X-Client-ID: YOUR_CLIENT_ID
Content-Type: application/json
```

---

## Endpoints

### Responses

#### Submit Response for Evaluation
```http
POST /v2/responses
```

Submit an AI-generated response for 4-pillar evaluation.

**Request Body:**
```json
{
  "responseId": "string (required)",
  "modelId": "string (required)",
  "provider": "string (required)",
  "context": {
    "userQuery": "string (required)",
    "aiResponse": "string (required)",
    "domain": "string (required)",
    "taskType": "string (required)",
    "language": "string (required, ISO 639-1)",
    "systemPrompt": "string (optional)",
    "conversationHistory": "array (optional)",
    "conversationTurn": "integer (optional)"
  },
  "priority": "string (optional: standard|high|critical)",
  "metadata": "object (optional)"
}
```

**Response:** `202 Accepted`
```json
{
  "entryId": "FB-2026-0547-001",
  "sessionId": "SES-2026-0547",
  "status": "queued",
  "estimatedCompletionTime": "2026-07-01T16:30:00.000Z"
}
```

---

#### Batch Submit Responses
```http
POST /v2/responses/batch
```

Submit multiple responses in a single request (max 100).

**Request Body:**
```json
{
  "responses": [
    { /* same structure as single submit */ }
  ]
}
```

**Response:** `202 Accepted`
```json
{
  "batchId": "BATCH-2026-0547",
  "entriesAccepted": 50,
  "entriesRejected": 0,
  "entries": [
    { "entryId": "FB-2026-0547-001", "responseId": "...", "status": "queued" }
  ]
}
```

---

### Feedback

#### Get Feedback Entry
```http
GET /v2/feedback/{entryId}
```

Retrieve a completed feedback entry with full 4-pillar analysis.

**Response:** `200 OK`
Returns the full feedback entry object as defined in [feedback-entry.schema.json](../schemas/feedback-entry.schema.json).

---

#### List Feedback Entries
```http
GET /v2/feedback?sessionId={sessionId}&status={status}&page={page}&limit={limit}
```

**Query Parameters:**
| Parameter | Type | Default | Description |
|---|---|---|---|
| `sessionId` | string | — | Filter by session |
| `status` | string | `completed` | `queued`, `in_progress`, `completed` |
| `startDate` | ISO 8601 | — | Filter by date range |
| `endDate` | ISO 8601 | — | Filter by date range |
| `domain` | string | — | Filter by domain tag |
| `modelId` | string | — | Filter by model |
| `minScore` | integer | — | Minimum composite score |
| `maxScore` | integer | — | Maximum composite score |
| `severity` | integer | — | Filter entries containing this severity level |
| `page` | integer | 1 | Page number |
| `limit` | integer | 50 | Results per page (max 100) |

**Response:** `200 OK`
```json
{
  "data": [ /* array of feedback entries */ ],
  "pagination": {
    "page": 1,
    "limit": 50,
    "total": 247,
    "totalPages": 5
  }
}
```

---

### Sessions

#### Get Session Report
```http
GET /v2/sessions/{sessionId}/report
```

Retrieve the aggregated session report.

**Response:** `200 OK`
Returns the full session report object as defined in [session-report.schema.json](../schemas/session-report.schema.json).

---

#### List Sessions
```http
GET /v2/sessions?startDate={date}&endDate={date}&page={page}
```

---

### Memory Rules

#### List Active Memory Rules
```http
GET /v2/memory?scope={scope}&type={type}&status=active
```

**Query Parameters:**
| Parameter | Type | Description |
|---|---|---|
| `scope` | string | `global`, `client:{clientId}`, `domain:{tag}`, `model:{modelId}` |
| `type` | string | `MEM_CLIENT_PREF`, `MEM_SAFETY_RULE`, etc. |
| `status` | string | `active`, `deprecated`, `all` |

---

### Webhooks

#### Configure Webhook
```http
POST /v2/webhooks
```

```json
{
  "url": "https://your-domain.com/webhook",
  "events": ["feedback.completed", "session.completed", "alert.p0_detected"],
  "secret": "your-webhook-secret"
}
```

#### Webhook Events
| Event | Description |
|---|---|
| `feedback.completed` | A feedback entry evaluation is complete |
| `session.completed` | An entire session is complete with report |
| `alert.p0_detected` | A P0 severity issue was detected |
| `alert.sla_breach` | An SLA breach occurred |
| `memory.rule_created` | A new memory rule was created |

---

## Rate Limits

| Tier | Requests/minute | Burst |
|---|---|---|
| Standard | 60 | 100 |
| Professional | 120 | 200 |
| Enterprise | 300 | 500 |

Rate limit headers are included in every response:
```http
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 45
X-RateLimit-Reset: 1719842400
```

---

## Error Responses

All errors follow a consistent format:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human-readable error description",
    "details": [
      {
        "field": "context.domain",
        "message": "must be a valid domain tag"
      }
    ],
    "requestId": "req-a1b2c3d4"
  }
}
```

| Error Code | HTTP Status | Description |
|---|---|---|
| `UNAUTHORIZED` | 401 | Invalid or missing API key |
| `FORBIDDEN` | 403 | Insufficient permissions |
| `NOT_FOUND` | 404 | Resource not found |
| `VALIDATION_ERROR` | 422 | Request payload validation failed |
| `RATE_LIMITED` | 429 | Rate limit exceeded |
| `INTERNAL_ERROR` | 500 | Server error (retry with backoff) |

---

> **See Also:** [Integration Guide →](../docs/INTEGRATION_GUIDE.md) | [Feedback Schema →](../docs/FEEDBACK_SCHEMA.md)
