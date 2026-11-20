---
paths:
  - "config/**"
  - "*.config.*"
  - ".env*"
  - "schemas/**"
  - "settings/**"
---
# Config, Secrets & Schema Rules

- Zero hard-coded environment values or secrets anywhere; externalize via env vars or secret managers (12-Factor).
- Only `.env.example` may be committed; keep `.env` in `.gitignore` and blocked in `.claude/settings.json`.
- Validate all config and external API inputs against strict schemas (Zod/Pydantic/JSON Schema) at startup/boundary.
- Document safe defaults for every config key in `.env.example` and `docs/ai/engineering-rules.md`.
- Enforce explicit timeouts and bounded retries on all outbound HTTP/DB client configurations.
