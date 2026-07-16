---
type: source
title: "Tree-Ring Watermarks: Fingerprints for Diffusion Images that are Invisible and Robust"
tags: [diffusion-models, watermarking, tree-ring-watermarking, ddim-inversion, image-provenance, generative-ai-safety]
related: ["[[tree-ring-watermark]]", "[[latent-diffusion-watermarking]]", "[[watermark-robustness]]", "[[generative-model-fingerprinting]]", "[[diffusion-model-fingerprinting-comparison]]"]
created: 2026-06-09
updated: 2026-07-16
authors: ["Yuxin Wen", "John Kirchenbauer", "Jonas Geiping", "Tom Goldstein"]
year: 2023
url: "https://github.com/YuxinWenRick/tree-ring-watermark"
venue: "arXiv:2305.20030"
---

# Tree-Ring Watermarks: Fingerprints for Diffusion Images that are Invisible and Robust

## One-sentence Summary

Tree-Ring Watermarking embeds a pattern in the Fourier space of the initial noise vector used for diffusion sampling instead of modifying pixels after generation. Detection approximately recovers the initial noise through DDIM inversion and checks for a predefined key.

## Problem

Post-hoc image watermarking modifies an existing image and is easy to remove in open-source or editable-image settings. The paper asks whether diffusion-model outputs can carry an invisible watermark robust to common image transformations without reducing generation quality or training a new model.

## Method

During generation, Tree-Ring Watermarking selects a special initial noise `x_T`. Its Fourier transform contains a key pattern inside a low-frequency circular mask `M`. The paper studies `Tree-Ring_Zeros`, `Tree-Ring_Rand`, and `Tree-Ring_Rings`; the rings pattern is more robust to transformations such as rotation while still supporting multiple random keys.

During detection, the model owner applies DDIM inversion to a candidate image to estimate the initial noise `x'_T`, then computes the distance between that noise and the key in Fourier space. A noncentral chi-square distribution produces a P-value for threshold-based false-positive control.

## Evidence

The paper evaluates Stable Diffusion v2 and a 256x256 ImageNet diffusion model using AUC, TPR@1%FPR, FID, and CLIP Score. Table 1 reports AUC/T@1%F near 1.000/1.000 for Tree-Ring variants in the clean Stable Diffusion setting. Under adversarial transformations, `Tree-Ring_Rings` reaches AUC 0.975, above the average adversarial AUC of DwtDct, DwtDctSvd, and RivaGAN. The paper also reports negligible FID impact from `Tree-Ring_Rand` and `Tree-Ring_Rings` and essentially unchanged CLIP Score.

Robustness evaluation covers rotation, JPEG compression, cropping and scaling, Gaussian blur, Gaussian noise, and color jitter. `Tree-Ring_Rings` has the best average performance, while different key patterns have distinct weaknesses: `Tree-Ring_Rand` performs poorly under rotation, and `Tree-Ring_Zeros` is weaker against Gaussian noise and color jitter.

## Limitations and Caveats

- The method depends on DDIM sampling and DDIM inversion and must be adapted when sampling changes.
- Verification requires the model parameters and watermarking algorithm held by the model owner, so third parties need an API.
- Multi-key capacity is unclear; assigning a unique key to each API user remains an explicit future question.
- The method is better suited to generated-image detection and provenance than to model-copy user attribution targeted by WOUAF and OmniMark.

## Use in This Project

This paper broadens the design space beyond decoder-rooted watermarking and decoder-weight fingerprinting to a noise-space and sampling-process route. It is useful for comparing the deployment boundaries of post-hoc watermarking, decoder-rooted watermarking, weight-modulated fingerprinting, and initial-noise watermarking.

## Original Sources

- `raw/sources/Wen 等 - 2023 - Tree-Ring Watermarks Fingerprints for Diffusion Images that are Invisible and Robust.pdf-009a7e2b-80bb-48a7-bf25-28b175fc8239/full.md`

## Related Pages

- [[tree-ring-watermark]]
- [[latent-diffusion-watermarking]]
- [[watermark-robustness]]
- [[generative-model-fingerprinting]]
- [[diffusion-model-fingerprinting-comparison]]
