---
trigger: glob
globs: "**/*.test.*, **/*.spec.*, tests/**, test/**"
description: TDD-first contract testing, zero flake, and regression logging
---
# Test Rules

- Write failing contract/unit tests (including edge/adversarial cases) before implementing.
- Never weaken, skip, or comment out failing assertions to force a green build.
- One test per behavior with descriptive names; 0% tolerated flake rate.
- Log every regression in `docs/ai/mistakes.md` with a regression test.
