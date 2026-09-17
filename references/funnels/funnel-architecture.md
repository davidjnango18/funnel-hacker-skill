# Funnel Architecture

## Scope

Primary architecture source: Brunson (`SRC-006`). Counterweights and decision lenses: MECLABS (`SRC-012`), CXL (`SRC-010`, `SRC-011`), Sharp (`SRC-004`), and Hormozi Offers (`SRC-008`).

## Architecture before page tactics

A funnel is a network of customer decisions, assets, offers, and transitions. A value ladder is only one possible economic structure. Map the observed journey before assigning a template.

## Node record

For every node capture:

- source ID, URL/file, capture time, market, language;
- topology state: `VERIFIED`, `OBSERVED`, `INFERRED`, `UNVERIFIED`, or `MISSING`;
- audience state and traffic source when known;
- asset job and required micro-decision;
- promise, proof, CTA, price/terms, friction, anxiety;
- outgoing edge and whether the transition was directly verified;
- owned metric required to evaluate the node.

## Edge record

Record trigger, destination, channel, delay, branching rule, and evidence. Never add an edge because funnels “normally” work that way.

## Architecture lenses

### Value progression

Does each step produce value or evidence that justifies the next commitment? Higher price is not itself a higher-value ladder step.

### Decision sequence

What must the prospect notice, understand, believe, prefer, exchange, and complete? A missing decision cannot be repaired by a later upsell.

### Economic role

Label a step as acquisition, qualification, conversion, expansion, continuity, retention, or reactivation. Do not infer self-liquidation, LTV, or profitability without owned data.

### Availability and brand

Does the architecture make the offer easy to access and buy? Are distinctive brand cues preserved across ads, pages, checkout, and follow-up?

## Common pattern labels

The corpus supports classification of two-step/free-plus-shipping, self-liquidating offer, continuity, webinar, product launch, and high-ticket application patterns. A label describes structure; it does not validate suitability or performance.

## Complexity test

Every added step must justify itself through one of these jobs:

- necessary qualification;
- material education or proof;
- risk/expectation setting;
- operational routing;
- relevant value expansion;
- consented follow-up.

If a step does none of these, it is a candidate for removal or consolidation—but validate downstream effects.

## Recommended specialists

`funnel-architecture`, `funnel-audit`, `competitor-offer-analysis`, `cro`, `analytics`, plus only the stage specialist required by observed evidence.
