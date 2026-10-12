# CASE-002 | Wearable Strength Training Intelligence

**Classification:** Fictional independent concept. Not a shipped product, customer engagement, deployed system, completed test, or validated clinical/technical result.

## One bounded V1 question

Can a wrist-worn IMU help a person review a small, preselected set of upper-body resistance-training repetitions and tempo without asking the sensor to infer more than it can observe?

This case keeps the answer intentionally narrow: repetition count, phase timing, confidence indication, and manual correction for three proposed supported exercises. It does not promise exercise-quality scoring, injury-risk prediction, diagnosis, or automatic load prescription.

## Classification of every claim

| Type | In this case |
| --- | --- |
| **Target** | Three supported exercises; proposed release gates for event precision, recall, count error, timing, latency, and confidence calibration. |
| **Assumption** | A general wrist-worn device can expose usable IMU signals; a state-based sampling design may manage energy use; people may correct clear errors in a session summary. |
| **Evidence Needed** | Target-hardware power/thermal behavior, reference-label agreement, subject-disjoint performance, worst-slice behavior, BLE reliability, and user comprehension of confidence. |
| **Not claimed** | Product deployment, customer use, completed data collection, model performance, achieved metric, clinical validation, diagnostic capability, injury prediction, or whole-body movement-quality scoring. |

## Product decision

The proposed V1 begins with a preselected exercise instead of general exercise recognition. A user selects a supported exercise, completes a set, receives a provisional repetition and tempo summary, and can correct it when confidence is low.

```text
preselected supported exercise
        ↓
IMU event window and phase inference
        ↓
confidence gate
        ├── sufficient confidence → provisional event summary
        ├── low confidence → review needed
        └── unsupported motion → unknown or manual logging
```

`Unknown` is a valid outcome. The system should not silently guess another exercise or turn a low-confidence event into a safety conclusion.

## Proposed scope

| Include in the proposed V1 | Exclude from the proposed V1 |
| --- | --- |
| Three selected upper-body resistance exercises | Lower-body movements and a broad exercise library |
| Repetition count, phase timing, set-level tempo consistency | Personalized coaching and automatic load prescription |
| Confidence indication and manual correction | Multi-device sensing and continuous raw-stream dependence |
| Explicit fallback for unknown or unsupported motion | Diagnosis, injury prediction, or form-safety scoring |

## Validation before expansion

The proposed release decision is based on aggregate performance **and** each predefined worst slice, not only a favourable average. The evidence plan would need to test exercise, relative load, tempo, wrist side, fatigue, fit, and background movement with subject-disjoint evaluation data.

If a predefined slice does not meet its proposed gate, the next decision is to narrow the scope, improve the fallback, or return to evidence collection. It is not to widen the promise.

## What this case demonstrates

- Scope control when sensor observability is limited.
- A product contract that makes confidence and unknown states visible.
- Validation gates that distinguish a proposal from a result.
- A rollout design that treats safety-relevant overclaiming as a product risk.

## Source and release boundary

This is an independently authored concept. It excludes interview material, client material, company names, confidential identifiers, and external assets, and has no MSL-specific name, logo, image, data, or source-material dependency.

