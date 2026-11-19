---
trigger: model_decision
description: Apply whenever editing auth, payments, SQL/DB migrations, logging, concurrency, or CI workflows
---
# Security & Operational Hygiene Guardrails

- Use parameterized queries/ORMs only (0 string-interpolated SQL) and reversible migrations.
- Use structured logging with correlation IDs; never emit PII, tokens, passwords, or session cookies.
- Pin every third-party GitHub Action to a full 40-character commit SHA (OWASP A03:2025).
- Flag auth, privacy, concurrency, and migration diffs for mandatory human `CODEOWNERS` review.
