---
type: concept
title: "Watermark Capacity for User Attribution"
created: 2026-06-09
updated: 2026-09-08
tags: [watermark-capacity, user-attribution, false-positives, scalability]
related: ["[[user-attribution]]", "[[tree-ring-watermark]]", "[[generative-model-fingerprinting]]", "[[watermark-robustness]]", "[[watermark-verification-operands]]", "[[how-to-scale-user-attribution-for-ldm]]", "[[molm]]", "[[fei-2026-anti-collusion-fingerprinting]]"]
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

## New Capacity Evidence

[[fares-2026-molm]] obtains 28 bits from 14 routing layers with four adapter choices each. A 108-bit U-Net route is possible in the paper's construction but visibly degrades quality, showing that combinatorial address space is not automatically usable capacity.

[[fei-2026-anti-collusion-fingerprinting]] uses 48-bit codes and calculates a Hamming-bound capacity of `1.98 x 10^7` models at minimum distance 12. That is a theoretical allocation bound; the largest reported identification experiment samples `10^4` users and uses only 1,000 negative images.
