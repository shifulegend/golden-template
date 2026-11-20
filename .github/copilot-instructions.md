# GitHub Copilot — Repository Instructions
<!-- Last updated: 2026-11-19 IST -->
<!-- Canonical source: docs/ai/ and AGENTS.md — if conflict exists, docs/ai/ wins -->

## Session Start (Mandatory)
1. Read `AGENTS.md`, `docs/ai/project-overview.md`, `docs/ai/engineering-rules.md`, `docs/ai/mistakes.md`, and `docs/ai/decision-log.md`.
2. Read relevant `.github/instructions/*.instructions.md` for the area being changed.
3. State assumptions, open risks, and relevant rules before editing.

## Core Semantic Hygiene Rules (Synced with `AGENTS.md`)
- DRY (search existing helpers before creating new ones); never append features to files >500 LOC.
- KISS & YAGNI (no nested ternaries, no speculative abstractions, <=20-line atomic functions).
- Least Astonishment (pure `get*`/`calc*`/`is*` helpers have zero side effects) & Curly's Law.
- SOLID boundaries, zero hard-coding, specific error boundaries (zero `except: pass`), structured PII-free logging, strict schemas, and explicit outbound timeouts/retries.
- Comments explain *why*, never *what*; delete dead code; tag all Markdown code fences (MD040).
- Never weaken test assertions and never auto-write the human PR Architecture & Mental-Model Summary.

## Verification & Dynamic Updates
- Verify: `python3 scripts/check_hygiene_gates.py` → lint → strict typecheck → test → build.
- Update `docs/ai/mistakes.md`, `docs/ai/decision-log.md`, and `docs/ai/change-trace.md` proactively every session.
- Follow `docs/ai/readme-guidance.md` for `README.md` and `docs/ai/context-efficiency.md` for code search.
