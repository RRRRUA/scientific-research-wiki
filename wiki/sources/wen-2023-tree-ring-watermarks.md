---
type: source
title: "Tree-Ring Watermarks: Fingerprints for Diffusion Images that are Invisible and Robust"
tags: [diffusion-models, watermarking, tree-ring-watermarking, ddim-inversion, image-provenance, generative-ai-safety]
related: ["[[tree-ring-watermark]]", "[[latent-diffusion-watermarking]]", "[[watermark-robustness]]", "[[generative-model-fingerprinting]]", "[[diffusion-model-fingerprinting-comparison]]"]
created: 2026-06-09
updated: 2026-06-09
authors: ["Yuxin Wen", "John Kirchenbauer", "Jonas Geiping", "Tom Goldstein"]
year: 2023
url: "https://github.com/YuxinWenRick/tree-ring-watermark"
venue: "arXiv:2305.20030"
---

# Tree-Ring Watermarks: Fingerprints for Diffusion Images that are Invisible and Robust

## 一句话结论

Tree-Ring Watermarking 把 watermark pattern 嵌入 diffusion sampling 的初始 noise vector 的 Fourier space，而不是在图像生成后修改像素；检测时通过 DDIM inversion 近似恢复初始 noise，并检查预设 key 是否存在。

## 问题

Post-hoc image watermarking 会对已生成图像做额外修改，在 open-source 或可编辑图像环境中容易被移除。论文要解决的是：能否在不降低生成质量、也不训练新模型的情况下，让 diffusion model output 带有对常见图像变换稳健的 invisible watermark。

## 方法

Tree-Ring Watermarking 在 generation phase 选择一个特殊初始噪声 `x_T`。该噪声的 Fourier transform 在低频圆形 mask `M` 内包含 key pattern。论文讨论了 `Tree-Ring_Zeros`、`Tree-Ring_Rand` 和 `Tree-Ring_Rings` 三类 key，其中 rings pattern 在旋转等图像变换下更稳健，同时仍可支持多个随机 key。

Detection phase 中，model owner 对待测图像执行 DDIM inversion 得到近似初始 noise `x'_T`，再在 Fourier space 计算该 noise 与 key 的距离。论文用 noncentral chi-square distribution 构造 P-value，以便用阈值控制 false positive rate。

## 证据

论文在 Stable Diffusion-v2 和 256x256 ImageNet diffusion model 上评估。主要指标包括 AUC、TPR@1%FPR、FID 和 CLIP Score。raw parse 的 Table 1 报告，在 Stable Diffusion clean setting 下，Tree-Ring variants 的 AUC/T@1%F 接近 1.000/1.000；在 adversarial setting 下，`Tree-Ring_Rings` 的 AUC 为 0.975，优于 DwtDct、DwtDctSvd 和 RivaGAN 的 average adversarial AUC。论文正文还指出 `Tree-Ring_Rand` 和 `Tree-Ring_Rings` 对 FID 的影响可忽略，并且 CLIP Score 基本不受影响。

Robustness 评估覆盖 rotation、JPEG compression、cropping and scaling、Gaussian blur、Gaussian noise、color jitter 等攻击。论文报告 `Tree-Ring_Rings` 的平均表现最好；同时也指出不同 key pattern 有不同弱点，例如 `Tree-Ring_Rand` 在 rotation 下表现较差，`Tree-Ring_Zeros` 对 Gaussian noise 和 color jitter 较弱。

## 局限与注意点

- 方法依赖 DDIM sampling 和 DDIM inversion；如果采样方法改变，需要适配。
- Watermark 只能由掌握模型参数和 watermarking algorithm 的 model owner 验证，第三方需要依赖 API。
- 多 key capacity 尚不明确，论文明确提出“是否可以给每个 API 用户分配唯一 key”仍是未来问题。
- 它更适合 generated-image detection / provenance，不直接解决 WOUAF 和 OmniMark 关注的 model-copy user attribution。

## 对本项目的用途

这篇扩展了本项目的技术空间：除了 decoder-rooted watermarking 和 decoder weight fingerprinting，还存在一种 noise-space / sampling-process watermarking 路线。它特别适合比较“post-hoc watermarking、decoder-rooted watermarking、weight-modulated fingerprinting、initial-noise watermarking”之间的部署边界。

## 原始来源

- `raw/sources/Wen 等 - 2023 - Tree-Ring Watermarks Fingerprints for Diffusion Images that are Invisible and Robust.pdf-009a7e2b-80bb-48a7-bf25-28b175fc8239/full.md`

## 相关页面

- [[tree-ring-watermark]]
- [[latent-diffusion-watermarking]]
- [[watermark-robustness]]
- [[generative-model-fingerprinting]]
- [[diffusion-model-fingerprinting-comparison]]
