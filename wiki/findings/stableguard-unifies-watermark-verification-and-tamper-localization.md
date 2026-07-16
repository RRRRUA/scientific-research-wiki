---
type: finding
title: "StableGuard Unifies Watermark Verification and Tamper Localization"
tags: [finding, stableguard, tamper-localization, watermark-verification]
related: ["[[yang-2025-stableguard]]", "[[stableguard]]", "[[tamper-localization-for-generated-images]]", "[[diffusion-model-fingerprinting-comparison]]"]
created: 2026-06-09
updated: 2026-07-16
source: "[[yang-2025-stableguard]]"
confidence: high
replicated: false
---

# StableGuard Unifies Watermark Verification and Tamper Localization

## Finding

[[yang-2025-stableguard]] extends diffusion-native watermarking from generated-image verification to pixel-level tamper localization: the same embedded watermark signal supports both copyright verification and tampered-region detection.

## Evidence

Table 5 marks StableGuard as supporting copyright protection, tampering localization, and joint optimization with a diffusion-native watermarking type. On the AIGC tampering dataset, Table 2 reports F1 around 0.979-0.981, AUC around 0.991-0.993, and IoU around 0.960-0.963 across SD Inpainting, SDXL, Kandinsky, ControlNet, and LaMa edits.

## Interpretation

StableGuard contributes more than stronger watermark-bit extraction; it uses the watermark as an active forensic cue. The wiki should keep it separate from user-attribution methods because it targets copyright verification plus tamper localization rather than large-scale per-user attribution.
