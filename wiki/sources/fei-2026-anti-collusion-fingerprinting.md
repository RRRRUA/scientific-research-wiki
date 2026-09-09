---
type: source
title: "Efficient, Robust, and Anti-Collusion Fingerprinting of Image Diffusion Models"
tags: [latent-diffusion, model-fingerprinting, anti-collusion, personalized-normalization, user-attribution]
related: ["[[generative-model-fingerprinting]]", "[[user-attribution]]", "[[watermark-robustness]]", "[[watermark-capacity-for-user-attribution]]", "[[anti-collusion-model-distribution-comparison]]", "[[act-makes-colluded-fingerprint-models-unusable]]"]
created: 2026-09-08
updated: 2026-09-08
authors: ["Jianwei Fei", "Yunshu Dai", "Zhihua Xia", "Xiaochun Cao", "Jiantao Zhou", "Alessandro Piva", "Benedetta Tondi"]
year: 2026
url: ""
venue: ""
sources: ["Fei 等 - 2026 - Efficient, Robust, and Anti-Collusion Fingerprinting of Image Diffusion Models/full.md"]
---

# Efficient, Robust, and Anti-Collusion Fingerprinting of Image Diffusion Models

## One-line Takeaway

This paper embeds 48-bit fingerprints through a personalized normalization module (PNM) and applies user-specific, function-invariant Anti-Collusion Transformations (ACT) so parameter merging destroys generation utility.

## Method

Fingerprint encoders generate PNM normalization coefficients inside the VAE decoder. Each distributed copy applies channel permutation, scaling, and sign-flip transformations that preserve that copy's function but move different users' parameters apart. Worst-case parameter perturbation training targets pruning, compression, noise, and fine-tuning robustness.

## Evidence

Table I averages raw bit accuracy over 32 fingerprints and 1,000 images per fingerprint and reports about `99.5%` across COCO, ImageNet, MagicBrush, and InstructPix2Pix. The identification study samples up to `10^4` users, with 10 images per user and 1,000 non-fingerprinted negatives.

Under equal-weight two-party parameter averaging, Table V reports FID `79.51` with ACT versus `23.55` without ACT, while matching accuracy remains around `75%` to either colluder and TPR is `0.467`. For 3 to 20 colluders, Table VI reports PSNR `12.64` down to `10.96 dB`. Nonlinear merges in Table VII yield PSNR `5.21-6.24 dB` and LPIPS `0.82-0.87`.

## Limitations and Caveats

- ACT deters collusion by utility destruction; it does not identify the colluders after a successful merge.
- The `1.98 x 10^7` model-capacity figure is a Hamming-bound calculation under a proposed code distance, not a deployment-scale tracing experiment.
- The `10^4`-user experiment uses a sampled user set and only 1,000 negative images, so it does not establish a platform-wide global FPR at larger scale.
- The paper assumes distributors can modify and deliver white-box model copies; it does not cover decoder replacement or distillation into a new architecture.
- Venue, DOI, and code URL are not present in the parse.

## Raw Source

- `raw/sources/Fei 等 - 2026 - Efficient, Robust, and Anti-Collusion Fingerprinting of Image Diffusion Models/full.md`

