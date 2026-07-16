---
type: concept
title: "Fourier Noise Watermarking"
created: 2026-06-09
updated: 2026-07-16
tags: [fourier-transform, diffusion-noise, watermarking, robustness]
related: ["[[tree-ring-watermark]]", "[[ddim-inversion-for-watermark-detection]]", "[[watermark-robustness]]", "[[latent-diffusion-watermarking]]", "[[generative-model-fingerprinting]]"]
sources: ["Wen 等 - 2023 - Tree-Ring Watermarks Fingerprints for Diffusion Images that are Invisible and Robust.pdf-009a7e2b-80bb-48a7-bf25-28b175fc8239/full.md"]
---

# Fourier Noise Watermarking

Fourier noise watermarking writes a watermark signal into the Fourier coefficients of a diffusion model's initial noise rather than into the final image or decoder weights. [[tree-ring-watermark]] represents this route in the wiki.

## Why Fourier Space

The Fourier transform has analyzable structural relationships with image transformations such as rotation, translation, cropping, and scaling. Tree-Ring places a key in a circular or ring-shaped mask so the detector can still recover it from estimated initial noise after common image transformations.

## Difference from Image Watermarking

Conventional Fourier image watermarking modifies frequency-domain coefficients of the final image. Fourier noise watermarking instead changes the initial noise before image formation. The output does not contain a simple post-hoc overlay; it retains statistical traces of a controlled sampling trajectory.

## Relation to Robustness

Tree-Ring experiments show strong AUC for the ring-shaped variant under many individual common image transformations. This is not absolute robustness: detection declines under combined attacks, and different key patterns have different weaknesses.
