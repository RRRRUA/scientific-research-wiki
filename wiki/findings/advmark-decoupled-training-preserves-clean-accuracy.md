---
type: finding
title: "AdvMark Decoupled Training Preserves Clean Accuracy"
tags: [finding, advmark, clean-accuracy, adversarial-training, watermark-robustness]
related: ["[[chen-2026-advmark]]", "[[advmark]]", "[[post-hoc-image-watermarking]]", "[[watermark-robustness]]"]
created: 2026-06-17
updated: 2026-07-16
source: "[[chen-2026-advmark]]"
confidence: high
replicated: false
---

# AdvMark Decoupled Training Preserves Clean Accuracy

## Finding

[[chen-2026-advmark]] reports that joint adversarial training sacrifices clean accuracy, while AdvMark's encoder-focused Stage 1 preserves clean bit accuracy and improves regeneration and WEvade robustness.

## Evidence

In Figure 2, MBRS-JAT Defense has clean accuracy 0.94, while MBRS-EAT and AdvMark both reach 1.00. AdvMark also scores 0.99, 0.87, and 0.98 under JPEG, Regen-SD-V1-4, and WEvade, above MBRS-EAT at 0.98, 0.65, and 0.77.

## Interpretation

This supports the paper's diagnosis: primarily changing the decoder decision boundary harms clean watermarked images, whereas fine-tuning the encoder first to move watermarked images into a non-attackable region preserves clean accuracy more effectively.
