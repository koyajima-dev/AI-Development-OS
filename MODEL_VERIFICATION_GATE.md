# Cross-project model verification gate

Scope: all Codex and Claude Code implementation instructions prepared for any development project.

Before recommending an execution model:
1. Identify the execution tool (Codex or Claude Code).
2. Consult the provider's current official model documentation. Record the source URL and date checked. Do not reuse a previous conversation's model names as current evidence.
3. Confirm exact model name and supported reasoning/effort settings in that tool; do not transfer names or settings between providers.
4. Select the least costly sufficient model based on task difficulty, failure impact, validation cost, and total work.
5. Distinguish provider-documented availability from availability verified in the user's own account. Mark the latter UNKNOWN if not checked.
6. Include the recommended model, effort, rationale, escalation condition, and Human decision point in the instruction.
7. If official verification fails, stop the model-specific recommendation rather than guessing; other safe work may continue.

Acceptance: the actual instruction contains a verifiable official source, checked date, concrete tool/model/effort combination, cost-risk rationale, and a separate account-availability status.

Limits: this repository policy does not automatically run inside unrelated ChatGPT chats, local repositories, or other agents. Cross-project enforcement requires verified delivery and execution in each target environment. A written policy alone is not a PASS for automatic propagation.
