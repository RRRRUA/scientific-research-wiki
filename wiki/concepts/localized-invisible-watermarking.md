---
type: concept
title: "Localized Invisible Watermarking"
tags: [image-watermarking, local-watermarking, fidelity, robustness]
related: ["[[hfrw]]", "[[ping-2026-hfrw]]", "[[post-hoc-image-watermarking]]", "[[watermark-robustness]]", "[[latent-diffusion-watermarking]]"]
created: 2026-06-11
updated: 2026-06-17
sources: ["HFRW_High_Fidelity_and_Robust_Watermarking_using_Deep_Reinforcement_Learning.pdf-1d97070b-78d6-4eb4-a7a0-f24fbfba014c/full.md"]
---

# Localized Invisible Watermarking

Localized invisible watermarking 是 [[post-hoc-image-watermarking]] 的一种局部嵌入策略：只在图像局部区域嵌入不可见 watermark。它试图结合 visible watermark 的低文件增长和 invisible watermark 的隐蔽性，同时避免 global invisible watermarking 对整张图像带来的质量损失。

## HFRW 的定义方式

[[ping-2026-hfrw]] 将 watermark embedding patch selection 建模为 MDP，并用 dueling DQN 选择 128x128 patch。该 patch 经过 encoder 嵌入 message，后续由 localization and synchronization module 找回，再交给 decoder 提取 watermark message。

## 主要收益

局部嵌入只修改图像的一小块区域，因此非嵌入区域保持原样。这能显著提高 PSNR / SSIM，并降低 file size variation rate (FSVR)，尤其适合大量高分辨率图像存储。

## 主要风险

局部嵌入的核心弱点是 severe cropping：如果攻击者删除或破坏嵌入 patch，watermark 可能无法恢复。HFRW 用图像内容自适应选择 patch 来降低位置可预测性，但不能消除这个 trade-off。
