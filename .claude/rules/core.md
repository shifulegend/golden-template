# Core Code Hygiene Rules — All Code
<!-- Unscoped rule: loads at launch alongside CLAUDE.md -->

- Search existing modules (`rg` / `ast-grep`) before writing new helpers (DRY); never duplicate business rules.
- Target <=20 lines and one atomic action per function; flatten nesting with early returns; ban nested ternaries (KISS).
- Solve only the requested requirement — zero speculative abstractions or unused flags (YAGNI).
- Pure getters/calculators (`get*`, `calc*`, `is*`) never mutate global state or trigger external I/O (Least Astonishment).
- Never repurpose variables mid-scope (Curly's Law); never append new features onto files >500 LOC.
- Use full, intent-revealing names; zero magic numbers/strings or hard-coded values.
- Catch specific exception types with structured logging; zero broad catches (`except: pass`).
- Write comments only for *why*, never *what*; delete commented-out dead code.
- Verify: `python3 scripts/check_hygiene_gates.py` → lint → strict typecheck → test → build.
