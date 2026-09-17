#!/usr/bin/env python3
"""Validate the Funnel Hacking knowledge-base manifest, routing, and cleanup."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "references"
MANIFEST = REFERENCES / "SOURCE_MANIFEST.md"
REQUIRED_MANIFEST_COLUMNS = {
    "source_id", "title", "author / organization", "year", "language",
    "source_type", "evidence_level", "temporal_sensitivity", "original_file(s)",
    "derived_md", "processing_status", "raw_source_removed",
}
RAW_SUFFIXES = {
    ".pdf", ".doc", ".docx", ".epub", ".html", ".htm", ".txt", ".rtf",
    ".jpeg", ".jpg", ".png", ".gif", ".webp", ".mp3", ".wav", ".m4a",
    ".mp4", ".mov", ".mkv", ".avi", ".zip",
}
REQUIRED_INDEX_TERMS = {
    "awareness", "market sophistication", "positioning", "offer", "PLF",
    "VSL", "ads", "hooks", "CRO", "checkout", "Brazil", "Mexico",
    "localization",
}
REQUIRED_LIVE_URLS = {
    "https://www.facebook.com/ads/library/",
    "https://ads.tiktok.com/business/creativecenter/",
    "https://adstransparency.google.com/",
    "https://business.google.com/think/",
    "https://business.google.com/es-all/think/",
    "https://www.rdstation.com/pesquisas/",
    "https://www.rdstation.com/blog/",
    "https://hotmart.com/pt-br/blog",
    "https://hotmart.com/mx",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--pre-cleanup",
        action="store_true",
        help="Allow inventoried raw sources while validating derived knowledge before deletion.",
    )
    return parser.parse_args()


def table_rows(text: str) -> list[dict[str, str]]:
    lines = text.splitlines()
    start = next((i for i, line in enumerate(lines) if line.startswith("| source_id |")), -1)
    if start < 0 or start + 2 >= len(lines):
        raise ValueError("source manifest table is missing")
    headers = [cell.strip() for cell in lines[start].strip("|").split("|")]
    rows: list[dict[str, str]] = []
    for line in lines[start + 2:]:
        if not line.startswith("|"):
            break
        values = [cell.strip() for cell in line.strip("|").split("|")]
        if len(values) != len(headers):
            raise ValueError(f"manifest row has {len(values)} cells; expected {len(headers)}: {line}")
        rows.append(dict(zip(headers, values)))
    return rows


def markdown_link_errors(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for match in re.finditer(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", text):
        raw = match.group(1).strip()
        target = raw.split(" ", 1)[0].strip("<>")
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0]
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken relative link {raw!r}")
    return errors


def matching_raw_paths(spec: str) -> list[Path]:
    spec = spec.strip("`")
    if " (" in spec:
        spec = spec.split(" (", 1)[0]
    if any(char in spec for char in "*?["):
        return [path for path in REFERENCES.glob(spec) if path.is_file()]
    path = REFERENCES / spec
    return [path] if path.is_file() else []


def validate(pre_cleanup: bool = False) -> list[str]:
    errors: list[str] = []
    for required in (REFERENCES / "INDEX.md", MANIFEST, REFERENCES / "live-sources.md"):
        if not required.is_file():
            errors.append(f"missing required file: {required.relative_to(ROOT)}")
    if errors:
        return errors

    manifest_text = MANIFEST.read_text(encoding="utf-8")
    try:
        rows = table_rows(manifest_text)
    except ValueError as exc:
        return [str(exc)]
    if not rows:
        errors.append("manifest contains no sources")
        return errors
    missing_columns = REQUIRED_MANIFEST_COLUMNS - rows[0].keys()
    if missing_columns:
        errors.append(f"manifest missing columns: {sorted(missing_columns)}")

    ids = [row["source_id"] for row in rows]
    if len(ids) != len(set(ids)):
        errors.append("manifest contains duplicate source IDs")
    for source_id in ids:
        if not re.fullmatch(r"SRC-\d{3}", source_id):
            errors.append(f"invalid source ID: {source_id}")

    for row in rows:
        source_id = row["source_id"]
        derived = REFERENCES / row["derived_md"].strip("`")
        if not derived.is_file():
            errors.append(f"{source_id}: missing derived note {derived.relative_to(ROOT)}")
            continue
        note = derived.read_text(encoding="utf-8")
        if source_id not in note:
            errors.append(f"{source_id}: ID absent from derived note")
        status = row["processing_status"].strip("`")
        if status not in {"INVENTORIED", "IN_PROGRESS", "COMPLETE", "NEEDS_REVIEW"}:
            errors.append(f"{source_id}: invalid processing status {status}")
        removed = row["raw_source_removed"].strip("`").lower()
        raw_paths = matching_raw_paths(row["original_file(s)"])
        if pre_cleanup:
            if status != "COMPLETE":
                errors.append(f"{source_id}: must be COMPLETE before raw cleanup")
        else:
            if status != "COMPLETE":
                errors.append(f"{source_id}: final status is not COMPLETE")
            if removed != "yes":
                errors.append(f"{source_id}: raw_source_removed is not yes")
            if raw_paths:
                errors.append(f"{source_id}: raw source still exists")

    index_text = (REFERENCES / "INDEX.md").read_text(encoding="utf-8")
    for term in REQUIRED_INDEX_TERMS:
        if term.casefold() not in index_text.casefold():
            errors.append(f"INDEX missing required route: {term}")
    live_text = (REFERENCES / "live-sources.md").read_text(encoding="utf-8")
    for url in REQUIRED_LIVE_URLS:
        if url not in live_text:
            errors.append(f"live-sources missing URL: {url}")

    for path in REFERENCES.rglob("*.md"):
        errors.extend(markdown_link_errors(path))
        text = path.read_text(encoding="utf-8")
        if "\ufffd" in text:
            errors.append(f"{path.relative_to(ROOT)}: contains Unicode replacement character")
        if re.search(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", text):
            errors.append(f"{path.relative_to(ROOT)}: possible private key")
        if re.search(r"\b(?:sk-[A-Za-z0-9]{24,}|AKIA[0-9A-Z]{16}|github_pat_[A-Za-z0-9_]{20,})\b", text):
            errors.append(f"{path.relative_to(ROOT)}: possible secret")

    if not pre_cleanup:
        for path in REFERENCES.rglob("*"):
            if path.is_file() and path.suffix.lower() in RAW_SUFFIXES:
                errors.append(f"raw source remains after cleanup: {path.relative_to(ROOT)}")
    return errors


def main() -> int:
    args = parse_args()
    errors = validate(pre_cleanup=args.pre_cleanup)
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"Knowledge-base validation failed with {len(errors)} error(s).")
        return 1
    mode = "pre-cleanup" if args.pre_cleanup else "final"
    print(f"Knowledge-base {mode} validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
