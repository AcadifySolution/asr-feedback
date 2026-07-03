/**
 * Example: Submit an AI response for evaluation and retrieve feedback.
 *
 * Usage:
 *   node submit-feedback.js
 */

const { ASRFeedbackClient, TaskType, Priority } = require('../asr-feedback-client');

async function main() {
  // Initialize the client
  const client = new ASRFeedbackClient({
    clientId: 'YOUR_CLIENT_ID',
    apiKey: 'YOUR_API_KEY',
    environment: 'staging', // Use 'production' for live
  });

  // Submit an AI response for evaluation
  const entryId = await client.submitResponse({
    responseId: 'demo-resp-001',
    modelId: 'gpt-4o-2025-08-06',
    userQuery: 'What are the benefits of cloud computing for small businesses?',
    aiResponse: [
      'Cloud computing offers several key benefits for small businesses:',
      '',
      '1. **Cost Savings** — No need to invest in expensive hardware.',
      '2. **Scalability** — Easily scale resources up or down.',
      '3. **Accessibility** — Access data from anywhere.',
      '4. **Security** — Major providers invest heavily in security.',
      '5. **Collaboration** — Enable real-time team collaboration.',
    ].join('\n'),
    domain: 'technology',
    taskType: TaskType.QUESTION_ANSWERING,
    provider: 'OpenAI',
    language: 'en',
    priority: Priority.STANDARD,
    metadata: {
      temperature: 0.7,
      maxTokens: 1024,
      customTags: ['cloud', 'small-business', 'benefits'],
    },
  });

  console.log(`✅ Response submitted for evaluation: ${entryId}`);

  // Retrieve feedback (in production, use webhooks)
  console.log(`\n📋 Retrieving feedback for ${entryId}...`);
  const feedback = await client.getFeedback(entryId);

  console.log(`\n${'='.repeat(60)}`);
  console.log(`Quality Score: ${feedback.qualityScore.composite}/100`);
  console.log(`${'='.repeat(60)}`);

  // Display Good Signals
  const good = feedback.pillars?.good || [];
  console.log(`\n✅ Good Signals (${good.length}):`);
  good.forEach((g) => {
    console.log(`  • [${g.categoryCode}] ${g.description}`);
  });

  // Display Bad Signals
  const bad = feedback.pillars?.bad || [];
  console.log(`\n❌ Bad Signals (${bad.length}):`);
  bad.forEach((b) => {
    console.log(`  • [P${b.severity}] [${b.categoryCode}] ${b.description}`);
  });

  // Display Learnings
  const learned = feedback.pillars?.learned || [];
  console.log(`\n📘 Learnings (${learned.length}):`);
  learned.forEach((l) => {
    console.log(`  • [${l.categoryCode}] ${l.observation}`);
  });

  // Display Memory Rules
  const remember = feedback.pillars?.remember || [];
  console.log(`\n🧠 Memory Rules (${remember.length}):`);
  remember.forEach((m) => {
    console.log(`  • [${m.ruleType}] ${m.ruleText}`);
  });
}

main().catch(console.error);
