#!/usr/bin/env python3
"""Generate the routing registry and human-readable catalog from installed skills."""

from __future__ import annotations

import argparse
import ast
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
REGISTRY = ROOT / "config" / "skills-registry.yaml"
CATALOG = ROOT / "docs" / "SKILLS_CATALOG.md"


CORE_HIGH = {
    "funnel-hacking-orchestrator", "rmbc-context", "unified-research-synthesizer",
    "competitor-offer-analysis", "funnel-architecture", "funnel-audit",
    "customer-research", "product-marketing", "competitor-profiling", "cro",
    "ads", "funnel-ad-creative", "analytics", "attribution", "ab-testing",
    "plf-walker", "translation", "apify-ads-intelligence", "video-analysis",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if generated files are stale.")
    return parser.parse_args()


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        try:
            return str(ast.literal_eval(value))
        except (ValueError, SyntaxError):
            return value[1:-1]
    return value


def frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"Missing frontmatter: {path}")
    marker = text.find("\n---\n", 4)
    if marker < 0:
        raise ValueError(f"Unclosed frontmatter: {path}")
    raw = text[4:marker]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if line.startswith((" ", "\t", "-")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = unquote(value)
    return data, text[marker + 5:]


def load_sources() -> dict[str, str]:
    path = ROOT / "config" / "upstreams.yaml"
    mapping: dict[str, str] = {}
    current = ""
    in_skills = False
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"  - name:\s*(\S+)", line)
        if match:
            current = match.group(1)
            in_skills = False
            continue
        if line == "    skills:":
            in_skills = True
            continue
        skill = re.match(r"      -\s+([a-z0-9-]+)$", line) if in_skills else None
        if skill:
            mapping[skill.group(1)] = current
        elif in_skills and not line.startswith("      -"):
            in_skills = False
    mapping["funnel-hacking-orchestrator"] = "local"
    return mapping


def stage_for(name: str) -> str:
    groups = {
        "orchestration": {"funnel-hacking-orchestrator", "write-copy", "marketing-plan", "marketing-council"},
        "collection": {"apify-ads-intelligence", "video-analysis", "competitor-profiling", "ingredient-research", "customer-research"},
        "research": {"rmbc-context", "unified-research-synthesizer", "product-marketing", "competitor-offer-analysis", "mechanism-ideation", "competitors"},
        "traffic": {"ads", "funnel-ad-creative", "ad-creative-audit", "ad-angle-generator", "hook-battery", "fb-ad-copy", "creative-brief", "media-buying-brief", "ugc-brief"},
        "pre-frame": {"advertorial-writer", "webinar-registration-copy", "lead-writer", "lead-magnets", "free-offer-brief", "events", "plf-walker"},
        "funnel": {"funnel-architecture", "funnel-audit", "cro", "lander-copy", "order-form-cro", "checkout-abandonment", "thank-you-page", "signup", "paywalls", "popups"},
        "offer": {"offers", "offer-stack", "bonus-stack", "guarantee-writer", "scarcity-urgency", "pricing", "pricing-strategy", "upsell-script"},
        "copy": {"copywriting", "copy-editing", "copy-rewrite", "rmbc-copy-audit", "vsl-script", "pdp-ecomm-template", "broadcast-email", "email-promo", "cold-email"},
        "follow-up": {"emails", "sms", "welcome-sequence", "email-retention-sequences", "post-purchase-sequence", "reengagement-sequence", "cart-abandonment-flow", "soap-opera-sequence", "upsell-sequence-writer", "onboarding", "churn-prevention"},
        "measurement": {"analytics", "attribution", "ab-testing", "ab-test-plan", "revops"},
        "localization": {"translation"},
    }
    for stage, names in groups.items():
        if name in names:
            return stage
    if any(token in name for token in ("seo", "schema", "site-architecture", "content-strategy")):
        return "discovery"
    if any(token in name for token in ("launch", "marketing", "referral", "community", "social", "influencer", "prospecting", "public-relations", "co-marketing")):
        return "growth"
    return "support"


