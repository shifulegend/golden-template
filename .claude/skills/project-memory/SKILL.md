---
name: project-memory
description: Synchronize durable lessons, mistakes, decisions, and rule updates across docs/ai/ and all tool adapters.
---
# Project Memory Update

1. Classify the lesson: mistake, architectural decision, repo-wide rule, or scoped rule.
2. Update `docs/ai/` first (`mistakes.md`, `decision-log.md`, `engineering-rules.md`, `change-trace.md`).
3. Sync `AGENTS.md` (<200 lines) and tool adapters per `docs/ai/tool-sync-policy.md`.
4. Run `python3 scripts/check_hygiene_gates.py` to verify all frontmatter and sync gates pass.
5. Propose commit: `ai(memory): ...`
