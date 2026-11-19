---
trigger: always_on
description: Core semantic code hygiene rules applied across all edits
---
# Core Code Hygiene Rules

- Search existing modules (`rg` / `ast-grep`) before creating new helpers (DRY); never duplicate business rules.
- Target <=20 lines and one atomic action per function; ban nested ternaries; flatten nesting with early returns (KISS).
- Solve only the requested requirement — zero speculative abstractions (YAGNI) and zero hard-coded values.
- Pure getters/calculators (`get*`, `calc*`, `is*`) never mutate global state or trigger I/O (Least Astonishment).
- Never repurpose variables mid-scope (Curly's Law); never append new features onto files >500 LOC.
- Catch specific exceptions only (zero `except: pass`); write *why* comments, never *what*; delete dead code.
- Verify: `python3 scripts/check_hygiene_gates.py` → lint → strict typecheck → test → build.
