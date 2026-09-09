---
type: source
title: "GenPTW: Latent Image Watermarking for Provenance Tracing and Tamper Localization"
tags: [latent-watermarking, provenance, tamper-localization, in-generation, post-hoc]
related: ["[[genptw]]", "[[tamper-localization-for-generated-images]]", "[[latent-diffusion-watermarking]]", "[[localized-watermarking-for-tamper-localization-comparison]]", "[[genptw-unifies-provenance-recovery-and-tamper-localization]]"]
created: 2026-09-08
updated: 2026-09-08
authors: ["Zhenliang Gan", "Chunya Liu", "Yichao Tang", "Binghao Wang", "Shiwen Cui", "Weiqiang Wang", "Xinpeng Zhang"]
year: 2026
url: ""
venue: ""
sources: ["Gan 等 - 2026 - GenPTW Latent Image Watermarking for Provenance Tracing and Tamper Localization/full.md"]
---

# GenPTW: Latent Image Watermarking for Provenance Tracing and Tamper Localization

## One-line Takeaway

[[genptw]] uses a single latent-space embedding path with semantic cross-attention and explicit spatial fusion to recover a message and predict a tamper mask in both in-generation and post-hoc settings.

## Method

Cross-Attention Fusion adapts watermark injection to latent semantics, while Spatial Fusion expands the same message into full-resolution spatial guidance. A shared tamper-aware extractor combines watermark features with DCT high-frequency features. JND, MSE, and LPIPS losses constrain visible perturbation.

## Evidence

On AI-generated images, Table 1 reports F1/AUC of `0.973/0.996` for Stable Diffusion inpainting, `0.965/0.993` for splicing, and `0.976/0.997` for LaMa. Table 2 reports `39.56 dB` PSNR for the 64-bit in-generation variant, with raw recovery from `0.969` to `1.000` across the listed global edits, local edits, and degradations.

The paper trains separate GenPTW variants for VAR, DiT, and SDXL. Under SD inpainting, Table 3 reports F1 from `0.945` to `0.989` and AUC from `0.991` to `0.999` across those variants.

## Limitations and Caveats

- The cross-architecture table reflects separately trained models, not zero-shot transfer of one trained watermark module.
- Message recovery supports provenance verification, but the parse does not provide a multi-user attribution protocol or platform-level false-positive study.
- The post-hoc and in-generation rows use different image populations; their quality and robustness values should not be treated as a paired head-to-head comparison.
- Full-image semantic rewriting is intentionally flagged as broadly tampered, which favors integrity sensitivity over edit-tolerant localization.
- Venue, DOI, and code URL are not present in the parse.

## Raw Source

- `raw/sources/Gan 等 - 2026 - GenPTW Latent Image Watermarking for Provenance Tracing and Tamper Localization/full.md`

