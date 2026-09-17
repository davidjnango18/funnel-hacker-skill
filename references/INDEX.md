# Funnel Hacking Knowledge Base Index

This is a routing map, not a compendium. Read only the smallest set of notes needed for the current question. Source notes support attribution and nuance; thematic notes support decisions. Current platform and market questions must also consult [live-sources.md](live-sources.md).

## Routing protocol

1. Classify supplied and discovered evidence using the orchestrator's evidence protocol.
2. Identify the decision or funnel stage under investigation.
3. Load one primary thematic note from the table below.
4. Add only the linked source note needed for attribution, limitations, or a framework detail.
5. Add live evidence when freshness rules require it.
6. Route to the smallest specialist set in `config/skills-registry.yaml`.
7. Keep evidence, principle, hypothesis, and original execution separate.

Never load the entire knowledge base for a single investigation.

## Topic router

| Analyze / decide | Read first | Add when needed | Recommended specialists |
| --- | --- | --- | --- |
| awareness | [Awareness and sophistication](foundations/awareness-and-sophistication.md) | [Schwartz](sources/schwartz-breakthrough-advertising.md), [conversion research](cro/conversion-research.md) | `customer-research`, `copywriting`, `lander-copy`, `vsl-script` |
| market sophistication | [Awareness and sophistication](foundations/awareness-and-sophistication.md) | [Creative strategy](acquisition/creative-strategy.md), current competitor ads via [live sources](live-sources.md) | `competitor-profiling`, `ad-angle-generator`, `hook-battery` |
| positioning | [Positioning and brand growth](foundations/positioning-and-brand-growth.md) | [Dunford](sources/dunford-obviously-awesome.md), [Sharp](sources/sharp-how-brands-grow.md) | `product-marketing`, `customer-research`, `competitor-profiling` |
| persuasion / proof | [Persuasion and ethics](foundations/persuasion-and-ethics.md) | [Cialdini](sources/cialdini-influence.md), [MECLABS](sources/meclabs-conversion-sequence-heuristic.md) | `marketing-psychology`, `copywriting`, `funnel-audit` |
| direct response | [Direct response](foundations/direct-response.md) | [Hopkins](sources/hopkins-scientific-advertising.md), [Schwartz](sources/schwartz-breakthrough-advertising.md) | `copywriting`, `cro`, `analytics`, `ab-testing` |
| funnel map / architecture | [Funnel architecture](funnels/funnel-architecture.md) | [Brunson](sources/brunson-dotcom-secrets.md), stage-specific note | `funnel-architecture`, `funnel-audit` |
| PLF / CPL / timed launch | [Launches and PLF](funnels/launches-and-plf.md) | [Walker](sources/walker-launch.md), [follow-up](funnels/follow-up.md) | `plf-walker`, `funnel-architecture`, `emails` |
| VSL / webinar sales argument | [Awareness and sophistication](foundations/awareness-and-sophistication.md) | [Persuasion](foundations/persuasion-and-ethics.md), [offers](monetization/offers-pricing-and-risk.md), transcript evidence | `vsl-script`, `rmbc-copy-audit`; `video-analysis` only if visuals matter |
| ads / creative | [Creative strategy](acquisition/creative-strategy.md) | [Awareness](foundations/awareness-and-sophistication.md), [live sources](live-sources.md) | `apify-ads-intelligence`, `ads`, `ad-creative`, `ad-creative-audit` |
| hooks / angles | [Creative strategy](acquisition/creative-strategy.md) | [Schwartz](sources/schwartz-breakthrough-advertising.md), [positioning](foundations/positioning-and-brand-growth.md) | `hook-battery`, `ad-angle-generator`, `customer-research` |
| lead generation / lead magnets | [Lead generation](acquisition/lead-generation.md) | [Hormozi Leads](sources/hormozi-100m-leads.md), [experimentation](cro/experimentation.md) | `lead-magnets`, `free-offer-brief`, `ads`, `content-strategy` |
| offer / pricing / guarantee / bonus | [Offers, pricing, and risk](monetization/offers-pricing-and-risk.md) | [Hormozi Offers](sources/hormozi-100m-offers.md), [Dunford](sources/dunford-obviously-awesome.md) | `offers`, `offer-stack`, `pricing-strategy`, `guarantee-writer`, `bonus-stack` |
| upsell / value ladder | [Funnel architecture](funnels/funnel-architecture.md) | [Offers](monetization/offers-pricing-and-risk.md), [Brunson](sources/brunson-dotcom-secrets.md) | `upsell-script`, `offer-stack`, `order-form-cro` |
| follow-up / email | [Follow-up](funnels/follow-up.md) | [Launches](funnels/launches-and-plf.md) for timed sequences | `emails` plus one asset-level sequence specialist |
| CRO diagnosis | [Conversion research](cro/conversion-research.md) | [MECLABS](sources/meclabs-conversion-sequence-heuristic.md), [CXL](sources/laja-conversionxl-cro-guide.md) | `cro`, `analytics`, `customer-research`, `funnel-audit` |
| experimentation / A/B testing | [Experimentation](cro/experimentation.md) | [CXL](sources/laja-conversionxl-cro-guide.md), current statistical guidance | `ab-testing`, `ab-test-plan`, `analytics` |
| checkout / order form | [Friction, anxiety, and checkout](cro/friction-anxiety-and-checkout.md) | [Offers](monetization/offers-pricing-and-risk.md), live local payments/policies | `order-form-cro`, `pricing-strategy`, `guarantee-writer`, `analytics` |
| Brazil | [Localization](markets/localization.md) + [live sources](live-sources.md) | orchestrator [pt-BR profile](../skills/funnel-hacking-orchestrator/references/markets/pt-BR.md) | `translation` plus relevant asset specialist |
| Mexico | [Localization](markets/localization.md) + [live sources](live-sources.md) | orchestrator [es-MX profile](../skills/funnel-hacking-orchestrator/references/markets/es-MX.md) | `translation` plus relevant asset specialist |
| localization | [Localization](markets/localization.md) | [live sources](live-sources.md), exactly one market profile | `translation`, `customer-research` when local VOC is needed |

