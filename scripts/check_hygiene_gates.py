#!/usr/bin/env python3
"""Deterministic Code Hygiene & Canonical AI Instruction Gate Runner.

Zero-dependency Python 3 script enforcing repository-level controls from the
59-Control Code Hygiene & Vibe Engineering Audit Checklist plus official
Anthropic Claude Code and Google Antigravity canonical document specs.

Usage:
    python3 scripts/check_hygiene_gates.py [--diff-base origin/main]
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
MAX_ENTRYPOINT_LINES = 200
MAX_APPEND_FILE_LOC = 500

SHA_PIN_RE = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)")
FULL_SHA_RE = re.compile(r"^[^@]+@[0-9a-f]{40}$")
SUPPRESSION_RE = re.compile(
    r"(#\s*noqa\b|eslint-disable\b|#\s*type:\s*ignore\b|//\s*nosec\b|#\s*nosec\b)",
    re.IGNORECASE,
)
SUPPRESSION_JUSTIFIED_RE = re.compile(
    r"(#\s*noqa(?::\s*[A-Z0-9,\s]+)?\s*(?:--|reason:|-)\s*\S+"
    r"|eslint-disable[^\n]*--\s*\S+"
    r"|#\s*type:\s*ignore(?:\[[^\]]+\])?\s*(?:--|reason:|-|#)\s*\S+"
    r"|(?://|#)\s*nosec[^\n]*(?:--|reason:|-)\s*\S+)",
    re.IGNORECASE,
)


def parse_frontmatter(text: str) -> dict[str, object] | None:
    """Parse minimal YAML frontmatter without external dependencies."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    end_idx = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_idx = idx
            break
    if end_idx is None:
        return None

    data: dict[str, object] = {}
    current_key: str | None = None
    for raw in lines[1:end_idx]:
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- ") and current_key is not None:
            existing = data.get(current_key)
            if not isinstance(existing, list):
                existing = []
                data[current_key] = existing
            existing.append(stripped[2:].strip().strip('"').strip("'"))
            continue
        if ":" in raw:
            key, val = raw.split(":", 1)
            key = key.strip()
            val = val.strip()
            current_key = key
            if val in ("", ">-", "|", ">"):
                data[key] = ""
            else:
                data[key] = val.strip('"').strip("'")
        elif current_key is not None and isinstance(data.get(current_key), str):
            prev = str(data[current_key])
            data[current_key] = (prev + " " + stripped).strip()
    return data


def check_json_files(errors: list[str]) -> None:
    """Validate all committed JSON configuration files."""
    json_paths = [
        ".markdownlint.json",
        ".claude/settings.json",
        ".agents/hooks.json",
    ]
    for rel in json_paths:
        path = ROOT / rel
        if not path.exists():
            errors.append(f"[CONFIG] Missing required JSON config: {rel}")
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"[JSON] Invalid JSON in {rel}: {exc}")


def check_yaml_and_sha_pinning(errors: list[str]) -> None:
    """Check YAML syntax (if PyYAML installed) and enforce 40-char SHA pinning."""
    try:
        import yaml  # type: ignore[import-untyped] -- optional stdlib fallback
    except ImportError:
        yaml = None

    yaml_files = list((ROOT / ".github").rglob("*.yml")) + [
        ROOT / ".pre-commit-config.yaml",
    ]
    for path in yaml_files:
        if not path.exists():
            continue
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        if yaml is not None:
            try:
                yaml.safe_load(text)
            except Exception as exc:  # noqa: BLE001 -- PyYAML error class varies
                errors.append(f"[YAML] Invalid YAML in {rel}: {exc}")

        if ".github/workflows/" in rel.as_posix():
            for lineno, line in enumerate(text.splitlines(), start=1):
                stripped = line.strip()
                if stripped.startswith("#"):
                    continue
                match = SHA_PIN_RE.match(line)
                if not match:
                    continue
                ref = match.group(1)
                if ref.startswith("./") or ref.startswith("../"):
                    continue
                if not FULL_SHA_RE.match(ref):
                    errors.append(
                        f"[OWASP A03:2025] Unpinned GitHub Action in {rel}:{lineno}: "
                        f"'{ref}' must be pinned to a full 40-character commit SHA"
                    )


