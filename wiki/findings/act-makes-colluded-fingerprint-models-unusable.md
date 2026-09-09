---
type: finding
title: "ACT Makes Colluded Fingerprint Models Unusable"
tags: [finding, anti-collusion, model-fingerprinting, utility-destruction]
related: ["[[fei-2026-anti-collusion-fingerprinting]]", "[[anti-collusion-model-distribution-comparison]]", "[[secure-distribution-collusion-removal-destroys-model-utility]]", "[[user-attribution]]"]
created: 2026-09-08
updated: 2026-09-08
source: "[[fei-2026-anti-collusion-fingerprinting]]"
confidence: high
replicated: false
---

# ACT Makes Colluded Fingerprint Models Unusable

## Finding

User-specific function-invariant transformations leave individual PNM fingerprint models usable but make parameter-level merging produce severely degraded outputs.

## Evidence

For equal-weight two-party averaging, Table V reports FID `79.51` with ACT versus `23.55` without it. Matching accuracy remains near `75%` to each colluder and verification TPR is `0.467`, so ACT does not preserve direct attribution; it removes the useful colluded model. Nonlinear two-party merges in Table VII yield PSNR `5.21-6.24 dB` and LPIPS `0.82-0.87`.

## Interpretation

This is proactive utility destruction, not colluder identification or traitor tracing. It supports the same defensive objective as [[secure-distribution-collusion-removal-destroys-model-utility]] through a different parameterization.

