# Google Antigravity — Workspace Instructions
<!-- Last updated: 2026-11-19 IST · Workspace root per antigravity.google/docs/cli/best-practices/ -->
<!-- Canonical source: docs/ai/ and AGENTS.md -->

Follow `AGENTS.md` and `docs/ai/engineering-rules.md` as the primary workspace rules.

## Project Context (Keep in sync with `docs/ai/project-overview.md`)
- **Purpose**: TODO
- **Stack**: TODO
- **Commands**: `python3 scripts/check_hygiene_gates.py` (hygiene gates); TODO (dev, lint, typecheck, test, build)

## Antigravity Native Governance (Official Spec)
- **Rules (`.agents/rules/*.md`):** Uses official YAML `trigger:` frontmatter (`always_on`, `glob`, `model_decision`, `manual`) to minimize per-turn token cost.
- **Skills (`.agents/skills/*/SKILL.md`):** Progressive-disclosure skills (`/session-start`, `/implement-task`, `/review-and-verify`, `/project-memory`) migrated from legacy `.agents/workflows/`.
- **Read-Only Subagent (`.agents/agents/hygiene-reviewer.md`):** Independent diff auditor with edit/shell tools omitted.
- **Deterministic Hooks (`.agents/hooks.json`):** `PreToolUse` guardrails blocking `.env`/secret edits and running `scripts/check_hygiene_gates.py` before `git push`.
