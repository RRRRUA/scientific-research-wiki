---
type: overview
title: "Wiki Index"
tags: [index, research-wiki]
related: ["[[overview]]", "[[diffusion-model-fingerprinting-comparison]]"]
created: 2026-06-11
updated: 2026-06-11
---

# Wiki Index

## Overview

- [[overview]] — 项目概览、阅读路径、当前结论和待跟踪问题。
- [[log]] — wiki 维护日志。

## Entities

- [[stable-signature]] — Stable Signature 方法实体。
- [[tree-ring-watermark]] — Tree-Ring Watermarking 方法实体。
- [[wouaf]] — WOUAF 方法实体。
- [[omnimark]] — OmniMark 方法实体。
- [[stableguard]] — StableGuard 方法实体。
- [[hfrw]] — HFRW 方法实体。

## Concepts

- [[generative-model-fingerprinting]] — 生成模型指纹识别，用于检测、溯源和归因。
- [[latent-diffusion-watermarking]] — Latent Diffusion Models 中的 watermark / fingerprint 嵌入机制。
- [[user-attribution]] — 将生成图像追溯到具体用户、key 或模型副本。
- [[watermark-robustness]] — 水印或指纹对图像变换、模型攻击和退化的鲁棒性。
- [[ddim-inversion-for-watermark-detection]] — 用 DDIM inversion 恢复初始 noise 并检测 watermark key。
- [[fourier-noise-watermarking]] — 在 initial noise 的 Fourier coefficients 中嵌入 watermark。
- [[private-vs-public-watermark-verification]] — 私有验证与公开验证的部署差异。
- [[watermark-capacity-for-user-attribution]] — 多 key / 多用户归因容量与 false positive control。
- [[tamper-localization-for-generated-images]] — 生成图像中的篡改区域定位。
- [[localized-invisible-watermarking]] — 局部不可见图像水印及其 fidelity / robustness 取舍。

## Sources

- [[fernandez-2023-stable-signature]] — Stable Signature: Rooting watermarks in latent diffusion models。
- [[wen-2023-tree-ring-watermarks]] — Tree-Ring Watermarks: Fingerprints for Diffusion Images that are Invisible and Robust。
- [[kim-2024-wouaf]] — WOUAF: Weight Modulation for User Attribution and Fingerprinting。
- [[fei-2025-omnimark]] — OmniMark: Efficient and Scalable Latent Diffusion Model Fingerprinting。
- [[yang-2025-stableguard]] — StableGuard: Copyright protection and tamper localization in LDMs。
- [[ping-2026-hfrw]] — HFRW: High Fidelity and Robust Watermarking using Deep Reinforcement Learning。

## Queries

- [[how-to-scale-user-attribution-for-ldm]] — LDM 的用户归因如何扩展到大规模用户？

## Comparisons

- [[decoder-fingerprinting-scalability-comparison]] — Stable Signature、WOUAF、OmniMark 的 decoder-rooted user-attribution scalability 对比。

## Synthesis

- [[diffusion-model-fingerprinting-comparison]] — 当前论文的方法谱系、任务边界和证据索引。

## Thesis

- [[decoder-rooted-fingerprinting-scales-through-weight-encoding]] — 大规模 user attribution 更可能依赖 weight modulation 或 multi-dimensional weight encoding。

## Findings

- [[stable-signature-detects-generated-images-at-low-fpr]] — Stable Signature 在低 false positive rate 下检测生成图像。
- [[stable-signature-user-identification-degrades-with-scale-and-edits]] — Stable Signature 的 user identification 会随用户规模和 image edits 下降。
- [[wouaf-generates-user-fingerprinted-models-under-one-second]] — WOUAF 报告小于 1 秒生成用户指纹模型。
- [[wouaf-decoder-only-modulation-preserves-quality-better]] — WOUAF decoder-only modulation 比 U-Net + decoder modulation 更保质量。
- [[omnimark-generates-fingerprinted-model-copies-under-100-ms]] — OmniMark 报告小于 100 ms 生成 fingerprinted model copies。
- [[omnimark-maintains-high-bit-accuracy-with-low-quality-impact]] — OmniMark 在 48-bit fingerprints 下保持高 Bit Acc 与低质量影响。
- [[stableguard-unifies-watermark-verification-and-tamper-localization]] — StableGuard 统一 copyright verification 与 tamper localization。
- [[stableguard-mpw-vae-enables-self-supervised-tamper-training]] — StableGuard 的 MPW-VAE 支撑 self-supervised tamper training。
- [[stableguard-maintains-watermark-accuracy-under-degradation-and-tampering]] — StableGuard 在 tampering ratio 与 image degradation 下保持较高 watermark accuracy。
- [[hfrw-local-watermarking-improves-fidelity-and-file-size-growth]] — HFRW 的局部水印显著改善 fidelity 和 file size growth。
- [[hfrw-rl-patch-selection-improves-embedding-quality]] — HFRW 的 RL patch selection 提升嵌入质量。
- [[hfrw-localized-embedding-trades-cropping-robustness-for-fidelity]] — HFRW 用 cropping robustness 换取高 fidelity 和低 FSVR。

## References

- [[reference-database]] — 从论文 raw parses 抽取的参考文献数据库。
- [[recommendations]] — 后续阅读建议；仅保留可靠、可解释的推荐。
