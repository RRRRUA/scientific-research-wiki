---
type: finding
title: "AdvMark Ablation Shows Two Defense Stages Are Complementary"
tags: [finding, advmark, ablation-study, watermark-robustness, image-optimization]
related: ["[[chen-2026-advmark]]", "[[advmark]]", "[[post-hoc-image-watermarking]]", "[[watermark-robustness]]"]
created: 2026-06-17
updated: 2026-06-17
source: "[[chen-2026-advmark]]"
confidence: high
replicated: false
---

# AdvMark Ablation Shows Two Defense Stages Are Complementary

## 发现

[[chen-2026-advmark]] 的 ablation 显示，Stage 1 主要贡献 adversarial robustness，Stage 2 主要恢复 distortion / regeneration robustness；缺任一阶段都会破坏 comprehensive robustness。

## 证据

Table 3 中，完整 AdvMark 的 PSNR 为 37.0，JPEG/combined distortion/Regen-SD-V1-4/Regen-SD-V1-5/WEvade 为 0.99/0.83/0.87/0.87/0.98。去掉 Stage 1 后，PSNR 降到 34.7，WEvade 降到 0.50。去掉 Stage 2 后，JPEG 降到 0.88，combined distortion 降到 0.65，Regen-SD-V1-4/1-5 降到 0.54/0.54，但 WEvade 仍为 0.99。

## 解释

这个结果支持 AdvMark 的 decoupling 设计：adversarial robustness 和 regeneration/distortion robustness 不是同一个优化问题。把所有攻击同时放进 joint training 可能损害 clean accuracy，而完全依赖 Stage 1 又不能覆盖 conventional distortions 和 regeneration。
