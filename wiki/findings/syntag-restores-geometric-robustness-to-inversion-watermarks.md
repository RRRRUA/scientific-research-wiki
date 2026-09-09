---
type: finding
title: "SynTag Restores Geometric Robustness to Inversion Watermarks"
tags: [finding, syntag, inversion, synchronization, geometric-robustness]
related: ["[[fang-2025-syntag]]", "[[syntag]]", "[[ddim-inversion-for-watermark-detection]]", "[[inversion-watermark-robustness-comparison]]"]
created: 2026-09-08
updated: 2026-09-08
source: "[[fang-2025-syntag]]"
confidence: medium
replicated: false
---

# SynTag Restores Geometric Robustness to Inversion Watermarks

## Finding

SynTag reports that an injected synchronization template plus geometric correction substantially improves inversion-watermark recovery after rotation, translation, scale, and shear.

## Evidence

Table 1 reports GauShad-SynTag geometric TPR `0.980/0.988` and raw bit accuracy `0.938/0.940` on Stable Diffusion v1.4/v2.1. Table 6 reports that adding the predictor raises TPR from `0.016` to `0.763`, and the full predictor plus pixel- and latent-level compensation reaches TPR `0.990` and raw bit accuracy `0.935`.

## Interpretation

The evidence isolates synchronization as a distinct robustness mechanism, but the principal test uses only 50 images. It does not empirically validate the claimed `10^-6` FPR operating point.

