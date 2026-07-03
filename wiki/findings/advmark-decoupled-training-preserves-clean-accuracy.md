---
type: finding
title: "AdvMark Decoupled Training Preserves Clean Accuracy"
tags: [finding, advmark, clean-accuracy, adversarial-training, watermark-robustness]
related: ["[[chen-2026-advmark]]", "[[advmark]]", "[[post-hoc-image-watermarking]]", "[[watermark-robustness]]"]
created: 2026-06-17
updated: 2026-06-17
source: "[[chen-2026-advmark]]"
confidence: high
replicated: false
---

# AdvMark Decoupled Training Preserves Clean Accuracy

## 发现

[[chen-2026-advmark]] 报告 joint adversarial training 会牺牲 clean accuracy，而 AdvMark 的 encoder-focused Stage 1 可以保持 clean bit accuracy，同时提升 regeneration 和 WEvade robustness。

## 证据

Figure 2 中，MBRS-JAT Defense 的 Clean accuracy 为 0.94，而 MBRS-EAT 和 AdvMark 均为 1.00。AdvMark 同时在 JPEG、Regen-SD-V1-4 和 WEvade 上达到 0.99、0.87、0.98，高于 MBRS-EAT 的 0.98、0.65、0.77。

## 解释

这支持论文的核心诊断：如果主要修改 decoder decision boundary，clean watermarked images 会受到影响；如果优先 fine-tune encoder，把 watermarked image 推向 non-attackable region，可以更好地保留 clean accuracy。
