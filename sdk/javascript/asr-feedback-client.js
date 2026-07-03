/**
 * ASR Feedback Client — JavaScript SDK
 * Version: 2.3.0
 *
 * Official JavaScript/Node.js client library for the ASR Feedback
 * Intelligence Platform. Provides methods for submitting AI responses,
 * retrieving feedback, managing sessions, and configuring webhooks.
 *
 * Installation:
 *   npm install @asr-feedback/client
 *
 * Usage:
 *   import { ASRFeedbackClient } from '@asr-feedback/client';
 *
 *   const client = new ASRFeedbackClient({
 *     clientId: 'YOUR_CLIENT_ID',
 *     apiKey: 'YOUR_API_KEY',
 *     environment: 'production'
 *   });
 */

const ENVIRONMENTS = {
  production: 'https://api.asrfeedback.com/v2',
  staging: 'https://staging-api.asrfeedback.com/v2',
};

const DEFAULT_TIMEOUT = 30000; // milliseconds
const DEFAULT_MAX_RETRIES = 3;
const DEFAULT_BACKOFF_FACTOR = 2;
const RETRYABLE_STATUS_CODES = new Set([429, 500, 502, 503, 504]);

// =============================================================================
// Enums
// =============================================================================

/** Supported AI task types for evaluation. */
const TaskType = Object.freeze({
  QUESTION_ANSWERING: 'question_answering',
  SUMMARIZATION: 'summarization',
  CODE_GENERATION: 'code_generation',
  CREATIVE_WRITING: 'creative_writing',
  DATA_ANALYSIS: 'data_analysis',
  CONVERSATION: 'conversation',
  TRANSLATION: 'translation',
  CLASSIFICATION: 'classification',
  EXTRACTION: 'extraction',
  REASONING: 'reasoning',
  MULTIMODAL: 'multimodal',
  AGENT_TASK: 'agent_task',
  OTHER: 'other',
});

/** Evaluation priority levels. */
const Priority = Object.freeze({
  STANDARD: 'standard',
  HIGH: 'high',
  CRITICAL: 'critical',
});

// =============================================================================
// Error Classes
// =============================================================================

class ASRFeedbackError extends Error {
  constructor(message, statusCode = null) {
    super(message);
    this.name = 'ASRFeedbackError';
    this.statusCode = statusCode;
  }
}

class AuthenticationError extends ASRFeedbackError {
  constructor(message) {
    super(message, 401);
    this.name = 'AuthenticationError';
  }
}

class ValidationError extends ASRFeedbackError {
  constructor(message, details = []) {
    super(message, 422);
    this.name = 'ValidationError';
    this.details = details;
  }
}

class RateLimitError extends ASRFeedbackError {
  constructor(message, retryAfter = null) {
    super(message, 429);
    this.name = 'RateLimitError';
    this.retryAfter = retryAfter;
  }
}

class NotFoundError extends ASRFeedbackError {
  constructor(message) {
    super(message, 404);
    this.name = 'NotFoundError';
  }
}

// =============================================================================
// Client
// =============================================================================

class ASRFeedbackClient {
  /**
   * Create a new ASR Feedback client.
   *
   * @param {Object} config - Client configuration
   * @param {string} config.clientId - Your ASR Feedback client identifier
   * @param {string} config.apiKey - Your API authentication key
   * @param {string} [config.environment='production'] - Target environment
   * @param {number} [config.timeout=30000] - Request timeout in milliseconds
   * @param {Object} [config.retryConfig] - Retry configuration
   * @param {number} [config.retryConfig.maxRetries=3] - Maximum retry attempts
   * @param {number} [config.retryConfig.backoffFactor=2] - Exponential backoff factor
   */
  constructor({
    clientId,
    apiKey,
    environment = 'production',
    timeout = DEFAULT_TIMEOUT,
    retryConfig = {},
  }) {
    if (!ENVIRONMENTS[environment]) {
      throw new Error(
        `Invalid environment '${environment}'. Must be: ${Object.keys(ENVIRONMENTS).join(', ')}`
      );
    }

    this._clientId = clientId;
    this._apiKey = apiKey;
    this._baseUrl = ENVIRONMENTS[environment];
    this._timeout = timeout;
    this._retryConfig = {
      maxRetries: retryConfig.maxRetries ?? DEFAULT_MAX_RETRIES,
      backoffFactor: retryConfig.backoffFactor ?? DEFAULT_BACKOFF_FACTOR,
      retryOn: retryConfig.retryOn
        ? new Set(retryConfig.retryOn)
        : RETRYABLE_STATUS_CODES,
    };
  }

