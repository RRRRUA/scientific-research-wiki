---
type: source
title: "OmniMark: Efficient and Scalable Latent Diffusion Model Fingerprinting"
tags: [latent-diffusion-models, model-fingerprinting, watermarking, user-attribution, generative-ai-safety]
related: ["[[generative-model-fingerprinting]]", "[[latent-diffusion-watermarking]]", "[[user-attribution]]", "[[watermark-robustness]]", "[[diffusion-model-fingerprinting-comparison]]"]
created: 2026-06-07
updated: 2026-06-09
authors: ["Jianwei Fei", "Yunshu Dai", "Zhihua Xia", "Fangjun Huang", "Jiantao Zhou"]
year: 2025
url: "https://github.com/jumpycat/OmniMark"
venue: ""
---

# OmniMark: Efficient and Scalable Latent Diffusion Model Fingerprinting

## 一句话结论
OmniMark 通过把 fingerprints 编码进 VAE decoder weights，实现面向 latent diffusion models 的可扩展 user-specific fingerprinting，使大量唯一模型副本可以快速生成，而不必为每个副本重新训练。

## 问题
已有 watermarking 和 fingerprinting 方法常依赖 post-processing、input modification，或为每个用户 fingerprint 重新训练/微调模型。当 model provider 需要分发大量可追踪模型副本时，这些路径效率不足。

## 方法
OmniMark 用 OmniMark layers 修改 LDM 的 VAE decoder。这些 layers 把 convolution kernels 扩展为多个 parallel kernels，并在 kernel、filter、channel、spatial 等维度编码 fingerprint。系统训练 fingerprint decoder，从生成图像中恢复 embedded bit string。方法还使用 noise layer 提升 image transformation robustness，并使用 sharpness-aware strategy 提升对 model fine-tuning 的鲁棒性。

## 证据
论文在 Stable Diffusion v2.0 的 text-to-image 与 image-to-image tasks 上评估，数据集包括 MS-COCO、ImageNet 和 MagicBrush。实验使用 48-bit fingerprints，并报告跨数据集约 99% bit accuracy，同时对 FID、CLIP score、PSNR、SSIM、LPIPS 等 image quality metrics 的影响较小。

## 关键结果
- 支持快速生成新的 fingerprinted model copies；摘要中报告低于 100 ms。
- 在嵌入 imperceptible fingerprints 的同时，保持接近原模型的 image quality。
- 相比 Stable Signature，可扩展性更强，因为新 user fingerprints 不需要 per-user fine-tuning。
- 在 fine-tuning 中加入 noise layer 后，鲁棒性明显提升。

## 局限与注意点
- Strong white-box attacks，尤其 model fine-tuning，仍是重要威胁；论文提出的 robust fingerprinting strategy 只能提高抵抗力，不能彻底消除风险。
- 评估主要集中在 image-generation LDM settings，迁移到其他模态仍是开放问题。
- 方法依赖可靠的 fingerprint decoding 和 statistical verification assumptions。

## 对本项目的用途
这篇是三篇中最强调 scalability 的来源，尤其适合回答“如何分发大量 user-specific diffusion models，同时保留 attribution capability”。

## 原始来源
- `raw/sources/fei-2025-omnimark/full.md`
- `raw/sources/fei-2025-omnimark/5495cb44-13cb-4607-9538-77d397de59e6_origin.pdf`

## 相关页面
- [[generative-model-fingerprinting]]
- [[latent-diffusion-watermarking]]
- [[user-attribution]]
- [[watermark-robustness]]
- [[diffusion-model-fingerprinting-comparison]]
