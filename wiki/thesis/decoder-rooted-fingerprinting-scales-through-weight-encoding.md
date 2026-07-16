---
type: thesis
title: "Decoder-Rooted Fingerprinting Scales through Weight Encoding"
tags: [thesis, latent-diffusion, fingerprinting, scalability, user-attribution]
related: ["[[latent-diffusion-watermarking]]", "[[generative-model-fingerprinting]]", "[[stable-signature-detects-generated-images-at-low-fpr]]", "[[stable-signature-user-identification-degrades-with-scale-and-edits]]", "[[wouaf-generates-user-fingerprinted-models-under-one-second]]", "[[omnimark-generates-fingerprinted-model-copies-under-100-ms]]", "[[stableguard-unifies-watermark-verification-and-tamper-localization]]", "[[decoder-fingerprinting-scalability-comparison]]"]
created: 2026-06-09
updated: 2026-07-16
confidence: medium
status: supported
---

# Decoder-Rooted Fingerprinting Scales through Weight Encoding

## Thesis

Decoder-rooted watermarking is a practical starting point for LDM provenance, but large-scale user attribution is more likely to depend on weight modulation or multi-dimensional weight encoding than on fine-tuning a separate decoder for every user.

## Supporting Evidence

- [[stable-signature-detects-generated-images-at-low-fpr]] shows that rooting a signature in the latent decoder can support generated-image detection at low FPR.
- [[stable-signature-user-identification-degrades-with-scale-and-edits]] shows that Stable Signature can identify users, but larger populations and image edits increase threshold pressure and reduce accuracy.
- [[wouaf-generates-user-fingerprinted-models-under-one-second]] shows that weight modulation can reduce user-specific model creation to `< 1 sec`.
- [[omnimark-generates-fingerprinted-model-copies-under-100-ms]] shows that multi-dimensional weight encoding can reduce fingerprinted model-copy generation to `<100 ms`.
- [[stableguard-unifies-watermark-verification-and-tamper-localization]] shows that decoder/VAE-rooted watermarking can also support proactive forensics, but this evidence targets tamper localization rather than user-attribution scalability.

## Falsification Conditions

If later work or reproduction experiments show that decoder replacement, model distillation, LoRA fine-tuning, or collusion can reliably remove these fingerprints without substantial image-quality loss, this thesis should be downgraded to apply only under a weak attacker model.

## Current Confidence

Medium. Stable Signature, WOUAF, and OmniMark point in the same direction, but their evidence comes mainly from separate experimental settings. The corpus lacks a unified benchmark, cross-model reproduction, and a realistic platform-scale attacker model. Tree-Ring and StableGuard broaden the design space but do not replace direct evidence for large-scale user attribution.
