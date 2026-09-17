#!/usr/bin/env python3
"""Pragmatic validation for the vendored Hermes skill collection."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REGISTRY = ROOT / "config" / "skills-registry.yaml"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_REGISTRY_FIELDS = {
    "skill_name", "source", "purpose", "triggers", "stage", "input_types",
    "output_types", "dependencies", "recommended_with", "avoid_when",
    "priority", "notes", "path",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verbose", action="store_true")
    return parser.parse_args()


def frontmatter(path: Path) -> tuple[dict[str, str], str, list[str]]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    has_frontmatter = text.startswith("---") and text.count("---") >= 2
    if has_frontmatter and "\t" in text.split("---", 2)[1]:
        errors.append("frontmatter contains a tab")
    if not text.startswith("---\n"):
        return {}, text, ["missing opening YAML delimiter"]
    marker = text.find("\n---\n", 4)
    if marker < 0:
        return {}, text, ["missing closing YAML delimiter"]
    raw = text[4:marker]
    data: dict[str, str] = {}
    top_keys: list[str] = []
    for number, line in enumerate(raw.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(" "):
            if (len(line) - len(line.lstrip(" "))) % 2:
                errors.append(f"frontmatter line {number} has odd indentation")
            continue
        if ":" not in line:
            errors.append(f"frontmatter line {number} is not key: value")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not re.fullmatch(r"[A-Za-z0-9_-]+", key):
            errors.append(f"frontmatter line {number} has invalid key {key!r}")
        if key in top_keys:
            errors.append(f"duplicate frontmatter key {key!r}")
        top_keys.append(key)
        if value.startswith(('"', "'")) and not value.endswith(value[0]):
            errors.append(f"frontmatter line {number} has an unclosed quote")
        data[key] = value.strip('"\'')
    return data, text[marker + 5:], errors


def markdown_link_errors(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for match in re.finditer(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", text):
        raw = match.group(1).strip()
        target = raw.split(" ", 1)[0].strip("<>")
        if not target or target.startswith(("http://", "https://", "mailto:", "#", "data:")):
            continue
        target = target.split("#", 1)[0]
        if not target or any(token in target for token in ("{", "}", "*", "<", ">")):
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"broken relative link {raw!r}")
    return errors


def registry_entries() -> tuple[list[dict[str, str]], list[str]]:
    if not REGISTRY.exists():
        return [], ["config/skills-registry.yaml is missing"]
    text = REGISTRY.read_text(encoding="utf-8")
    errors: list[str] = []
    if "\t" in text:
        errors.append("registry contains tab indentation")
    entries: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for number, line in enumerate(text.splitlines(), 1):
        start = re.match(r"  - skill_name:\s*([a-z0-9-]+)\s*$", line)
        if start:
            if current:
                entries.append(current)
            current = {"skill_name": start.group(1)}
            continue
        field = re.match(r"    ([a-z_]+):(?:\s*(.*))?$", line)
        if field and current is not None:
            key, value = field.group(1), (field.group(2) or "")
            current[key] = value
        elif line.strip() and not (
            line.startswith(("schema_version:", "generated_by:", "evidence_policy:", "knowledge_base_index:", "live_sources_policy:", "skills:", "      - "))
            or line.startswith("  #")
        ):
            errors.append(f"registry line {number} has unexpected structure")
    if current:
        entries.append(current)
    for entry in entries:
        missing = REQUIRED_REGISTRY_FIELDS - entry.keys()
        if missing:
            errors.append(f"registry entry {entry.get('skill_name')} missing fields: {sorted(missing)}")
    return entries, errors


def scan_secrets() -> list[str]:
    findings: list[str] = []
    patterns = {
        "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        "GitHub token": re.compile(r"\b(?:ghp|github_pat)_[A-Za-z0-9_]{20,}\b"),
        "OpenAI-like token": re.compile(r"\bsk-[A-Za-z0-9]{24,}\b"),
        "Apify token": re.compile(r"\bapify_api_[A-Za-z0-9]{20,}\b"),
        "Stripe live key": re.compile(r"\b(?:sk|rk)_live_[A-Za-z0-9]{16,}\b"),
    }
    ignored_dirs = {".git", ".upstream-work", "node_modules", ".venv", "__pycache__"}
    text_suffixes = {".md", ".py", ".js", ".mjs", ".sh", ".yaml", ".yml", ".json", ".txt", ".toml", ".example"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in ignored_dirs for part in path.parts):
            continue
        if path.name.startswith(".env") and path.name != ".env.example":
            findings.append(f"unignored environment file: {path.relative_to(ROOT)}")
            continue
        if path.suffix.lower() not in text_suffixes and path.name not in {"Dockerfile", "LICENSE"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in patterns.items():
            if pattern.search(text):
                findings.append(f"{label}: {path.relative_to(ROOT)}")
    return findings


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    warnings: list[str] = []
    if not SKILLS.exists():
        print("ERROR: skills/ is missing")
        return 1

    skill_dirs = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    skill_paths: list[Path] = []
    names: list[str] = []
    claude_only = re.compile(r"AskUserQuestion|CLAUDE_SKILL_DIR|allowed-tools:\s*.*(?:Bash|WebFetch|WebSearch)|/bin/rmbc-workspace|~/.claude|\.cursor/")
    external_runtime = re.compile(r"(?<!https:)(?<!http:)(?:[A-Za-z]:\\Users\\|/Users/|/home/|~/(?!\.cache/huggingface))")

    for directory in skill_dirs:
        skill_file = directory / "SKILL.md"
        if not skill_file.exists():
            errors.append(f"{directory.relative_to(ROOT)}: missing SKILL.md")
            continue
        skill_paths.append(skill_file)
        data, body, fm_errors = frontmatter(skill_file)
        errors.extend(f"{skill_file.relative_to(ROOT)}: {message}" for message in fm_errors)
        name = data.get("name", "")
        description = data.get("description", "")
        if not name:
            errors.append(f"{skill_file.relative_to(ROOT)}: missing name")
        else:
            names.append(name)
            if not NAME_RE.fullmatch(name) or len(name) > 64:
                errors.append(f"{skill_file.relative_to(ROOT)}: invalid skill name {name!r}")
            if name != directory.name:
                errors.append(f"{skill_file.relative_to(ROOT)}: name does not match directory")
        if not description or len(description) > 1024:
            errors.append(f"{skill_file.relative_to(ROOT)}: description missing or over 1024 characters")
        if claude_only.search(skill_file.read_text(encoding="utf-8")):
            errors.append(f"{skill_file.relative_to(ROOT)}: critical Claude/Cursor-only runtime dependency remains")
        if external_runtime.search(body):
            errors.append(f"{skill_file.relative_to(ROOT)}: machine-specific external runtime path remains")

    for name, count in Counter(names).items():
        if count > 1:
            errors.append(f"duplicate skill name {name!r} appears {count} times")

    entries, registry_errors = registry_entries()
    errors.extend(registry_errors)
    registered = [entry["skill_name"] for entry in entries]
    for name, count in Counter(registered).items():
        if count > 1:
            errors.append(f"registry contains duplicate skill {name!r}")
    missing_registry = sorted(set(names) - set(registered))
    missing_disk = sorted(set(registered) - set(names))
    if missing_registry:
        errors.append(f"skills missing from registry: {missing_registry}")
    if missing_disk:
        errors.append(f"registry entries missing on disk: {missing_disk}")

    for path in SKILLS.rglob("*.md"):
        errors.extend(f"{path.relative_to(ROOT)}: {message}" for message in markdown_link_errors(path))
    documentation = [ROOT / "README.md", ROOT / "AGENTS.md"]
    documentation.extend((ROOT / "docs").rglob("*.md"))
    documentation.extend((ROOT / "references").rglob("*.md"))
    for path in documentation:
        if path.exists():
            errors.extend(f"{path.relative_to(ROOT)}: {message}" for message in markdown_link_errors(path))

    for path in ROOT.rglob("*"):
        if path.is_symlink():
            errors.append(f"symlink is not portable: {path.relative_to(ROOT)}")

    errors.extend(scan_secrets())

    provenance = ROOT / "config" / "upstreams.yaml"
    if not provenance.exists():
        errors.append("config/upstreams.yaml is missing")
    else:
        provenance_text = provenance.read_text(encoding="utf-8")
        shas = re.findall(r"^    commit:\s*([0-9a-f]{40})$", provenance_text, re.M)
        if len(shas) != 6:
            errors.append(f"provenance should contain 6 exact 40-character commit SHAs; found {len(shas)}")

    if args.verbose:
        for warning in warnings:
            print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    print(f"Validated {len(skill_paths)} skills, {len(entries)} registry entries, and 6 provenance sources.")
    if errors:
        print(f"Validation failed with {len(errors)} error(s).")
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
