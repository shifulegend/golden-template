---
trigger: glob
globs: "config/**, *.config.*, .env*, schemas/**, settings/**"
description: 12-Factor configuration, secrets protection, and strict schema validation
---
# Config & Settings Rules

- Zero hard-coded values or secrets anywhere; externalize via env vars or secret managers.
- Only `.env.example` may be committed; never read or write real `.env` files.
- Validate all config and external API payloads against strict schemas (Zod/Pydantic/JSON Schema).
- Enforce explicit timeouts and bounded retries on all outbound HTTP/DB clients.
