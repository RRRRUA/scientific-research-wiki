---
type: finding
title: "OmniMark Generates Fingerprinted Model Copies under 100 ms"
tags: [finding, omnimark, scalability, latent-diffusion, model-fingerprinting]
related: ["[[fei-2025-omnimark]]", "[[generative-model-fingerprinting]]", "[[user-attribution]]", "[[how-to-scale-user-attribution-for-ldm]]", "[[decoder-fingerprinting-scalability-comparison]]"]
created: 2026-06-09
updated: 2026-07-16
source: "[[fei-2025-omnimark]]"
confidence: high
replicated: false
---

# OmniMark Generates Fingerprinted Model Copies under 100 ms

## Finding

[[fei-2025-omnimark]] reports that OmniMark rapidly creates LDM model copies with unique fingerprints without retraining for each user.

## Evidence

The OmniMark abstract reports scalable ad-hoc generation in `<100 ms` after changing fingerprints and re-encoding weights. The contribution section further states that a single forward pass constructs standardized fingerprinted convolution layers in under 100 ms without increasing user inference cost.

## Interpretation

This makes OmniMark the most directly platform-oriented distribution method among the three papers: it encodes user-specific identity across multiple decoder-weight dimensions instead of relying on per-user fine-tuning for scalability.

## Caveat

`<100 ms` measures the computation for constructing fingerprinted layers. Platform deployment still requires evaluation of model-copy management, verifier throughput, key lifecycle, and collusion risk when an attacker obtains multiple copies.
