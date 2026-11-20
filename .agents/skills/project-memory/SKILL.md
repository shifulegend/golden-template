---
name: project-memory
description: Update shared project memory in docs/ai/ and synchronize all tool adapters per docs/ai/tool-sync-policy.md.
---
# Update Project Memory

1. Classify the lesson: mistake, decision, rule, or workflow improvement.
2. Update `docs/ai/` first (`mistakes.md`, `decision-log.md`, `engineering-rules.md`, `change-trace.md`).
3. Sync `AGENTS.md`, `GEMINI.md`, `.agents/rules/*.md`, and sibling adapters per `docs/ai/tool-sync-policy.md`.
4. Verify with `python3 scripts/check_hygiene_gates.py` and propose commit: `ai(memory): ...`
