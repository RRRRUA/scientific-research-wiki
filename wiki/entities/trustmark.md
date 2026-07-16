---
type: entity
title: "TrustMark"
aliases: ["TrustMark-RM", "TrustMark: Universal Watermarking for Arbitrary Resolution Images"]
tags: [method, image-watermarking, post-hoc-image-watermarking, arbitrary-resolution, watermark-removal]
related: ["[[bui-2023-trustmark]]", "[[post-hoc-image-watermarking]]", "[[arbitrary-resolution-image-watermarking]]", "[[watermark-robustness]]", "[[trustmark-achieves-high-quality-watermarking-on-arbitrary-resolution-benchmarks]]", "[[trustmark-noise-simulation-improves-robustness-across-perturbations]]", "[[trustmark-rm-supports-high-quality-re-watermarking]]"]
created: 2026-07-06
updated: 2026-07-06
sources: ["Bui 等 - 2023 - TrustMark Universal Watermarking for Arbitrary Resolution Images.pdf-28de830f-aa55-4f9a-b0ee-83e4bffaa789/full.md"]
---

# TrustMark

TrustMark is the GAN-based post-hoc image watermarking method introduced by [[bui-2023-trustmark]]. It targets arbitrary-resolution image assets rather than diffusion-native provenance or model-copy attribution.

## Components

- Embedder: early image-watermark fusion, a customized MUNIT-based body, and a post-process module based on `1 x 1` convolutions.
- Extractor: ResNet50 with a sigmoid output layer for recovering an `l`-bit watermark.
- Noise module: differentiable simulation of geometric transforms and diverse photometric/noise perturbations.
- Resolution scaling: fixed-resolution inference that computes residuals at `256 x 256`, scales them to the original image size, and adds them back to the original-resolution image.
- TrustMark-RM: a KBNet-based watermark remover trained to reconstruct cover images and enable cleaner re-watermarking.

## Role in This Wiki

TrustMark is a post-hoc comparator for arbitrary-resolution deployment and re-watermarking workflows. It complements hfrw, which studies local patch watermarking for high fidelity and low file-size growth, and [[advmark]], which studies decoupled defenses against distortion, regeneration, and adversarial attacks.

## Boundary

TrustMark can carry a provenance identifier inside image content, but it does not by itself solve scalable [[user-attribution]], model-copy fingerprinting, or diffusion-native provenance binding.
