# Calculation guide

## Question and evidence

What changes when training remains within data silos?

Synthetic client shards and a separate synthetic test set.

**Status:** SYNTHETIC / RULE-BASED PROTOTYPE | no educational validity claim.

## Design

Compute client-mean logistic gradients; clip; optionally add Gaussian noise; average clients and update shared weights.

## Calculation and interpretation

`g = Xᵀ(sigmoid(Xw)-y)/n; w_next = w - learning_rate×mean(client gradients).`

Clients receive equal weight, not sample-size weight. Clipping plus noise has no stated epsilon/delta accountant, secure aggregation, or attack evaluation. It is not a formal differential-privacy guarantee.

## Evidence table

Selected recorded values (units and context shown). Full precision below is for traceability, not a claim of measurement precision.

| Quantity | Value | Unit / meaning | JSON path |
|---|---:|---|---|
| federated_accuracy | 0.77 | unitless | `federated_accuracy` |
| noisy_federated_accuracy_noise_0_10 | 0.769 | unitless | `noisy_federated_accuracy_noise_0_10` |
| utility_delta | 0.001 | unitless | `utility_delta` |

Source: [results/demo_metrics.json](results/demo_metrics.json). Values resolve directly from this file when figures are regenerated.

This federated-learning demonstration keeps synthetic learner records in local shards while sharing clipped, optionally noisy gradients. A separate synthetic test set shows how noise changes predictive utility, with the update rule and client weighting exposed for inspection. The project demonstrates data-local computation, while explicitly leaving formal privacy accounting, secure aggregation, and adversarial evaluation unimplemented.

## Verification performed in this review

The existing suite requires unavailable dependencies; no full-suite pass is claimed. The bundled demonstration executed successfully in this review.

The figure-generation check verifies agreement between the selected source values and SVGs. It does not validate the raw dataset, fitted model, identification assumptions, or external generalization.

```bash
python scripts/build_review_figures.py
python scripts/build_review_figures.py --check
```

## Implementation map

Follow these functions to inspect each transformation. Validation helpers and private functions remain visible in the linked modules.

| Function | Purpose / documented behavior |
|---|---|
| [`main`](src/privacy_preserving_learning_analytics/cli.py#L5) | Inspect the explicit implementation and its callers. |
| [`sigmoid`](src/privacy_preserving_learning_analytics/core.py#L8) | Inspect the explicit implementation and its callers. |
| [`gradient`](src/privacy_preserving_learning_analytics/core.py#L9) | Inspect the explicit implementation and its callers. |
| [`clip_and_noise`](src/privacy_preserving_learning_analytics/core.py#L11) | Inspect the explicit implementation and its callers. |
| [`federated_train`](src/privacy_preserving_learning_analytics/core.py#L13) | Inspect the explicit implementation and its callers. |
| [`accuracy`](src/privacy_preserving_learning_analytics/core.py#L18) | Inspect the explicit implementation and its callers. |
| [`make_shards`](src/privacy_preserving_learning_analytics/synthetic.py#L3) | Inspect the explicit implementation and its callers. |

## What remains before a stronger research claim

Clients receive equal weight, not sample-size weight. Clipping plus noise has no stated epsilon/delta accountant, secure aggregation, or attack evaluation. It is not a formal differential-privacy guarantee. A successful software test is not validation of a scientific construct. New experiments should state their split unit, comparator, outcome, uncertainty procedure and failure criteria before examining final test results.
