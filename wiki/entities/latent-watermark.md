---
type: entity
title: "Latent Watermark"
tags: [method, latent-space, watermarking, attribution]
related: ["[[meng-2024-latent-watermark]]", "[[latent-diffusion-watermarking]]", "[[user-attribution]]", "[[watermark-robustness]]"]
created: 2026-09-08
updated: 2026-09-08
sources: ["Meng 等 - 2024 - Latent Watermark Inject and Detect Watermarks in Latent Diffusion Space/full.md"]
---

# Latent Watermark

Latent Watermark (LW) injects and recovers a multi-bit message in VAE latent space while keeping the base latent diffusion model frozen. A three-stage training schedule initializes message coding, near-identity coupling, and joint fidelity/recovery optimization in sequence.

