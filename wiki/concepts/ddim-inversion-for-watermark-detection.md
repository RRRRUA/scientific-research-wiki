---
type: concept
title: "DDIM Inversion for Watermark Detection"
created: 2026-06-09
updated: 2026-06-09
tags: [ddim-inversion, diffusion-models, watermark-detection]
related: ["[[tree-ring-watermark]]", "[[fourier-noise-watermarking]]", "[[latent-diffusion-watermarking]]", "[[watermark-robustness]]", "[[private-vs-public-watermark-verification]]"]
sources: ["Wen 等 - 2023 - Tree-Ring Watermarks Fingerprints for Diffusion Images that are Invisible and Robust.pdf-009a7e2b-80bb-48a7-bf25-28b175fc8239/full.md"]
---

# DDIM Inversion for Watermark Detection

DDIM inversion for watermark detection 是把一张最终图像近似反推回 diffusion sampling 初始 noise 的检测步骤。在 [[tree-ring-watermark]] 中，watermark key 不在最终图像像素里，而在初始 noise 的 Fourier space 里，因此检测器必须先恢复或近似恢复这个 noise。

## 在 Tree-Ring 中的作用

Tree-Ring 生成阶段把 key 写入初始 noise。检测阶段从待测图像出发，沿 diffusion process 反向估计初始 noise，再把估计结果转换到 Fourier space，检查指定 mask 中是否存在 secret key pattern。论文还使用统计检验控制 false positive rate。

## 优点

- 检测不要求知道原始 text prompt；论文在 Stable Diffusion 设置中使用 empty prompt 做 inversion。
- Watermark 不需要作为 post-hoc pattern 叠加到图像上。
- 只要 inversion 足够准确，检测可以验证生成过程中的 hidden key。

## 局限

检测质量直接依赖 inversion 质量。强图像编辑、多个 transformations 叠加、采样器变化或无法访问兼容模型，都会削弱这个检测路径。因此它通常更适合作为 model owner 的 private verification，而不是完全开放的 public verification。
