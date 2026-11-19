# 59-Control Code Hygiene & Governance Map
<!-- Last updated: 2026-11-19 IST -->
<!-- Reference map linking all 59 controls across 7 domains to their owner layer -->

| Layer | Controls | Share | Enforcement Mechanism |
| --- | --- | --- | --- |
| Deterministic CI Gate | 23 | 39% | `.github/workflows/ci.yml`, `security-hygiene.yml`, `scripts/check_hygiene_gates.py`, linters, SAST/SCA |
| Canonical AI Agent Instructions | 21 | 36% | `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, scoped rules + read-only `hygiene-reviewer` subagent |
| Hybrid Assistive (AI + Human) | 11 | 19% | CI proxy + AI draft/flag + mandatory human/CODEOWNERS sign-off |
| Irreducible Human / Org Process | 4 | 7% | Human PR walkthrough, review SLAs, IAM secret rotation (`SECURITY.md`), local trace hooks |
| **Total** | **59** | **100%** | **17 P0 (0 blind spots) · 31 P1 · 11 P2** |

## Official Canonical Document Compliance
- **Anthropic Claude Code:** `CLAUDE.md` (<200 lines, imports `@AGENTS.md`), `.claude/rules/*.md` (YAML `paths:` frontmatter), `.claude/skills/<name>/SKILL.md` (YAML `name`/`description`), `.claude/agents/hygiene-reviewer.md` (read-only), `.claude/settings.json` (deterministic `permissions.deny` + hooks).
- **Google Antigravity:** Root `GEMINI.md` + `AGENTS.md` (<200 lines), `.agents/rules/*.md` (YAML `trigger:` frontmatter: `always_on`/`glob`/`model_decision`/`manual`), `.agents/skills/<name>/SKILL.md` (migrated from legacy `.agents/workflows/`), `.agents/agents/hygiene-reviewer.md` (read-only), `.agents/hooks.json` (deterministic `PreToolUse` gates).
- **GitHub Copilot:** `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` (`applyTo:`), `.github/prompts/*.prompt.md`.
