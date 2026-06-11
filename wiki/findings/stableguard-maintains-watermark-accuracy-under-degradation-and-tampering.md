---
type: finding
title: "StableGuard Maintains Watermark Accuracy under Degradation and Tampering"
tags: [finding, stableguard, watermark-robustness, bit-accuracy, image-degradation]
related: ["[[yang-2025-stableguard]]", "[[stableguard]]", "[[watermark-robustness]]"]
created: 2026-06-09
updated: 2026-06-09
source: "[[yang-2025-stableguard]]"
confidence: high
replicated: false
---

# StableGuard Maintains Watermark Accuracy under Degradation and Tampering

## 发现

[[yang-2025-stableguard]] 报告 StableGuard 的 watermark extraction 对 tampering ratio 和 common image degradations 保持较高 Bit Acc，但 tamper localization 的 F1 会比 bit extraction 更受压缩、降采样等退化影响。

## 证据

Table 8 报告在 AIGC tampering dataset 中，tampering ratio 从 10% 到 90% 时，StableGuard 的 watermark extraction accuracy 分别为 99.98、99.98、99.96、99.27、89.58，高于 EditGuard、OmniGuard 和 WAM。

Table 3 报告在 Gaussian noise、JPEG compression 和 Poisson noise 下，StableGuard 的 Bit Acc / F1 仍高于对比方法；例如 JPEG Q=70 时为 99.73 / 0.908。Table 11 的更强 real-world degradations 中，JPEG Q=30 时 StableGuard 为 98.87 / 0.866，WebP Q=50 时为 98.95 / 0.703。

## 注意

论文在 limitations 中明确指出，forensic accuracy 仍会因 image degradation 下降。因此这条 finding 不应理解为“水印不可移除”，而应理解为“在论文评估的退化范围内，bit extraction 比 localization 更稳健”。
