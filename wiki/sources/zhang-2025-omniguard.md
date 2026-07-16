---
type: source
title: "OmniGuard: Hybrid Manipulation Localization via Augmented Versatile Deep Image Watermarking"
tags: [image-watermarking, tamper-localization, proactive-forensics, aigc-editing, copyright-protection]
related: ["[[omniguard]]", "[[editguard]]", "[[tamper-localization-for-generated-images]]", "[[localized-invisible-watermarking]]", "[[watermark-robustness]]", "[[localized-watermarking-for-tamper-localization-comparison]]", "[[omniguard-improves-localization-under-degradation]]"]
created: 2026-07-16
updated: 2026-07-16
authors: ["Xuanyu Zhang", "Zecheng Tang", "Zhipei Xu", "Runyi Li", "Youmin Xu", "Bin Chen", "Feng Gao", "Jian Zhang"]
year: 2025
url: ""
venue: ""
sources: ["Zhang 等 - 2025 - OmniGuard Hybrid Manipulation Localization via Augmented Versatile Deep Image Watermarking/full.md"]
---

# OmniGuard: Hybrid Manipulation Localization via Augmented Versatile Deep Image Watermarking

## One-line Takeaway

[[omniguard]] augments versatile deep image watermarking with an adaptive localization watermark, a degradation-aware passive tamper extractor, and AIGC-editing simulation for more robust copyright recovery and mask localization.

## Problem

Prior dual-watermark methods use a fixed localization tag and residual subtraction, which couples container-image fidelity to reconstruction accuracy and can fail under severe degradation. The paper targets flexible localization tags, improved fidelity, and resilience to global and local AIGC editing.

## Method

OmniGuard retains proactive embedding of spatial and copyright watermarks but replaces direct residual-threshold masks with a learned extractor that consumes the received image and reconstructed watermark artifact map. An adaptive transform makes the localization watermark content-aware. A lightweight VAE-based AIGC-editing simulator trains copyright recovery against global and local edits.

## Evidence

The abstract reports improvements over EditGuard of `4.25 dB` container-image PSNR, `20.7%` F1 under noisy conditions, and `14.8%` average bit accuracy. Table 6 reports joint training PSNR `41.59`, SSIM `0.985`, F1 `0.975`, and AUC `0.999`, versus `35.46`, `0.966`, `0.953`, and `0.986` for separate watermark embedding.

Under JPEG Q=60, Table 7 reports OmniGuard F1 `0.810` versus EditGuard `0.515`; under brightness degradation, it reports `0.927` versus `0.536`. The paper also evaluates unseen MagicQuill and SDXL-inpainting edits without fine-tuning.

## Limitations and Caveats

- Under degradation beyond the underlying image-into-image steganography robustness threshold, localization approaches passive-detector performance.
- Resolution scaling can amplify watermark artifacts on ultra-high-resolution images.
- The paper addresses image assets and AIGC editing rather than model-copy user attribution.

## Use in This Project

OmniGuard is a direct successor comparator to EditGuard that distinguishes blind extraction and degradation-aware localization from residual-only proactive forensics.

## Raw Sources

- `raw/sources/Zhang 等 - 2025 - OmniGuard Hybrid Manipulation Localization via Augmented Versatile Deep Image Watermarking/full.md`

## Related Pages

- [[omniguard]]
- [[editguard]]
- [[tamper-localization-for-generated-images]]
