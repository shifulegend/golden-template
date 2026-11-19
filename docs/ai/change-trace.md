# Change Trace
<!-- DYNAMIC FILE — updated by AI agents after each meaningful implementation sub-step -->
<!-- Newest entries first -->

## Entry Template
```markdown
### [TIMESTAMP] — <Change Title>
- **What Changed**: 
- **Why**: 
- **Affected Areas**: 
- **Related Commit**: 
- **Risks / Follow-ups**: 
```

---

### [2026-11-19 IST] — Remediate 59 Code Hygiene Controls & Official Claude/Antigravity Canonical Docs
- **What Changed**: Added `scripts/check_hygiene_gates.py`, `.github/workflows/security-hygiene.yml`, `.pre-commit-config.yaml`, `.editorconfig`, `.markdownlint.json`, `SECURITY.md`, `.github/PULL_REQUEST_TEMPLATE.md`, `docs/ai/code-hygiene-controls.md`, root `GEMINI.md`, `.claude/settings.json`, `.claude/agents/hygiene-reviewer.md`, `.agents/hooks.json`, `.agents/agents/hygiene-reviewer.md`, `.agents/rules/security-hygiene.md`, and `.agents/skills/*/SKILL.md`. Fixed SHA pinning in `.github/workflows/ci.yml`, YAML frontmatter in `.claude/rules/*.md`, `.claude/skills/*/SKILL.md`, and `.agents/rules/*.md`, error/encoding handling in `scripts/generate-repo-map.js`, `CODEOWNERS`, `.gitignore`, and untagged Markdown code fences.
- **Why**: Align golden template with all 59 Code Hygiene controls and official Anthropic Claude Code & Google Antigravity canonical document standards.
- **Affected Areas**: CI/CD, security, root configs, `docs/ai/`, `.claude/`, `.agents/`, `.github/`, `scripts/`.
- **Related Commit**: see `git log`
- **Risks / Follow-ups**: Legacy `.agents/workflows/*.md` replaced by `.agents/skills/*/SKILL.md` per official Antigravity migration guide.

### [2026-10-30 IST] — Fix CI YAML and embed the README standard
- **What Changed**: Quoted the CI stub `run:` values (the workflow was invalid YAML). Added `docs/ai/readme-guidance.md` and `docs/README.template.md`; added README Standard pointers to `CLAUDE.md`, `AGENTS.md`, `gemini/GEMINI.md`, `.github/copilot-instructions.md`, and a bullet to each docs rule file; updated `tool-sync-policy.md` and the template README.
- **Why**: CI failed on every push for this template and its children; owner asked to embed the readme-guidance playbook.
- **Affected Areas**: CI, docs/ai, tool adapters, README
- **Related Commit**: see `git log`
- **Risks / Follow-ups**: Repos already created from the template keep the broken CI until patched (diagram-explainer-videos already fixed).

### [2026-07-11 03:05 IST] — Token minimization rules embedded (search, repo-map, compression, caching)
- **What Changed**: Added `docs/ai/context-efficiency.md` as a new, purely additive canonical
  file defining four token-minimization practices: (1) structural code search via ripgrep first,
  ast-grep/tree-sitter for precision, semantic search as last resort — never speculative
  directory listing or whole-file reads; (2) a maintained, script-generated
  `docs/ai/repo-map.md` (pattern from Aider's repo-map) for instant codebase orientation
  without re-scanning; (3) compressing/filtering large terminal, log, and JSON tool output
  before it enters context, rather than pasting raw output; (4) static-first, dynamic-last
  prompt ordering to maximize prompt-cache hit rates (per Anthropic's official prompt-caching
  docs — cached tokens cost ~10% of standard input rate, with published case studies showing
  90% cost reduction from reordering alone, no model change). Added a scaffold script
  `scripts/generate-repo-map.js` implementing the repo-map generation pattern (tree-sitter-based,
  to be wired to the repo's actual language parser). Wired lightweight one-paragraph pointers
  into all 4 top-level tool entrypoints (`.github/copilot-instructions.md`, `CLAUDE.md`,
  `gemini/GEMINI.md`, `AGENTS.md`), `docs/ai/tool-sync-policy.md`, and `README.md`'s file index
  — no existing file content was rewritten or removed, this is purely additive.
- **Why**: User researched and proposed embedding token-minimization practices used by leading
  AI coding tools (Aider's repo-map, ast-grep's structural search, Anthropic's prompt-caching
  guidance, MCP-based output compression) into the golden template, without losing any existing
  intelligence or rules.
- **Affected Areas**: docs/ai/, scripts/, .github/copilot-instructions.md, CLAUDE.md,
  gemini/GEMINI.md, AGENTS.md, README.md, docs/ai/tool-sync-policy.md
- **Related Commit**: docs(context-efficiency): add token minimization rules (search, repo-map, compression, caching)
- **Compliance Impact**: None — process/tooling standard only, no rule content removed.
- **Risks / Follow-ups**: `scripts/generate-repo-map.js` is a scaffold — `extractSymbols()` uses
  a naive regex placeholder and must be wired to an actual tree-sitter parser (or ast-grep) for
  the specific language(s) used once a real project is built from this template.

<!-- No entries yet. First change will be logged here. -->