  // ---------------------------------------------------------------------------
  // Response Submission
  // ---------------------------------------------------------------------------

  /**
   * Submit an AI response for 4-pillar evaluation.
   *
   * @param {Object} params - Submission parameters
   * @param {string} params.responseId - Your unique identifier for this response
   * @param {string} params.modelId - AI model identifier
   * @param {string} params.userQuery - The user's input query
   * @param {string} params.aiResponse - The AI-generated response
   * @param {string} params.domain - Domain classification
   * @param {string} params.taskType - Type of task (see TaskType)
   * @param {string} [params.provider='Custom'] - AI model provider
   * @param {string} [params.language='en'] - ISO 639-1 language code
   * @param {string} [params.systemPrompt] - System prompt used
   * @param {Array} [params.conversationHistory] - Prior conversation turns
   * @param {number} [params.conversationTurn=1] - Turn number
   * @param {string} [params.priority='standard'] - Evaluation priority
   * @param {Object} [params.metadata] - Additional metadata
   * @returns {Promise<string>} The entry ID for tracking
   */
  async submitResponse({
    responseId,
    modelId,
    userQuery,
    aiResponse,
    domain,
    taskType,
    provider = 'Custom',
    language = 'en',
    systemPrompt = null,
    conversationHistory = null,
    conversationTurn = 1,
    priority = Priority.STANDARD,
    metadata = null,
  }) {
    const payload = {
      responseId,
      modelId,
      provider,
      context: {
        userQuery,
        aiResponse,
        domain,
        taskType,
        language,
        conversationTurn,
      },
      priority,
    };

    if (systemPrompt) payload.context.systemPrompt = systemPrompt;
    if (conversationHistory) payload.context.conversationHistory = conversationHistory;
    if (metadata) payload.metadata = metadata;

    const response = await this._request('POST', '/responses', payload);
    return response.entryId;
  }

  /**
   * Submit multiple responses for evaluation in a single request.
   *
   * @param {Array<Object>} responses - Array of response payloads (max 100)
   * @returns {Promise<Object>} Batch submission result
   */
  async submitBatch(responses) {
    if (responses.length > 100) {
      throw new ValidationError('Batch size cannot exceed 100 responses');
    }
    return this._request('POST', '/responses/batch', { responses });
  }

  // ---------------------------------------------------------------------------
  // Feedback Retrieval
  // ---------------------------------------------------------------------------

  /**
   * Retrieve a completed feedback entry with full 4-pillar analysis.
   *
   * @param {string} entryId - The feedback entry identifier
   * @returns {Promise<Object>} Complete feedback entry
   */
  async getFeedback(entryId) {
    return this._request('GET', `/feedback/${entryId}`);
  }

  /**
   * List feedback entries with filtering and pagination.
   *
   * @param {Object} [params] - Filter parameters
   * @returns {Promise<Object>} Paginated feedback entries
   */
  async listFeedback(params = {}) {
    const query = new URLSearchParams();
    Object.entries(params).forEach(([key, value]) => {
      if (value !== null && value !== undefined) {
        query.set(key, String(value));
      }
    });
    const queryString = query.toString();
    const path = queryString ? `/feedback?${queryString}` : '/feedback';
    return this._request('GET', path);
  }

  // ---------------------------------------------------------------------------
  // Sessions
  // ---------------------------------------------------------------------------

  /**
   * Retrieve the aggregated session report.
   *
   * @param {string} sessionId - Session identifier
   * @returns {Promise<Object>} Session report
   */
  async getSessionReport(sessionId) {
    return this._request('GET', `/sessions/${sessionId}/report`);
  }

