---
type: entity
title: "Secure Distribution"
tags: [latent-diffusion, watermarking, anti-collusion, spectral-weight-modulation]
related: ["[[dai-2026-secure-distribution]]", "[[user-attribution]]", "[[watermark-robustness]]", "[[how-to-scale-user-attribution-for-ldm]]"]
created: 2026-07-16
updated: 2026-07-16
sources: ["Dai 等 - 2026 - Secure Distribution Anti-Collusion Watermarking via Spectral Weight Modulation in Latent Diffusion Models/full.md"]
---

# Secure Distribution

Secure Distribution is a diffusion-model watermarking framework that uses Lie-group LoRA for watermark embedding and Spectral Weight Modulation to create user-specific but functionally equivalent model parameters.

Its anti-collusion objective is to make merged copies lose usable image-generation quality when their watermarks become untraceable.

## Related Pages

- [[dai-2026-secure-distribution]]
- [[user-attribution]]
- [[watermark-robustness]]
