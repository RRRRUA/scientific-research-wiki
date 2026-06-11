---
type: finding
title: "WOUAF Decoder-Only Modulation Preserves Quality Better"
tags: [finding, wouaf, decoder, image-quality, weight-modulation]
related: ["[[kim-2024-wouaf]]", "[[latent-diffusion-watermarking]]", "[[generative-model-fingerprinting]]", "[[decoder-fingerprinting-scalability-comparison]]"]
created: 2026-06-09
updated: 2026-06-09
source: "[[kim-2024-wouaf]]"
confidence: high
replicated: false
---

# WOUAF Decoder-Only Modulation Preserves Quality Better

## 发现

[[kim-2024-wouaf]] 的实验支持 decoder-only modulation，而不是同时调制 denoising U-Net 和 decoder。

## 证据

WOUAF 在方法部分说明，它把 fingerprints 只嵌入 Stable Diffusion 的 decoder weights。raw parse 的 Sec. 4.5 报告，同时调制 diffusion model `epsilon_theta` 和 decoder D 的 variant 无法同时优化 attribution accuracy 与 generation quality：最高 attribution accuracy 只有 89%，Clip-score 为 0.68，FID 为 63.48；而 decoder-only 的 WOUAF-conv/WOUAF-all 在 Table 1 中保持 0.99 attribution accuracy，并且 CLIP/FID 接近 Original SD。

## 解释

这个 finding 强化了一个跨论文模式：LDM decoder 是 provenance embedding 的高价值位置，因为它直接影响最终像素，同时不必扰动整个 diffusion process。

## 注意

这不意味着 decoder 永远是唯一正确位置。更强的 white-box attacker 可以替换、蒸馏或再训练 decoder；这些攻击仍需要单独建模。
