---
type: finding
title: "StableGuard Maintains Watermark Accuracy under Degradation and Tampering"
tags: [finding, stableguard, watermark-robustness, bit-accuracy, image-degradation]
related: ["[[yang-2025-stableguard]]", "[[stableguard]]", "[[watermark-robustness]]"]
created: 2026-06-09
updated: 2026-07-16
source: "[[yang-2025-stableguard]]"
confidence: high
replicated: false
---

# StableGuard Maintains Watermark Accuracy under Degradation and Tampering

## Finding

[[yang-2025-stableguard]] reports that StableGuard maintains high Bit Acc for watermark extraction across tampering ratios and common image degradations, while tamper-localization F1 is more affected by compression, downsampling, and similar degradation.

## Evidence

Table 8 reports StableGuard watermark extraction accuracy of 99.98, 99.98, 99.96, 99.27, and 89.58 as tampering ratio increases from 10% to 90% on the AIGC tampering dataset, above EditGuard, OmniGuard, and WAM.

Table 3 reports higher Bit Acc/F1 than comparison methods under Gaussian noise, JPEG compression, and Poisson noise; for example, 99.73/0.908 at JPEG Q=70. Under stronger real-world degradations in Table 11, StableGuard reaches 98.87/0.866 at JPEG Q=30 and 98.95/0.703 at WebP Q=50.

## Caveat

The paper explicitly states that image degradation reduces forensic accuracy. This finding should not be read as an unremovable watermark; it means bit extraction is more robust than localization within the evaluated degradation range.
