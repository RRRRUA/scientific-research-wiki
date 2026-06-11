---
type: entity
title: "Tree-Ring Watermarking"
aliases: ["Tree-Ring Watermarks"]
tags: [method, watermarking, diffusion-models, ddim-inversion, fourier-noise]
related: ["[[wen-2023-tree-ring-watermarks]]", "[[latent-diffusion-watermarking]]", "[[watermark-robustness]]", "[[generative-model-fingerprinting]]", "[[ddim-inversion-for-watermark-detection]]", "[[fourier-noise-watermarking]]", "[[private-vs-public-watermark-verification]]", "[[watermark-capacity-for-user-attribution]]"]
created: 2026-06-09
updated: 2026-06-09
sources: ["Wen 等 - 2023 - Tree-Ring Watermarks Fingerprints for Diffusion Images that are Invisible and Robust.pdf-009a7e2b-80bb-48a7-bf25-28b175fc8239/full.md"]
---

# Tree-Ring Watermarking

Tree-Ring Watermarking 是 [[wen-2023-tree-ring-watermarks]] 提出的 diffusion image watermarking 方法。它把秘密 key 嵌入 diffusion sampling 的初始 noise vector，而不是修改生成后的 image pixels，也不需要 fine-tune decoder。

## 核心机制

方法在 sampling 开始前把初始 noise 转换到 Fourier space，并在预设 mask 中写入 key pattern。检测时，model owner 对待测图像执行 [[ddim-inversion-for-watermark-detection]]，近似恢复初始 noise，再检查 Fourier coefficients 是否匹配 secret key。

Tree-Ring 的 ring-shaped key pattern 试图利用 Fourier domain 对 rotation 等变换的结构性质，从而提升对常见 image transformations 的鲁棒性。

## 与本项目的关系

Tree-Ring Watermarking 扩展了 [[latent-diffusion-watermarking]] 的方法谱系：watermark 可以根植于 sampling process，而不一定要根植于 decoder 或 model weights。它不同于 [[stable-signature]] 的 decoder-rooted watermarking，也不同于 [[wouaf]]、[[omnimark]] 这类更面向 user-specific model copies 的路线。

## 关键性质

- 不对最终图像做 post-hoc 修改。
- 不需要重新训练 diffusion model。
- 检测通常依赖 model owner 可执行的 DDIM inversion，因此更接近 private verification。
- 更适合 generated-image detection / provenance；是否能扩展为大规模 [[user-attribution]] 仍未被证明。

## 局限

- 方法依赖兼容的 sampling 与 inversion procedure。
- 多个 image transformations 叠加时，低 false positive rate 下的 true positive rate 会明显下降。
- 多 key capacity 仍是开放问题，因此不能直接替代 WOUAF 或 OmniMark 的 user attribution 目标。
