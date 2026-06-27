# Golden Template — shifulegend

A cross-tool AI development template for starting any new repository with a full documentation-first, modular, verification-first workflow.

## What's Included

### Shared Canonical Memory (`docs/ai/`)
| File | Purpose |
|------|---------|
| `project-overview.md` | Project purpose, stack, architecture |
| `engineering-rules.md` | Modularity, zero-hardcoding, verification rules |
| `mistakes.md` | Central mistake log — read first every session |
| `decision-log.md` | Timestamped decisions |
| `change-trace.md` | Notable changes per sub-step |
| `session-start-checklist.md` | Mandatory startup checklist |
| `commit-log-guidance.md` | Commit message standards |
| `tool-sync-policy.md` | How tool-specific files stay in sync |

### GitHub Copilot (`.github/`)
- `copilot-instructions.md` — repo-wide instructions
- `instructions/*.instructions.md` — scoped instructions (core, docs, tests, config)
- `prompts/*.prompt.md` — reusable prompts (start-session, plan, implement, review, debug, memory)

### Claude Code (`CLAUDE.md` + `.claude/`)
- `CLAUDE.md` — project memory entrypoint
- `.claude/rules/` — modular scoped rules (core, docs, tests, config)
- `.claude/skills/` — reusable skills (session-start, project-memory, review-verify, implement)

### Google Antigravity (`gemini/` + `.agents/`)
- `gemini/GEMINI.md` — global Antigravity rules
- `AGENTS.md` — cross-tool portability layer
- `.agents/rules/` — scoped rules (core, docs, tests, config)
- `.agents/workflows/` — reusable workflows (start-session, review-verify, update-memory)

## How to Use

### Creating a New Repo from This Template
1. Go to [github.com/shifulegend/golden-template](https://github.com/shifulegend/golden-template)
2. Click **Use this template** → **Create a new repository**
3. Fill in the new repo details and create

### After Creating from Template
1. Update `docs/ai/project-overview.md` with your project's purpose, stack, and architecture.
2. Search for all `TODO` markers and fill them in.
3. Update the `TIMESTAMP` placeholders or let your AI agent update them.
4. Run your first AI session using `start-session` prompt/skill/workflow.

## Core Principles
- **Extremely modular** — smallest sensible unit, explicit interfaces
- **Zero hard-coding** — config files, env vars, schemas, or databases for all behavior
- **Documentation-first** — docs updated proactively every session
- **Mistake-first sessions** — always read mistake log before coding
- **Granular commits** — one small, reviewable sub-step per commit
- **Cross-tool portable** — Claude Code, GitHub Copilot, and Google Antigravity all supported

## AI Agent Dynamic Update Rule
All files in this template are **dynamic**. Any AI agent working in a repo created from this template must proactively update the relevant files every session — without waiting for explicit user prompts.