def check_env_and_gitignore(errors: list[str]) -> None:
    """Enforce 12-Factor config: .env gitignored and zero real .env committed."""
    gitignore = ROOT / ".gitignore"
    if not gitignore.exists():
        errors.append("[12-FACTOR] Missing .gitignore")
        return
    gi_lines = {line.strip() for line in gitignore.read_text(encoding="utf-8").splitlines()}
    for required in (".env", "!.env.example", "CLAUDE.local.md"):
        if required not in gi_lines:
            errors.append(f"[12-FACTOR] .gitignore missing required entry: {required}")

    for path in ROOT.rglob(".env*"):
        if ".git" in path.parts:
            continue
        if path.name != ".env.example":
            errors.append(
                f"[SECRETS] Real env file must not exist in repo: {path.relative_to(ROOT)}"
            )


def check_canonical_ai_docs(errors: list[str]) -> None:
    """Validate official Anthropic Claude Code & Google Antigravity canonical docs."""
    for entrypoint in ("AGENTS.md", "CLAUDE.md", "GEMINI.md"):
        path = ROOT / entrypoint
        if not path.exists():
            errors.append(f"[AI-CANONICAL] Missing root entrypoint: {entrypoint}")
            continue
        line_count = len(path.read_text(encoding="utf-8").splitlines())
        if line_count > MAX_ENTRYPOINT_LINES:
            errors.append(
                f"[AI-CANONICAL] {entrypoint} has {line_count} lines "
                f"(exceeds official {MAX_ENTRYPOINT_LINES}-line target)"
            )

    claude_rules_dir = ROOT / ".claude" / "rules"
    if claude_rules_dir.exists():
        for rule_file in sorted(claude_rules_dir.glob("*.md")):
            text = rule_file.read_text(encoding="utf-8")
            rel = rule_file.relative_to(ROOT)
            if "<!-- paths:" in text:
                errors.append(
                    f"[CLAUDE-SPEC] {rel} uses HTML comment '<!-- paths: -->' which "
                    "Claude Code strips; use YAML frontmatter 'paths:' instead"
                )
            if rule_file.name != "core.md":
                fm = parse_frontmatter(text)
                if fm is None or "paths" not in fm:
                    errors.append(
                        f"[CLAUDE-SPEC] Scoped rule {rel} missing YAML 'paths:' frontmatter"
                    )

    valid_triggers = {"always_on", "glob", "model_decision", "manual"}
    agents_rules_dir = ROOT / ".agents" / "rules"
    if agents_rules_dir.exists():
        for rule_file in sorted(agents_rules_dir.glob("*.md")):
            text = rule_file.read_text(encoding="utf-8")
            rel = rule_file.relative_to(ROOT)
            fm = parse_frontmatter(text)
            if fm is None or str(fm.get("trigger", "")) not in valid_triggers:
                errors.append(
                    f"[ANTIGRAVITY-SPEC] {rel} missing valid YAML 'trigger:' "
                    f"({', '.join(sorted(valid_triggers))})"
                )
            elif fm.get("trigger") == "glob" and not fm.get("globs"):
                errors.append(f"[ANTIGRAVITY-SPEC] {rel} has trigger: glob but missing 'globs:'")

    for skills_root in (ROOT / ".claude" / "skills", ROOT / ".agents" / "skills"):
        if not skills_root.exists():
            errors.append(
                f"[SKILLS-SPEC] Missing skills directory: {skills_root.relative_to(ROOT)}"
            )
            continue
        for skill_md in sorted(skills_root.glob("*/SKILL.md")):
            rel = skill_md.relative_to(ROOT)
            fm = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
            if fm is None or not fm.get("name") or not fm.get("description"):
                errors.append(
                    f"[SKILLS-SPEC] {rel} missing required YAML 'name' and 'description'"
                )
            elif fm.get("name") != skill_md.parent.name:
                errors.append(
                    f"[SKILLS-SPEC] {rel} frontmatter name '{fm.get('name')}' "
                    f"must match directory '{skill_md.parent.name}'"
                )

    for agent_rel in (".claude/agents/hygiene-reviewer.md", ".agents/agents/hygiene-reviewer.md"):
        agent_path = ROOT / agent_rel
        if not agent_path.exists():
            errors.append(f"[AI-CANONICAL] Missing read-only reviewer subagent: {agent_rel}")
            continue
        fm = parse_frontmatter(agent_path.read_text(encoding="utf-8"))
        if fm is None or not fm.get("name") or not fm.get("description"):
            errors.append(f"[AI-CANONICAL] {agent_rel} missing YAML 'name'/'description'")


