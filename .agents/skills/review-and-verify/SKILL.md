---
name: review-and-verify
description: Run deterministic CI hygiene gates and invoke the read-only hygiene-reviewer subagent before committing or opening a PR.
---
# Review and Verify

1. Run `python3 scripts/check_hygiene_gates.py`, lint, strict typecheck, tests, and build.
2. Invoke the read-only `hygiene-reviewer` subagent (`.agents/agents/hygiene-reviewer.md`) on the git diff.
3. Fix all P0 Blocker and P1 High findings before committing.
4. Escalate auth, privacy, concurrency, and DB migration changes to human `CODEOWNERS`.
5. Leave the PR Architecture & Mental-Model Walkthrough for the human author to write.
