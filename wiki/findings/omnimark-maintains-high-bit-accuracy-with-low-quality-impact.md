---
type: finding
title: "OmniMark Maintains High Bit Accuracy with Low Quality Impact"
tags: [finding, omnimark, bit-accuracy, image-quality, watermark-robustness]
related: ["[[fei-2025-omnimark]]", "[[watermark-robustness]]", "[[generative-model-fingerprinting]]", "[[decoder-fingerprinting-scalability-comparison]]"]
created: 2026-06-09
updated: 2026-06-09
source: "[[fei-2025-omnimark]]"
confidence: high
replicated: false
---

# OmniMark Maintains High Bit Accuracy with Low Quality Impact

## 发现

[[fei-2025-omnimark]] 报告 OmniMark 在 48-bit fingerprints 下保持接近 99% 的 Bit Acc，同时对 image quality metrics 的影响较小。

## 证据

OmniMark raw parse 中，实验使用 SDv2.0、9 个 OmniMark Layers 和 48-bit fingerprints。Table 2 报告，在 CoCo、ImageNet、MagicBrush 上，Ours 的 Bit Acc 分别为 99.757、99.642、99.812。Model Fidelity 部分报告 OmniMark 平均 PSNR 约 31、SSIM 约 0.88、LPIPS 约 0.13，FID 相比 baseline 增加不到 1 点，CLIP score 基本不受影响。

## 解释

这个 finding 支持“多维 weight encoding 可以同时保持 fingerprint effectiveness 与 perceptual quality”的判断，也是 OmniMark 相比单一维度编码或 per-user fine-tuning 更有吸引力的原因。

## 注意

这些指标来自论文设置。它们不能直接证明在新模型架构、flow-matching models、LoRA fine-tuning 或强 collusion 场景下仍然成立。
