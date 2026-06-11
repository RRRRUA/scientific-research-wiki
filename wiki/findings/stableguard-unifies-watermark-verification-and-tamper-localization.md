---
type: finding
title: "StableGuard Unifies Watermark Verification and Tamper Localization"
tags: [finding, stableguard, tamper-localization, watermark-verification]
related: ["[[yang-2025-stableguard]]", "[[stableguard]]", "[[tamper-localization-for-generated-images]]", "[[diffusion-model-fingerprinting-comparison]]"]
created: 2026-06-09
updated: 2026-06-09
source: "[[yang-2025-stableguard]]"
confidence: high
replicated: false
---

# StableGuard Unifies Watermark Verification and Tamper Localization

## 发现

[[yang-2025-stableguard]] 把 diffusion-native watermarking 从 generated-image verification 扩展到 pixel-level tamper localization：同一个 embedded watermark signal 同时用于 copyright verification 和 tampered region detection。

## 证据

论文的 Table 5 将 StableGuard 标为同时支持 copyright protection、tampering localization、joint optimization，且 watermarking type 为 diffusion-native。Table 2 在 AIGC tampering dataset 上报告 StableGuard 对 SD Inpainting、SDXL、Kandinsky、ControlNet、LaMa 五类编辑的 F1 约 0.979-0.981、AUC 约 0.991-0.993、IoU 约 0.960-0.963。

## 解释

这说明 StableGuard 的贡献不只是更强的 watermark bit extraction，而是把 watermark 作为主动 forensic cue 使用。它在本 wiki 中应和 user attribution 路线区分开：它解决的是 copyright verification + tamper localization，而不是大规模 per-user attribution。