## Evidence-level router

| Need | Preferred sources |
| --- | --- |
| Classic direct-response principles | Hopkins (`SRC-001`), Schwartz (`SRC-002`) |
| Research-backed persuasion synthesis | Cialdini (`SRC-003`) with current primary research for material claims |
| Marketing-science counterweight | Sharp (`SRC-004`) |
| Practitioner positioning | Dunford (`SRC-005`) |
| Practitioner funnel/launch frameworks | Brunson (`SRC-006`), Walker (`SRC-007`) |
| Practitioner offer/lead frameworks | Hormozi (`SRC-008`, `SRC-009`) |
| Research-led CRO process | CXL (`SRC-010`, `SRC-011`) |
| Decision heuristic | MECLABS (`SRC-012`) |
| Current ads/platform/market state | [Live sources](live-sources.md) captured during the investigation |

## Practitioner routing

Use [Practitioner Framework Map](practitioners/framework-map.md) to distinguish supported ingested sources from named coverage gaps. Practitioner claims never become `research_backed` merely through repetition across practitioner books.

## Source notes

- [SRC-001 — Hopkins, Scientific Advertising](sources/hopkins-scientific-advertising.md)
- [SRC-002 — Schwartz, Breakthrough Advertising](sources/schwartz-breakthrough-advertising.md)
- [SRC-003 — Cialdini, Influence](sources/cialdini-influence.md)
- [SRC-004 — Sharp, How Brands Grow](sources/sharp-how-brands-grow.md)
- [SRC-005 — Dunford, Obviously Awesome](sources/dunford-obviously-awesome.md)
- [SRC-006 — Brunson, DotCom Secrets](sources/brunson-dotcom-secrets.md)
- [SRC-007 — Walker, Launch](sources/walker-launch.md)
- [SRC-008 — Hormozi, $100M Offers](sources/hormozi-100m-offers.md)
- [SRC-009 — Hormozi, $100M Leads](sources/hormozi-100m-leads.md)
- [SRC-010 / SRC-011 — Laja/CXL conversion optimization guide](sources/laja-conversionxl-cro-guide.md)
- [SRC-012 — MECLABS Conversion Sequence Heuristic](sources/meclabs-conversion-sequence-heuristic.md)

See [SOURCE_MANIFEST.md](SOURCE_MANIFEST.md) for provenance, editions, processing status, and raw-source removal state.
