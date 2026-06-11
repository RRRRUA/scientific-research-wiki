---
type: source
title: "The Stable Signature: Rooting Watermarks in Latent Diffusion Models"
tags: [latent-diffusion-models, watermarking, stable-diffusion, detection, user-identification, generative-ai-safety]
related: ["[[latent-diffusion-watermarking]]", "[[user-attribution]]", "[[watermark-robustness]]", "[[generative-model-fingerprinting]]", "[[diffusion-model-fingerprinting-comparison]]"]
created: 2026-06-07
updated: 2026-06-09
authors: ["Pierre Fernandez", "Guillaume Couairon", "Herve Jegou", "Matthijs Douze", "Teddy Furon"]
year: 2023
url: ""
venue: ""
---

# The Stable Signature: Rooting Watermarks in Latent Diffusion Models

## 一句话结论
Stable Signature 通过 fine-tune latent decoder，把 invisible binary signature 嵌入 latent diffusion model 生成的所有图像，从而在不依赖 post-generation watermarking 的情况下支持 detection 和 user identification。

## 问题
Post-generation watermarks 容易被移除或绕过，尤其当用户可以访问 open-source generation pipelines 时。Passive forensic detection 也难以在极低 false-positive requirements 下稳定工作，并且通常不能可靠识别是哪一个模型副本生成了图像。

## 方法
该方法先 pre-train watermark extractor，然后只 fine-tune latent diffusion model 的 latent decoder，使生成图像包含固定 binary signature。Detection 和 identification 通过 bit matching 与 binomial statistical tests 完成。

## 证据
论文在 Stable-Diffusion-like models 上评估 48-bit signatures，使用 MS-COCO prompts，并覆盖 text-to-image、image editing、inpainting、super-resolution 等任务。结果报告在很低 false positive rates 下仍有较高 detection rates，并评估了 cropping、brightness shift、JPEG compression 和 combined transformations 下的鲁棒性。

## 关键结果
- 在极低 false-positive rates 下能检测多数未修改 generated images。
- 对 100,000 users，未修改图像的 identification 报告约为 98%；combined image edits 下准确率下降。
- 对多个 LDM tasks 的 generation quality 影响较小。
- 相比 post-hoc watermarking，signature root in generation process 带来更强安全性和效率。

## 局限与注意点
- 每个新 signature 都需要 fine-tune 一个模型副本，大用户规模下存在 scalability pressure。
- Strong combined transformations 和 informed attacks 会降低 robustness。
- 在较强假设下，model-level purification 可以降低 watermark accuracy，同时保留可接受 image quality。

## 对本项目的用途
这篇是 decoder-rooted LDM watermarking 的基础来源，提供了 detection 与 identification 的统计框架；后续 WOUAF 和 OmniMark 都可以在这个框架上比较扩展性与鲁棒性。

## 原始来源
- `raw/sources/fernandez-2023-stable-signature/full.md`
- `raw/sources/fernandez-2023-stable-signature/e021a8c6-b67d-4617-8516-b4933b6cb194_origin.pdf`

## 相关页面
- [[latent-diffusion-watermarking]]
- [[user-attribution]]
- [[watermark-robustness]]
- [[generative-model-fingerprinting]]
- [[diffusion-model-fingerprinting-comparison]]
