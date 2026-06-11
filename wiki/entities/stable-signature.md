---
type: entity
title: "Stable Signature"
tags: [method, latent-diffusion, watermarking]
related: ["[[fernandez-2023-stable-signature]]", "[[latent-diffusion-watermarking]]", "[[watermark-robustness]]"]
created: 2026-06-08
updated: 2026-06-08
---

# Stable Signature

Stable Signature 是 [[fernandez-2023-stable-signature]] 提出的 decoder-rooted watermarking 方法。它通过微调 latent diffusion model 的 image decoder，让生成图像携带可检测的隐藏二进制签名。

在本项目中，它是理解 [[latent-diffusion-watermarking]] 的基础方法，也是 WOUAF 和 OmniMark 的重要对照。
