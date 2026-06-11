---
type: finding
title: "HFRW Localized Embedding Trades Cropping Robustness for Fidelity"
tags: [finding, hfrw, watermark-robustness, cropping, tradeoff]
related: ["[[ping-2026-hfrw]]", "[[hfrw]]", "[[localized-invisible-watermarking]]", "[[watermark-robustness]]"]
created: 2026-06-11
updated: 2026-06-11
source: "[[ping-2026-hfrw]]"
confidence: high
replicated: false
---

# HFRW Localized Embedding Trades Cropping Robustness for Fidelity

## 发现

HFRW 在 JPEG、color jitter、Gaussian noise、Gaussian blur、resize、padding、PIP 等常见攻击下保持较高 bit accuracy，但 localized embedding 对 severe cropping 有固有弱点。

## 证据

Fig. 7 报告 HFRW 在 JPEG quality 60-90 下约 92-99，在 color jitter 和 Gaussian noise 下接近 100，在 resize 和 padding 下接近 100，在 PIP scale factor 1.4-2.0 下约 92-98。Crop attack 下随着 crop ratio 增加，HFRW 从 0.05 时约 98 下降到 0.35 时约 84。

论文的 robustness discussion 明确解释：HFRW 的 watermark 嵌入在 128x128 patch 中，如果该区域被完全移除，无论 decoder 能力如何都无法恢复 watermark。结论部分也承认 severe cropping 是 localized embedding strategy 的限制。

## 解释

这条 finding 把 HFRW 的优势边界说清楚：local watermarking 换来了极高 fidelity 和低 FSVR，但对“直接删除嵌入区域”的攻击不如全局分布式水印自然稳健。
