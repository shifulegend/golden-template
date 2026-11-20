# Claude Code — Project Instructions
<!-- Last updated: 2026-11-19 IST · Target: <200 lines per code.claude.com/docs/en/memory -->

@AGENTS.md

## Project Context (Keep in sync with `docs/ai/project-overview.md`)
- **Purpose**: TODO
- **Stack**: TODO
- **Commands**: `python3 scripts/check_hygiene_gates.py` (hygiene gates); TODO (dev, lint, typecheck, test, build)

## Claude Code Native Governance (Official Spec)
- **Deterministic Enforcement (`.claude/settings.json`):** Hard blocks on reading/editing `.env` and secret files (`permissions.deny`) plus lifecycle hooks — never rely on prose alone for zero-exception rules.
- **Path-Scoped Rules (`.claude/rules/*.md`):** Loaded automatically via YAML `paths:` frontmatter when touching matching files (`core.md`, `config.md`, `docs.md`, `tests.md`).
- **On-Demand Skills (`.claude/skills/*/SKILL.md`):** Invoked via `/session-start`, `/implement-task`, `/review-and-verify`, `/project-memory`.
- **Independent Read-Only Auditor (`.claude/agents/hygiene-reviewer.md`):** Delegate diff audits to `hygiene-reviewer` so the writing session never grades its own homework.
- **Personal Overrides:** Put local preferences in gitignored `CLAUDE.local.md` or `.claude/settings.local.json`.
