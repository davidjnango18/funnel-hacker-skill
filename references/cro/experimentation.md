# Experimentation and Learning

## Scope

Synthesis of CXL (`SRC-010`, `SRC-011`) and Hopkins (`SRC-001`). CXL modernizes the accountable-testing impulse; neither source should replace current statistical guidance for a specific experiment.

## Minimum experiment plan

- decision to be informed;
- evidence-backed problem;
- falsifiable mechanism hypothesis;
- control and treatment definition;
- eligible population and randomization unit;
- primary metric and guardrails;
- baseline, minimum effect of interest, power/sample method;
- planned duration and seasonality/business-cycle considerations;
- stopping rule and multiple-testing approach;
- instrumentation QA;
- analysis and decision rule;
- limitations and post-implementation monitoring.

## Interpretation rules

- Statistical significance is not practical importance.
- A threshold crossing is not permission to stop if the design did not allow sequential monitoring.
- “No significant difference” is not proof of equivalence.
- Segment exploration after the result is exploratory unless planned and powered.
- A winning test is local to the population, implementation, metric, and period studied.
- A test can increase the primary conversion while harming refunds, qualification, margin, support, retention, or brand.

## When not to A/B test

- the path is technically broken;
- traffic/events cannot support the decision;
- instrumentation is unreliable;
- the change is a mandatory safety/compliance fix;
- variants cannot be isolated operationally;
- qualitative research can answer the immediate question more efficiently.

## Learning record

Store the hypothesis, evidence, design, deviations, result, uncertainty, segment notes, guardrails, and next decision. Preserve losses and inconclusive results to prevent repeat testing and outcome-only storytelling.

## Practitioner-framework boundary

Tests should evaluate a local hypothesis from Schwartz, Brunson, Walker, Hormozi, or MECLABS. A named framework does not lower the standard of evidence or determine the expected effect.

## Recommended specialists

`ab-testing`, `ab-test-plan`, `analytics`, `attribution` only for owned data, and the relevant asset specialist.
