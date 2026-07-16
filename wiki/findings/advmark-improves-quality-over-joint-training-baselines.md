---
type: finding
title: "AdvMark Improves Quality over Joint-training Baselines"
tags: [finding, advmark, image-fidelity, psnr, watermarking]
related: ["[[chen-2026-advmark]]", "[[advmark]]", "[[post-hoc-image-watermarking]]", "[[watermark-robustness]]"]
created: 2026-06-17
updated: 2026-07-16
source: "[[chen-2026-advmark]]"
confidence: high
replicated: false
---

# AdvMark Improves Quality over Joint-training Baselines

## Finding

[[chen-2026-advmark]] reports that AdvMark maintains strong PSNR, SSIM, and LPIPS across multiple message lengths and image sizes, outperforming MBRS, Stable Signature, PIMoG, DADW, StegaStamp, EditGuard, and VINE in the same table.

## Evidence

In Table 1, under the 128x128, 30-bit setting on MS-COCO, AdvMark reaches PSNR 37.0, SSIM 0.99, and LPIPS 0.01; MBRS reaches 32.1/0.95/0.09 and DADW 33.4/0.98/0.05. Under the 256x256, 100-bit setting, AdvMark reaches 38.9/0.99/0.01 on MS-COCO and 38.8/0.99/0.01 on DiffusionDB.

## Caveat

These metrics show that AdvMark balances visual quality and robustness in the paper's setting, but it still requires per-image optimization. PSNR should therefore be considered together with encoding overhead and attack coverage.
