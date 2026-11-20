# Branch Strategy & Protection Rules
<!-- Last updated: 2026-11-19 IST -->

## Branches
| Branch    | Purpose                        | Protected |
|-----------|--------------------------------|-----------|
| `main`    | Production-ready code          | Yes       |
| `develop` | Integration branch             | Yes       |
| `feat/*`  | Feature branches               | No        |
| `fix/*`   | Bug fix branches               | No        |
| `chore/*` | Maintenance tasks              | No        |
| `ai/*`    | AI memory/instruction updates  | No        |

## Required Protection Rules (Control 6.4 — Settings → Branches)
- Require Pull Request before merging to `main` (no auto-merge bypass)
- Require at least 1 approving review + `CODEOWNERS` review on protected paths
- Require status checks to pass (`hygiene-gates`, `ci`, `secrets-scan`)
- Require signed commits and MFA for all contributors
- Restrict force pushes and delete head branches after merge
- Require human environment approval for production deployments

## Commit Convention
See `docs/ai/commit-log-guidance.md`.
