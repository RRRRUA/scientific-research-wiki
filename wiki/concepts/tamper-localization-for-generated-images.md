---
type: concept
title: "Tamper Localization for Generated Images"
tags: [tamper-localization, image-forensics, watermarking, generated-images]
related: ["[[stableguard]]", "[[yang-2025-stableguard]]", "[[watermark-robustness]]", "[[latent-diffusion-watermarking]]", "[[private-vs-public-watermark-verification]]"]
created: 2026-06-11
updated: 2026-06-11
sources: ["Yang 等 - 2025 - StableGuard Towards Unified Copyright Protection and Tamper Localization in Latent Diffusion Model.pdf-d8a32816-0fa0-4c8d-934e-e96205ef30ed/full.md"]
---

# Tamper Localization for Generated Images

Tamper localization for generated images 指在一张疑似被编辑的生成图像中定位哪些区域被 splicing、inpainting、copy-paste、removal 或其他 editing methods 修改。它比 generated-image detection 更细：不仅判断图像来源，还要给出 tampered region mask。

## 两条路线

- Passive localization：只根据图像本身的视觉或统计异常判断篡改区域，通常需要 paired supervision，面对新型 AIGC editing methods 时容易泛化不足。
- Proactive localization：在生成或发布时嵌入 auxiliary signal，之后通过该信号是否缺失或异常来定位篡改区域。

[[yang-2025-stableguard]] 属于 proactive route。它用 MPW-VAE 把 holistic watermark 嵌入生成过程，再让 MoE-GFN 从 watermark pattern、local traces 和 boundary cues 中联合恢复 copyright signal 与 tamper mask。

## 与 watermarking 的关系

Watermarking 通常只回答“这张图是否来自某个模型或 key”。Tamper localization 要回答“图像的哪些区域不再符合该 watermark pattern”。StableGuard 的核心假设是：holistic watermark 在空间上分布充分，局部篡改会破坏局部 watermark cues，因此 missing watermark features 可以成为 localization 线索。

## 局限

这种方法假设原图在生成阶段已经带有 watermark。对无水印图像、来自其他模型的图像、或严重压缩/降采样后的图像，localization 的解释边界需要谨慎处理。
