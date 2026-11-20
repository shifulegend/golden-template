# Decision Log
<!-- DYNAMIC FILE — updated by AI agents when architectural, tooling, or workflow decisions are made -->
<!-- Newest entries first -->

## Entry Template
```markdown
### [TIMESTAMP] — <Decision Title>
- **Context**: Why this decision was needed
- **Decision**: What was decided
- **Rationale**: Why this option was chosen
- **Alternatives Rejected**: What else was considered and why rejected
- **Consequences**: What this means going forward
- **Reversible**: Yes / No / Partially
```

---

### [2026-11-19 IST] — Embed 59-Control Code Hygiene, SHA-Pinned CI & Official Claude/Antigravity Specs
- **Context**: Audited the golden template against the 59-control Code Hygiene & Vibe Engineering Checklist and live official Anthropic Claude Code and Google Antigravity canonical documentation.
- **Decision**: (1) Added deterministic CI gates (`scripts/check_hygiene_gates.py`, SHA-pinned `ci.yml`, `security-hygiene.yml`, `.pre-commit-config.yaml`, `.editorconfig`, `.markdownlint.json`, `SECURITY.md`, PR template). (2) Upgraded `.claude/rules/*.md` from stripped HTML comments to YAML `paths:` frontmatter, added YAML frontmatter to all `SKILL.md` files, added `.claude/settings.json` deny/hook guardrails, and added read-only `.claude/agents/hygiene-reviewer.md`. (3) Upgraded Google Antigravity to root `GEMINI.md` + `AGENTS.md`, YAML `trigger:` frontmatter in `.agents/rules/*.md`, migrated workflows to `.agents/skills/*/SKILL.md`, and added `.agents/agents/hygiene-reviewer.md` + `.agents/hooks.json`.
- **Rationale**: Aligns the template with official harness discovery rules so scoped rules, progressive skills, and deterministic hooks actually fire, while ensuring zero P0 blind spots across all 59 controls.
- **Alternatives Rejected**: Keeping unscoped HTML-comment rules and legacy `.agents/workflows/` (ignored or deprecated by current harnesses); putting all 59 controls into blocking CI (causes false-positive fatigue on the 7 semantic controls).
- **Consequences**: Every repo created from this template ships with passing deterministic hygiene gates and official multi-tool AI governance out of the box.
- **Reversible**: Yes

### [2026-10-30 IST] — Adopt a README standard from readme-guidance
- **Context**: READMEs in repos created from this template were written ad hoc; the owner keeps a curated README playbook in `shifulegend/readme-guidance`.
- **Decision**: Add `docs/ai/readme-guidance.md` (condensed playbook + checklist) and `docs/README.template.md`; point every tool entrypoint and docs rule at it.
- **Rationale**: One canonical source, synced to Claude Code, Copilot and Antigravity per `tool-sync-policy.md`.
- **Alternatives Rejected**: Copying the whole guidance archive (too large, mostly third-party verbatim docs); linking only to the private repo (not readable by agents in new repos).
- **Consequences**: Agents follow the same README order and checklist in every new repo.
- **Reversible**: Yes

