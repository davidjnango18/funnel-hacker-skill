# Architecture

## Design goal

The repository is a curated Hermes skill tap, not one giant prompt. Its control plane chooses a minimal set of domain skills, passes normalized evidence between them, and preserves claim provenance from collection through test planning.

```text
user brief + source descriptors
              |
              v
  funnel-hacking-orchestrator
  intake -> classify -> route
              |
       skills-registry.yaml
              |
    +---------+----------+----------------+
    |                    |                |
 collection          analysis         creation/test
 Apify/video     funnel/copy/CRO/PLF   original concepts
    |                    |                |
    +--------- evidence ledger -----------+
                         |
                  dossier + backlog
```

## Layers

### Control plane

`skills/funnel-hacking-orchestrator` owns intake, evidence classes, topology states, routing, market selection, reconstruction sequence, and output shape. Its `SKILL.md` is intentionally compact and links to focused references only when needed.

### Specialist plane

The 98 vendored specialists retain their full upstream methodologies and support files. Local compatibility and evidence patches give them a common contract without flattening them into one style.

- DTC/RMBC skills: direct-response research, copy, funnel assets, offer mechanics, audit, and testing.
- Corey marketing skills: general marketing strategy, research, acquisition, conversion, retention, measurement, and channel practices.
- PLF Walker: CPL/launch sequencing and adaptation.
- Translation: meaning-preserving translation and localization handoff.
- Apify ads intelligence: public ad collection and dataset preparation.
- Video analysis: local transcript, frame, OCR, and scene evidence where dependencies permit.

### Registry plane

`config/skills-registry.yaml` is generated from skill frontmatter plus curated routing rules. Every entry contains purpose, triggers, stage, input/output types, dependencies, recommendations, avoidance conditions, priority, notes, and path. `docs/SKILLS_CATALOG.md` is the human-readable projection of the same data.

### Knowledge plane

`references/INDEX.md` routes questions to the smallest relevant thematic note and, only when needed, its attributed source note. `references/live-sources.md` separates stable frameworks from ads, platforms, policies, benchmarks, payments, trends, and market behavior that must be checked at research time. The knowledge plane informs specialists; it does not replace current evidence or load wholesale into the orchestrator.

### Provenance plane

`config/upstreams.yaml` pins six exact Git commits, licenses, selections, and modification summaries. `licenses/` preserves upstream license texts. `scripts/sync_upstreams.py` makes selection and transformations inspectable and repeatable.

## Evidence flow

1. Inventory sources and assign `SRC-NNN` identifiers.
2. Preserve source, capture timestamp, locale, asset type, access status, and exact extract.
3. Label each claim `OBSERVED`, `USER-PROVIDED`, `DERIVED`, `INFERRED`, or `MISSING`.
4. Map nodes and edges using `VERIFIED`, `OBSERVED`, `INFERRED`, `UNVERIFIED`, or `MISSING`.
5. Route only evidence relevant to each specialist.
6. Reconnect findings to Source IDs in synthesis.
7. Separate extracted principle from hypothesis and original execution.
8. Express tests as falsifiable proposals; compute impact only from explicit, traceable inputs.

## Channel-degradation rules

Video and WhatsApp are optional evidence surfaces, not workflow gates.

| Detected state | Behavior |
| --- | --- |
| Transcript available | Analyze spoken content; make no visual claims. |
| Local video and visuals matter | Route to `video-analysis`. |
| Embedded video unavailable | Mark relevant stage `MISSING`; continue. |
| WhatsApp export available | Preserve sender/order/timestamps and analyze chronologically. |
| WhatsApp link without history | Mark internal sequence `MISSING`; continue. |
| Channel not detected | Continue silently; do not manufacture a gap. |

## Market model

Original-language evidence is immutable. Localization follows this chain:

`ORIGINAL -> understand -> extract principle -> translate meaning -> adapt to market -> review`

The orchestrator loads exactly one market profile (`es-MX`, `pt-BR`, or `global`) for the target context. The profiles are constraints and research prompts, not bundles of cultural stereotypes or fabricated regulatory facts.

## Update model

Vendoring is intentional so installed multi-file skills remain self-contained. An update is: fetch pinned/reviewed sources, copy the declared selections, apply transparent transforms, regenerate catalog, validate, test, review diff, then change provenance pins. No upstream script is executed automatically.
