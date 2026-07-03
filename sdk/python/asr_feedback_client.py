"""
ASR Feedback Client — Python SDK
Version: 2.3.0

Official Python client library for the ASR Feedback Intelligence Platform.
Provides type-safe methods for submitting AI responses, retrieving feedback,
managing sessions, and configuring webhooks.

Installation:
    pip install asr-feedback-client

Usage:
    from asr_feedback_client import ASRFeedbackClient

    client = ASRFeedbackClient(
        client_id="YOUR_CLIENT_ID",
        api_key="YOUR_API_KEY",
        environment="production"
    )

    # Submit a response for evaluation
    entry_id = client.submit_response(
        response_id="resp-001",
        model_id="gpt-4o-2025-08-06",
        user_query="What is cloud computing?",
        ai_response="Cloud computing is...",
        domain="technology",
        task_type="question_answering"
    )

    # Retrieve feedback
    feedback = client.get_feedback(entry_id)
"""

from __future__ import annotations

import time
import json
import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Optional
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode


# =============================================================================
# Constants
# =============================================================================

ENVIRONMENTS = {
    "production": "https://api.asrfeedback.com/v2",
    "staging": "https://staging-api.asrfeedback.com/v2",
}

DEFAULT_TIMEOUT = 30  # seconds
DEFAULT_MAX_RETRIES = 3
DEFAULT_BACKOFF_FACTOR = 2
RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}

logger = logging.getLogger("asr_feedback")


# =============================================================================
# Enums
# =============================================================================

class TaskType(Enum):
    """Supported AI task types for evaluation."""
    QUESTION_ANSWERING = "question_answering"
    SUMMARIZATION = "summarization"
    CODE_GENERATION = "code_generation"
    CREATIVE_WRITING = "creative_writing"
    DATA_ANALYSIS = "data_analysis"
    CONVERSATION = "conversation"
    TRANSLATION = "translation"
    CLASSIFICATION = "classification"
    EXTRACTION = "extraction"
    REASONING = "reasoning"
    MULTIMODAL = "multimodal"
    AGENT_TASK = "agent_task"
    OTHER = "other"


class Priority(Enum):
    """Evaluation priority levels."""
    STANDARD = "standard"
    HIGH = "high"
    CRITICAL = "critical"


class FeedbackStatus(Enum):
    """Feedback entry status."""
    QUEUED = "queued"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class QualityBand(Enum):
    """Quality score classification bands."""
    EXCELLENT = "excellent"      # 90-100
    GOOD = "good"                # 75-89
    ACCEPTABLE = "acceptable"    # 60-74
    POOR = "poor"                # 40-59
    CRITICAL = "critical"        # 0-39


# =============================================================================
# Data Classes
# =============================================================================

@dataclass
class GoodSignal:
    """Represents a positive behavior identified in the AI response."""
    category_code: str
    description: str
    evidence: str
    reinforcement_value: float


@dataclass
class BadSignal:
    """Represents an issue identified in the AI response."""
    category_code: str
    severity: int
    description: str
    evidence: str
    root_cause: str
    remediation: str


@dataclass
class Learning:
    """Represents a novel insight discovered during evaluation."""
    category_code: str
    observation: str
    evidence: str
    implication: str
    recommended_action: str


@dataclass
class MemoryRule:
    """Represents a persistent rule for future evaluations."""
    rule_type: str
    rule_text: str
    scope: str
    expires_at: Optional[str] = None


@dataclass
class QualityScore:
    """Composite quality score with breakdown."""
    composite: float
    band: str
    good_signal_score: float
    bad_signal_penalty: float
    severity_impact: float
    completeness_score: float
    consistency_score: float


@dataclass
class Pillars:
    """Container for all 4-pillar feedback data."""
    good: list[GoodSignal] = field(default_factory=list)
    bad: list[BadSignal] = field(default_factory=list)
    learned: list[Learning] = field(default_factory=list)
    remember: list[MemoryRule] = field(default_factory=list)


@dataclass
class FeedbackEntry:
    """Complete feedback entry with 4-pillar analysis and quality score."""
    entry_id: str
    session_id: str
    response_id: str
    timestamp: str
    status: str
    pillars: Pillars
    quality_score: QualityScore
    model_id: str
    domain: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class SubmissionResult:
    """Result of submitting a response for evaluation."""
    entry_id: str
    session_id: str
    status: str
    estimated_completion_time: Optional[str] = None