  // ---------------------------------------------------------------------------
  // Memory Rules
  // ---------------------------------------------------------------------------

  /**
   * List active memory rules.
   *
   * @param {Object} [params] - Filter parameters
   * @returns {Promise<Array>} Array of memory rules
   */
  async listMemoryRules(params = {}) {
    const query = new URLSearchParams({ status: 'active', ...params });
    const data = await this._request('GET', `/memory?${query.toString()}`);
    return data.rules || [];
  }

  // ---------------------------------------------------------------------------
  // Webhooks
  // ---------------------------------------------------------------------------

  /**
   * Configure a webhook endpoint.
   *
   * @param {Object} config - Webhook configuration
   * @param {string} config.url - Your webhook endpoint URL
   * @param {Array<string>} config.events - Event types to subscribe to
   * @param {string} config.secret - Webhook signature secret
   * @returns {Promise<Object>} Webhook configuration result
   */
  async configureWebhook({ url, events, secret }) {
    return this._request('POST', '/webhooks', { url, events, secret });
  }

  // ---------------------------------------------------------------------------
  // Internal Methods
  // ---------------------------------------------------------------------------

  /**
   * Make an authenticated HTTP request with retry logic.
   * @private
   */
  async _request(method, path, body = null) {
    const url = `${this._baseUrl}${path}`;
    const headers = {
      Authorization: `Bearer ${this._apiKey}`,
      'X-Client-ID': this._clientId,
      'Content-Type': 'application/json',
      'User-Agent': 'asr-feedback-js/2.3.0',
    };

    let lastError = null;

    for (let attempt = 0; attempt <= this._retryConfig.maxRetries; attempt++) {
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), this._timeout);

        const fetchOptions = {
          method,
          headers,
          signal: controller.signal,
        };
        if (body) {
          fetchOptions.body = JSON.stringify(body);
        }

        const response = await fetch(url, fetchOptions);
        clearTimeout(timeoutId);

        if (response.ok) {
          return response.json();
        }

        const errorBody = await response.text();
        const status = response.status;

        if (status === 401) throw new AuthenticationError('Authentication failed');
        if (status === 404) throw new NotFoundError(`Resource not found: ${path}`);
        if (status === 422) throw new ValidationError(`Validation error: ${errorBody}`);
        if (status === 429) {
          const retryAfter = response.headers.get('Retry-After');
          if (attempt < this._retryConfig.maxRetries) {
            const waitTime = retryAfter
              ? parseInt(retryAfter, 10) * 1000
              : this._retryConfig.backoffFactor ** attempt * 1000;
            await this._sleep(waitTime);
            continue;
          }
          throw new RateLimitError('Rate limit exceeded', retryAfter);
        }

        if (this._retryConfig.retryOn.has(status)) {
          lastError = new ASRFeedbackError(`HTTP ${status}: ${errorBody}`, status);
          if (attempt < this._retryConfig.maxRetries) {
            const waitTime = this._retryConfig.backoffFactor ** attempt * 1000;
            await this._sleep(waitTime);
            continue;
          }
          throw lastError;
        }

        throw new ASRFeedbackError(`API error ${status}: ${errorBody}`, status);
      } catch (error) {
        if (
          error instanceof ASRFeedbackError ||
          error instanceof AuthenticationError ||
          error instanceof ValidationError ||
          error instanceof RateLimitError ||
          error instanceof NotFoundError
        ) {
          throw error;
        }

        lastError = error;
        if (attempt < this._retryConfig.maxRetries) {
          const waitTime = this._retryConfig.backoffFactor ** attempt * 1000;
          await this._sleep(waitTime);
          continue;
        }
        throw new ASRFeedbackError(`Connection failed: ${error.message}`);
      }
    }

    throw new ASRFeedbackError(`Request failed after all retries: ${lastError?.message}`);
  }

  /** @private */
  _sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }
}

// =============================================================================
// Exports
// =============================================================================

module.exports = {
  ASRFeedbackClient,
  TaskType,
  Priority,
  ASRFeedbackError,
  AuthenticationError,
  ValidationError,
  RateLimitError,
  NotFoundError,
};
