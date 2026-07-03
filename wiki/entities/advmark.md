---
type: entity
title: AdvMark
aliases: ["Decoupling Defense Strategies for Robust Image Watermarking"]
tags: [method, image-watermarking, robust-watermarking, adversarial-training, post-hoc-image-watermarking]
related: ["[[chen-2026-advmark]]", "[[post-hoc-image-watermarking]]", "[[watermark-robustness]]", "[[advmark-decoupled-training-preserves-clean-accuracy]]", "[[advmark-improves-quality-over-joint-training-baselines]]", "[[advmark-improves-comprehensive-robustness-against-advanced-attacks]]", "[[advmark-ablation-shows-two-defense-stages-are-complementary]]"]
created: 2026-06-17
updated: 2026-07-01
sources: ["Chen 等 - 2026 - Decoupling Defense Strategies for Robust Image Watermarking.pdf-8147032b-37f6-4091-8de2-a8ec3a76b5f6/full.md", "Chen 等 - 2026 - Decoupling Defense Strategies for Robust Image Watermarking.pdf-8147032b-37f6-4091-8de2-a8ec3a76b5f6/2e67c9e1-0e9f-47d0-b921-f7013c3073cd_origin.pdf"]
---

# AdvMark

AdvMark 是 [[chen-2026-advmark]] 在 2026 年提出的 robust post-hoc image watermarking method / two-stage robust image watermarking framework。它面向 ordinary image watermarking 和 [[post-hoc-image-watermarking]]，而不是 Latent Diffusion Models 内部的 provenance watermarking。

AdvMark 的核心思想是 decouple defense strategies：不同于把 encoder 和 decoder 联合训练到同时抵御所有攻击，它使用两个相互区分的防御阶段，分别处理 adversarial robustness 与 distortion / regeneration robustness。

## 方法结构

| 阶段 | 目标 | 机制 |
| --- | --- | --- |
| Stage 1 | 提升 adversarial robustness，同时保护 clean accuracy | encoder-focused adversarial fine-tuning |
| Stage 2 | 提升 distortion robustness 和 regeneration robustness | quality-aware direct image optimization |
| Quality-aware early stop | 控制图像质量下界 | 用 PSNR budget 替代传统 PGD epsilon-ball projection |

## Stage 1: Encoder-Focused Adversarial Fine-Tuning

第一阶段主要 fine-tune encoder 来获得 adversarial robustness。它使用 defender-tailored adversarial examples 训练 encoder，目标是把 watermarked image 移到 input space 中更稳定的区域，而不是激进地改变 decoder 的 decision boundary。

Decoder 不是始终同步更新，而是只在 adversarial bit accuracy 低于阈值时条件性更新。这样做的目的是保护 clean bit accuracy，避免为了抵御 adversarial examples 而过度牺牲无攻击条件下的解码准确率。

## Stage 2: Quality-Aware Direct Image Optimization

第二阶段直接优化 encoded image，以增强对 conventional distortions 和 regeneration attacks 的鲁棒性。

这一阶段的 loss 约束 optimized image 同时接近：

- 原始 cover image / original image
- Stage 1 产生的 encoded image

这种 constrained image loss 既限制图像质量退化，又帮助保留第一阶段获得的 adversarial robustness。

## 攻击与鲁棒性范围

AdvMark 强调 ordinary image watermarking 的 robustness 不能只看 JPEG、blur、noise 等 conventional distortions，还需要区分更强的攻击类型，包括：

- diffusion regeneration attacks
- WEvade
- Black-Q
- Black-S
- 其他 adversarial attacks

因此，AdvMark 是 [[watermark-robustness]] 中 advanced-attack benchmark 的重要对照案例。

## 与本 wiki 的关系

AdvMark 是 [[post-hoc-image-watermarking]] 的 strong comparator。它不直接解决 Latent Diffusion Models 中可扩展的 [[user-attribution]] 问题，也不回答 model-copy fingerprinting 问题。

它对本 wiki 的主要价值在于扩展 robustness 分析框架：AdvMark 显示，水印鲁棒性可以通过分离防御目标来改进，并帮助本项目为 [[watermark-robustness]] 建立更细的攻击分类和 benchmark 维度。
