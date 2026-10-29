# README Standard
<!-- Last updated: 2026-10-30 IST -->
<!-- DYNAMIC FILE — canonical README rules for every repo created from this template -->
<!-- Source: condensed from shifulegend/readme-guidance (private) — "The README Engineering Playbook" and its
     quick-reference checklist, which draw on GitHub's official docs, the Standard Readme spec and 20+ top READMEs. -->

Every AI agent that creates or changes `README.md` follows this file, then runs the checklist at the end.
Start from [`docs/README.template.md`](../README.template.md).

## 1. The 5-second filter (inverted pyramid)
Visitors decide in seconds, so order the README by what they need first:

| Reader's time | Their question | Answer with |
| --- | --- | --- |
| 0–5 s | What is this, what problem does it solve, is it maintained? | Title, one-line pitch, hero visual, CI/version/license badges |
| 5–30 s | How does it work in practice? | A copy-pastable example or one quickstart command |
| 30–120 s | How do I install, configure and integrate it? | Prerequisites, install commands, configuration table |
| Deep dive | Architecture, API, contributing, licence | Detailed sections, or links to fuller docs |

## 2. Anatomy (in this order; drop what does not apply)
1. **Identity:** project name, one-sentence plain-language tagline (no jargon), badge row (CI status, version, license).
2. **Why:** the problem it solves and how it differs from the alternatives, in 2–4 sentences.
3. **Hero demo:** screenshot, short recording or diagram showing it working, with descriptive alt text.
4. **Features:** 4–8 bullets, each a capability plus a few words on why it matters.
5. **Prerequisites and installation:** exact versions (e.g. Python ≥ 3.11) and package-manager commands.
6. **Quickstart:** the smallest realistic example that runs as pasted.
7. **Configuration and architecture:** a table of options or env vars (name, type, default, description); a Mermaid diagram
   for data flow instead of a static image.
8. **Status and roadmap:** alpha / beta / production, and what is next.
9. **Contributing and development:** how to run tests locally; link `CONTRIBUTING.md` if it exists.
10. **Licence and credits:** SPDX name linked to `LICENSE`; third-party licences (fonts, assets, data) named.

## 3. Match the archetype
| Archetype | Lead with | Must include | Avoid |
| --- | --- | --- | --- |
| Library / SDK | A zero-to-run code snippet | API reference link, package matrix, benchmarks if relevant | Long setup prose before any code |
| App / service | Architecture and environment setup | System dependencies, `.env.example` explained, compose/quickstart, security policy | Hiding required services |
| CLI / dev tool | Terminal output (recording or screenshot) | Install via package managers, flag reference table | Text-only descriptions of visual output |
| AI skill / plugin | What the user asks for and what they get | Install path, example prompts, requirements, what runs where | Internal file walkthroughs before usage |
| Curated / educational | Navigation | Table of contents with working anchors, inclusion criteria | Unsorted lists |

## 4. Visuals and media
- Light and dark themes: check every image on both; use `<picture>` with `prefers-color-scheme` sources when needed.
- No heavy GIFs (20 MB GIFs lag on mobile); prefer compressed MP4/WebM or a short terminal recording (VHS/asciinema).
- Diagrams as native Mermaid code blocks so they stay current.

## 5. GitHub Markdown techniques
- Alerts for things people must not miss: `> [!NOTE]`, `[!TIP]`, `[!IMPORTANT]`, `[!WARNING]`, `[!CAUTION]`.
- `<details><summary>…</summary>` for long tables, logs and full option lists.
- `diff` code blocks to show configuration changes.
- Tables for anything compared across the same attributes.

## 6. Accessibility and language
- Descriptive alt text ("Terminal showing install finishing in 1.2 s", not "screenshot").
- Never colour alone for state: pair it with a word or icon.
- Headings in order (`#` → `##` → `###`), no skipped levels; one `#` per file.
- Plain words first; explain any acronym on first use.
- Translations, if any, linked from a language row under the title.

## 7. Checklist (run before every README commit)
- [ ] **One-liner:** the first sentence says what it is and who it is for, without jargon
- [ ] **Hero asset:** a screenshot, diagram or recording near the top, with alt text
- [ ] **Badges:** CI status, version (if released) and licence, all resolving
- [ ] **Quickstart:** a command or snippet that works as pasted in under 2 minutes
- [ ] **Prerequisites:** runtimes and system tools with versions, stated before install
- [ ] **Long content collapsed:** big tables, logs and option lists inside `<details>`
- [ ] **Themes:** images and diagrams checked on light and dark GitHub themes
- [ ] **Links:** every relative link, anchor and badge URL works
- [ ] **Contributing path:** how to run tests and where to start
- [ ] **Licence:** named and linked; third-party licences listed
- [ ] **No template leftovers:** no `TODO`, placeholder names or golden-template wording remain
