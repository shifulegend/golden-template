# Golden Template — shifulegend

A cross-tool AI development template embedding the **59-control Code Hygiene & Vibe Engineering Standard**, deterministic SHA-pinned CI/CD security gates, and official canonical instruction architectures for **Anthropic Claude Code**, **Google Antigravity**, and **GitHub Copilot**.

## What's Included

### 1. Deterministic CI, Security & Supply-Chain Gates (Controls 1–6)
- `.github/workflows/ci.yml` — 100% SHA-pinned CI running `scripts/check_hygiene_gates.py` (repo + PR diff ratchets) and stack lint/typecheck/test/build gates.
- `.github/workflows/security-hygiene.yml` — SHA-pinned full-history Gitleaks secret scan + SAST/SCA/SBOM activation stubs.
- `scripts/check_hygiene_gates.py` — Zero-dependency validator enforcing 40-char SHA pinning, `.env`/`.gitignore` parity, YAML/JSON validity, MD040 code fence tags, suppression justification, >500 LOC append guard, `CODEOWNERS`, and official Claude/Antigravity canonical doc specs.
- `.pre-commit-config.yaml`, `.editorconfig`, `.markdownlint.json`, `SECURITY.md`, `.github/dependabot.yml`, `.github/PULL_REQUEST_TEMPLATE.md`, and `CODEOWNERS`.

### 2. Official Canonical AI Instructions (21 Semantic Hygiene Controls)
- **Cross-Tool Canonical Root:** `AGENTS.md` (<200 lines) + `docs/ai/**` (`engineering-rules.md`, `code-hygiene-controls.md`, `tool-sync-policy.md`, `context-efficiency.md`, `readme-guidance.md`, logs).
- **Anthropic Claude Code:** `CLAUDE.md` (imports `@AGENTS.md`), `.claude/settings.json` (deterministic `permissions.deny` + hooks), `.claude/rules/*.md` (YAML `paths:` frontmatter), `.claude/skills/*/SKILL.md` (YAML frontmatter), and read-only `.claude/agents/hygiene-reviewer.md`.
- **Google Antigravity:** Workspace-root `GEMINI.md` (+ `gemini/GEMINI.md` mirror), `.agents/hooks.json` (`PreToolUse` gates), `.agents/rules/*.md` (YAML `trigger:` frontmatter), `.agents/skills/*/SKILL.md` (migrated from legacy workflows), and read-only `.agents/agents/hygiene-reviewer.md`.
- **GitHub Copilot:** `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`, `.github/prompts/*.prompt.md`.

## Quickstart
```bash
cp .env.example .env
pre-commit install
python3 scripts/check_hygiene_gates.py
```

## After Creating a New Repo from This Template
1. Update `docs/ai/project-overview.md`, `docs/ai/architecture.md`, and `docs/SETUP.md`.
2. Replace the stack stubs in `.github/workflows/ci.yml` (keeping all GitHub Actions pinned to full 40-char commit SHAs).
3. Uncomment your ecosystem in `.github/dependabot.yml` and enable branch protection per `docs/BRANCHES.md`.
4. Copy `docs/README.template.md` over `README.md` following `docs/ai/readme-guidance.md`.
5. Start your first AI session with `/session-start`.

## License
MIT — see [LICENSE](LICENSE).
