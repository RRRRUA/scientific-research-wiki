---
type: finding
title: "StableGuard MPW-VAE Enables Self-Supervised Tamper Training"
tags: [finding, stableguard, mpw-vae, self-supervised-learning, tamper-localization]
related: ["[[yang-2025-stableguard]]", "[[stableguard]]", "[[tamper-localization-for-generated-images]]"]
created: 2026-06-09
updated: 2026-06-09
source: "[[yang-2025-stableguard]]"
confidence: high
replicated: false
---

# StableGuard MPW-VAE Enables Self-Supervised Tamper Training

## 发现

StableGuard 的 MPW-VAE 可以从同一 latent code 生成 watermarked / watermark-free paired images，再用 random 或 SAM-generated masks 合成 tampering samples，因此 MoE-GFN 不需要人工篡改标注即可训练。

## 证据

论文方法部分说明 MPW-VAE 的 watermark adapter 可开关，并用 paired samples 通过 random masks 或 semantic masks 构造 training images。Table 4 的 ablation 显示，去掉 MPW-VAE 后 F1/AUC/IoU 为 0.811/0.796/0.774；完整 decoder placement 版本为 0.980/0.992/0.961，Bit Acc 为 99.98。

## 解释

这条结果支持“watermark embedding 与 forensic detector 应联合设计”的判断。StableGuard 相比 post-hoc unified methods 的关键差异，是把生成时的水印机制和后续定位网络放在同一个 self-supervised loop 中优化。
