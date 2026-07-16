---
type: source
title: "OmniMark: Efficient and Scalable Latent Diffusion Model Fingerprinting"
tags: [latent-diffusion-models, model-fingerprinting, watermarking, user-attribution, generative-ai-safety]
related: ["[[generative-model-fingerprinting]]", "[[latent-diffusion-watermarking]]", "[[user-attribution]]", "[[watermark-robustness]]", "[[diffusion-model-fingerprinting-comparison]]"]
created: 2026-06-07
updated: 2026-07-16
authors: ["Jianwei Fei", "Yunshu Dai", "Zhihua Xia", "Fangjun Huang", "Jiantao Zhou"]
year: 2025
url: "https://github.com/jumpycat/OmniMark"
venue: ""
sources: ["Fei 等 - 2025 - OmniMark Efficient and Scalable Latent Diffusion Model Fingerprinting/full.md"]
---

# OmniMark: Efficient and Scalable Latent Diffusion Model Fingerprinting

## One-sentence Summary
OmniMark encodes fingerprints in VAE decoder weights for scalable user-specific fingerprinting of latent diffusion models, allowing many unique model copies to be created quickly without retraining each copy.

## Problem
Existing watermarking and fingerprinting methods often depend on post-processing, input modification, or retraining and fine-tuning for each user fingerprint. These routes are inefficient when a model provider must distribute many traceable model copies.

## Method
OmniMark modifies the LDM VAE decoder with OmniMark layers. These layers expand convolution kernels into parallel kernels and encode a fingerprint across kernel, filter, channel, and spatial dimensions. A fingerprint decoder recovers the embedded bit string from generated images. A noise layer improves robustness to image transformations, while a sharpness-aware strategy improves resistance to model fine-tuning.

## Evidence
The paper evaluates text-to-image and image-to-image tasks with Stable Diffusion v2.0 on MS-COCO, ImageNet, and MagicBrush. With 48-bit fingerprints, it reports about 99% bit accuracy across datasets and limited impact on FID, CLIP score, PSNR, SSIM, and LPIPS.

## Key Results
- Supports rapid creation of new fingerprinted model copies, reported below 100 ms in the abstract.
- Preserves image quality close to the original model while embedding imperceptible fingerprints.
- Scales better than Stable Signature because new user fingerprints do not require per-user fine-tuning.
- Adding a noise layer during fine-tuning substantially improves robustness.

## Limitations and Caveats
- Strong white-box attacks, especially model fine-tuning, remain important threats. The proposed robust fingerprinting strategy improves resistance but does not eliminate the risk.
- Evaluation focuses on image-generation LDM settings; transfer to other modalities remains open.
- The method depends on reliable fingerprint decoding and statistical verification assumptions.

## Use in This Project
Among the three decoder-rooted papers, this one emphasizes scalability most directly and is central to the question of distributing many user-specific diffusion models while preserving attribution capability.

## Original Sources
- `raw/sources/Fei 等 - 2025 - OmniMark Efficient and Scalable Latent Diffusion Model Fingerprinting/full.md`

## Related Pages
- [[generative-model-fingerprinting]]
- [[latent-diffusion-watermarking]]
- [[user-attribution]]
- [[watermark-robustness]]
- [[diffusion-model-fingerprinting-comparison]]
