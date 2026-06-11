---
type: concept
title: "Latent Diffusion Watermarking"
tags: [latent-diffusion-models, watermarking, stable-diffusion]
related: ["[[generative-model-fingerprinting]]", "[[user-attribution]]", "[[watermark-robustness]]", "[[tamper-localization-for-generated-images]]", "[[localized-invisible-watermarking]]", "[[fernandez-2023-stable-signature]]", "[[wen-2023-tree-ring-watermarks]]", "[[fei-2025-omnimark]]", "[[kim-2024-wouaf]]", "[[yang-2025-stableguard]]", "[[ping-2026-hfrw]]"]
created: 2026-06-07
updated: 2026-06-09
---

# Latent Diffusion Watermarking

## 定义

潜在扩散模型水印（latent diffusion watermarking）是在 latent diffusion model 生成流程中嵌入隐藏信号。常见位置包括 VAE decoder、model weights、initial noise 或 generation-time adapters；核心目标是让 watermark 成为生成过程的一部分，而不是生成后附加的 post-processing watermark。

## 核心思想

Stable Diffusion 风格模型先在 latent space 中 denoise，再通过 decoder 生成 RGB 图像。由于 decoder 直接决定最终像素，把签名嵌入 decoder 可以让每张生成图像携带隐藏 signature，同时尽量不改变 denoising process 和 prompt 行为。

## 相关论文

- [[fernandez-2023-stable-signature]]：fine-tune latent decoder，嵌入固定 signature。

- [[wen-2023-tree-ring-watermarks]]：在 initial noise 的 Fourier space 中嵌入 ring-shaped key，并用 DDIM inversion 检测。

- [[kim-2024-wouaf]]：在 T2I diffusion models 中用 weight modulation 生成用户特定 fingerprints。

- [[fei-2025-omnimark]]：用 OmniMark layers 修改 VAE decoder，以支持可扩展 fingerprint generation。

- [[yang-2025-stableguard]]：用 MPW-VAE 在 VAE decoder 中嵌入 holistic watermark，并用 MoE-GFN 同时做 copyright verification 和 tamper localization。

- [[ping-2026-hfrw]]：不是 latent diffusion watermarking，但提供 post-hoc localized image watermarking 对照，说明 local patch embedding 可显著改善 fidelity 和 FSVR。

## 设计权衡

- Decoder-only 修改通常更容易保持与不同 LDM tasks 的兼容性。

- Post-generation watermarking 在 open-source pipeline 中更容易被绕过。

- Per-user fine-tuning 可以准确，但扩展到大量用户时成本高。

- Scalable fingerprint generation 必须同时维持 attribution accuracy 和 perceptual quality。

- Tamper localization 需要 watermark signal 具有足够空间分布，使局部缺失或破坏可以被 forensic detector 利用。
