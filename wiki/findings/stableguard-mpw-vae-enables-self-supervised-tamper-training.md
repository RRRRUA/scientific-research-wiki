---
type: finding
title: "StableGuard MPW-VAE Enables Self-Supervised Tamper Training"
tags: [finding, stableguard, mpw-vae, self-supervised-learning, tamper-localization]
related: ["[[yang-2025-stableguard]]", "[[stableguard]]", "[[tamper-localization-for-generated-images]]"]
created: 2026-06-09
updated: 2026-07-16
source: "[[yang-2025-stableguard]]"
confidence: high
replicated: false
---

# StableGuard MPW-VAE Enables Self-Supervised Tamper Training

## Finding

StableGuard's MPW-VAE generates paired watermarked and watermark-free images from the same latent code. Random or SAM-generated masks then synthesize tampering samples, allowing MoE-GFN to train without manual tamper annotations.

## Evidence

The method section describes a switchable MPW-VAE watermark adapter and constructs training images from paired samples with random or semantic masks. In the Table 4 ablation, removing MPW-VAE yields F1/AUC/IoU of 0.811/0.796/0.774; the full decoder-placement version reaches 0.980/0.992/0.961 with Bit Acc 99.98.

## Interpretation

This result supports jointly designing watermark embedding and the forensic detector. StableGuard differs from post-hoc unified methods by optimizing the generation-time watermark mechanism and downstream localization network in the same self-supervised loop.
