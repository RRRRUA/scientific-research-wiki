---
type: finding
title: "LatentShield Multi-Objective Training Improves Composite-Attack Recovery"
tags: [finding, latentshield, multi-objective-optimization, composite-attacks]
related: ["[[bekkari-2026-latentshield]]", "[[latentshield]]", "[[watermark-robustness]]", "[[watermark-verification-operands]]"]
created: 2026-09-08
updated: 2026-09-08
source: "[[bekkari-2026-latentshield]]"
confidence: medium
replicated: false
---

# LatentShield Multi-Objective Training Improves Composite-Attack Recovery

## Finding

LatentShield reports that automatic loss-weight search contributes more composite-attack recovery than either adversarial or semantic-edit training alone, while the full combination performs best.

## Evidence

Table 12 reports raw bit accuracy of `71.2%` for fixed weights, `79.8%` with adversarial training, `76.5%` with semantic-edit training, `82.1%` with H-DFWA, and `84.2%` with all components under JPEG QF 70 plus 20% inpainting plus 15-degree rotation. PSNR remains between `43.85` and `44.27 dB` across the reported variants.

## Interpretation

This is a within-paper ablation, not independent replication. Confidence is medium because the paper contains separate numerical contradictions in its global-edit comparison and low-FPR validation.

