---
type: concept
title: "Fourier Noise Watermarking"
created: 2026-06-09
updated: 2026-06-09
tags: [fourier-transform, diffusion-noise, watermarking, robustness]
related: ["[[tree-ring-watermark]]", "[[ddim-inversion-for-watermark-detection]]", "[[watermark-robustness]]", "[[latent-diffusion-watermarking]]", "[[generative-model-fingerprinting]]"]
sources: ["Wen 等 - 2023 - Tree-Ring Watermarks Fingerprints for Diffusion Images that are Invisible and Robust.pdf-009a7e2b-80bb-48a7-bf25-28b175fc8239/full.md"]
---

# Fourier Noise Watermarking

Fourier noise watermarking 是把 watermark signal 写入 diffusion model 初始 noise 的 Fourier coefficients，而不是写入最终图像或 decoder weights。[[tree-ring-watermark]] 是本 wiki 中这个路线的代表。

## 为什么使用 Fourier space

Fourier transform 对 rotation、translation、cropping、scaling 等图像变换有可分析的结构关系。Tree-Ring 把 key 放进 circular 或 ring-shaped mask 中，使检测器在常见 image transformations 后仍有机会从恢复出的初始 noise 中找到 key。

## 与图像水印的区别

传统 Fourier image watermarking 通常改动最终图像的频域系数。Fourier noise watermarking 则在 generation before image formation 阶段改动初始 noise。最终图像并没有一个简单的后处理叠加 pattern，而是保留了被控制 sampling trajectory 的统计痕迹。

## 与鲁棒性的关系

Tree-Ring 的实验表明，ring-shaped variant 对多种单一 common image transformations 有较强 AUC。但这不是绝对鲁棒：多个攻击叠加时，检测性能会下降；不同 key pattern 也有不同弱点。