def triggers_for(name: str, description: str) -> list[str]:
    triggers = [name.replace("-", " ")]
    for phrase in re.findall(r"[\"']([^\"']{2,48})[\"']", description):
        phrase = phrase.strip().lower()
        if phrase not in triggers and len(phrase.split()) <= 8:
            triggers.append(phrase)
        if len(triggers) >= 8:
            break
    return triggers


def inputs_for(name: str, stage: str) -> list[str]:
    special = {
        "funnel-hacking-orchestrator": ["URLs", "files", "transcripts", "videos", "ad evidence", "WhatsApp/email exports", "research brief"],
        "apify-ads-intelligence": ["advertiser or keyword", "platform", "country", "result limit", "Apify authentication optional"],
        "video-analysis": ["local video or supported URL", "subtitles optional", "analysis question"],
        "translation": ["source content", "source locale", "target locale", "market brief", "glossary optional"],
        "plf-walker": ["launch evidence or brief", "CPL/PLC assets", "timeline", "channel exports optional"],
        "attribution": ["owned tracking data", "business model", "conversion definitions", "time window"],
    }
    if name in special:
        return special[name]
    by_stage = {
        "collection": ["target", "public sources", "user-provided evidence", "scope"],
        "traffic": ["ad copy/creative", "audience", "platform", "performance data optional"],
        "funnel": ["page or funnel evidence", "audience", "offer context", "owned metrics optional"],
        "offer": ["offer evidence or brief", "audience", "price/proof when known"],
        "copy": ["source copy or brief", "audience", "offer", "proof assets"],
        "follow-up": ["sequence/export", "audience state", "timing", "offer/context"],
        "measurement": ["owned baseline", "metric definitions", "events or variants", "time window"],
        "research": ["product/market brief", "customer or competitor evidence", "research question"],
    }
    return by_stage.get(stage, ["task brief", "available evidence", "constraints"])


def outputs_for(name: str, stage: str) -> list[str]:
    special = {
        "funnel-hacking-orchestrator": ["source ledger", "funnel map", "evidence-backed dossier", "opportunities", "test ideas", "missing evidence"],
        "apify-ads-intelligence": ["public ad records", "observable dates", "landing destinations", "collection summary"],
        "video-analysis": ["manifest", "metadata", "sampled frames", "contact sheet", "subtitle/OCR/ASR artifacts optional"],
        "translation": ["translator brief", "translation", "glossary/style notes", "localization QA"],
        "plf-walker": ["PLF/CPL structure", "launch sequence", "timeline", "communications plan"],
    }
    if name in special:
        return special[name]
    by_stage = {
        "collection": ["source-backed research artifacts"],
        "traffic": ["ad/creative analysis or concepts", "testing notes"],
        "funnel": ["audit or architecture", "prioritized hypotheses"],
        "offer": ["offer/pricing analysis or original structure"],
        "copy": ["copy analysis or original draft", "evidence gaps"],
        "follow-up": ["sequence analysis or original flow"],
        "measurement": ["measurement plan", "calculations from owned inputs", "guardrails"],
        "research": ["research synthesis", "positioning inputs", "evidence gaps"],
    }
    return by_stage.get(stage, ["specialist recommendations or deliverable"])


def dependencies_for(name: str, source: str) -> list[str]:
    if source == "dtc-copywriting-skills" and name not in {"rmbc-context", "rmbc-upgrade", "write-copy"}:
        return ["rmbc-context"]
    if name == "video-analysis":
        return ["Python 3.10+", "FFmpeg", "FFprobe", "Pillow", "optional yt-dlp/Tesseract/faster-whisper/Docker"]
    if name == "apify-ads-intelligence":
        return ["Apify CLI when automated collection is used", "APIFY_TOKEN or apify login", "optional jq"]
    return []


