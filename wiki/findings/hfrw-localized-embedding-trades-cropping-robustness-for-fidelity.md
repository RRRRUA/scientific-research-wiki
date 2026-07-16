---
type: finding
title: "HFRW Localized Embedding Trades Cropping Robustness for Fidelity"
tags: [finding, hfrw, watermark-robustness, cropping, tradeoff]
related: ["[[hfrw]]", "[[ping-2026-hfrw]]", "[[watermark-robustness]]", "[[localized-invisible-watermarking]]"]
created: 2026-06-11
updated: 2026-07-16
source: "[[ping-2026-hfrw]]"
confidence: high
replicated: false
---

# HFRW Localized Embedding Trades Cropping Robustness for Fidelity

## Finding

HFRW maintains high bit accuracy under common attacks such as JPEG, color jitter, Gaussian noise, Gaussian blur, resize, padding, and PIP, but localized embedding has an inherent weakness against severe cropping.

## Evidence

Figure 7 reports HFRW at about 92-99 under JPEG quality 60-90, near 100 under color jitter and Gaussian noise, near 100 under resize and padding, and about 92-98 for PIP scale factors 1.4-2.0. Under crop attacks, performance falls from about 98 at crop ratio 0.05 to about 84 at 0.35.

The robustness discussion explains that HFRW embeds its watermark in a 128x128 patch. If that region is removed completely, no decoder can recover the watermark. The conclusion also identifies severe cropping as a limitation of the localized embedding strategy.

## Interpretation

This finding defines HFRW's boundary: local watermarking achieves very high fidelity and low FSVR, but it is less naturally robust than globally distributed watermarks to attacks that directly delete the embedding region.
