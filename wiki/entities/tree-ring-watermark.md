---
type: entity
title: "Tree-Ring Watermarking"
aliases: ["Tree-Ring Watermarks"]
tags: [method, watermarking, diffusion-models, ddim-inversion, fourier-noise]
related: ["[[wen-2023-tree-ring-watermarks]]", "[[latent-diffusion-watermarking]]", "[[watermark-robustness]]", "[[generative-model-fingerprinting]]", "[[ddim-inversion-for-watermark-detection]]", "[[fourier-noise-watermarking]]", "[[private-vs-public-watermark-verification]]", "[[watermark-capacity-for-user-attribution]]"]
created: 2026-06-09
updated: 2026-07-16
sources: ["Wen 等 - 2023 - Tree-Ring Watermarks Fingerprints for Diffusion Images that are Invisible and Robust.pdf-009a7e2b-80bb-48a7-bf25-28b175fc8239/full.md"]
---

# Tree-Ring Watermarking

Tree-Ring Watermarking is a diffusion image watermarking method introduced by [[wen-2023-tree-ring-watermarks]]. It embeds a secret key in the initial noise vector used for diffusion sampling instead of modifying generated-image pixels or fine-tuning the decoder.

## Core Mechanism

Before sampling, the method transforms the initial noise into Fourier space and writes a key pattern inside a predefined mask. During detection, the model owner runs [[ddim-inversion-for-watermark-detection]] on a candidate image, approximately recovers the initial noise, and checks whether its Fourier coefficients match the secret key.

Tree-Ring's ring-shaped key pattern exploits structural properties of transformations such as rotation in the Fourier domain to improve robustness to common image transformations.

## Role in This Project

Tree-Ring Watermarking broadens the [[latent-diffusion-watermarking]] lineage by showing that a watermark can be rooted in the sampling process rather than in the decoder or model weights. It differs from decoder-rooted [[stable-signature]] and from [[wouaf]] and [[omnimark]], which target user-specific model copies more directly.

## Key Properties

- Does not apply post-hoc modifications to the final image.
- Does not require retraining the diffusion model.
- Detection generally depends on DDIM inversion performed by the model owner, making it closer to private verification.
- Better suited to generated-image detection and provenance; scalability to large-scale [[user-attribution]] is not established.

## Limitations

- Requires compatible sampling and inversion procedures.
- Under combined image transformations, true positive rate drops substantially at low false positive rate.
- Multi-key capacity remains open, so the method cannot directly replace the user-attribution goals of WOUAF or OmniMark.
