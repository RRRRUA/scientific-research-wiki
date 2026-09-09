---
type: methodology
title: "Watermark Verification Operands"
tags: [methodology, bit-accuracy, detection, attribution, false-positive-rate, tamper-localization]
related: ["[[user-attribution]]", "[[watermark-robustness]]", "[[watermark-capacity-for-user-attribution]]", "[[tamper-localization-for-generated-images]]", "[[meng-2024-latent-watermark]]", "[[huang-2026-robin-plus-plus]]"]
created: 2026-09-08
updated: 2026-09-08
sources: ["Meng 等 - 2024 - Latent Watermark Inject and Detect Watermarks in Latent Diffusion Space/full.md", "Fares 等 - 2026 - MOLM Mixture of LoRA Markers/full.md", "Huang 等 - 2026 - ROBIN++ Unified Copyright Protection and Tamper Localization for Diffusion Models Via Dual-Domain S/full.md", "Gan 等 - 2026 - GenPTW Latent Image Watermarking for Provenance Tracing and Tamper Localization/full.md"]
---

# Watermark Verification Operands

## Why the Operand Matters

Watermark papers often reuse the words accuracy, robustness, and tracing for different random variables and decision rules. A valid comparison identifies what is predicted, against which target, over which population, and at which threshold.

| Reported quantity | Operand | Supports | Does not by itself support |
| --- | --- | --- | --- |
| Raw BitAcc | Recovered payload bits versus embedded bits | Average bit recovery | Exact message recovery, low FPR, or user identification |
| TPR at fixed FPR | Thresholded statistic on positive and negative images | Presence detection at the stated operating point | Payload fidelity or platform-wide attribution |
| Exact-message or Top-1 identification | Recovered code versus a registered user pool | Closed-set attribution for that pool | Open-world global FPR or colluder tracing |
| Zero-bit accuracy/AUC | Watermarked versus clean score | Presence verification | Multi-bit capacity or user attribution |
| F1/AUC/IoU for masks | Pixel predictions versus tamper masks | Localization performance | Copyright ownership or payload recovery |

## Corpus Examples

- [[latent-watermark-separates-thresholded-detection-from-bit-recovery]] reports `90%` raw BitAcc but `100%` TPR in the same all-attack condition; the thresholded detector tolerates message errors.
- [[huang-2026-robin-plus-plus]] explicitly renames zero-bit binary classification accuracy as `Bit Accuracy`; it must not be pooled with the multi-bit rows in the same paper.
- [[fei-2026-anti-collusion-fingerprinting]] evaluates up to `10^4` sampled users, while its negative set contains only 1,000 images. User-pool size and empirical negative coverage are separate scale axes.
- [[gan-2026-genptw]] reports message accuracy and mask F1/AUC. Both matter, but neither can substitute for the other.

## Low-FPR Validation Rule

With `N` independent negative samples, empirical rates change in increments of `1/N`. A claim below that resolution is model-based, extrapolated, or unsupported by the stated count unless an additional estimator is specified. Always record the threshold model and the actual number of negatives separately.

