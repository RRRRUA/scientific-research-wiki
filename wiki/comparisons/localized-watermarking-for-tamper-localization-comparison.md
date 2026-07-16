---
type: comparison
title: "Localized Watermarking for Tamper Localization Comparison"
tags: [comparison, localized-watermarking, tamper-localization, proactive-forensics, image-watermarking]
related: ["[[ping-2026-hfrw]]", "[[sander-2025-watermark-anything]]", "[[zhang-2023-editguard]]", "[[zhang-2025-omniguard]]", "[[tamper-localization-for-generated-images]]", "[[localized-invisible-watermarking]]"]
created: 2026-07-16
updated: 2026-07-16
sources: ["Ping 等 - 2026 - HFRW High Fidelity and Robust Watermarking using Deep Reinforcement Learning/full.md", "Sander 等 - 2025 - Watermark Anything with Localized Messages/full.md", "Zhang 等 - 2023 - EditGuard Versatile image watermarking for tamper localization and copyright protection/full.md", "Zhang 等 - 2025 - OmniGuard Hybrid Manipulation Localization via Augmented Versatile Deep Image Watermarking/full.md"]
---

# Localized Watermarking for Tamper Localization Comparison

## Comparison

| Method | Spatial signal | Primary task | Reported strength | Main boundary |
| --- | --- | --- | --- | --- |
| [[hfrw]] | One RL-selected local patch | Asset traceability with high fidelity | High PSNR and low file-size growth | Cropping can remove the local evidence; no tamper mask objective |
| [[watermark-anything]] | Pixel-level watermarked-area mask and local message bits | Localized messages, detection, and splicing-aware provenance | Several small regions can carry distinct messages | Missing watermark evidence is not automatically a tamper decision |
| [[editguard]] | Semi-fragile spatial tag plus robust copyright bits | Proactive tamper localization and copyright recovery | Zero-shot localization design without tampered training samples | Fixed tag and residual masks degrade under severe distortions |
| [[omniguard]] | Adaptive spatial tag plus artifact map and learned mask extractor | Degradation-robust localization and copyright recovery | Improves EditGuard under reported JPEG and brightness conditions | Very severe degradation reduces the benefit of proactive evidence |

## Synthesis

These methods use locality for different reasons. HFRW localizes embedding to preserve fidelity; WAM localizes detection and messages to distinguish several watermarked regions; EditGuard and OmniGuard localize a semi-fragile signal to infer edits. Their shared vocabulary should not hide those different decision rules.

## Evaluation Implications

Image quality and bit accuracy are not enough. A comparison should also state the minimum protected surface, crop conditions, whether local evidence is a direct watermark mask or an inferred tamper mask, and robustness to ordinary degradation separately from AIGC editing.
