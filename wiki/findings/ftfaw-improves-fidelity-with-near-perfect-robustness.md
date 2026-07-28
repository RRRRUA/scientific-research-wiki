---
type: finding
title: "FTFAW Improves Fidelity with Near-Perfect Reported Robustness"
tags: [finding, ftfaw, model-fingerprinting, image-quality, watermark-robustness]
related: ["[[ftfaw]]", "[[pan-2025-ftfaw]]", "[[kim-2024-wouaf]]", "[[watermark-robustness]]"]
created: 2026-07-20
updated: 2026-07-20
source: "[[pan-2025-ftfaw]]"
confidence: high
replicated: false
---

# FTFAW Improves Fidelity with Near-Perfect Reported Robustness

## Finding

FTFAW reports substantially higher image-fidelity metrics than WOUAF-Robust on Stable Diffusion v1.4 MS-COCO while retaining near-perfect clean and post-processing fingerprint recovery.

## Evidence

Table II reports FTFAW PSNR `35.19`, SSIM `0.944`, LPIPS `0.0220`, clean Bit Acc `0.9993`, attacked Bit Acc `0.9957`, and attacked TPR `0.9999` at 1% FPR. WOUAF-Robust reports PSNR `28.51`, SSIM `0.759`, LPIPS `0.0567`, clean Bit Acc `0.9997`, attacked Bit Acc `0.9987`, and attacked TPR `0.9993`.

## Interpretation

The table supports the paper's quality-focused optimization claim for this evaluation configuration. It does not show that FTFAW is more robust than WOUAF-Robust on every attack, because its attacked Bit Acc is slightly lower in the reported aggregate.
