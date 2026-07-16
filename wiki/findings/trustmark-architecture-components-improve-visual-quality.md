---
type: finding
title: "TrustMark Architecture Components Improve Visual Quality"
tags: [finding, trustmark, ablation-study, image-fidelity, focal-frequency-loss]
related: ["[[bui-2023-trustmark]]", "[[trustmark]]", "[[arbitrary-resolution-image-watermarking]]", "[[post-hoc-image-watermarking]]"]
created: 2026-07-06
updated: 2026-07-06
source: "[[bui-2023-trustmark]]"
confidence: high
replicated: false
---

# TrustMark Architecture Components Improve Visual Quality

## Finding

[[bui-2023-trustmark]] reports that TrustMark's GAN loss, focal frequency loss, and post-process module mainly improve visual quality while the staged training strategy keeps watermark recovery stable across ablations.

## Evidence

Table 4 evaluates TrustMark-B on DIV2K. With GAN, FFL, and the post-process module enabled, PSNR / SSIM / clean accuracy / noised accuracy are `40.203 / 0.987 / 0.999 / 0.973`. With all three disabled, the values are `36.300 / 0.976 / 0.991 / 0.959`.

The paper summarizes the component effects as follows: adding GAN improves PSNR by `0.7 dB`, adding the post-process module improves PSNR by `1.6 dB`, adding FFL improves PSNR by `1.7 dB`, and all three together make up about `4 dB` PSNR and `1.4%` bit accuracy.

## Interpretation

The result supports TrustMark's design claim that image-fidelity improvements come from the visual-quality components, while the staged training procedure protects watermark recovery.
