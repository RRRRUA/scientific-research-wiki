---
type: finding
title: "ROBIN++ Dual-Domain Synergy Improves Joint Verification"
tags: [finding, robin-plus-plus, dual-domain, tamper-localization, copyright]
related: ["[[huang-2026-robin-plus-plus]]", "[[robin-plus-plus]]", "[[tamper-localization-for-generated-images]]", "[[watermark-verification-operands]]", "[[localized-watermarking-for-tamper-localization-comparison]]"]
created: 2026-09-08
updated: 2026-09-08
source: "[[huang-2026-robin-plus-plus]]"
confidence: high
replicated: false
---

# ROBIN++ Dual-Domain Synergy Improves Joint Verification

## Finding

ROBIN++ reports that separating robust frequency evidence from fragile spatial evidence, then sharing them during verification, improves the joint copyright/localization operating point.

## Evidence

Table IV raises localization IoU from `0.543` without CAP to `0.947` with CAP and to `0.971` with Frequency-to-Spatial synergy. Spatial-to-Frequency refinement raises average copyright classification accuracy from `0.970` to `0.973`. Under combined degradation and tampering, the paper reports IoU `0.879` and verification accuracy `0.996`.

## Interpretation

The copyright value called `Bit Accuracy` is zero-bit binary classification accuracy, not multi-bit recovery. Localization IoU and copyright accuracy must therefore remain separate operands even when their branches cooperate.

