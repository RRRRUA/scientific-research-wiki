---
type: concept
title: "Watermark Robustness"
tags: [watermarking, robustness, adversarial-attacks]
related: ["[[generative-model-fingerprinting]]", "[[latent-diffusion-watermarking]]", "[[user-attribution]]", "[[tree-ring-watermark]]", "[[stableguard]]", "[[hfrw]]", "[[advmark]]", "[[localized-invisible-watermarking]]", "[[post-hoc-image-watermarking]]", "[[tamper-localization-for-generated-images]]", "[[diffusion-model-fingerprinting-comparison]]"]
created: 2026-06-07
updated: 2026-06-17
---

# Watermark Robustness

## 定义

水印鲁棒性（watermark robustness）指嵌入的 signature 或 fingerprint 在经历变换、质量退化或对抗性移除后仍能被检测和验证的能力。

## 图像级变换

常见评估包括 cropping、JPEG compression、亮度/对比度变化、rotation、blur、noise、text overlay、resizing、erasing，以及多种变换组合。

## 模型级攻击

对 model fingerprinting 来说，white-box users 可能通过 pruning、quantization、parameter noise、model compression、fine-tuning 或 model purification 来削弱 fingerprint。

## 当前论文的共同模式

- [[fernandez-2023-stable-signature]] 表明 decoder-rooted watermarks 能抵抗许多 image edits，但在 informed model/image-level attacks 下仍有弱点。

- [[wen-2023-tree-ring-watermarks]] 表明 initial-noise Fourier watermarking 可以在不 post-hoc 修改图像的情况下，对多种 common image transformations 保持较高 AUC。

- [[kim-2024-wouaf]] 在实验中相对 Stable Signature 提高了对 image post-processing 的鲁棒性。

- [[fei-2025-omnimark]] 通过 noise-layer training 和 sharpness-aware robustness 提升对 image attacks 与 model attacks 的抵抗力。

- [[yang-2025-stableguard]] 把 holistic watermark 用作 forensic cue；论文报告在 tampering ratio、compression、noise 等设置下保持较高 Bit Acc，但也承认 localization accuracy 会随 degradation 下降。

- [[ping-2026-hfrw]] 通过 local patch embedding、DQN patch selection 和 localization/synchronization module 提升 ordinary image watermarking 的 fidelity、FSVR 和 common-attack robustness，但 severe cropping 仍是主要弱点。

- [[chen-2026-advmark]] 将 adversarial defense 与 distortion / regeneration defense 解耦：Stage 1 主要提升 WEvade / Black-S 等 adversarial robustness，Stage 2 用 direct image optimization 补足 conventional distortions 与 diffusion regeneration robustness。

## 研究张力

更强 robustness 往往会与 image quality、计算成本和大规模用户扩展性发生冲突。AdvMark 进一步提示：不同攻击族可能需要不同防御策略，不能只用一个 aggregate robustness 数字概括。
