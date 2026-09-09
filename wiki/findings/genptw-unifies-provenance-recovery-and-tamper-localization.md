---
type: finding
title: "GenPTW Unifies Provenance Recovery and Tamper Localization"
tags: [finding, genptw, provenance, tamper-localization, latent-watermarking]
related: ["[[gan-2026-genptw]]", "[[genptw]]", "[[tamper-localization-for-generated-images]]", "[[localized-watermarking-for-tamper-localization-comparison]]"]
created: 2026-09-08
updated: 2026-09-08
source: "[[gan-2026-genptw]]"
confidence: high
replicated: false
---

# GenPTW Unifies Provenance Recovery and Tamper Localization

## Finding

GenPTW reports that one latent embedding can support both 64-bit message recovery and dense tamper-mask prediction in in-generation and post-hoc pipelines.

## Evidence

For in-generation Stable Diffusion outputs, Table 1 reports F1/AUC `0.973/0.996` under SD inpainting, `0.965/0.993` for splicing, and `0.976/0.997` for LaMa. Table 2 reports PSNR `39.56 dB` and raw bit accuracy from `0.969` to `1.000` across its listed global edits, local edits, and common degradations.

## Interpretation

The watermark supplies active spatial evidence rather than relying only on passive forensic traces. The work does not show multi-user global false-positive control, and its cross-architecture results use separately trained variants.

