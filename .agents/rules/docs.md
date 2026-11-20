---
trigger: glob
globs: "**/*.md, docs/**"
description: Timestamped documentation, MD040 code fences, and README standards
---
# Documentation Rules

- Timestamp every documentation update (`YYYY-MM-DD HH:MM IST`); newest entries first in log files.
- Tag every fenced code block with an explicit language (`bash`, `python`, `text`) — MD040.
- Update `docs/ai/mistakes.md` on errors, `docs/ai/decision-log.md` on durable decisions, and `docs/ai/change-trace.md` per sub-step.
- Follow `docs/ai/readme-guidance.md` and `docs/README.template.md` when editing `README.md`.
