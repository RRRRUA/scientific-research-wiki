---
type: entity
title: "HFRW"
aliases: ["High Fidelity and Robust Watermarking using Deep Reinforcement Learning"]
tags: [method, image-watermarking, deep-reinforcement-learning, local-watermarking]
related: ["[[ping-2026-hfrw]]", "[[post-hoc-image-watermarking]]", "[[localized-invisible-watermarking]]", "[[watermark-robustness]]", "[[hfrw-local-watermarking-improves-fidelity-and-file-size-growth]]", "[[hfrw-rl-patch-selection-improves-embedding-quality]]"]
created: 2026-06-11
updated: 2026-06-17
sources: ["HFRW_High_Fidelity_and_Robust_Watermarking_using_Deep_Reinforcement_Learning.pdf-1d97070b-78d6-4eb4-a7a0-f24fbfba014c/full.md"]
---

# HFRW

HFRW 是 [[ping-2026-hfrw]] 提出的 high-fidelity robust image watermarking framework。它将 watermark 嵌入局部 patch，而不是全图 global embedding，并用 deep reinforcement learning 选择嵌入位置。

## 组成

- Dueling DQN self-optimization module：选择局部 watermark embedding patch。
- CBAM-enhanced encoder / decoder：提高水印嵌入和提取质量。
- U2-Net localization and synchronization module：定位局部水印区域，并对 resize、padding、PIP 等几何变换进行同步。

## 与本 wiki 的关系

HFRW 属于 [[post-hoc-image-watermarking]]，不是 Latent Diffusion Models 的内部 watermarking 方法。它的价值在于提供一个外部对照：若把 watermark 嵌入局部区域，fidelity 和 file size growth rate 可以显著改善，但 severe cropping 会成为更直接的风险。
