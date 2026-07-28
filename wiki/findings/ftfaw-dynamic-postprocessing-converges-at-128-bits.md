---
type: finding
title: "FTFAW Dynamic Post-Processing Converges at 128 Bits"
tags: [finding, ftfaw, watermark-robustness, fingerprint-capacity, training]
related: ["[[ftfaw]]", "[[pan-2025-ftfaw]]", "[[watermark-robustness]]", "[[watermark-capacity-for-user-attribution]]"]
created: 2026-07-20
updated: 2026-07-20
source: "[[pan-2025-ftfaw]]"
confidence: high
replicated: false
---

# FTFAW Dynamic Post-Processing Converges at 128 Bits

## Finding

Progressively increasing post-processing difficulty enables substantially higher reported fingerprint recovery than a static post-processing layer in FTFAW's 128-bit training experiment.

## Evidence

After 55,000 training steps at 128-bit capacity, the paper reports fingerprint accuracy `0.6109` with the static post-processing layer and `0.9865` with the dynamic layer. The dynamic layer begins with one low-intensity operation and increases attack intensity and variety after the extractor meets a threshold for consecutive batches.

## Interpretation

The result identifies curriculum-like robustness training as a capacity-enabling optimization in this method. It does not establish a general comparison across different watermark architectures or attack curricula.
