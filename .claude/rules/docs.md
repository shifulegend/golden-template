---
paths:
  - "**/*.md"
  - "docs/**"
---
# Documentation & Markdown Hygiene Rules

- Timestamp every documentation update (`YYYY-MM-DD HH:MM IST`); keep newest entries first in logs.
- Every fenced code block MUST specify an explicit language tag (e.g., `bash`, `python`, `text`) — MD040.
- Update public docblocks and README/API docs in the same diff whenever signatures or behavior change.
- Update `docs/ai/mistakes.md` on errors, `docs/ai/decision-log.md` on durable decisions, and `docs/ai/change-trace.md` per sub-step.
- When editing `README.md`, follow `docs/ai/readme-guidance.md` and `docs/README.template.md`.
