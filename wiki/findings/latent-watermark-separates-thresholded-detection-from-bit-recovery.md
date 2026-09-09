---
type: finding
title: "Latent Watermark Separates Thresholded Detection from Bit Recovery"
tags: [finding, latent-watermark, bit-accuracy, detection, attribution]
related: ["[[meng-2024-latent-watermark]]", "[[latent-watermark]]", "[[user-attribution]]", "[[watermark-verification-operands]]"]
created: 2026-09-08
updated: 2026-09-08
source: "[[meng-2024-latent-watermark]]"
confidence: high
replicated: false
---

# Latent Watermark Separates Thresholded Detection from Bit Recovery

## Finding

Under the all-attack pipeline, Latent Watermark can cross a presence-detection threshold on every tested COCO image even though the recovered 64-bit messages are not exact.

## Evidence

Table 1 reports `90.00%` raw bit accuracy and `100%` TPR@0.01FPR for the 64-bit COCO all-attack setting. On Flickr30k, the corresponding values are `91.81%` and `99.74%`.

## Interpretation

Thresholded presence detection tolerates bit errors; exact user attribution does not. Reporting the TPR as perfect attribution would therefore change the task and the operand.

