# Engineering Rules (59-Control Code Hygiene & Vibe Engineering Standard)
<!-- Last updated: 2026-11-19 IST -->
<!-- DYNAMIC FILE — canonical source of truth; tool adapters point here -->

## 1. Governance Split (Where CI Ends & Canonical Instructions Begin)
- **Deterministic CI (23 controls):** Formatting, strict types, complexity/nesting caps, broad-catch bans, acyclic graphs, SAST, SHA-pinned actions, SCA/SBOM, tests — enforced by `scripts/check_hygiene_gates.py` and `.github/workflows/`.
- **Canonical Agent Rules (21 controls):** Semantic hygiene rules below, enforced at generation time by `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` and audited by the read-only `hygiene-reviewer` subagent.
- **Assistive Hybrid (11 controls):** Concurrency, DB migrations, LSP contracts, Modular Mirage, hot-path efficiency, AppSec edge cases, TDD test authoring — AI flags/drafts, humans must verify.
- **Never Delegate to AI (4 controls):** Human mental-model PR walkthroughs, peer-review context/SLA discipline, external IAM secret-rotation SLAs, and local IDE trace capture.

## 2. Mandatory Semantic Hygiene Rules (21 Canonical Agent Rules)
- **DRY (semantic):** Search existing utilities (`rg` / `ast-grep`) before creating new helpers; never duplicate business rules across modules.
- **KISS:** Ban nested ternaries and clever one-liners; flatten nesting with guard clauses and extract complex conditionals into named booleans.
- **YAGNI:** Solve only the requested requirement; zero speculative abstractions, unused flags, or premature scalability hooks.
- **Least Astonishment:** Pure getters/calculators/validators (`get*`, `calc*`, `is*`) must never mutate global state, write storage, or trigger network/email side effects.
- **Curly's Law:** One variable, function, or class = one semantic purpose; never repurpose variables mid-scope.
- **Boy Scout Rule:** Leave touched files cleaner — zero net new warnings, remove dead branches, and resolve or ticket obsolete TODOs.
- **SOLID & Boundaries:** Single responsibility (no God Classes); prefer extension via interfaces/composition (OCP); narrow client-specific interfaces with zero empty/`NotImplementedError` stubs (ISP); domain logic depends on abstractions, not concrete DB/HTTP drivers (DIP); strict UI/domain/persistence firewalls.
- **Naming & Constants:** Use full, pronounceable, intent-revealing identifiers; extract all business thresholds, rates, and status literals into named constants (zero hard-coding).
- **Short, Atomic Functions:** Target <=20 lines and one atomic action per function (excluding declarative UI/config/fixtures).
- **Comments, Docs & Dead Code:** Write comments only to explain *why* (business constraints, invariants, tradeoffs), never *what*. Delete commented-out code. Update public docblocks and README/API docs in the same diff; tag all Markdown code fences (MD040).
- **Operational & Data Safety:** Use structured logging with correlation IDs; never log PII, tokens, passwords, or raw secrets. Validate every external input against a strict schema (Zod/Pydantic/JSON Schema) and enforce explicit timeouts + bounded retries on outbound calls.
- **Context-Saturation Guard:** Check file length before editing; never append new features onto files >500 LOC — extract a cohesive module instead.

## 3. Verification & Definition of Done
- [ ] `python3 scripts/check_hygiene_gates.py` passes
- [ ] Lint, strict typecheck, tests (with edge/adversarial cases), and build pass
- [ ] Independent read-only `hygiene-reviewer` subagent audited the diff
- [ ] Human author wrote the PR mental-model summary (never AI-generated)
- [ ] `docs/ai/change-trace.md` updated (+ `mistakes.md` / `decision-log.md` if applicable)
- [ ] Granular commit message explains what + why

## 4. Security & Safety
- Never read, print, or commit `.env` or credentials (enforced deterministically via `.claude/settings.json` deny rules and `.agents/hooks.json`).
- Report vulnerabilities via `SECURITY.md`.
