# Decision Log
<!-- DYNAMIC FILE — updated by AI agents when architectural, tooling, or workflow decisions are made -->
<!-- Newest entries first -->

## Entry Template
```
### [TIMESTAMP] — <Decision Title>
- **Context**: Why this decision was needed
- **Decision**: What was decided
- **Rationale**: Why this option was chosen
- **Alternatives Rejected**: What else was considered and why rejected
- **Consequences**: What this means going forward
- **Reversible**: Yes / No / Partially
```

---

### [2026-10-30 IST] — Adopt a README standard from readme-guidance
- **Context**: READMEs in repos created from this template were written ad hoc; the owner keeps a curated README playbook in `shifulegend/readme-guidance`.
- **Decision**: Add `docs/ai/readme-guidance.md` (condensed playbook + checklist) and `docs/README.template.md`; point every tool entrypoint and docs rule at it.
- **Rationale**: One canonical source, synced to Claude Code, Copilot and Antigravity per `tool-sync-policy.md`.
- **Alternatives Rejected**: Copying the whole guidance archive (too large, mostly third-party verbatim docs); linking only to the private repo (not readable by agents in new repos).
- **Consequences**: Agents follow the same README order and checklist in every new repo.
- **Reversible**: Yes

