---
type: finding
title: "OmniGuard Improves Localization Under Degradation"
tags: [finding, omniguard, tamper-localization, watermarking, degradation-robustness]
related: ["[[omniguard]]", "[[zhang-2025-omniguard]]", "[[editguard]]", "[[tamper-localization-for-generated-images]]"]
created: 2026-07-16
updated: 2026-07-16
source: "[[zhang-2025-omniguard]]"
confidence: high
replicated: false
---

# OmniGuard Improves Localization Under Degradation

## Finding

OmniGuard's learned degradation-aware extractor reports substantially stronger local-edit F1 than EditGuard under JPEG and brightness degradation.

## Evidence

Table 7 reports F1 `0.810` for OmniGuard versus `0.515` for EditGuard at JPEG Q=60, and `0.927` versus `0.536` under the reported brightness degradation. The abstract reports a `20.7%` F1 improvement under noisy conditions.

## Interpretation

This supports using a learned mask extractor rather than direct residual thresholding when reconstruction artifacts can be mistaken for tampering. It does not remove the need for quality thresholds when degradation becomes extreme.