def recommended_for(name: str, body: str, all_names: set[str]) -> list[str]:
    section = body.split("## Related Skills", 1)[-1] if "## Related Skills" in body else body[-2500:]
    found: list[str] = []
    for candidate in sorted(all_names, key=lambda item: (-len(item), item)):
        if candidate == name:
            continue
        if re.search(rf"(?<![a-z0-9-]){re.escape(candidate)}(?![a-z0-9-])", section, re.I):
            found.append(candidate)
        if len(found) >= 6:
            break
    curated = {
        "funnel-hacking-orchestrator": ["customer-research", "competitor-profiling", "funnel-architecture", "funnel-audit"],
        "apify-ads-intelligence": ["ads", "funnel-ad-creative", "ad-creative-audit", "competitor-profiling"],
        "video-analysis": ["vsl-script", "rmbc-copy-audit", "funnel-hacking-orchestrator"],
        "plf-walker": ["funnel-architecture", "emails", "competitor-offer-analysis", "translation"],
        "translation": ["copywriting", "customer-research", "funnel-hacking-orchestrator"],
        "attribution": ["analytics", "revops", "ab-testing"],
    }
    return curated.get(name, found)


def avoid_for(name: str) -> list[str]:
    return {
        "apify-ads-intelligence": ["private/access-controlled data", "performance conclusions from ad presence or longevity", "manual evidence is already sufficient"],
        "video-analysis": ["transcript fully answers the question and visuals are irrelevant", "no video exists"],
        "translation": ["market strategy is needed without source content", "literal translation would be mistaken for localization"],
        "attribution": ["competitor funnel without owned conversion/revenue data", "event tracking is not yet defined"],
        "funnel-audit": ["monetary-impact estimates without traceable traffic, conversion, and AOV inputs"],
        "plf-walker": ["evergreen structure with no launch sequence", "benchmarks are being requested as guaranteed outcomes"],
    }.get(name, [])


def notes_for(name: str, source: str) -> str:
    notes = {
        "funnel-hacking-orchestrator": "Control plane. Consult the registry and load only the smallest sufficient specialist set.",
        "apify-ads-intelligence": "Collection/intelligence only. Longevity and observed counts do not prove winner status, spend, ROAS, or profit.",
        "video-analysis": "Transcript-first for spoken copy. Missing/inaccessible video is non-blocking.",
        "plf-walker": "Treat benchmark files as methodological references, not forecasts or universal targets.",
        "translation": "Keep semantic translation and market localization separate; preserve the original.",
        "funnel-audit": "Without traceable owned metrics, monetary impact and expected lift remain UNKNOWN or labeled scenarios.",
        "attribution": "Use for owned data; an observed competitor journey is not attribution.",
    }
    if name in notes:
        return notes[name]
    if source == "dtc-copywriting-skills":
        return "Vendored RMBC methodology with local Hermes portability and evidence-first overrides."
    if source == "corey-marketingskills":
        return "Vendored Corey Haines marketing skill with project-local context and evidence-first overrides."
    return "Vendored specialist with local evidence-first safeguards."


def quote(value: object) -> str:
    text = str(value).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")
    return f'"{text}"'


def list_yaml(lines: list[str], indent: str, values: list[str]) -> None:
    for value in values:
        lines.append(f"{indent}- {quote(value)}")


