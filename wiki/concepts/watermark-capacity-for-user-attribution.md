---
type: concept
title: "Watermark Capacity for User Attribution"
created: 2026-06-09
updated: 2026-07-16
tags: [watermark-capacity, user-attribution, false-positives, scalability]
related: ["[[user-attribution]]", "[[tree-ring-watermark]]", "[[generative-model-fingerprinting]]", "[[watermark-robustness]]", "[[how-to-scale-user-attribution-for-ldm]]"]
sources: ["Wen 等 - 2023 - Tree-Ring Watermarks Fingerprints for Diffusion Images that are Invisible and Robust.pdf-009a7e2b-80bb-48a7-bf25-28b175fc8239/full.md"]
---

# Watermark Capacity for User Attribution

Watermark capacity for user attribution is the number of distinct keys, users, or model copies a watermarking or fingerprinting method can support while controlling false positives, preserving image quality, and remaining detectable after attacks.

## Why It Matters

Generated-image detection only asks whether an image came from a watermarked model family. [[user-attribution]] must also identify the user, key, or model copy. More candidate users require more fingerprint comparisons and stricter false-positive control.

## Open Question for Tree-Ring

The random and ring variants of [[tree-ring-watermark]] are better suited to multiple keys than the zero key because they can generate distinct key patterns. The paper does not establish scaling to thousands or more users and does not fully analyze how thresholds change under multi-key verification.

## Implication for the Current Thesis

This supports the wiki's current judgment: initial-noise watermarking can provide robust provenance detection, but large-scale user attribution is more likely to require weight modulation or multi-dimensional fingerprint encoding such as [[wouaf]] and [[omnimark]].
