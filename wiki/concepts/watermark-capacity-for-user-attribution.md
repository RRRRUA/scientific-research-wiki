---
type: concept
title: "Watermark Capacity for User Attribution"
created: 2026-06-09
updated: 2026-06-09
tags: [watermark-capacity, user-attribution, false-positives, scalability]
related: ["[[user-attribution]]", "[[tree-ring-watermark]]", "[[generative-model-fingerprinting]]", "[[watermark-robustness]]", "[[how-to-scale-user-attribution-for-ldm]]"]
sources: ["Wen 等 - 2023 - Tree-Ring Watermarks Fingerprints for Diffusion Images that are Invisible and Robust.pdf-009a7e2b-80bb-48a7-bf25-28b175fc8239/full.md"]
---

# Watermark Capacity for User Attribution

Watermark capacity for user attribution 指一个 watermarking / fingerprinting 方法能支持多少不同 keys、users 或 model copies，同时仍能控制 false positives、保持 image quality，并在攻击后可靠检测。

## 为什么重要

Generated-image detection 只问“这张图是否来自某类带水印模型”。[[user-attribution]] 要进一步回答“来自哪个用户、哪个 key 或哪个模型副本”。候选用户越多，检测器需要比较的 fingerprints 越多，false positive control 越严格。

## Tree-Ring 的开放问题

[[tree-ring-watermark]] 的 random 和 ring variants 比 zero key 更适合 multiple keys，因为它们可以生成不同 key patterns。但论文没有证明它能扩展到成千上万或更多用户，也没有完整分析多 key 阈值如何改变。

## 对当前 thesis 的影响

这支持本 wiki 的当前判断：robust provenance detection 可以由 initial-noise watermarking 实现，但大规模 user attribution 更可能需要 [[wouaf]]、[[omnimark]] 这类 weight modulation 或 multi-dimensional fingerprint encoding 路线。
