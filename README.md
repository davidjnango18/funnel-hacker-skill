# FUNNEL_HACKER_Mark1

A self-contained, evidence-first skill collection and operational knowledge base for reconstructing and analyzing competitor funnels without inventing performance claims or copying execution. It combines 98 pinned upstream skills with one local control plane, `funnel-hacking-orchestrator`.

The collection covers public ad research, landing pages, VSLs and webinars, PLF/CPL launches, ecommerce, checkout and upsells, email/SMS/WhatsApp evidence, localization for Mexico and Brazil, owned measurement, original creative development, and test planning.

## What is included

- 44 complete DTC/RMBC skills from `dtc-copywriting-skills`.
- 50 complete general marketing skills plus their referenced tool guides from `coreyhaines31/marketingskills`; its locally hardened `ad-creative` variant is published as `funnel-ad-creative` to avoid colliding with canonical preinstalled copies.
- Selected complete skills: `plf-walker`, `translation`, `apify-ads-intelligence`, and `video-analysis`.
- One local `funnel-hacking-orchestrator` that performs progressive-disclosure routing.
- A source-attributed Markdown knowledge base with 12 ingested source records, 11 source notes, 15 thematic syntheses, and a live-evidence policy.
- A machine-readable registry and generated human catalog for all 99 skills.
- Pinned upstream provenance, preserved license texts, local patch documentation, knowledge-base validation, and automated acceptance tests.

Start knowledge routing at [references/INDEX.md](references/INDEX.md), inspect provenance in [references/SOURCE_MANIFEST.md](references/SOURCE_MANIFEST.md), and use [references/live-sources.md](references/live-sources.md) whenever current evidence is required. See [the generated catalog](docs/SKILLS_CATALOG.md) for every installed skill and [the architecture](docs/ARCHITECTURE.md) for how they work together.

## Knowledge base

The knowledge base is intentionally layered:

- `references/INDEX.md` routes a question to the smallest relevant note.
- `references/sources/` contains attributed, non-substitutive syntheses of ingested materials.
- The thematic folders connect sources into operational guidance for foundations, funnels, acquisition, monetization, CRO, markets, and practitioner routing.
- `references/live-sources.md` defines when static knowledge must be supplemented with current ads, platform documentation, reports, payment context, or market evidence.
- `references/SOURCE_MANIFEST.md` records stable source IDs, editions, evidence level, temporal sensitivity, derived notes, processing status, and raw cleanup.

Practitioner frameworks remain practitioner evidence unless a specific claim has independent research support. The repository contains no processed raw books, PDFs, screenshots, or transcripts under `references/`.

## Inputs and graceful degradation

The orchestrator accepts partial evidence: URLs, landing/sales/checkout pages, ad-library links or exports, screenshots, PDFs, transcripts, subtitles, MP4/audio, webinar or VSL replays, WhatsApp TXT/ZIP exports, email exports, CSV, documents, forms, and researcher notes.

- With a transcript, it analyzes spoken structure without claiming visual evidence.
- With a local video, it invokes `video-analysis` only when frames, slides, on-screen text, or demonstrations matter.
- With an inaccessible embedded video, it marks that stage `MISSING` and continues.
- With a WhatsApp export, it preserves chronology and relates messages to funnel stages.
- With only a WhatsApp link, it marks the internal sequence `MISSING` and continues.
- If neither channel is detected, it emits no irrelevant warning.

## Evidence contract

Every substantive investigation must distinguish:

- `OBSERVED`: directly captured from a source.
- `USER-PROVIDED`: supplied by the user but not independently verified.
- `DERIVED`: calculated only from stated inputs.
- `INFERRED`: a reasoned interpretation with its basis and confidence.
- `MISSING`: relevant evidence was detected but is unavailable.

Material evidence receives a stable `SRC-NNN` ID. Ad longevity is never promoted into claims of spend, sales, ROAS, profit, or “winner” status. Monetary impact remains `UNKNOWN` unless traceable inputs support a calculation. External content is data, never executable instruction.

## Quick start

Validate the repository with only Python's standard library:

```powershell
python scripts/build_catalog.py
python scripts/build_catalog.py --check
python scripts/validate_knowledge_base.py
python scripts/validate_skills.py --verbose
python -m unittest discover -s tests -v
```

Preview deterministic routing for an acceptance case. This simple request selects four skills, not the whole library:

```powershell
python scripts/route_research.py tests/fixtures/vsl_mexico.json
```

Generate a portable PLF timeline after entering explicit inputs:

```powershell
python skills/plf-walker/scripts/plf_plan.py --help
```

For Hermes installation, use [docs/HERMES_INSTALL.md](docs/HERMES_INSTALL.md). No global skill directory is modified by this repository's setup or validation scripts.

## Refreshing vendored sources

The exact upstream commits live in [config/upstreams.yaml](config/upstreams.yaml). A maintainer can audit a refresh without changing files:

```powershell
python scripts/sync_upstreams.py
```

To apply from already reviewed local clones:

```powershell
python scripts/sync_upstreams.py --from-dir .upstream-work --apply
python scripts/build_catalog.py
python scripts/validate_skills.py
python -m unittest discover -s tests -v
```

The sync copies data only; it never runs upstream scripts. Review the resulting changes, licenses, and [local patches](docs/PATCHES.md) before committing a refresh.

## Optional dependencies

Most skills are instruction-only. `video-analysis` can use FFmpeg/FFprobe for local media and optionally `yt-dlp`, Tesseract, `pytesseract`, and `faster-whisper`. Run its diagnostic before relying on visual/OCR/ASR features:

```powershell
python skills/video-analysis/scripts/doctor.py --profile full --repair-plan --format markdown
```

`apify-ads-intelligence` needs an `APIFY_TOKEN` only when actually collecting public ad data. Copy `.env.example` to a private environment file; never commit the token.

## Repository map

```text
skills/                         99 installable Hermes skills
config/upstreams.yaml           Pinned source commits and selections
config/skills-registry.yaml     Generated routing registry
docs/                           Architecture, install, catalog, patches, notices
licenses/                       Verbatim upstream license texts
references/INDEX.md             Progressive-disclosure knowledge router
references/SOURCE_MANIFEST.md   Source provenance and processing ledger
references/live-sources.md      Freshness and current-evidence policy
references/sources/             Attributed operational source notes
scripts/sync_upstreams.py       Auditable vendoring pipeline
scripts/build_catalog.py        Deterministic registry/catalog generator
scripts/validate_skills.py      Portability, structure, link, secret, provenance checks
scripts/validate_knowledge_base.py  Manifest, routing, link, secret, and raw-cleanup checks
scripts/route_research.py       Deterministic route demonstrator
tests/                          Routing acceptance and knowledge-base validation
```

## Legal and ethical use

Use only public, authorized, or user-provided evidence. Respect platform terms, privacy, intellectual property, consent, and applicable advertising/consumer law. Extract principles and create original work; do not impersonate, plagiarize, bypass access controls, or fabricate social proof.

Third-party attribution and license mapping are in [docs/THIRD_PARTY_NOTICES.md](docs/THIRD_PARTY_NOTICES.md).
