# Research design

## Project aim

Learning analytics can be useful while still collecting too much. This repo makes privacy an engineering variable rather than a footnote by comparing centralized, federated, and noisy training regimes on the same prediction task.

## Research questions

1. How much utility is retained when raw learner records stay local?
2. How does clipping and noise change model quality?
3. What privacy–utility trade-offs should be reported before deployment?

## Baseline analytic pipeline

1. Local learner silos
2. Local gradients
3. Federated aggregation
4. DP clipping + noise
5. Privacy–utility evaluation

## Construct-to-measure discipline

The repository intentionally distinguishes **constructs** from **proxies**. A behavioral feature may be consistent with a construct without proving that construct exists. A real study should establish content validity, reliability, sensitivity to context, and convergent/discriminant evidence before attaching strong interpretations.

## Minimum empirical extension

1. Pre-register the main research question and analysis plan.
2. Recruit a context-appropriate sample with consent and a documented data-governance plan.
3. Establish annotation reliability or measurement reliability before model comparison.
4. Split exploratory analysis from confirmatory evaluation.
5. Report uncertainty, subgroup performance, missing-data patterns, and negative findings.
6. Evaluate whether the output is understandable and useful to the people expected to act on it.

## Threats to validity

- Noise scale in this demo is not converted into a formal epsilon guarantee.
- Synthetic clients do not reproduce real institutional heterogeneity.
- Federated learning reduces data movement but does not, by itself, guarantee privacy.

## Next experiments

- Integrate Opacus or TensorFlow Privacy for formal accounting.
- Add secure aggregation and membership-inference attacks.
- Benchmark non-IID client distributions and fairness across learner subgroups.
