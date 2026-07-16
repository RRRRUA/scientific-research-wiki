---
type: finding
title: "OmniMark Maintains High Bit Accuracy with Low Quality Impact"
tags: [finding, omnimark, bit-accuracy, image-quality, watermark-robustness]
related: ["[[fei-2025-omnimark]]", "[[watermark-robustness]]", "[[generative-model-fingerprinting]]", "[[decoder-fingerprinting-scalability-comparison]]"]
created: 2026-06-09
updated: 2026-07-16
source: "[[fei-2025-omnimark]]"
confidence: high
replicated: false
---

# OmniMark Maintains High Bit Accuracy with Low Quality Impact

## Finding

[[fei-2025-omnimark]] reports that OmniMark maintains nearly 99% Bit Acc for 48-bit fingerprints with limited impact on image-quality metrics.

## Evidence

The OmniMark experiments use SDv2.0, nine OmniMark Layers, and 48-bit fingerprints. Table 2 reports Bit Acc of 99.757, 99.642, and 99.812 on COCO, ImageNet, and MagicBrush. The Model Fidelity section reports average PSNR around 31, SSIM around 0.88, LPIPS around 0.13, less than one FID point over baseline, and essentially unchanged CLIP score.

## Interpretation

This supports the judgment that multi-dimensional weight encoding can preserve fingerprint effectiveness and perceptual quality together, making OmniMark more attractive than single-dimension encoding or per-user fine-tuning.

## Caveat

These metrics come from the paper's setting and do not establish the same behavior under new architectures, flow-matching models, LoRA fine-tuning, or strong collusion.
