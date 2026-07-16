---
type: concept
title: "Arbitrary-resolution Image Watermarking"
tags: [image-watermarking, arbitrary-resolution, post-hoc-watermarking, image-fidelity]
related: ["[[trustmark]]", "[[bui-2023-trustmark]]", "[[post-hoc-image-watermarking]]", "hfrw", "[[watermark-robustness]]"]
created: 2026-07-06
updated: 2026-07-06
sources: ["Bui 等 - 2023 - TrustMark Universal Watermarking for Arbitrary Resolution Images.pdf-28de830f-aa55-4f9a-b0ee-83e4bffaa789/full.md"]
---

# Arbitrary-resolution Image Watermarking

Arbitrary-resolution image watermarking means embedding and extracting watermarks while preserving the original image resolution, rather than forcing all inputs through a fixed small model resolution.

## Why It Matters

Creative and provenance workflows often involve high-resolution images. If a watermarking model only operates at about `200 x 200` or `256 x 256`, evaluating it at model-designed resolution can overstate quality and hide the cost of scaling back to the original asset size.

## TrustMark's Approach

[[bui-2023-trustmark]] proposes residual-based resolution scaling. The model first runs at `256 x 256`, computes the watermark or removal residual, interpolates that residual to the original `H x W`, and adds it to the original-resolution image. The paper reports near-equivalent performance across DIV2K resolution variants, with encoding PSNR varying by only `+-0.02 dB` and decoding bit accuracy by only `+-1e-4` on average.

## Relation to HFRW

ping-2026-hfrw also targets high-resolution image watermarking, but it does so by embedding into a selected local patch. TrustMark instead keeps the watermarking model fixed-resolution and scales residuals across the full image. These are different responses to the same deployment pressure: ordinary images are often much larger than the neural watermarking model's native resolution.

## Caveats

Arbitrary-resolution support is not the same as diffusion-native provenance. It improves practical deployment for image assets, but it does not identify the generator, user, or model copy unless the surrounding system binds the payload to those records.
