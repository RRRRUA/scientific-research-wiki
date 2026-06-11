---
type: finding
title: "Stable Signature Detects Generated Images at Low FPR"
tags: [finding, stable-signature, detection, false-positive-rate, latent-diffusion]
related: ["[[fernandez-2023-stable-signature]]", "[[latent-diffusion-watermarking]]", "[[watermark-robustness]]", "[[decoder-rooted-fingerprinting-scales-through-weight-encoding]]"]
created: 2026-06-09
updated: 2026-06-09
source: "[[fernandez-2023-stable-signature]]"
confidence: high
replicated: false
---

# Stable Signature Detects Generated Images at Low FPR

## 发现

[[fernandez-2023-stable-signature]] 报告，Stable Signature 在 text-to-image 生成图像上可以以很低 false positive rate（FPR）完成 generated-image detection。

## 证据

论文在 MS-COCO prompts 上生成图像，并用 48-bit signature 与 binomial statistical test 做 detection。raw parse 中报告：未修改生成图像在 `FPR = 10^-9` 时可检测约 99%；即使图像 crop 到只保留 10% 内容，在同一 FPR 下仍可检测约 84%；组合变换下约 65%。

## 解释

这个结果支持 decoder-rooted watermarking 的基础价值：水印不是生成后附加，而是由 latent decoder 直接写入生成过程，因此比 passive forensic detection 或 post-hoc watermarking 更适合做低误报场景下的 provenance signal。

## 注意

这些结果是论文报告结果，不是本项目复现实验。FPR 的极低区间主要依赖 binomial model 与论文中的 empirical check；平台部署仍需要独立验证 bit independence 和阈值稳定性。
