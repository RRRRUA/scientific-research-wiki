---
type: entity
title: "StableGuard"
aliases: ["MPW-VAE", "MoE-GFN", "Mixture-of-Experts Guided Forensic Network"]
tags: [method, latent-diffusion-models, watermarking, tamper-localization, copyright-protection]
related: ["[[yang-2025-stableguard]]", "[[latent-diffusion-watermarking]]", "[[watermark-robustness]]", "[[tamper-localization-for-generated-images]]", "[[stableguard-unifies-watermark-verification-and-tamper-localization]]", "[[stableguard-mpw-vae-enables-self-supervised-tamper-training]]"]
created: 2026-06-11
updated: 2026-07-16
sources: ["Yang 等 - 2025 - StableGuard Towards Unified Copyright Protection and Tamper Localization in Latent Diffusion Model.pdf-d8a32816-0fa0-4c8d-934e-e96205ef30ed/full.md"]
---

# StableGuard

StableGuard is a Latent Diffusion Models watermarking and forensics framework introduced by [[yang-2025-stableguard]]. It supports copyright verification and tamper localization jointly.

## Components

- Multiplexing Watermark VAE (MPW-VAE): adds a residual-based watermark adapter to the VAE decoder so the same latent code can generate watermarked or watermark-free images.
- Mixture-of-Experts Guided Forensic Network (MoE-GFN): jointly recovers watermark bits and localizes tampered regions from watermarked or tampered images.
- Mixture-of-Forensic-Experts (MoFE): combines a Watermark Extraction Expert, Tampering Localization Expert, and Boundary Enhancement Expert through a Dynamic Soft Router.

## Core Mechanism

StableGuard uses MPW-VAE to generate paired watermarked and clean samples, then mixes them with random or SAM-generated semantic masks to create self-supervised tampering data. MoE-GFN learns to identify missing watermark patterns, local tampering traces, and boundary anomalies, producing both watermark verification and a tamper mask.

## Differences from Other Methods

| Method | Main task | Embedding location |
| --- | --- | --- |
| [[stable-signature]] | generated-image detection / limited identification | latent decoder |
| [[wouaf]] | user attribution | decoder weight modulation |
| [[omnimark]] | scalable model-copy fingerprinting | VAE decoder weight encoding |
| [[tree-ring-watermark]] | provenance detection | initial noise Fourier space |
| StableGuard | copyright verification + tamper localization | VAE decoder adapter + forensic network |

StableGuard, WOUAF, and OmniMark all involve the decoder or VAE decoder, but StableGuard does not focus on distributing unique model copies to many users. It turns the watermark signal into an active cue for subsequent forensic localization.

## Limitations

StableGuard assumes that generated images have already been watermarked; unwatermarked images fall outside its target setting. The paper also notes that image degradation reduces forensic accuracy, especially for pixel-level localization.
