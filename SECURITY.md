# Security Policy

## Reporting a Vulnerability
- **Do not** open a public GitHub issue for security vulnerabilities.
- Report privately via GitHub Security Advisories (**Security → Advisories → New draft advisory**) or contact the repository maintainer (`@shifulegend`) directly.
- Include reproduction steps, affected files/versions, and estimated impact.

## Secrets & Credential Hygiene (OWASP CICD-SEC-6)
- Zero hardcoded secrets in source, CI workflows, Docker `ENV`/`ARG`, or committed AI traces.
- Use short-lived **OIDC workload identities** scoped per CI job rather than long-lived static cloud keys.
- **Rotation & Revocation SLA:** Any leaked credential must be revoked within **1 hour**, rotated immediately, and scrubbed from Git history.

## Supply-Chain & CI Posture (OWASP A03:2025)
- All third-party GitHub Actions are pinned to immutable **40-character commit SHAs**.
- Lockfiles and container base-image digests are committed and pinned.
- All canonical AI instruction files (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.claude/**`, `.agents/**`, `.github/**`, `docs/ai/**`) are protected by `CODEOWNERS` to prevent prompt/rule backdoors.
