---
name: implement-task
description: Execute an approved implementation plan with TDD-first verification, tight modular diffs, and continuous project-memory updates.
---
# Implement Task

1. Confirm the implementation plan is approved and scoped to one logical concern.
2. Check file size before editing — extract a new module instead of appending to files >500 LOC.
3. Follow Red → Green → Refactor (never weaken assertions to pass).
4. Run `python3 scripts/check_hygiene_gates.py`, lint, strict typecheck, tests, and build.
5. Update `docs/ai/change-trace.md` and propose a granular commit message (what + why).
