---
type: finding
title: "WOUAF Decoder-Only Modulation Preserves Quality Better"
tags: [finding, wouaf, decoder, image-quality, weight-modulation]
related: ["[[kim-2024-wouaf]]", "[[latent-diffusion-watermarking]]", "[[generative-model-fingerprinting]]", "[[decoder-fingerprinting-scalability-comparison]]"]
created: 2026-06-09
updated: 2026-07-16
source: "[[kim-2024-wouaf]]"
confidence: high
replicated: false
---

# WOUAF Decoder-Only Modulation Preserves Quality Better

## Finding

The experiments in [[kim-2024-wouaf]] support decoder-only modulation instead of modulating both the denoising U-Net and decoder.

## Evidence

WOUAF embeds fingerprints only in Stable Diffusion decoder weights. Section 4.5 reports that the variant modulating both diffusion model `epsilon_theta` and decoder D cannot optimize attribution accuracy and generation quality together: its best attribution accuracy is 89%, CLIP score 0.68, and FID 63.48. Decoder-only WOUAF-conv/WOUAF-all maintain 0.99 attribution accuracy in Table 1 with CLIP/FID close to Original SD.

## Interpretation

This reinforces a cross-paper pattern: the LDM decoder is a high-value site for provenance embedding because it directly affects final pixels without perturbing the full diffusion process.

## Caveat

This does not mean the decoder is always the only valid site. A stronger white-box attacker can replace, distill, or retrain it, and those attacks require separate modeling.
