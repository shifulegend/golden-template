## Summary (Single Logical Concern — Control 5.1)
- **What changed:**
- **Why:**
- **Linked issue:** Refs #

## Human Architecture & Mental-Model Walkthrough (Control 7.2.5)
<!-- MANDATORY HUMAN-WRITTEN SECTION — DO NOT LET AN AI AGENT AUTO-WRITE THIS.
     Briefly explain in your own words how the change works, key invariants, and failure modes. -->
- **Key flow / state transitions:**
- **Edge cases & rollback plan:**

## Verification & Hygiene Checklist
- [ ] Local checks pass (`python3 scripts/check_hygiene_gates.py`, lint, strict typecheck, tests, build)
- [ ] Tests ship in this PR covering happy path + adversarial/edge cases (0% flake)
- [ ] Zero hardcoded secrets, PII in logs, or unmotivated linter/SAST suppressions
- [ ] Docs updated (`docs/ai/change-trace.md`, plus `decision-log.md` / `mistakes.md` if applicable)
- [ ] Specialist reviewer tagged if touching auth, privacy, concurrency, migrations, or AI rules
- [ ] UI screenshot or recording attached (if UI changed; otherwise N/A)

## AI Dual-Trace Reference (Control 7.2.6 — if AI-assisted)
- **Reasoning / system trace ID or link (PII & secrets redacted):** N/A
