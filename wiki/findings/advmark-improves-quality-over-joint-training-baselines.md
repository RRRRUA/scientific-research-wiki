---
type: finding
title: "AdvMark Improves Quality over Joint-training Baselines"
tags: [finding, advmark, image-fidelity, psnr, watermarking]
related: ["[[chen-2026-advmark]]", "[[advmark]]", "[[post-hoc-image-watermarking]]", "[[watermark-robustness]]"]
created: 2026-06-17
updated: 2026-06-17
source: "[[chen-2026-advmark]]"
confidence: high
replicated: false
---

# AdvMark Improves Quality over Joint-training Baselines

## 发现

[[chen-2026-advmark]] 报告 AdvMark 在多个 message length 和 image size 设置下保持较高 PSNR / SSIM / LPIPS，优于同表中的 MBRS、Stable Signature、PIMoG、DADW、StegaStamp、EditGuard 和 VINE 等 baselines。

## 证据

Table 1 中，128x128、30-bit 设置下 AdvMark 在 MS-COCO 上为 PSNR 37.0、SSIM 0.99、LPIPS 0.01；MBRS 为 32.1、0.95、0.09，DADW 为 33.4、0.98、0.05。AdvMark 在 256x256、100-bit 设置下达到 MS-COCO PSNR 38.9、SSIM 0.99、LPIPS 0.01，DiffusionDB PSNR 38.8、SSIM 0.99、LPIPS 0.01。

## 注意

这些指标说明 AdvMark 在论文设置中兼顾 visual quality 和 robustness，但它仍需要 per-image optimization；因此不能只看 PSNR，还要同时比较 encoding overhead 和攻击覆盖范围。
