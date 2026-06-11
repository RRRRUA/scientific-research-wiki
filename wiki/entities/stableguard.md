---
type: entity
title: "StableGuard"
aliases: ["MPW-VAE", "MoE-GFN", "Mixture-of-Experts Guided Forensic Network"]
tags: [method, latent-diffusion-models, watermarking, tamper-localization, copyright-protection]
related: ["[[yang-2025-stableguard]]", "[[latent-diffusion-watermarking]]", "[[watermark-robustness]]", "[[tamper-localization-for-generated-images]]", "[[stableguard-unifies-watermark-verification-and-tamper-localization]]", "[[stableguard-mpw-vae-enables-self-supervised-tamper-training]]"]
created: 2026-06-11
updated: 2026-06-11
sources: ["Yang 等 - 2025 - StableGuard Towards Unified Copyright Protection and Tamper Localization in Latent Diffusion Model.pdf-d8a32816-0fa0-4c8d-934e-e96205ef30ed/full.md"]
---

# StableGuard

StableGuard 是 [[yang-2025-stableguard]] 提出的 Latent Diffusion Models watermarking / forensics framework，用于同时支持 copyright verification 和 tamper localization。

## 组成

- Multiplexing Watermark VAE (MPW-VAE)：在 VAE decoder 中加入 residual-based watermark adapter，让同一 latent code 可以生成 watermarked 或 watermark-free 图像。
- Mixture-of-Experts Guided Forensic Network (MoE-GFN)：从 watermarked / tampered 图像中同时恢复 watermark bits 和定位 tampered regions。
- Mixture-of-Forensic-Experts (MoFE)：包含 Watermark Extraction Expert、Tampering Localization Expert、Boundary Enhancement Expert，并由 Dynamic Soft Router 融合。

## 关键机制

StableGuard 使用 MPW-VAE 生成 paired watermarked / clean samples，再通过 random masks 或 SAM-generated semantic masks 混合成 self-supervised tampering training data。MoE-GFN 学习识别 watermark pattern 的缺失、局部篡改痕迹和边界异常，从而输出 watermark verification 与 tamper mask。

## 与其他方法的区别

| 方法 | 主要任务 | 嵌入位置 |
| --- | --- | --- |
| [[stable-signature]] | generated-image detection / limited identification | latent decoder |
| [[wouaf]] | user attribution | decoder weight modulation |
| [[omnimark]] | scalable model-copy fingerprinting | VAE decoder weight encoding |
| [[tree-ring-watermark]] | provenance detection | initial noise Fourier space |
| StableGuard | copyright verification + tamper localization | VAE decoder adapter + forensic network |

StableGuard 与 WOUAF、OmniMark 都涉及 decoder / VAE decoder，但它的研究重点不是给大量用户分发唯一模型副本，而是把水印信号变成后续 forensic localization 的主动线索。

## 局限

StableGuard 的操作前提是生成图像已经被水印化；未水印图像不在系统目标范围内。论文也指出 image degradation 会降低 forensic accuracy，尤其是需要像素级定位的部分。
