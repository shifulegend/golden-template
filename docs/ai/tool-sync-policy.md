# Tool Sync Policy
<!-- Last updated: 2026-11-19 IST -->
<!-- DYNAMIC FILE — verified deterministically by scripts/check_hygiene_gates.py -->

## Canonical Source of Truth
`docs/ai/**` is the primary source of truth for project memory, rules, and decisions. `AGENTS.md` is the concise (<200 lines) cross-tool entrypoint shared across Claude Code, Google Antigravity, and other agents.

## Official Adapter Layout (Validated by CI)
| Tool | Entrypoint | Scoped Rules | Skills / Prompts | Read-Only Reviewer | Deterministic Guardrails |
| --- | --- | --- | --- | --- | --- |
| **Claude Code** | `CLAUDE.md` (imports `@AGENTS.md`) | `.claude/rules/*.md` (YAML `paths:`) | `.claude/skills/*/SKILL.md` | `.claude/agents/hygiene-reviewer.md` | `.claude/settings.json` (`permissions.deny` + hooks) |
| **Google Antigravity** | `GEMINI.md` + `AGENTS.md` (+ `gemini/GEMINI.md` mirror) | `.agents/rules/*.md` (YAML `trigger:`) | `.agents/skills/*/SKILL.md` | `.agents/agents/hygiene-reviewer.md` | `.agents/hooks.json` (`PreToolUse`) |
| **GitHub Copilot** | `.github/copilot-instructions.md` | `.github/instructions/*.instructions.md` | `.github/prompts/*.prompt.md` | `.github/prompts/review-changes.prompt.md` | `.github/workflows/ci.yml` |

## Sync Rules
1. Update shared `docs/ai/` files FIRST.
2. Update `AGENTS.md` if a repo-wide rule changes (keep under 200 lines).
3. Sync tool-specific rules, skills, and hooks; run `python3 scripts/check_hygiene_gates.py`.
4. Record the change in `docs/ai/change-trace.md` and propose a commit checkpoint.

## Conflict Resolution
If any tool-specific file conflicts with `docs/ai/`, `docs/ai/` wins. All canonical AI files are protected by `CODEOWNERS`.
