"""
Example: Submit an AI response for evaluation and retrieve feedback.

Usage:
    python submit_feedback.py
"""

from asr_feedback_client import ASRFeedbackClient, TaskType, Priority


def main():
    # Initialize the client
    client = ASRFeedbackClient(
        client_id="YOUR_CLIENT_ID",
        api_key="YOUR_API_KEY",
        environment="staging",  # Use "production" for live
    )

    # Submit an AI response for evaluation
    entry_id = client.submit_response(
        response_id="demo-resp-001",
        model_id="gpt-4o-2025-08-06",
        user_query="What are the benefits of cloud computing for small businesses?",
        ai_response=(
            "Cloud computing offers several key benefits for small businesses:\n\n"
            "1. **Cost Savings** — No need to invest in expensive hardware or "
            "maintain on-premise servers. Pay only for what you use.\n\n"
            "2. **Scalability** — Easily scale resources up or down based on "
            "demand, without long-term commitments.\n\n"
            "3. **Accessibility** — Access your data and applications from "
            "anywhere with an internet connection.\n\n"
            "4. **Security** — Major cloud providers invest heavily in security, "
            "often exceeding what small businesses can achieve independently.\n\n"
            "5. **Collaboration** — Enable real-time collaboration across teams, "
            "regardless of location.\n\n"
            "For most small businesses, starting with a cloud-based productivity "
            "suite (like Google Workspace or Microsoft 365) is the simplest first "
            "step."
        ),
        domain="technology",
        task_type=TaskType.QUESTION_ANSWERING,
        provider="OpenAI",
        language="en",
        priority=Priority.STANDARD,
        metadata={
            "temperature": 0.7,
            "max_tokens": 1024,
            "custom_tags": ["cloud", "small-business", "benefits"],
        },
    )

    print(f"✅ Response submitted for evaluation: {entry_id}")

    # Retrieve feedback (in production, use webhooks instead of polling)
    print(f"\n📋 Retrieving feedback for {entry_id}...")
    feedback = client.get_feedback(entry_id)

    print(f"\n{'='*60}")
    print(f"Quality Score: {feedback.quality_score.composite}/100 "
          f"({feedback.quality_score.band.upper()})")
    print(f"{'='*60}")

    # Display Good Signals
    print(f"\n✅ Good Signals ({len(feedback.pillars.good)}):")
    for good in feedback.pillars.good:
        print(f"  • [{good.category_code}] {good.description}")
        print(f"    Evidence: {good.evidence[:80]}...")
        print(f"    Reinforcement: {good.reinforcement_value}")

    # Display Bad Signals
    print(f"\n❌ Bad Signals ({len(feedback.pillars.bad)}):")
    for bad in feedback.pillars.bad:
        print(f"  • [P{bad.severity}] [{bad.category_code}] {bad.description}")
        print(f"    Root Cause: {bad.root_cause[:80]}...")
        print(f"    Remediation: {bad.remediation[:80]}...")

    # Display Learnings
    print(f"\n📘 Learnings ({len(feedback.pillars.learned)}):")
    for learning in feedback.pillars.learned:
        print(f"  • [{learning.category_code}] {learning.observation}")

    # Display Memory Rules
    print(f"\n🧠 Memory Rules ({len(feedback.pillars.remember)}):")
    for memory in feedback.pillars.remember:
        print(f"  • [{memory.rule_type}] {memory.rule_text}")
        print(f"    Scope: {memory.scope}")

    # Score Breakdown
    print(f"\n📊 Score Breakdown:")
    qs = feedback.quality_score
    print(f"  Good Signal Score:    {qs.good_signal_score}")
    print(f"  Bad Signal Penalty:   {qs.bad_signal_penalty}")
    print(f"  Severity Impact:      {qs.severity_impact}")
    print(f"  Completeness Score:   {qs.completeness_score}")
    print(f"  Consistency Score:    {qs.consistency_score}")
    print(f"  ────────────────────")
    print(f"  Composite Score:      {qs.composite}")


if __name__ == "__main__":
    main()
