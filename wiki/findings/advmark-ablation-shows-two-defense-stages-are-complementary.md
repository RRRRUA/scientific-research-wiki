---
type: finding
title: "AdvMark Ablation Shows Two Defense Stages Are Complementary"
tags: [finding, advmark, ablation-study, watermark-robustness, image-optimization]
related: ["[[chen-2026-advmark]]", "[[advmark]]", "[[post-hoc-image-watermarking]]", "[[watermark-robustness]]"]
created: 2026-06-17
updated: 2026-07-16
source: "[[chen-2026-advmark]]"
confidence: high
replicated: false
---

# AdvMark Ablation Shows Two Defense Stages Are Complementary

## Finding

The ablation in [[chen-2026-advmark]] shows that Stage 1 contributes primarily to adversarial robustness, while Stage 2 restores distortion and regeneration robustness. Removing either stage weakens comprehensive robustness.

## Evidence

In Table 3, full AdvMark has PSNR 37.0 and scores 0.99/0.83/0.87/0.87/0.98 under JPEG/combined distortion/Regen-SD-V1-4/Regen-SD-V1-5/WEvade. Without Stage 1, PSNR falls to 34.7 and WEvade accuracy to 0.50. Without Stage 2, JPEG falls to 0.88, combined distortion to 0.65, and Regen-SD-V1-4/1-5 to 0.54/0.54, while WEvade remains 0.99.

## Interpretation

This result supports AdvMark's decoupled design: adversarial robustness and regeneration/distortion robustness are not the same optimization problem. Jointly training against all attacks can harm clean accuracy, while Stage 1 alone does not cover conventional distortions and regeneration.
