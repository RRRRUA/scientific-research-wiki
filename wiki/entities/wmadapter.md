---
type: entity
title: "WMAdapter"
tags: [latent-diffusion, watermarking, watermark-adapter, vae]
related: ["[[ci-2024-wmadapter]]", "[[latent-diffusion-watermarking]]", "[[watermark-robustness]]", "[[msat-ldm]]"]
created: 2026-07-16
updated: 2026-07-16
sources: ["Ci 等 - 2024 - WMAdapter Adding WaterMark Control to Latent Diffusion Models/full.md"]
---

# WMAdapter

WMAdapter is a contextual watermark adapter attached to a latent diffusion VAE decoder. It receives both watermark bits and VAE features, produces feature residuals, and supports dynamic message selection without retraining a decoder for each message.

Its hybrid finetuning trains the adapter with the VAE decoder but deploys it with the original VAE decoder to improve image quality while keeping the plug-in interface.

## Related Pages

- [[ci-2024-wmadapter]]
- [[latent-diffusion-watermarking]]
- [[msat-ldm]]
