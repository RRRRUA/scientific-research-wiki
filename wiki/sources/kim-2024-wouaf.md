---
type: source
title: "WOUAF: Weight Modulation for User Attribution and Fingerprinting in Text-to-Image Diffusion Models"
tags: [text-to-image, diffusion-models, model-fingerprinting, weight-modulation, user-attribution, generative-ai-safety]
related: ["[[generative-model-fingerprinting]]", "[[user-attribution]]", "[[watermark-robustness]]", "[[latent-diffusion-watermarking]]", "[[diffusion-model-fingerprinting-comparison]]"]
created: 2026-06-07
updated: 2026-06-09
authors: ["Changhoon Kim", "Kyle Min", "Maitreya Patel", "Sheng Cheng", "Yezhou Yang"]
year: 2024
url: "https://github.com/kylemin/WOUAF"
venue: ""
---

# WOUAF: Weight Modulation for User Attribution and Fingerprinting in Text-to-Image Diffusion Models

## 一句话结论

WOUAF 通过用户特定的 weight modulation 为 text-to-image diffusion models 嵌入 fingerprint，目标是在 distributor-side user attribution 中兼顾效率、生成质量和对 image post-processing 的鲁棒性。

## 问题

传统 fingerprinting modules 在 open-source generation pipelines 中容易被绕过，而 per-user model fine-tuning 难以扩展。Distributor 需要一种方法，为每个用户分配可追踪模型副本，同时避免明显损害 image quality 或承担昂贵的 per-user training 成本。

## 方法

WOUAF 把 user fingerprint 映射成 modulation parameters，用来调制 selected model weights，重点是 Stable Diffusion 的 VAE decoder。Fingerprint decoding network 再从生成图像中恢复嵌入的 bit string。论文比较了只调制 convolution layers、调制全部 decoder layers，以及调制 U-Net + decoder 的不同变体，并与 DAG 和 Stable Signature 对比。

## 证据

论文在 MS-COCO 和 LAION-Aesthetics 上评估 Stable Diffusion T2I generation。结果报告在常见 fingerprint dimensions 下接近满分的 attribution accuracy，FID/CLIP degradation 较小，并在 erasing、rotation、blur、cropping、brightness jitter、Gaussian noise、JPEG compression 和 combined post-processing 下保持较强鲁棒性。

## 关键结果

- 32-bit fingerprints 是主要平衡设置，理论上支持超过 40 亿个 user identifiers。

- 16、32、64-bit fingerprint settings 下报告了接近满分的 attribution accuracy。

- 相比 Stable Signature，论文报告 WOUAF 在 image post-processing 下的平均 robustness 提升约 11%。

- 新 user-specific models 可以通过一次 lightweight forward pass 创建，不需要完整 per-user fine-tuning。

## 局限与注意点

- Fingerprint dimension 增大时 attribution accuracy 会下降，128 bits 尤其明显。

- 对 strong auto-encoder compression 和 model purification 的抵抗仍然依赖与 image quality 的权衡。

- 论文主要覆盖 text-to-image diffusion models，text、audio、video 等模态仍属于未来扩展。

## 对本项目的用途

这篇适合作为 weight modulation 与 distributor-oriented attribution 的核心来源。它位于 Stable Signature 和 OmniMark 之间：比 per-signature fine-tuning 更可扩展，但不如 OmniMark 那样明确强调 multi-dimensional kernel/filter/channel/spatial encoding。

## 原始来源

- `raw/sources/kim-2024-wouaf/full.md`

- `raw/sources/kim-2024-wouaf/9daaa5d1-066d-47c8-a411-5e597493deb9_origin.pdf`

## 相关页面

- [[generative-model-fingerprinting]]
- [[user-attribution]]
- [[watermark-robustness]]
- [[latent-diffusion-watermarking]]
- [[diffusion-model-fingerprinting-comparison]]
