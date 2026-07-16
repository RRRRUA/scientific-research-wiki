---
type: source
title: "WMAdapter: Adding WaterMark Control to Latent Diffusion Models"
tags: [latent-diffusion, watermarking, diffusion-native-watermarking, watermark-adapter, image-quality]
related: ["[[wmadapter]]", "[[latent-diffusion-watermarking]]", "[[watermark-robustness]]", "[[user-attribution]]", "[[diffusion-model-fingerprinting-comparison]]", "[[wmadapter-hybrid-finetuning-improves-image-quality]]"]
created: 2026-07-16
updated: 2026-07-16
authors: ["Hai Ci", "Yiren Song", "Pei Yang", "Jinheng Xie", "Mike Zheng Shou"]
year: 2024
url: ""
venue: ""
sources: ["Ci 等 - 2024 - WMAdapter Adding WaterMark Control to Latent Diffusion Models/full.md"]
---

# WMAdapter: Adding WaterMark Control to Latent Diffusion Models

## One-line Takeaway

[[wmadapter]] is a lightweight, plug-and-play VAE-decoder adapter for latent diffusion models. It conditions on both watermark bits and decoder features to imprint user-selected messages during generation without per-message VAE fine-tuning.

## Problem

Stable Signature-style decoder watermarking requires a separately fine-tuned VAE decoder for each watermark. The paper targets flexible message selection and stronger image quality while retaining diffusion-native integration.

## Method

WMAdapter attaches six contextual Fuser modules before the Stable Diffusion VAE decoder blocks. Each Fuser combines a 48-bit watermark representation with the current VAE feature and outputs a residual. A pretrained HiDDeN decoder recovers the message.

Training first freezes the VAE and watermark decoder, then learns the adapter with image-consistency and bit-recovery losses. Hybrid finetuning updates the adapter and VAE decoder during training but deploys the fine-tuned adapter with the original VAE decoder. This is designed to remove artifacts without giving up plug-and-play inference.

## Evidence

On COCO 2017 at `512 x 512`, Table 2 reports WMAdapter-I PSNR `34.8`, SSIM `0.96`, FID `2.5`, and combined-attack bit accuracy `0.91`; Stable Signature reports `29.7`, `0.87`, `3.2`, and `0.94`, respectively. WMAdapter-F reports combined-attack bit accuracy `0.93` with PSNR `33.1`.

Table 5 compares finetuning strategies. Hybrid finetuning reaches PSNR `34.8`, SSIM `0.96`, and FID `2.5` at combined-attack bit accuracy `0.91`; joint VAE finetuning has higher combined-attack accuracy `0.94` but lower PSNR `29.9` and SSIM `0.87`. The appendix reports `0.99` bit accuracy across the tested SD1.5, SD2.1, SDXL, and DiT VAEs before finetuning.

## Limitations and Caveats

- The reported robustness depends on a pretrained HiDDeN decoder and is weak under significant Gaussian noise.
- Adapter-F can create artifacts on images with homogeneous backgrounds.
- The paper supports flexible watermark messages, not an evaluated platform-scale attribution or collusion-defense protocol.

## Use in This Project

WMAdapter is a diffusion-native adapter route between per-key decoder fine-tuning and full weight-modulation fingerprinting. It separates flexible message control from permanent VAE modification.

## Raw Sources

- `raw/sources/Ci 等 - 2024 - WMAdapter Adding WaterMark Control to Latent Diffusion Models/full.md`

## Related Pages

- [[wmadapter]]
- [[latent-diffusion-watermarking]]
- [[watermark-robustness]]
- [[diffusion-model-fingerprinting-comparison]]
