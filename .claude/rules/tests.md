---
paths:
  - "**/*.test.*"
  - "**/*.spec.*"
  - "tests/**"
  - "test/**"
---
# Testing & TDD Rules

- Follow TDD-first: write failing contract/unit tests (including edge/adversarial cases) before implementing.
- Never weaken, skip, or delete existing assertions to make tests pass.
- One test per behavior with descriptive names stating input + expected outcome; 0% tolerated flake rate.
- Every bug fix ships with a regression test and a `docs/ai/mistakes.md` entry.
- Verify log-redaction and schema-validation boundaries in unit tests.
