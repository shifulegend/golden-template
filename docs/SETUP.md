# Setup Guide
<!-- Last updated: 2026-11-19 IST -->

## Prerequisites
- Git, Python >= 3.11 (for deterministic hygiene gates), and `pre-commit`
- GitHub CLI (optional): `brew install gh`

## First-Time Setup
```bash
# 1. Clone
git clone https://github.com/shifulegend/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

# 2. Copy env template (NEVER commit .env)
cp .env.example .env

# 3. Install pre-commit hooks & run deterministic hygiene gates
pre-commit install
python3 scripts/check_hygiene_gates.py

# 4. Install project dependencies (replace for your stack)
# TODO: npm ci | uv sync --frozen | go mod download
```

## Available Commands
| Command | Purpose |
| --- | --- |
| `python3 scripts/check_hygiene_gates.py` | Deterministic hygiene, SHA-pinning & canonical AI doc checks |
| `node scripts/generate-repo-map.js` | Regenerate `docs/ai/repo-map.md` |
| `TODO` | Lint & format |
| `TODO` | Strict typecheck |
| `TODO` | Deterministic test suite |
| `TODO` | Build |

## AI Agent Setup (Claude Code · Google Antigravity · Copilot)
1. Open the repo in Claude Code, Google Antigravity, or GitHub Copilot.
2. Run `/session-start` (Claude Code / Antigravity skill) or `start-session.prompt.md` (Copilot).
3. Fill in `docs/ai/project-overview.md` and `docs/ai/architecture.md` TODOs.
4. Before opening a PR, run `/review-and-verify` so the read-only `hygiene-reviewer` subagent audits your diff.
