---
type: concept
title: "Post-hoc Image Watermarking"
tags: [image-watermarking, post-hoc-watermarking, watermark-robustness, copyright-protection]
related: ["[[hfrw]]", "[[advmark]]", "[[ping-2026-hfrw]]", "[[chen-2026-advmark]]", "[[localized-invisible-watermarking]]", "[[watermark-robustness]]", "[[latent-diffusion-watermarking]]"]
created: 2026-06-17
updated: 2026-06-17
sources: ["HFRW_High_Fidelity_and_Robust_Watermarking_using_Deep_Reinforcement_Learning.pdf-1d97070b-78d6-4eb4-a7a0-f24fbfba014c/full.md", "Chen 等 - 2026 - Decoupling Defense Strategies for Robust Image Watermarking.pdf-8147032b-37f6-4091-8de2-a8ec3a76b5f6/full.md"]
---

# Post-hoc Image Watermarking

Post-hoc image watermarking 指在图像已经生成或取得之后，再通过 encoder、patch embedding、image optimization 等方式把 watermark message 写入像素空间。它不同于 [[latent-diffusion-watermarking]]：后者把 provenance signal 放进 generation workflow，例如 decoder、initial noise 或 model weights。

## 当前语料中的两条路线

[[ping-2026-hfrw]] 代表 localized invisible watermarking：只在局部 patch 中嵌入 watermark，以降低整图质量损失和 file size growth rate。

[[chen-2026-advmark]] 代表 advanced-attack oriented robust watermarking：不主打局部嵌入，而是把 adversarial attack defense 与 distortion / regeneration defense 拆成两个阶段。

## 评价维度

Post-hoc image watermarking 通常更关注 PSNR、SSIM、LPIPS、file size growth、bit accuracy 和 image post-processing robustness。AdvMark 进一步把 diffusion regeneration 和 adversarial attacks 纳入核心评估，说明 conventional distortions 之外还需要单独衡量 advanced removal attacks。

## 与 diffusion-native 方法的边界

Post-hoc image watermarking 可以保护普通图像，也可以作为 generated images 的后处理步骤，但它通常不能证明图像来自某个特定 model copy，也不天然解决大规模 [[user-attribution]]。因此它适合作为 LDM provenance 的外部对照，而不是替代 [[stable-signature]]、[[tree-ring-watermark]]、[[wouaf]]、[[omnimark]] 或 [[stableguard]]。
