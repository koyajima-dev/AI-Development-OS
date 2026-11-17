# Pending cross-project model-selection safeguards

Recorded: 2026-11-18. Owner: AID OS. Status: PARK / NOT VERIFIED (not a Task OS Native blocking dependency).

## Confirmed baseline
- AID OS: MODEL_VERIFICATION_GATE.md and AGENTS.md committed on GitHub.
- GitHub AGENTS.md applied and re-fetched in task-os, FinanceAI, shift-tool and AI-Development-OS (four accessible repositories).
- task-os pre-existing AGENTS.md rules preserved.

## Deferred work / acceptance
1. **Local sync** — Check actual Mac local repository HEAD and diff against GitHub; do not assume sync. Preserve dirty/untracked and do not force pull. PASS only with direct local evidence.
2. **Additional projects** — Inventory development projects not represented by the four accessible GitHub repositories; reuse existing rules and distribution path. Do not create repositories merely to distribute this policy.
3. **AID OS propagation** — Inspect existing knowledge distribution mechanism before modifying. Connect only if existing machinery supports it safely. Confirm send, receipt, and applied policy separately; do not equate a committed markdown file with automatic distribution.
4. **ChatGPT chat-level enforcement** — Repository AGENTS.md does not automatically govern ordinary ChatGPT conversations. Investigate supported shared instruction mechanisms; record technical limits and verify behavior rather than asserting guaranteed enforcement.
5. **Behavioral validation** — At next actual Codex/Claude Code model-selection instruction, check official model documentation and effort levels, source/date, rationale, account-specific availability, escalation stop. PASS only after reviewing the real generated instruction; do not invent model names.

## Guardrails
- No new infrastructure, accounts, App IDs, containers, or repositories without evidence of necessity.
- Preserve user data and existing project work. Escalate only for permission changes, destructive or irreversible changes, cost, or scope changes.
- Keep this backlog outside Task OS Native's Trial 020 critical path. Resume Trial 020 without waiting for these items.
