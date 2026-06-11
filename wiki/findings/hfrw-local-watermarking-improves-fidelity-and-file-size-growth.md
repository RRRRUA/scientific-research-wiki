---
type: finding
title: "HFRW Local Watermarking Improves Fidelity and File Size Growth"
tags: [finding, hfrw, image-fidelity, file-size-growth, watermarking]
related: ["[[ping-2026-hfrw]]", "[[hfrw]]", "[[localized-invisible-watermarking]]", "[[watermark-robustness]]"]
created: 2026-06-11
updated: 2026-06-11
source: "[[ping-2026-hfrw]]"
confidence: high
replicated: false
---

# HFRW Local Watermarking Improves Fidelity and File Size Growth

## 发现

[[ping-2026-hfrw]] 报告 localized invisible watermarking 显著提高 image fidelity，并把 file size growth rate 降到接近可忽略，同时保持 30-bit message 的高 bit accuracy。

## 证据

Table I 报告 HFRW 在 Flickr30k、COCO、OpenImages 上的 PSNR 分别为 54.32、56.21、61.22，SSIM 分别为 0.9988、0.9991、0.9996，Bit Accuracy 均为 100，FSVR 分别为 0.31、0.27、0.17。Table II 的三数据集平均值为 PSNR 57.25、SSIM 0.9992、FSVR 0.25。

## 解释

这些结果支持一个重要对照：相比 global image watermarking，local patch embedding 可以把 fidelity 和 storage cost 做得很低。但这仍是 image-level post-hoc watermarking，不等同于 LDM 内部的 provenance / user attribution。
