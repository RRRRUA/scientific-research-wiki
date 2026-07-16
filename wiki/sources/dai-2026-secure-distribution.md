---
type: source
title: "Secure Distribution: Anti-Collusion Watermarking via Spectral Weight Modulation in Latent Diffusion Models"
tags: [latent-diffusion, watermarking, user-attribution, anti-collusion, weight-modulation, lora]
related: ["[[secure-distribution]]", "[[user-attribution]]", "[[watermark-robustness]]", "[[latent-diffusion-watermarking]]", "[[how-to-scale-user-attribution-for-ldm]]", "[[diffusion-model-fingerprinting-comparison]]", "[[secure-distribution-collusion-removal-destroys-model-utility]]"]
created: 2026-07-16
updated: 2026-07-16
authors: ["Yunshu Dai", "Jianwei Fei", "Wenhong Huang", "Fangjun Huang", "Zhihua Xia"]
year: 2026
url: ""
venue: ""
sources: ["Dai 等 - 2026 - Secure Distribution Anti-Collusion Watermarking via Spectral Weight Modulation in Latent Diffusion Models/full.md"]
---

# Secure Distribution: Anti-Collusion Watermarking via Spectral Weight Modulation in Latent Diffusion Models

## One-line Takeaway

[[secure-distribution]] combines Lie-group-parameterized LoRA watermark embedding with Spectral Weight Modulation (SWM) to distribute functionally equivalent but parameter-distinct latent diffusion model copies whose collusion damages model utility.

## Problem

User-specific model watermarks can be removed when colluders combine several white-box model copies. The paper targets parameter averaging and nonlinear merges while retaining watermark verification and generation quality for legitimate copies.

## Method

The method embeds a multi-bit watermark while fine-tuning the VAE decoder through a multiplicative Lie-group LoRA update. At distribution time, SWM applies a user-specific frequency-domain scrambling transform to one convolutional kernel and its inverse to the next layer. The paired transforms preserve model behavior while making user copies parameter-distinct.

## Evidence

Table 5 reports bit accuracy of `99.54%`, `99.64%`, and `99.56%` on COCO text-to-image, ImageNet text-to-image, and MagicBrush image-to-image, with TPR `1.0` and FPR `0.0` at the reported threshold. Table 7 reports SWM output SSIM `1.00` and MSE below `1 x 10^-6` on all three datasets.

Under the reported nonlinear collusion attacks, Table 4 gives watermark extraction accuracy near random guessing (`49.11%-52.04%`) while PSNR falls below `7 dB` and LPIPS is about `0.85`; the paper interprets the colluded outputs as unusable. It also reports over `90%` watermark accuracy under 50% cropping and extreme brightness reduction.

## Limitations and Caveats

- The reported anti-collusion result is a utility-destruction mechanism, not identification of individual colluders.
- The method is evaluated on specific VAE-decoder adaptation layers; generalization to other architectures is left open.
- Maintaining user-specific instances can still create deployment-scale overhead.

## Use in This Project

This is the corpus's first direct anti-collusion evidence. It strengthens the user-attribution question by adding collusion resistance to copy-creation speed, capacity, and verification thresholds.

## Raw Sources

- `raw/sources/Dai 等 - 2026 - Secure Distribution Anti-Collusion Watermarking via Spectral Weight Modulation in Latent Diffusion Models/full.md`

## Related Pages

- [[secure-distribution]]
- [[user-attribution]]
- [[watermark-robustness]]
- [[how-to-scale-user-attribution-for-ldm]]
