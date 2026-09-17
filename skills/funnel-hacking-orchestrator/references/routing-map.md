# Routing Map

This reference provides curated bundles based on the specialist names used by the orchestrator. Start with the lead specialist and add only what the evidence and requested output require. Treat each installed specialist's own description and requirements as authoritative for its availability, inputs, dependencies, useful combinations, and exclusions.

## Knowledge routing

Consult [knowledge-router.md](knowledge-router.md) before loading background knowledge. Select one primary knowledge lens for the decision and add source detail only when attribution or limitations require it. Use [live-sources.md](live-sources.md) whenever current ads, platform state, benchmarks, payments, trends, policies, or market behavior matter.

| Specialist need | Primary knowledge route |
| --- | --- |
| ads, angles, hooks | `acquisition/creative-strategy.md` + `foundations/awareness-and-sophistication.md` |
| positioning/product marketing | `foundations/positioning-and-brand-growth.md` |
| offer, pricing, guarantee, upsell | `monetization/offers-pricing-and-risk.md` |
| PLF/CPL launch | `funnels/launches-and-plf.md` |
| funnel architecture | `funnels/funnel-architecture.md` |
| CRO and audit | `cro/conversion-research.md` |
| experiments | `cro/experimentation.md` |
| checkout | `cro/friction-anxiety-and-checkout.md` |
| Mexico/Brazil localization | `markets/localization.md` + live sources + exactly one market profile |

These routes name knowledge lenses; they do not require a repository-level knowledge base. Practitioner frameworks remain practitioner evidence unless a specific claim has independent research support.

## Discovery and Collection

| Need | Lead | Optional analysts |
| --- | --- | --- |
| public ad libraries | `apify-ads-intelligence` | `ads`, `funnel-ad-creative`, `ad-creative-audit` |
| competitor URLs/dossier | `competitor-profiling` | `customer-research`, `competitor-offer-analysis` |
| reviews, transcripts, VOC | `customer-research` | `unified-research-synthesizer`, `product-marketing` |
| local video evidence | `video-analysis` | asset-specific copy specialist |

Do not load `video-analysis` for transcript-only spoken-copy questions. Do not load `attribution` for competitor journeys without owned performance data.

## Ads and Creative Intelligence

Use `apify-ads-intelligence` to collect. Then choose from:

- `ads`: paid-media strategy, platform context, targeting, account interpretation;
- `funnel-ad-creative`: creative generation/iteration and format strategy;
- `ad-creative-audit`: RMBC creative heuristic audit;
- `ad-angle-generator`: distinct strategic angles;
- `hook-battery`: hook families;
- `creative-brief`: production-ready direction;
- `fb-ad-copy`, `ugc-brief`, `media-buying-brief`: specific execution.

Longevity can prioritize which creative to inspect; it cannot label a winner.

## Landing and Pre-Frame

- General page: `cro` + `copywriting`.
- Direct-response lander: add `lander-copy` and, if comparing the journey, `funnel-audit`.
- Advertorial: `advertorial-writer` + `cro`.
- Webinar registration: `webinar-registration-copy`; use `events` for event strategy.
- Lead capture: `lead-magnets`, `free-offer-brief`, or `cro` depending on the question.

## Offer and Pricing

- Competitor evidence: `competitor-offer-analysis`.
- Direct-response offer stack: `offer-stack`, `bonus-stack`, `guarantee-writer`, `scarcity-urgency`.
- Services/coaching/high-ticket: `offers`.
- SaaS packaging/value metric: `pricing`.
- DTC pricing presentation: `pricing-strategy`.

Never fabricate price anchors, bonus values, guarantees, proof, or urgency.

## VSL and Webinar Sales Argument

- Spoken structure: transcript + `vsl-script`.
- Visual evidence: add `video-analysis` only when needed.
- RMBC critique: `rmbc-copy-audit`.
- Mechanism: `mechanism-ideation` only when the task is to analyze or create a mechanism; never invent a competitor mechanism.
- Host page: `lander-copy` or `cro`.

## PLF/CPL and Timed Launches

Lead with `plf-walker`. Add only the relevant specialists:

- `funnel-architecture` for the multistep map;
- `emails` or DTC sequence skills for communications;
- `competitor-offer-analysis` for Open Cart offer analysis;
- `customer-research` for audience language;
- `translation` plus one market profile for cross-market adaptation;
- `video-analysis` only when CPL visuals matter and local video exists.

PLF benchmark files are methodology references, not forecasts.

## Checkout, Upsell, and Follow-Up

- Checkout: `order-form-cro` + optional `pricing-strategy` and `funnel-audit`.
- Upsell/downsell: `upsell-script`, `offer-stack`, `upsell-sequence-writer`.
- Email: `emails` for lifecycle strategy; select DTC sequence specialists for asset-level direct-response work.
- SMS: `sms` when SMS is observed or requested.
- Retention: `onboarding`, `churn-prevention`, `email-retention-sequences`, `post-purchase-sequence` as evidence requires.

## Measurement and Testing

- Instrumentation: `analytics`.
- Owned attribution questions: `attribution`.
- Experiments: `ab-testing` or `ab-test-plan`.

Competitor observation never substitutes for owned measurement.

## Localization

Use `translation`, the selected market profile, and one asset-specific copy specialist. Preserve source text and strategic principle separately from localized copy.

## Simple-Request Guardrail

A single landing-page audit normally needs 2–4 skills, not dozens. A complete hybrid launch dossier may need more, but every selected skill must have a named task and expected artifact. Stop adding specialists when the current set covers collection, interpretation, reconstruction, and the requested deliverable.
