---
type: concept
title: "Generative Model Fingerprinting"
tags: [model-fingerprinting, generative-ai-safety, attribution]
related: ["[[user-attribution]]", "[[latent-diffusion-watermarking]]", "[[watermark-robustness]]", "[[tamper-localization-for-generated-images]]", "[[localized-invisible-watermarking]]", "[[tree-ring-watermark]]", "[[stableguard]]", "[[hfrw]]", "[[fei-2025-omnimark]]", "[[kim-2024-wouaf]]", "[[fernandez-2023-stable-signature]]", "[[wen-2023-tree-ring-watermarks]]", "[[yang-2025-stableguard]]", "[[ping-2026-hfrw]]"]
created: 2026-06-07
updated: 2026-06-09
---

# Generative Model Fingerprinting

## 定义

生成模型指纹识别（generative model fingerprinting）是在生成模型或其输出中嵌入可追踪标识，使生成内容能够回溯到模型提供方、模型副本或具体用户。

## 为什么重要

对 text-to-image diffusion models 来说，fingerprinting 面向的是 deepfake、误导性内容、版权滥用和违规生成等责任归属问题。它不只要判断图像是否由 AI 生成，还要在需要时定位到责任模型副本或用户。

## 本项目关注的方法

- Decoder-rooted watermarking：[[fernandez-2023-stable-signature]] fine-tune LDM decoder，把固定 binary signature 嵌入生成过程。
- Noise-space watermarking：[[wen-2023-tree-ring-watermarks]] 把 key pattern 放进 diffusion initial noise 的 Fourier space，再通过 DDIM inversion 检测。
- Weight modulation：[[kim-2024-wouaf]] 使用用户特定的 weight modulation，支持 distributor-side user attribution。
- Scalable multi-dimensional fingerprint encoding：[[fei-2025-omnimark]] 在 decoder weight 的 kernel、filter、channel、spatial 等维度编码 fingerprint，以快速生成模型副本。
- Proactive forensic watermarking：[[yang-2025-stableguard]] 把 holistic watermark 用作 copyright verification 与 [[tamper-localization-for-generated-images]] 的共同线索。
- Post-hoc image watermarking comparator：[[ping-2026-hfrw]] 不属于 generative model fingerprinting，但提供 local invisible watermarking 在 fidelity、FSVR 和 common-attack robustness 上的对照证据。

## 评价维度

- 归因准确率（attribution accuracy）或 bit accuracy。
- False positive rate 与统计置信度。
- 生成质量影响：FID、CLIP score、PSNR、SSIM、LPIPS。
- 对 image post-processing 和 model-level attacks 的鲁棒性。
- 面向大量用户时的生成、存储和验证成本。
- 如果目标包含 tamper localization，还要评估 F1、AUC、IoU 和 degradation 下的 mask quality。

## 开放问题

- 面对 informed white-box users，model-level fingerprints 能有多稳健？
- Fingerprint capacity、attribution accuracy 和 image quality 之间的最佳权衡是什么？
- 这些方法能否迁移到 video、audio 和 text 等非图像模态？
