---
type: thesis
title: "Decoder-Rooted Fingerprinting Scales through Weight Encoding"
tags: [thesis, latent-diffusion, fingerprinting, scalability, user-attribution]
related: ["[[latent-diffusion-watermarking]]", "[[generative-model-fingerprinting]]", "[[stable-signature-detects-generated-images-at-low-fpr]]", "[[stable-signature-user-identification-degrades-with-scale-and-edits]]", "[[wouaf-generates-user-fingerprinted-models-under-one-second]]", "[[omnimark-generates-fingerprinted-model-copies-under-100-ms]]", "[[stableguard-unifies-watermark-verification-and-tamper-localization]]", "[[decoder-fingerprinting-scalability-comparison]]"]
created: 2026-06-09
updated: 2026-06-09
confidence: medium
status: supported
---

# Decoder-Rooted Fingerprinting Scales through Weight Encoding

## Thesis

Decoder-rooted watermarking 是 LDM provenance 的实用起点；但大规模 user attribution 更可能依赖 weight modulation 或 multi-dimensional weight encoding，而不是为每个用户单独 fine-tune decoder。

## 支持证据

- [[stable-signature-detects-generated-images-at-low-fpr]] 表明，把 signature root 到 latent decoder 可以在低 FPR 下检测生成图像。
- [[stable-signature-user-identification-degrades-with-scale-and-edits]] 表明，Stable Signature 可以做 user identification，但用户规模和 image edits 会提高阈值压力并降低 accuracy。
- [[wouaf-generates-user-fingerprinted-models-under-one-second]] 表明，weight modulation 可以把用户特定模型生成压到 `< 1 sec`。
- [[omnimark-generates-fingerprinted-model-copies-under-100-ms]] 表明，multi-dimensional weight encoding 可以进一步把 fingerprinted model-copy generation 压到 `<100 ms`。
- [[stableguard-unifies-watermark-verification-and-tamper-localization]] 表明，decoder/VAE-rooted watermarking 还可以支撑 proactive forensics，但这条证据主要服务 tamper localization，不直接证明 user attribution scalability。

## 反驳条件

如果后续论文或复现实验证明 decoder replacement、model distillation、LoRA fine-tuning 或 collusion 可以在不显著损害 image quality 的情况下稳定移除这些 fingerprints，那么这个 thesis 需要降级为“仅适用于弱攻击模型”。

## 当前信心

Medium。Stable Signature、WOUAF 和 OmniMark 的方向一致，但证据仍主要来自各自实验设置，缺少统一 benchmark、跨模型复现和真实平台级 attacker model。Tree-Ring 和 StableGuard 扩展了方法边界，但不能替代大规模 user attribution 的直接证据。
