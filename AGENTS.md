# AGENTS.md — Canonical Cross-Tool Project Instructions
<!-- Last updated: 2026-11-19 IST · Target: <200 lines -->
<!-- Canonical source: docs/ai/ — if conflict exists, docs/ai/ wins -->

## Session Start (Mandatory)
1. Read `docs/ai/project-overview.md`, `docs/ai/engineering-rules.md`, `docs/ai/mistakes.md`, and `docs/ai/decision-log.md`.
2. Consult `docs/ai/repo-map.md` and use `rg` / `ast-grep` for code search (see `docs/ai/context-efficiency.md`).
3. State relevant rules, recent mistakes, open risks, and assumptions before editing.

## Non-Negotiable Semantic Hygiene Rules (21 Agent-Enforced Controls)
- **DRY & Context Saturation:** Search existing helpers before creating new ones; never duplicate business rules. Never append new features onto files >500 LOC — extract a cohesive module.
- **KISS & YAGNI:** No nested ternaries, clever one-liners, or speculative abstractions. Flatten nesting with guard clauses and named booleans.
- **Least Astonishment & Curly's Law:** Pure getters/calculators (`get*`, `calc*`, `is*`) never mutate global state or trigger I/O. Never repurpose a variable mid-scope.
- **SOLID & Boundaries:** Single responsibility (no God Classes); prefer extension via interfaces (OCP); narrow interfaces with zero `NotImplementedError` stubs (ISP); domain logic depends on abstractions, not concrete DB/HTTP drivers (DIP).
- **Functions, Naming & Constants:** Target <=20 lines and one atomic action per function. Use full, intent-revealing names; zero magic numbers/strings or hard-coded values.
- **Comments, Docs & Dead Code:** Comments explain *why*, never *what*. Delete commented-out code. Update public docblocks, `README.md` (per `docs/ai/readme-guidance.md`), and `docs/ai/change-trace.md` in the same diff.
- **Operational & Data Safety:** Use structured logging with correlation IDs; never log PII, tokens, or secrets. Validate all external inputs with strict schemas (Zod/Pydantic/JSON Schema) and set explicit timeouts + bounded retries on outbound calls.

## Boundaries — Never Delegate to AI
- Never weaken or delete test assertions to make failing tests pass (TDD-first).
- Never author the human PR Architecture & Mental-Model Walkthrough on the developer's behalf.
- Flag auth, privacy, concurrency, and DB migration diffs for mandatory human specialist review.

## Verification Before Commit
Run: `python3 scripts/check_hygiene_gates.py` → lint → strict typecheck → test → build, then invoke the read-only `hygiene-reviewer` subagent on your diff.

## Dynamic Memory Updates
Proactively update `docs/ai/mistakes.md` (on errors), `docs/ai/decision-log.md` (on decisions), and `docs/ai/change-trace.md` (per sub-step). See `docs/ai/tool-sync-policy.md`.
