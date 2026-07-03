/**
 * TypeScript definitions for the ASR Feedback JavaScript SDK.
 * Version: 2.3.0
 */

export enum TaskType {
  QUESTION_ANSWERING = 'question_answering',
  SUMMARIZATION = 'summarization',
  CODE_GENERATION = 'code_generation',
  CREATIVE_WRITING = 'creative_writing',
  DATA_ANALYSIS = 'data_analysis',
  CONVERSATION = 'conversation',
  TRANSLATION = 'translation',
  CLASSIFICATION = 'classification',
  EXTRACTION = 'extraction',
  REASONING = 'reasoning',
  MULTIMODAL = 'multimodal',
  AGENT_TASK = 'agent_task',
  OTHER = 'other'
}

export enum Priority {
  STANDARD = 'standard',
  HIGH = 'high',
  CRITICAL = 'critical'
}

export interface GoodSignal {
  categoryCode: string;
  description: string;
  evidence: string;
  reinforcementValue: number;
}

export interface BadSignal {
  categoryCode: string;
  severity: number;
  description: string;
  evidence: string;
  rootCause: string;
  remediation: string;
}

export interface Learning {
  categoryCode: string;
  observation: string;
  evidence: string;
  implication: string;
  recommendedAction: string;
}

export interface MemoryRule {
  ruleType: string;
  ruleText: string;
  scope: string;
  expiresAt: string | null;
}

export interface QualityScoreBreakdown {
  goodSignalScore: number;
  badSignalPenalty: number;
  severityImpact: number;
  completenessScore: number;
  consistencyScore: number;
}

export interface QualityScore {
  composite: number;
  band: 'excellent' | 'good' | 'acceptable' | 'poor' | 'critical';
  breakdown: QualityScoreBreakdown;
}

export interface FeedbackPillars {
  good: GoodSignal[];
  bad: BadSignal[];
  learned: Learning[];
  remember: MemoryRule[];
}

export interface FeedbackEntry {
  entryId: string;
  sessionId: string;
  responseId: string;
  timestamp: string;
  status: 'queued' | 'in_progress' | 'completed';
  pillars: FeedbackPillars;
  qualityScore: QualityScore;
  model: {
    modelId: string;
    provider: string;
    temperature?: number;
    maxTokens?: number;
  };
  context: {
    domain: string;
    taskType: TaskType;
    language: string;
    conversationTurn?: number;
    userQuery?: string;
    systemPrompt?: string;
  };
  metadata?: Record<string, any>;
}

export interface SubmitResponseParams {
  responseId: string;
  modelId: string;
  userQuery: string;
  aiResponse: string;
  domain: string;
  taskType: TaskType | string;
  provider?: string;
  language?: string;
  systemPrompt?: string | null;
  conversationHistory?: Array<Record<string, any>> | null;
  conversationTurn?: number;
  priority?: Priority | string;
  metadata?: Record<string, any> | null;
}

export interface SessionReportSummary {
  totalEntries: number;
  totalResponses: number;
  averageCompositeScore: number;
  scoreDistribution: {
    excellent: number;
    good: number;
    acceptable: number;
    poor: number;
    critical: number;
  };
}

export interface SessionReportPillarSummary {
  good: {
    totalSignals: number;
    topCategories: string[];
    averageReinforcementValue: number;
  };
  bad: {
    totalSignals: number;
    bySeverity: {
      P0: number;
      P1: number;
      P2: number;
      P3: number;
      P4: number;
    };
    topCategories: string[];
  };
  learned: {
    totalInsights: number;
    topCategories: string[];
  };
  remember: {
    newRules: number;
    existingRulesApplied: number;
    existingRulesViolated: number;
  };
}

export interface SessionReport {
  reportId: string;
  sessionId: string;
  clientId: string;
  evaluator: {
    evaluatorId: string;
    name?: string;
  };
  period: {
    startTime: string;
    endTime: string;
    totalDuration: number;
  };
  model: {
    modelId: string;
    provider: string;
  };
  summary: SessionReportSummary;
  pillarSummary: SessionReportPillarSummary;
  topIssues: Array<{
    rank: number;
    category: string;
    occurrences: number;
    description: string;
  }>;
  keyLearnings: string[];
  newMemoryRules: string[];
  recommendations: string[];
}

export interface ClientConfig {
  clientId: string;
  apiKey: string;
  environment?: 'production' | 'staging';
  timeout?: number;
  retryConfig?: {
    maxRetries?: number;
    backoffFactor?: number;
    retryOn?: number[];
  };
}

export class ASRFeedbackError extends Error {
  statusCode: number | null;
  constructor(message: string, statusCode?: number | null);
}

export class AuthenticationError extends ASRFeedbackError {}
export class ValidationError extends ASRFeedbackError {
  details: any[];
  constructor(message: string, details?: any[]);
}
export class RateLimitError extends ASRFeedbackError {
  retryAfter: number | null;
  constructor(message: string, retryAfter?: number | null);
}
export class NotFoundError extends ASRFeedbackError {}

export class ASRFeedbackClient {
  constructor(config: ClientConfig);

  submitResponse(params: SubmitResponseParams): Promise<string>;
  submitBatch(responses: Array<Record<string, any>>): Promise<Record<string, any>>;
  getFeedback(entryId: string): Promise<FeedbackEntry>;
  listFeedback(params?: Record<string, any>): Promise<Record<string, any>>;
  getSessionReport(sessionId: string): Promise<SessionReport>;
  listMemoryRules(params?: Record<string, any>): Promise<MemoryRule[]>;
  configureWebhook(config: { url: string; events: string[]; secret: string }): Promise<Record<string, any>>;
}
