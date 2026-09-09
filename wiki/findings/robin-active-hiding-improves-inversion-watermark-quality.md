---
type: finding
title: "ROBIN Active Hiding Improves Inversion-Watermark Quality"
tags: [finding, robin, inversion, watermark-robustness, image-quality]
related: ["[[huang-2024-robin]]", "[[robin]]", "[[fourier-noise-watermarking]]", "[[inversion-watermark-robustness-comparison]]"]
created: 2026-09-08
updated: 2026-09-08
source: "[[huang-2024-robin]]"
confidence: high
replicated: false
---

# ROBIN Active Hiding Improves Inversion-Watermark Quality

## Finding

ROBIN reports that an optimized hiding prompt lets a stronger intermediate-state frequency watermark retain better same-seed image similarity than Tree-Ring while preserving high verification AUC.

## Evidence

Table 4 reports Stable Diffusion PSNR `24.03 dB` and SSIM `0.768` for ROBIN versus `15.37 dB` and `0.568` for Tree-Ring, both measured against their unwatermarked same-seed images. Table 1 reports average attack AUC `0.983` for ROBIN and `0.975` for Tree-Ring in the paper's evaluation.

## Interpretation

This is zero-bit presence verification under the paper's own implementations. It does not establish payload recovery or multi-user attribution, and AUC drops to `0.556` under six simultaneous attacks.

