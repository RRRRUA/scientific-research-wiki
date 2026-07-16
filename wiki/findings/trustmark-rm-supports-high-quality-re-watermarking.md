---
type: finding
title: "TrustMark-RM Supports High-quality Re-watermarking"
tags: [finding, trustmark, watermark-removal, re-watermarking, image-fidelity]
related: ["[[bui-2023-trustmark]]", "[[trustmark]]", "[[post-hoc-image-watermarking]]"]
created: 2026-07-06
updated: 2026-07-06
source: "[[bui-2023-trustmark]]"
confidence: high
replicated: false
---

# TrustMark-RM Supports High-quality Re-watermarking

## Finding

[[bui-2023-trustmark]] introduces TrustMark-RM as a watermark removal network for re-watermarking workflows, and reports that it removes TrustMark artifacts with much higher image quality than an I-FGSM removal baseline.

## Evidence

Table 3 evaluates watermark removal for TrustMark-B on DIV2K. TrustMark-RM reports PSNR `48.48`, SSIM `0.997`, and bit accuracy `0.553`, while I-FGSM reports PSNR `23.48`, SSIM `0.613`, and bit accuracy `0.629`.

Figure 3 reports that re-watermarking bit accuracy is not affected by whether the remover is used, but TrustMark-RM preserves image quality better than direct repeated re-watermarking. The paper also notes that the denoising effect weakens after each re-watermarking pass because unwanted TrustMark-RM noise accumulates over time.

## Interpretation

TrustMark-RM makes post-hoc provenance workflows more editable, but it also shows a dual-use tension: if an imperceptible watermark can be treated as removable noise, the surrounding provenance system must account for removal and replacement.
