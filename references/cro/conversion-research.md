# Conversion Research

## Scope

Primary process: CXL (`SRC-010`, `SRC-011`). Diagnostic complement: MECLABS (`SRC-012`). Strategic counterweights: Dunford (`SRC-005`) and Sharp (`SRC-004`).

## Research order

1. **Technical integrity:** verify that key paths work across relevant devices/browsers and that speed/errors are measured.
2. **Instrumentation:** confirm event definitions, data quality, identity/session limits, and business KPIs.
3. **Quantitative localization:** identify where and for whom outcomes differ.
4. **Structured heuristic review:** flag possible relevance, clarity, motivation, friction, distraction, and anxiety issues.
5. **Behavioral observation:** use replays/maps carefully to see interaction patterns, not hidden intent.
6. **Qualitative research:** collect customer, visitor, sales, support, and usability evidence.
7. **Synthesis:** group converging observations into problems and hypotheses.
8. **Prioritization:** weigh evidence strength, affected reach, decision importance, risk, and effort.

## Evidence matrix

| Evidence type | Can help answer | Cannot establish alone |
| --- | --- | --- |
| Analytics | where, when, segment magnitude | why behavior occurred |
| Heat/click/scroll map | aggregate interaction patterns | motivation or causality |
| Session replay | concrete usability episodes | prevalence without sampling |
| Survey/interview | language, objections, perceived alternatives | population frequency without design |
| User test | comprehension and task friction | market-wide conversion impact |
| Heuristic review | expert hypotheses | actual user problem or lift |
| Competitor observation | possible patterns and questions | suitability, profit, or causation |

## Issue record

```yaml
issue_id: CRO-001
observation: "..."
evidence_class: OBSERVED
sources: [SRC-...]
affected_segment: "..."
decision_barrier: "clarity | motivation | friction | anxiety | technical"
confidence: low | medium | high
limits: "..."
hypothesis: "If ..., then ..., because ..."
required_measurement: "..."
```

## Guardrails

- Remove personal data from replays and research exports.
- Preserve exact survey wording and respondent context.
- Do not convert a loud anecdote into frequency.
- Do not estimate monetary impact without traceable traffic, conversion, price, cost, and time-window inputs.
- Include availability, brand recognition, qualification, margin, and retention when local optimization could harm them.

## Recommended specialists

`cro`, `analytics`, `customer-research`, `funnel-audit`, then the relevant page/offer specialist.
