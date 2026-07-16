---
type: finding
title: "WMAdapter Hybrid Finetuning Improves Image Quality"
tags: [finding, wmadapter, latent-diffusion, image-quality, watermarking]
related: ["[[wmadapter]]", "[[ci-2024-wmadapter]]", "[[latent-diffusion-watermarking]]", "[[watermark-robustness]]"]
created: 2026-07-16
updated: 2026-07-16
source: "[[ci-2024-wmadapter]]"
confidence: high
replicated: false
---

# WMAdapter Hybrid Finetuning Improves Image Quality

## Finding

WMAdapter's hybrid finetuning preserves stronger image-quality metrics than joint VAE-decoder finetuning while keeping similar combined-attack bit recovery.

## Evidence

Table 5 reports hybrid finetuning at PSNR `34.8`, SSIM `0.96`, FID `2.5`, and combined-attack bit accuracy `0.91`. Joint finetuning reports PSNR `29.9`, SSIM `0.87`, FID `3.1`, and bit accuracy `0.94`. The paper deploys the hybrid adapter with the original VAE decoder, unlike joint finetuning.

## Interpretation

The result supports a deployment pattern in which an adapter learns with model parameters but avoids permanently replacing the base VAE at inference. It does not establish that hybrid finetuning dominates when the application prioritizes robustness above visual quality.
