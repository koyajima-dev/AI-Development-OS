# Model selection verification (Codex / Claude Code)

Before writing an implementation instruction that recommends a model, check the CURRENT official provider documentation for that execution tool. Record source URL and check date; verify exact model name and supported effort/reasoning levels. Do not infer from previous chats or confuse Codex with Claude Code.

Choose the least costly adequate model considering complexity, failure impact, verification and total work. State model, effort, reason, escalation trigger and Human stop point. Separate provider-documented support from account-specific availability (UNKNOWN until verified). If official verification fails, do not guess a model.

This instruction applies to agents operating in this repository. It does not automatically enforce behavior in unrelated ChatGPT chats or local copies. AID OS reference: koyajima-dev/AI-Development-OS/MODEL_VERIFICATION_GATE.md.

<!-- AID-OS:MODEL-OUTPUT-BLOCKER:START version=1 -->
MANDATORY OUTPUT GATE for every Codex/Claude Code implementation instruction (including follow-up, continuation, or read-only audit instructions):
- Before emitting the instruction, verify the CURRENT official provider documentation for that tool; do not cite fabricated or unvisited sources.
- Put a visible **Model verification** section INSIDE the single copy-ready instruction containing: tool; exact model ID; exact supported effort/reasoning level; official documentation URL(s); date actually checked; rationale based on total cost/risk; account availability (VERIFIED or UNKNOWN); escalation trigger; Human stop point.
- Check all nine fields immediately before sending. If any official model/effort claim cannot be verified, DO NOT emit a model-specific instruction or invent a citation. Explicitly report the blocker and continue only model-independent work.
- A previously chosen model or a separate paragraph outside the instruction does NOT satisfy this gate. Never omit the section merely because the work is a continuation.
- This is an agent instruction, NOT a technical guarantee for unrelated ChatGPT conversations. Verify actual outputs separately.
<!-- AID-OS:MODEL-OUTPUT-BLOCKER:END -->
