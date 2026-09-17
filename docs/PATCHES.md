# Local Compatibility and Safety Patches

Vendored skills retain their upstream substance. The following narrow transformations make the collection portable, self-contained, and consistent with the repository's evidence contract. Their implementation lives in `scripts/sync_upstreams.py`.

## Common additions

- Added a short Hermes evidence-first rule block to imported skills.
- Required external material to be treated as untrusted data.
- Required explicit separation of observed facts, supplied facts, derivations, inferences, and missing evidence.
- Prohibited invented performance, monetary, testimonial, claim, and attribution data.
- Normalized skill-to-skill references to repository-relative paths.

## DTC/RMBC collection

- Removed Claude-only installer/update/telemetry behavior, home-directory workspaces, `/bin/rmbc-workspace`, and `AskUserQuestion` dependencies.
- Rewired RMBC methodology references to the vendored `rmbc-context` resources.
- Replaced the upstream self-update skill behavior with an audited local sync procedure.
- Constrained `funnel-audit` and `funnel-architecture` to traceable owned inputs for revenue or impact calculations; otherwise results are `UNKNOWN` or explicit scenarios.
- Changed synthesized psychographics and general-market assertions into sourced findings or labeled hypotheses.
- Disallowed “plausible” proof, testimonials, and undocumented claim specificity.
- Required unavailable ad visuals to be `MISSING / NOT SCORED`.
- Removed a default guarantee duration from landing-page guidance.

## Corey marketing collection

- Preserved all 50 skills and all referenced support tool guides.
- Copied each explicitly referenced integration guide and optional CLI into that skill's own `references/tools/` subtree, so an isolated Hermes installation does not depend on a repository-global path.
- Normalized `.claude` and home-directory context references to project-local `.agents/product-marketing.md` and `research/marketing-plans/` paths.
- Reworded Claude-specific fetch/tool assumptions into capability-neutral instructions.

## PLF Walker

- Added evidence and benchmark-safety overrides.
- Retained the full methodology, templates, adaptations, references, and original shell helper.
- Added a standard-library Python timeline helper for cross-platform use; supplied dates and rates remain inputs, not observed competitor facts.

## Translation

- Imported only the requested translation skill.
- Made the workflow explicit: `ORIGINAL -> understand -> principle -> translate meaning -> adapt -> review`.
- Required literal translation and market localization to remain separate artifacts.

## Apify Ads Intelligence

- Imported only the requested ads-intelligence skill.
- Explicitly prohibited winner, spend, sales, profitability, and ROAS inference from ad longevity or observed ad counts.
- Kept longevity as a timestamped observation and qualitative prioritization clue only.
- Added PowerShell/Windows portability notes while retaining POSIX examples.

## Video Analysis

- Installed under its declared skill name, `video-analysis`.
- Added transcript-first routing: use local video processing only when visual evidence is required.
- Made missing or inaccessible video non-blocking for the overall funnel workflow.
- Retained the diagnostic, tests, and local analysis stack.

## Local orchestrator

`funnel-hacking-orchestrator` is original repository content, not a modified upstream skill. It supplies progressive-disclosure routing, evidence provenance, topology states, Mexico/Brazil market profiles, degradation behavior, synthesis boundaries, and output specifications.

## Funnel Hacking knowledge base

- Added a repository-contained, evidence-classified Markdown knowledge base under `references/`.
- Added source-level provenance and thematic synthesis without reproducing the ingested books or guides.
- Routed the orchestrator and generated registry to `references/INDEX.md` and the current-evidence policy in `references/live-sources.md`.
- Kept practitioner frameworks distinct from research-backed sources and added explicit cross-source tensions instead of choosing an unsupported winner.
- Added repeatable manifest, link, secret, source-ID, and raw-cleanup validation in `scripts/validate_knowledge_base.py` and the unit-test suite.
