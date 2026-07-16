---
type: finding
title: "Stable Signature User Identification Degrades with Scale and Edits"
tags: [finding, stable-signature, user-identification, scalability, false-positive-rate]
related: ["[[fernandez-2023-stable-signature]]", "[[user-attribution]]", "[[how-to-scale-user-attribution-for-ldm]]", "[[decoder-fingerprinting-scalability-comparison]]"]
created: 2026-06-09
updated: 2026-07-16
source: "[[fernandez-2023-stable-signature]]"
confidence: high
replicated: false
---

# Stable Signature User Identification Degrades with Scale and Edits

## Finding

[[fernandez-2023-stable-signature]] supports user identification, but larger user populations and image edits substantially reduce identification accuracy.

## Evidence

The paper uses 48-bit signatures, fine-tunes `N' = 1000` models, generates 100 images per model, and extrapolates to larger user sets. At `N = 10^5`, it reports about 98% identification accuracy for unmodified images and about 40% under combined edits. As N grows, the threshold must rise to control global FPR, trading away detection and identification accuracy.

## Interpretation

This finding motivates the project's scalable user-attribution question. Stable Signature can root a fixed signature in the decoder, but if each user requires a separately fine-tuned model copy and thresholds tighten with user count, it is a foundation rather than a final platform-scale solution.

## Caveat

The reported identification results partly depend on extrapolation and do not cover repeated generation, user collusion, model redistribution, or long-term drift in a real platform.
