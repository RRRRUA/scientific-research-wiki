---
type: thesis
title: "Decoder-Rooted Fingerprinting Scales through Weight Encoding"
tags: [thesis, latent-diffusion, fingerprinting, scalability, user-attribution]
related: ["[[latent-diffusion-watermarking]]", "[[generative-model-fingerprinting]]", "[[stable-signature-detects-generated-images-at-low-fpr]]", "[[stable-signature-user-identification-degrades-with-scale-and-edits]]", "[[wouaf-generates-user-fingerprinted-models-under-one-second]]", "[[ftfaw-improves-fidelity-with-near-perfect-robustness]]", "[[ftfaw-traces-one-million-user-pool]]", "[[omnimark-generates-fingerprinted-model-copies-under-100-ms]]", "[[molm-routes-keys-without-per-key-retraining]]", "[[act-makes-colluded-fingerprint-models-unusable]]", "[[stableguard-unifies-watermark-verification-and-tamper-localization]]", "[[decoder-fingerprinting-scalability-comparison]]", "[[anti-collusion-model-distribution-comparison]]", "[[watermark-verification-operands]]"]
created: 2026-06-09
updated: 2026-09-08
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
- [[ftfaw-improves-fidelity-with-near-perfect-robustness]] shows that staged fine-tuning and adaptive loss weighting can substantially improve the reported visual fidelity of a decoder weight-modulation method while retaining high recovery.
- [[ftfaw-traces-one-million-user-pool]] adds sampled-pool tracing evidence at `10^6` users for a 48-bit decoder weight-modulation design.
- [[omnimark-generates-fingerprinted-model-copies-under-100-ms]] shows that multi-dimensional weight encoding can reduce fingerprinted model-copy generation to `<100 ms`.
- [[molm-routes-keys-without-per-key-retraining]] shows a second amortized route: combine a fixed set of LoRA markers into many binary routing keys without per-key training.
- [[act-makes-colluded-fingerprint-models-unusable]] shows that user-specific function-invariant transforms can turn model-parameter averaging into severe output-quality loss, although this is not colluder identification.
- [[stableguard-unifies-watermark-verification-and-tamper-localization]] shows that decoder/VAE-rooted watermarking can also support proactive forensics, but this evidence targets tamper localization rather than user-attribution scalability.

## Falsification Conditions

If later work or reproduction experiments show that decoder replacement, model distillation, LoRA fine-tuning, or collusion can reliably remove these fingerprints without substantial image-quality loss, this thesis should be downgraded to apply only under a weak attacker model.

## Current Confidence

Medium. Stable Signature, WOUAF, FTFAW, OmniMark, MOLM, and personalized-normalization evidence point toward amortized model personalization, but they use different payloads, candidate populations, and verification operands. The corpus still lacks a unified benchmark, cross-model reproduction, calibrated platform-scale false-positive control, and colluder identification. Tree-Ring and dual-task forensic methods broaden the design space but do not replace direct evidence for large-scale user attribution.
