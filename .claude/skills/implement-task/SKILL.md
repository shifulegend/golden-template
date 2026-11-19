---
name: implement-task
description: Implement an approved plan with TDD-first discipline, tight single-concern diffs, deterministic verification, and continuous project-memory updates.
---
# Implement Task

1. Confirm the plan is approved and scope is a single logical concern.
2. Check file sizes before editing — extract a new module rather than appending to files >500 LOC.
3. Write or verify failing tests first (Red), implement minimal clean code (Green), then refactor for KISS/DRY/SOLID.
4. Run `python3 scripts/check_hygiene_gates.py`, lint, strict typecheck, tests, and build.
5. Update `docs/ai/change-trace.md` (plus `mistakes.md` / `decision-log.md` if applicable) and propose a granular commit message (what + why).
