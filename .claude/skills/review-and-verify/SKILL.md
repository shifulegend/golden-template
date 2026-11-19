---
name: review-and-verify
description: Run deterministic CI hygiene checks and delegate an independent read-only diff audit before committing or opening a PR.
---
# Review and Verify

1. Run `python3 scripts/check_hygiene_gates.py` plus lint, strict typecheck, tests, and build.
2. Spawn the read-only `hygiene-reviewer` subagent (`.claude/agents/hygiene-reviewer.md`) to audit the git diff independently.
3. Resolve all P0 Blocker and P1 High findings before committing.
4. Flag auth, privacy, concurrency, and DB migration diffs for mandatory human specialist sign-off.
5. Remind the human author to write the PR Architecture & Mental-Model Summary in their own words (never auto-write it).