def check_codeowners(errors: list[str]) -> None:
    """Verify CODEOWNERS protects all canonical AI instruction & CI paths."""
    co_path = ROOT / "CODEOWNERS"
    if not co_path.exists():
        errors.append("[CODEOWNERS] Missing CODEOWNERS file")
        return
    co_text = co_path.read_text(encoding="utf-8")
    required_patterns = (
        "docs/ai/**",
        "AGENTS.md",
        "CLAUDE.md",
        "GEMINI.md",
        ".claude/**",
        ".agents/**",
        ".github/workflows/**",
    )
    for pattern in required_patterns:
        if pattern not in co_text:
            errors.append(f"[CODEOWNERS] Missing protection rule for '{pattern}'")


def check_markdown_fences(errors: list[str]) -> None:
    """Enforce explicit language tags on fenced code blocks (Control 3.4.3 / MD040)."""
    md_files: Iterable[Path] = list((ROOT / "docs").rglob("*.md")) + list(ROOT.glob("*.md"))
    for md_path in sorted(md_files):
        in_fence = False
        rel = md_path.relative_to(ROOT)
        for lineno, line in enumerate(md_path.read_text(encoding="utf-8").splitlines(), start=1):
            stripped = line.strip()
            if stripped.startswith("```"):
                if not in_fence:
                    lang = stripped[3:].strip()
                    if not lang:
                        errors.append(
                            f"[MD040] Untagged fenced code block at {rel}:{lineno} "
                            "(add language tag, e.g., ```bash or ```text)"
                        )
                    in_fence = True
                else:
                    in_fence = False


def check_git_diff_ratchets(diff_base: str, errors: list[str]) -> None:
    """Enforce suppression justification (3.4.4) and >500 LOC append guard (7.1.2) on PR diffs."""
    try:
        diff_out = subprocess.check_output(
            ["git", "diff", "--unified=0", f"{diff_base}...HEAD"],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return

    current_file = ""
    for line in diff_out.splitlines():
        if line.startswith("+++ b/"):
            current_file = line[6:]
            continue
        if not line.startswith("+") or line.startswith("+++"):
            continue
        added = line[1:]
        if current_file == "scripts/check_hygiene_gates.py":
            continue
        if SUPPRESSION_RE.search(added) and not SUPPRESSION_JUSTIFIED_RE.search(added):
            errors.append(
                f"[SUPPRESSION] Unjustified linter/SAST suppression in {current_file}: "
                "append '-- <brief reason>' to explain why"
            )

    try:
        numstat = subprocess.check_output(
            ["git", "diff", "--numstat", f"{diff_base}...HEAD"],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return

    for row in numstat.splitlines():
        parts = row.split("\t")
        if len(parts) != 3 or parts[0] == "-" or parts[1] == "-":
            continue
        added_n, deleted_n, rel_file = int(parts[0]), int(parts[1]), parts[2]
        if added_n <= deleted_n:
            continue
        target = ROOT / rel_file
        if target.exists() and target.suffix in {".py", ".js", ".ts", ".tsx", ".go", ".rs", ".c", ".cpp"}:
            total_loc = len(target.read_text(encoding="utf-8", errors="ignore").splitlines())
            if total_loc > MAX_APPEND_FILE_LOC:
                errors.append(
                    f"[LARGE-FILE-APPEND] {rel_file} is {total_loc} LOC and grew by "
                    f"+{added_n - deleted_n} lines; extract a new module instead of appending"
                )


def main() -> int:
    parser = argparse.ArgumentParser(description="Run deterministic code hygiene CI gates.")
    parser.add_argument("--diff-base", default="", help="Git base ref for PR diff ratchets.")
    args = parser.parse_args()

    errors: list[str] = []
    check_json_files(errors)
    check_yaml_and_sha_pinning(errors)
    check_env_and_gitignore(errors)
    check_canonical_ai_docs(errors)
    check_codeowners(errors)
    check_markdown_fences(errors)
    if args.diff_base:
        check_git_diff_ratchets(args.diff_base, errors)

    if errors:
        print(f"HYGIENE GATES FAILED ({len(errors)} finding(s)):")
        for item in errors:
            print(f"  - {item}")
        return 1

    print("ALL DETERMINISTIC CODE HYGIENE & CANONICAL AI DOC GATES PASSED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