def build() -> tuple[str, str]:
    sources = load_sources()
    skill_paths = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    parsed: list[tuple[Path, dict[str, str], str]] = [(p, *frontmatter(p)) for p in skill_paths]
    all_names = {data["name"] for _, data, _ in parsed}
    rows = []
    for path, data, body in parsed:
        name = data["name"]
        description = data.get("description", "")
        source = sources.get(name, "unknown")
        stage = stage_for(name)
        rows.append({
            "skill_name": name,
            "source": source,
            "purpose": description,
            "triggers": triggers_for(name, description),
            "stage": stage,
            "input_types": inputs_for(name, stage),
            "output_types": outputs_for(name, stage),
            "dependencies": dependencies_for(name, source),
            "recommended_with": recommended_for(name, body, all_names),
            "avoid_when": avoid_for(name),
            "priority": "high" if name in CORE_HIGH else "medium",
            "notes": notes_for(name, source),
            "path": path.relative_to(ROOT).as_posix(),
        })

    lines = [
        "schema_version: 1",
        "generated_by: scripts/build_catalog.py",
        "evidence_policy: skills/funnel-hacking-orchestrator/references/evidence-protocol.md",
        "knowledge_base_index: references/INDEX.md",
        "live_sources_policy: references/live-sources.md",
        "skills:",
    ]
    for row in rows:
        lines.extend([
            f"  - skill_name: {row['skill_name']}",
            f"    source: {row['source']}",
            f"    purpose: {quote(row['purpose'])}",
            "    triggers:",
        ])
        list_yaml(lines, "      ", row["triggers"])
        lines.append(f"    stage: {row['stage']}")
        for key in ("input_types", "output_types", "dependencies", "recommended_with", "avoid_when"):
            if row[key]:
                lines.append(f"    {key}:")
                list_yaml(lines, "      ", row[key])
            else:
                lines.append(f"    {key}: []")
        lines.extend([
            f"    priority: {row['priority']}",
            f"    notes: {quote(row['notes'])}",
            f"    path: {row['path']}",
        ])

    source_counts = Counter(row["source"] for row in rows)
    stage_counts = Counter(row["stage"] for row in rows)
    catalog = [
        "# Skills Catalog",
        "",
        f"This repository contains **{len(rows)}** discoverable skills. The orchestrator uses the compact registry for routing and loads specialist details only when required.",
        "",
        "Knowledge routing starts at [`references/INDEX.md`](../references/INDEX.md). Current ads, platform state, and market evidence follow [`references/live-sources.md`](../references/live-sources.md).",
        "",
        "## Inventory",
        "",
        "### By source",
        "",
        "| Source | Skills |",
        "| --- | ---: |",
    ]
    catalog.extend(f"| `{source}` | {count} |" for source, count in sorted(source_counts.items()))
    catalog.extend(["", "### By stage", "", "| Stage | Skills |", "| --- | ---: |"])
    catalog.extend(f"| `{stage}` | {count} |" for stage, count in sorted(stage_counts.items()))
    catalog.extend([
        "",
        "## Routing Catalog",
        "",
        "| Skill | Source | Stage | Priority | Purpose | Recommended with |",
        "| --- | --- | --- | --- | --- | --- |",
    ])
    for row in rows:
        purpose = row["purpose"].replace("|", "\\|")
        if len(purpose) > 180:
            purpose = purpose[:177].rstrip() + "..."
        rec = ", ".join(f"`{name}`" for name in row["recommended_with"]) or "—"
        catalog.append(f"| [`{row['skill_name']}`](../{row['path']}) | `{row['source']}` | `{row['stage']}` | {row['priority']} | {purpose} | {rec} |")
    catalog.extend([
        "",
        "## Routing Rules",
        "",
        "- Start with `funnel-hacking-orchestrator` for multistage investigations.",
        "- Use `apify-ads-intelligence` for collection and marketing skills for interpretation.",
        "- Use `video-analysis` only when visual evidence matters; a transcript is sufficient for spoken-copy analysis.",
        "- Use `attribution` only with owned measurement data, never to infer competitor performance.",
        "- Treat PLF and other benchmarks as labeled methodological context or scenarios.",
        "- Never load the full library for a narrow request.",
        "",
    ])
    return "\n".join(lines) + "\n", "\n".join(catalog)


def write_or_check(path: Path, content: str, check: bool) -> bool:
    current = path.read_text(encoding="utf-8") if path.exists() else None
    if check:
        if current != content:
            print(f"STALE: {path.relative_to(ROOT)}")
            return False
        return True
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"WROTE: {path.relative_to(ROOT)}")
    return True


def main() -> int:
    args = parse_args()
    registry, catalog = build()
    ok = write_or_check(REGISTRY, registry, args.check)
    ok = write_or_check(CATALOG, catalog, args.check) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
