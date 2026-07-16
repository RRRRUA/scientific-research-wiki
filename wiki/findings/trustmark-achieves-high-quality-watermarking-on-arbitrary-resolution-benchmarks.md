---
type: finding
title: "TrustMark Achieves High-quality Watermarking on Arbitrary-resolution Benchmarks"
tags: [finding, trustmark, image-fidelity, arbitrary-resolution, bit-accuracy]
related: ["[[bui-2023-trustmark]]", "[[trustmark]]", "[[arbitrary-resolution-image-watermarking]]", "[[post-hoc-image-watermarking]]"]
created: 2026-07-06
updated: 2026-07-06
source: "[[bui-2023-trustmark]]"
confidence: high
replicated: false
---

# TrustMark Achieves High-quality Watermarking on Arbitrary-resolution Benchmarks

## Finding

[[bui-2023-trustmark]] reports that TrustMark maintains high image quality and strong watermark recovery on CLIC, DIV2K, and MetFace while evaluating at original image resolution through residual-based resolution scaling.

## Evidence

Table 1 reports TrustMark-Q PSNR / SSIM of `43.26 / 0.99` on CLIC, `42.39 / 0.99` on DIV2K, and `45.34 / 0.99` on MetFace. Clean bit accuracy is `1.00` across all three benchmarks, and noised bit accuracy is `0.95`, `0.95`, and `0.96`.

TrustMark-B trades image quality for recovery: PSNR is `41.53`, `40.20`, and `43.87`, while noised bit accuracy is `0.97` on all three benchmarks. The arbitrary-resolution ablation reports that encoding PSNR varies by only `+-0.02 dB` and decoding bit accuracy by `+-1e-4` on average across DIV2K resolution variants.

## Interpretation

This finding makes TrustMark a useful comparator for high-resolution image provenance workflows. It is still post-hoc image watermarking, not diffusion-native provenance.
