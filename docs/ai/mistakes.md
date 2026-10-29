# Mistake Log
<!-- DYNAMIC FILE — updated immediately by AI agents when any mistake is identified -->
<!-- Newest entries first. Read this FIRST at the start of every session. -->

## Entry Template
```
### [TIMESTAMP] — <Short Title>
- **Summary**: What went wrong
- **Root Cause**: Why it happened
- **Affected Files/Modules**: 
- **Detection Method**: How it was found
- **Correction**: What was done to fix it
- **Prevention Rule**: Rule to avoid recurrence
```

---

### [2026-10-30 IST] — CI workflow rejected before any job ran
- **Summary**: Every push to the template and to repos created from it failed CI with "workflow file issue".
- **Root Cause**: Stub steps `run: echo "TODO: npm ..."` are unquoted YAML scalars containing `: `, which YAML rejects.
- **Affected Files/Modules**: `.github/workflows/ci.yml`
- **Detection Method**: First push of `shifulegend/diagram-explainer-videos` (created from this template) failed; `yaml.safe_load` pointed to line 43; the template's own recent runs fail the same way.
- **Correction**: Single-quoted the five stub `run:` values; added a header comment explaining the rule.
- **Prevention Rule**: Parse workflow YAML locally (`python3 -c "import yaml; yaml.safe_load(open('.github/workflows/ci.yml'))"`) before pushing any workflow change.

