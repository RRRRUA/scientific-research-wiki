---
type: concept
title: "Tamper Localization for Generated Images"
tags: [tamper-localization, image-forensics, watermarking, generated-images]
related: ["[[stableguard]]", "[[yang-2025-stableguard]]", "[[editguard]]", "[[omniguard]]", "[[watermark-anything]]", "[[genptw]]", "[[robin-plus-plus]]", "[[watermark-robustness]]", "[[watermark-verification-operands]]", "[[latent-diffusion-watermarking]]", "[[localized-watermarking-for-tamper-localization-comparison]]"]
created: 2026-06-11
updated: 2026-09-08
sources: ["Yang 等 - 2025 - StableGuard Towards Unified Copyright Protection and Tamper Localization in Latent Diffusion Model.pdf-d8a32816-0fa0-4c8d-934e-e96205ef30ed/full.md", "Gan 等 - 2026 - GenPTW Latent Image Watermarking for Provenance Tracing and Tamper Localization/full.md", "Huang 等 - 2026 - ROBIN++ Unified Copyright Protection and Tamper Localization for Diffusion Models Via Dual-Domain S/full.md"]
---

# Tamper Localization for Generated Images

Tamper localization for generated images identifies regions of a generated image modified by splicing, inpainting, copy-paste, removal, or other editing methods. It is more granular than generated-image detection because it must produce a tampered-region mask in addition to determining provenance.

## Two Routes

- Passive localization infers modified regions from visual or statistical anomalies in the image itself. It often requires paired supervision and can generalize poorly to new AIGC editing methods.
- Proactive localization embeds an auxiliary signal during generation or publication and later localizes modifications through missing or anomalous signal regions.

[[yang-2025-stableguard]] follows the proactive route. MPW-VAE embeds a holistic watermark during generation, and MoE-GFN jointly recovers the copyright signal and tamper mask from the watermark pattern, local traces, and boundary cues.

[[zhang-2023-editguard]] and [[zhang-2025-omniguard]] apply proactive dual watermarking to image assets: a robust copyright signal is paired with a semi-fragile spatial signal. EditGuard compares a recovered spatial tag with the pre-embedded tag; OmniGuard instead learns a degradation-aware mask extractor from the received image and reconstructed-tag artifacts. [[sander-2025-watermark-anything]] is adjacent rather than identical: it locates watermarked regions and messages, which can support splicing-aware provenance without directly asserting a tamper mask.

[[gan-2026-genptw]] uses one latent message with semantic and spatial fusion, then shares features between message recovery and mask prediction. [[huang-2026-robin-plus-plus]] instead injects two function-specific signals into separated frequency bands and exchanges evidence only during verification. The former tests a unified payload path; the latter tests decoupled injection with synergistic decoding.

## Relation to Watermarking

Watermarking usually asks whether an image came from a model or key. Tamper localization asks which regions no longer conform to the watermark pattern. StableGuard assumes that a holistic watermark is sufficiently distributed in space that local tampering disrupts local watermark cues, making missing watermark features useful for localization.

For dual-watermark methods, the local signal should be semi-fragile while the copyright signal remains robust. Evaluations therefore need separate recovery, mask, degradation, and AIGC-editing measures rather than one aggregate watermark score.

ROBIN++ adds a further operand warning: its copyright `Bit Accuracy` is zero-bit classification accuracy, whereas GenPTW reports multi-bit message recovery. Neither is interchangeable with localization F1, AUC, or IoU; see [[watermark-verification-operands]].

## Limitations

This approach assumes that the original image was watermarked during generation. Localization results require careful interpretation for unwatermarked images, images from other models, or images subjected to severe compression or downsampling.
