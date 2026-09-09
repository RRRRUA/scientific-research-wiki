---
type: source
title: "OmniMark: Efficient and Scalable Latent Diffusion Model Fingerprinting"
tags: [latent-diffusion-models, model-fingerprinting, watermarking, user-attribution, generative-ai-safety]
related: ["[[omnimark]]", "[[generative-model-fingerprinting]]", "[[latent-diffusion-watermarking]]", "[[user-attribution]]", "[[watermark-robustness]]", "[[diffusion-model-fingerprinting-comparison]]", "[[decoder-fingerprinting-scalability-comparison]]", "[[omnimark-generates-fingerprinted-model-copies-under-100-ms]]", "[[omnimark-maintains-high-bit-accuracy-with-low-quality-impact]]"]
created: 2026-06-07
updated: 2026-09-08
authors: ["Jianwei Fei", "Yunshu Dai", "Zhihua Xia", "Fangjun Huang", "Jiantao Zhou"]
year: 2025
url: "https://github.com/jumpycat/OmniMark"
venue: ""
sources: ["Fei 等 - 2025 - OmniMark Efficient and Scalable Latent Diffusion Model Fingerprinting/full.md"]
---

# OmniMark: Efficient and Scalable Latent Diffusion Model Fingerprinting

## One-line Takeaway

[[omnimark]] encodes a fingerprint across several dimensions of VAE decoder weights so one trained system can rapidly construct many fingerprinted model copies without per-user retraining.

## Method

OmniMark layers expand decoder convolutions into parallel kernels and condition their weights on a fingerprint. After training, the conditional weights are folded into ordinary convolution weights for distribution. A fingerprint decoder recovers the 48-bit string from generated images, while a noise layer and sharpness-aware training target image- and model-level robustness.

## Evidence

The paper evaluates Stable Diffusion v2.0 on MS-COCO, ImageNet, and MagicBrush. It reports about `99%` raw bit accuracy for 48-bit fingerprints, less than one FID point of degradation in its principal settings, and below `100 ms` to construct the fingerprinted layers.

## Limitations and Caveats

- The sub-100-ms figure measures layer construction, not end-to-end distribution, storage, loading, verification, or user-management latency.
- The experiments do not establish platform-scale global false-positive control or resistance to attackers holding several copies.
- Fine-tuning remains a meaningful white-box threat even after the proposed robustness training.

## Raw Source

- `raw/sources/Fei 等 - 2025 - OmniMark Efficient and Scalable Latent Diffusion Model Fingerprinting/full.md`
