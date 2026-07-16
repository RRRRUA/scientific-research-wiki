---
type: concept
title: "Post-hoc Image Watermarking"
tags: [image-watermarking, post-hoc-watermarking, watermark-robustness, copyright-protection]
related: ["[[advmark]]", "[[trustmark]]", "[[hfrw]]", "[[watermark-anything]]", "[[editguard]]", "[[omniguard]]", "[[chen-2026-advmark]]", "[[bui-2023-trustmark]]", "[[ping-2026-hfrw]]", "[[sander-2025-watermark-anything]]", "[[zhang-2023-editguard]]", "[[zhang-2025-omniguard]]", "[[localized-invisible-watermarking]]", "[[arbitrary-resolution-image-watermarking]]", "[[watermark-robustness]]", "[[latent-diffusion-watermarking]]"]
created: 2026-06-17
updated: 2026-07-06
sources: ["Chen 等 - 2026 - Decoupling Defense Strategies for Robust Image Watermarking.pdf-8147032b-37f6-4091-8de2-a8ec3a76b5f6/full.md", "Bui 等 - 2023 - TrustMark Universal Watermarking for Arbitrary Resolution Images.pdf-28de830f-aa55-4f9a-b0ee-83e4bffaa789/full.md"]
---

# Post-hoc Image Watermarking

Post-hoc image watermarking embeds a watermark after an image already exists, usually in pixel space through an encoder, local patch embedding, residual scaling, or image optimization. It differs from [[latent-diffusion-watermarking]], where the provenance signal is rooted inside the generation workflow, such as the decoder, initial noise, or model weights.

## Current Routes in the Corpus

ping-2026-hfrw represents localized invisible watermarking. It embeds only in a selected local patch to reduce whole-image distortion and file size growth.

[[chen-2026-advmark]] represents advanced-attack-oriented robust watermarking. It does not focus on local embedding; instead, it separates adversarial defense from distortion and regeneration defense.

[[bui-2023-trustmark]] represents arbitrary-resolution asset watermarking. It uses a fixed-resolution neural watermarking model, residual-based resolution scaling, and TrustMark-RM for watermark removal and re-watermarking workflows.

## Evaluation Dimensions

Post-hoc image watermarking usually emphasizes PSNR, SSIM, LPIPS, file size growth, bit accuracy, payload size, image post-processing robustness, and deployment cost. AdvMark adds diffusion regeneration and adversarial removal to this evaluation frame. TrustMark adds arbitrary-resolution behavior and re-watermarking quality.

## Boundary with Diffusion-native Methods

Post-hoc image watermarking can protect ordinary images and can also be applied to generated images after generation. By itself, however, it usually cannot prove that an image came from a specific model copy or solve large-scale [[user-attribution]]. It is therefore an external comparator for LDM provenance rather than a replacement for [[stable-signature]], [[tree-ring-watermark]], [[wouaf]], [[omnimark]], or [[stableguard]].
