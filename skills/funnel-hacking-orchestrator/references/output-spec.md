# Output Specification

## Scalable Dossier Layout

Use only the files the investigation needs:

```text
research/<target>/
|-- 00-executive-summary.md
|-- 01-source-ledger.md
|-- 02-funnel-map.md
|-- 03-traffic-and-ads.md
|-- 04-messaging-and-copy.md
|-- 05-offer-breakdown.md
|-- 06-sequence-analysis.md
|-- 07-localization.md
|-- 08-opportunities.md
|-- 09-creative-intelligence.md
|-- 10-test-ideas.md
`-- MISSING_EVIDENCE.md
```

Small investigations may use one markdown file with equivalent sections.

## Executive Summary

Include target/market/date, research question, observed funnel type(s), coverage, 3–7 evidence-backed findings, major uncertainty, and the most useful next action. Do not place unsupported performance estimates in the summary.

## Source Ledger

List Source ID, evidence class, type, origin, locale/market, capture time, access/status, and notes. Keep user-provided and publicly observed sources distinguishable.

## Funnel Map

Include node and edge ledgers plus a compact diagram when useful. State topology status and Source IDs. Provide a legend for `VERIFIED`, `OBSERVED`, `INFERRED`, `UNVERIFIED`, and `MISSING`.

## Creative Intelligence

Extract angle, hook family, promise, pain, desire, mechanism, objection, awareness, visual pattern, CTA, format, and proof type. Then explain:

- why the pattern may work;
- what evidence supports that interpretation;
- what remains unknown;
- an original hypothesis for the user's funnel;
- a measurement plan.

## Opportunities

Use four columns or subsections: competitor evidence, principle, hypothesis, original execution. Never blur them.

## Test Ideas

Each test needs a falsifiable hypothesis, control, one material variable, primary metric, guardrails, required sample/baseline inputs, and stop criteria. If sample-size inputs are missing, state what is required rather than inventing a duration or lift.

## Missing Evidence

List only detected/strongly indicated gaps, their affected conclusion, current workaround, and optional addition. Missing video/WhatsApp should not block the rest of the dossier.