@dataclass
class RetryConfig:
    """Configuration for retry behavior on transient failures."""
    max_retries: int = DEFAULT_MAX_RETRIES
    backoff_factor: int = DEFAULT_BACKOFF_FACTOR
    retry_on: set[int] = field(default_factory=lambda: RETRYABLE_STATUS_CODES)


# =============================================================================
# Exceptions
# =============================================================================

class ASRFeedbackError(Exception):
    """Base exception for ASR Feedback client errors."""
    pass


class AuthenticationError(ASRFeedbackError):
    """Raised when API authentication fails."""
    pass


class ValidationError(ASRFeedbackError):
    """Raised when request validation fails."""
    pass


class RateLimitError(ASRFeedbackError):
    """Raised when API rate limit is exceeded."""
    def __init__(self, message: str, retry_after: Optional[int] = None):
        super().__init__(message)
        self.retry_after = retry_after


class NotFoundError(ASRFeedbackError):
    """Raised when a requested resource is not found."""
    pass


# =============================================================================
# Client
# =============================================================================

class ASRFeedbackClient:
    """
    Official Python client for the ASR Feedback Intelligence Platform.

    Provides methods for:
    - Submitting AI responses for 4-pillar evaluation
    - Retrieving completed feedback with full analysis
    - Managing evaluation sessions
    - Configuring webhooks for real-time notifications

    Args:
        client_id: Your ASR Feedback client identifier.
        api_key: Your API authentication key.
        environment: Target environment ('production' or 'staging').
        timeout: Request timeout in seconds (default: 30).
        retry_config: Configuration for retry behavior on transient failures.

    Example:
        >>> client = ASRFeedbackClient(
        ...     client_id="YOUR_CLIENT_ID",
        ...     api_key="YOUR_API_KEY"
        ... )
        >>> entry_id = client.submit_response(
        ...     response_id="resp-001",
        ...     model_id="gpt-4o",
        ...     user_query="What is Python?",
        ...     ai_response="Python is a programming language...",
        ...     domain="technology",
        ...     task_type="question_answering"
        ... )
    """

    def __init__(
        self,
        client_id: str,
        api_key: str,
        environment: str = "production",
        timeout: int = DEFAULT_TIMEOUT,
        retry_config: Optional[RetryConfig] = None,
    ):
        if environment not in ENVIRONMENTS:
            raise ValueError(
                f"Invalid environment '{environment}'. "
                f"Must be one of: {list(ENVIRONMENTS.keys())}"
            )

        self._client_id = client_id
        self._api_key = api_key
        self._base_url = ENVIRONMENTS[environment]
        self._timeout = timeout
        self._retry_config = retry_config or RetryConfig()

        logger.info(
            "ASR Feedback client initialized | env=%s | client=%s",
            environment,
            client_id,
        )

    # -------------------------------------------------------------------------
    # Response Submission
    # -------------------------------------------------------------------------

    def submit_response(
        self,
        response_id: str,
        model_id: str,
        user_query: str,
        ai_response: str,
        domain: str,
        task_type: str | TaskType,
        *,
        provider: str = "Custom",
        language: str = "en",
        system_prompt: Optional[str] = None,
        conversation_history: Optional[list[dict]] = None,
        conversation_turn: int = 1,
        priority: str | Priority = Priority.STANDARD,
        metadata: Optional[dict[str, Any]] = None,
    ) -> str:
        """
        Submit an AI response for 4-pillar evaluation.

        Args:
            response_id: Your unique identifier for this response.
            model_id: Identifier of the AI model that generated the response.
            user_query: The user's input query.
            ai_response: The AI-generated response to evaluate.
            domain: Domain classification (see taxonomy/domain-tags.yaml).
            task_type: Type of task (see TaskType enum).
            provider: AI model provider (default: "Custom").
            language: ISO 639-1 language code (default: "en").
            system_prompt: Optional system prompt used.
            conversation_history: Optional prior conversation turns.
            conversation_turn: Turn number in multi-turn conversation.
            priority: Evaluation priority (default: standard).
            metadata: Optional additional metadata.

        Returns:
            The entry ID (str) for tracking this evaluation.

        Raises:
            ValidationError: If required fields are missing or invalid.
            AuthenticationError: If API credentials are invalid.
            RateLimitError: If rate limit is exceeded.
        """
        if isinstance(task_type, TaskType):
            task_type = task_type.value
        if isinstance(priority, Priority):
            priority = priority.value

        payload = {
            "responseId": response_id,
            "modelId": model_id,
            "provider": provider,
            "context": {
                "userQuery": user_query,
                "aiResponse": ai_response,
                "domain": domain,
                "taskType": task_type,
                "language": language,
                "conversationTurn": conversation_turn,
            },
            "priority": priority,
        }

        if system_prompt:
            payload["context"]["systemPrompt"] = system_prompt
        if conversation_history:
            payload["context"]["conversationHistory"] = conversation_history
        if metadata:
            payload["metadata"] = metadata

        response = self._request("POST", "/responses", payload)
        result = SubmissionResult(
            entry_id=response["entryId"],
            session_id=response["sessionId"],
            status=response["status"],
            estimated_completion_time=response.get("estimatedCompletionTime"),
        )

        logger.info(
            "Response submitted | entry_id=%s | response_id=%s",
            result.entry_id,
            response_id,
        )
        return result.entry_id

    def submit_batch(
        self,
        responses: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """
        Submit multiple responses for evaluation in a single request.

        Args:
            responses: List of response payloads (max 100).

        Returns:
            Batch submission result with entry IDs and status.
        """
        if len(responses) > 100:
            raise ValidationError("Batch size cannot exceed 100 responses")

        return self._request("POST", "/responses/batch", {"responses": responses})

    # -------------------------------------------------------------------------
    # Feedback Retrieval
    # -------------------------------------------------------------------------

    def get_feedback(self, entry_id: str) -> FeedbackEntry:
        """
        Retrieve a completed feedback entry with full 4-pillar analysis.

        Args:
            entry_id: The feedback entry identifier.

        Returns:
            FeedbackEntry with complete evaluation data.

        Raises:
            NotFoundError: If the entry ID doesn't exist.
        """
        data = self._request("GET", f"/feedback/{entry_id}")
        return self._parse_feedback_entry(data)

    def list_feedback(
        self,
        *,
        session_id: Optional[str] = None,
        status: str = "completed",
        domain: Optional[str] = None,
        model_id: Optional[str] = None,
        min_score: Optional[int] = None,
        max_score: Optional[int] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        page: int = 1,
        limit: int = 50,
    ) -> dict[str, Any]:
        """
        List feedback entries with filtering and pagination.

        Returns:
            Dictionary with 'data' (list of entries) and 'pagination' metadata.
        """
        params = {"status": status, "page": page, "limit": min(limit, 100)}
        if session_id:
            params["sessionId"] = session_id
        if domain:
            params["domain"] = domain
        if model_id:
            params["modelId"] = model_id
        if min_score is not None:
            params["minScore"] = min_score
        if max_score is not None:
            params["maxScore"] = max_score
        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date

        query_string = urlencode(params)
        return self._request("GET", f"/feedback?{query_string}")

    # -------------------------------------------------------------------------
    # Sessions
    # -------------------------------------------------------------------------

    def get_session_report(self, session_id: str) -> dict[str, Any]:
        """Retrieve the aggregated session report."""
        return self._request("GET", f"/sessions/{session_id}/report")

    def list_sessions(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        page: int = 1,
        limit: int = 50,
    ) -> dict[str, Any]:
        """List evaluation sessions with filtering and pagination."""
        params: dict[str, Any] = {"page": page, "limit": min(limit, 100)}
        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date
        query_string = urlencode(params)
        return self._request("GET", f"/sessions?{query_string}")

    # -------------------------------------------------------------------------
    # Memory Rules
    # -------------------------------------------------------------------------

    def list_memory_rules(
        self,
        scope: Optional[str] = None,
        rule_type: Optional[str] = None,
        status: str = "active",
    ) -> list[dict[str, Any]]:
        """List active memory rules with optional filtering."""
        params: dict[str, Any] = {"status": status}
        if scope:
            params["scope"] = scope
        if rule_type:
            params["type"] = rule_type
        query_string = urlencode(params)
        data = self._request("GET", f"/memory?{query_string}")
        return data.get("rules", [])

    # -------------------------------------------------------------------------
    # Webhooks
    # -------------------------------------------------------------------------

    def configure_webhook(
        self,
        url: str,
        events: list[str],
        secret: str,
    ) -> dict[str, Any]:
        """
        Configure a webhook endpoint for real-time notifications.

        Args:
            url: Your webhook endpoint URL.
            events: List of event types to subscribe to.
            secret: Secret for webhook signature verification.
        """
        payload = {
            "url": url,
            "events": events,
            "secret": secret,
        }
        return self._request("POST", "/webhooks", payload)

    # -------------------------------------------------------------------------
    # Internal Methods
    # -------------------------------------------------------------------------

    def _request(
        self,
        method: str,
        path: str,
        body: Optional[dict] = None,
    ) -> dict[str, Any]:
        """Make an authenticated HTTP request with retry logic."""
        url = f"{self._base_url}{path}"
        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "X-Client-ID": self._client_id,
            "Content-Type": "application/json",
            "User-Agent": "asr-feedback-python/2.3.0",
        }

        data = json.dumps(body).encode("utf-8") if body else None
        last_error = None

        for attempt in range(self._retry_config.max_retries + 1):
            try:
                req = Request(url, data=data, headers=headers, method=method)
                with urlopen(req, timeout=self._timeout) as response:
                    return json.loads(response.read().decode("utf-8"))

            except HTTPError as e:
                status = e.code
                error_body = e.read().decode("utf-8", errors="replace")

                if status == 401:
                    raise AuthenticationError(
                        "Authentication failed. Check your API key and client ID."
                    )
                elif status == 404:
                    raise NotFoundError(f"Resource not found: {path}")
                elif status == 422:
                    raise ValidationError(f"Validation error: {error_body}")
                elif status == 429:
                    retry_after = e.headers.get("Retry-After")
                    if attempt < self._retry_config.max_retries:
                        wait_time = int(retry_after) if retry_after else (
                            self._retry_config.backoff_factor ** attempt
                        )
                        logger.warning(
                            "Rate limited, retrying in %ds (attempt %d/%d)",
                            wait_time, attempt + 1, self._retry_config.max_retries,
                        )
                        time.sleep(wait_time)
                        continue
                    raise RateLimitError(
                        "Rate limit exceeded",
                        retry_after=int(retry_after) if retry_after else None,
                    )
                elif status in self._retry_config.retry_on:
                    last_error = e
                    if attempt < self._retry_config.max_retries:
                        wait_time = self._retry_config.backoff_factor ** attempt
                        logger.warning(
                            "Request failed with %d, retrying in %ds (attempt %d/%d)",
                            status, wait_time, attempt + 1,
                            self._retry_config.max_retries,
                        )
                        time.sleep(wait_time)
                        continue
                    raise ASRFeedbackError(f"Request failed after retries: {status}")
                else:
                    raise ASRFeedbackError(
                        f"API error {status}: {error_body}"
                    )

            except URLError as e:
                last_error = e
                if attempt < self._retry_config.max_retries:
                    wait_time = self._retry_config.backoff_factor ** attempt
                    logger.warning(
                        "Connection error, retrying in %ds (attempt %d/%d): %s",
                        wait_time, attempt + 1,
                        self._retry_config.max_retries, str(e),
                    )
                    time.sleep(wait_time)
                    continue
                raise ASRFeedbackError(f"Connection failed: {e}") from e

        raise ASRFeedbackError(f"Request failed after all retries: {last_error}")

    @staticmethod
    def _parse_feedback_entry(data: dict[str, Any]) -> FeedbackEntry:
        """Parse raw API response into a FeedbackEntry dataclass."""
        pillars_data = data.get("pillars", {})

        pillars = Pillars(
            good=[
                GoodSignal(**g) for g in pillars_data.get("good", [])
            ],
            bad=[
                BadSignal(**b) for b in pillars_data.get("bad", [])
            ],
            learned=[
                Learning(**l) for l in pillars_data.get("learned", [])
            ],
            remember=[
                MemoryRule(**m) for m in pillars_data.get("remember", [])
            ],
        )

        score_data = data.get("qualityScore", {})
        breakdown = score_data.get("breakdown", {})
        quality_score = QualityScore(
            composite=score_data.get("composite", 0),
            band=score_data.get("band", "unknown"),
            good_signal_score=breakdown.get("goodSignalScore", 0),
            bad_signal_penalty=breakdown.get("badSignalPenalty", 0),
            severity_impact=breakdown.get("severityImpact", 0),
            completeness_score=breakdown.get("completenessScore", 0),
            consistency_score=breakdown.get("consistencyScore", 0),
        )

        return FeedbackEntry(
            entry_id=data["entryId"],
            session_id=data["sessionId"],
            response_id=data["responseId"],
            timestamp=data["timestamp"],
            status=data.get("status", "completed"),
            pillars=pillars,
            quality_score=quality_score,
            model_id=data.get("model", {}).get("modelId", "unknown"),
            domain=data.get("context", {}).get("domain", "unknown"),
            metadata=data.get("metadata", {}),
        )
