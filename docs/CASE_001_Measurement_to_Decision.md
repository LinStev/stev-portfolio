# CASE-001 | From Measurement to Decision

## What this case is

This is a method case about how to turn a measurement into a decision someone can act on. It uses a Motion Science Lab (MSL) context only as **historical work context**. It does not disclose an MSL report, participant record, internal rule table, screenshot, raw data, or operational metric.

## Claim and role boundary

| Material | Label | What it supports |
| --- | --- | --- |
| Historical work context | **Actual work** | Stev has worked in a force-plate assessment setting where a reader must decide what a measurement can and cannot mean. The company-specific scope remains subject to release approval. |
| Decision workflow in this case | **Method explainer** | A reusable way to separate conditions, observations, interpretation limits, and next actions. It is not an account of a completed company deployment. |
| Rule-based interpretation and longitudinal-tracking direction | **Personal proposal** | A proposal described in the supporting PRD and validation protocol. It is not a company-approved roadmap, released feature, or completed study. |

## The decision problem

A measurement does not become a useful product outcome merely because it is precise or visually clear. The reader still needs to know:

1. What decision is being made?
2. Under what conditions was the measure collected?
3. What was observed, without adding an unsupported conclusion?
4. What uncertainty changes the interpretation?
5. What is the smallest responsible next action?

The case therefore starts with the decision, rather than a metric catalogue.

## Method: measurement-to-decision workflow

| Step | Question | Output boundary |
| --- | --- | --- |
| 1. Define the decision | What must the reader choose, prioritize, monitor, or defer? | State the decision and audience before selecting metrics. |
| 2. Check measurement conditions | Are protocol, population, timing, and repeated-measure conditions appropriate for the intended comparison? | Report conditions and gaps; do not treat a number as context-free. |
| 3. Separate observation from interpretation | What is directly shown, and what is only a hypothesis or rule-based inference? | Label the two separately. |
| 4. Check the evidence boundary | Does the proposed conclusion exceed measurement error, validity evidence, or the instrument's intended use? | Retain `Unknown` where the evidence does not support a conclusion. |
| 5. Choose the next action | What should be reviewed, measured again, investigated, or explicitly not claimed? | Give an action that is proportionate to evidence, not a diagnosis or prediction. |

## Example decision architecture

The following architecture is a **personal proposal**, not a statement about an existing MSL product.

```text
measurement conditions
        ↓
observations and data-quality checks
        ↓
explicit interpretation rules and uncertainty labels
        ↓
decision-ready summary
        ↓
review, re-measurement, or a scoped next action
```

The proposal deliberately does not convert force-plate data into injury prediction, medical diagnosis, or an unqualified whole-person performance score. A change claim would require an evidence plan that addresses measurement error before it is called meaningful.

## What the case demonstrates

- Product framing: begin with the decision a reader needs to make.
- Scientific restraint: preserve the difference between measurement, interpretation, and outcome.
- Evidence design: specify what must be estimated before a longitudinal change claim is allowed.
- Role clarity: describe Stev's method and proposal work without assigning engineering implementation or company approval to him.

## Sources used for this case

| Source | Use in this case | Release status |
| --- | --- | --- |
| `docs/PRD_MSL_Report_v2.md` | Personal proposal for decision-oriented reporting and explicit non-goals | Published on this portfolio. |
| `docs/Validation_Protocol_MSL_Reliability.md` | Personal proposal for reliability, typical error, and detectable-change evidence | Published on this portfolio. |

## Release boundary

This case contains no logo, screenshot, client or participant information, operational number, or internal rule threshold.
