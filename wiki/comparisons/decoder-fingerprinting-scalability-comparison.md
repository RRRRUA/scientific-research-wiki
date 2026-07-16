---
type: comparison
title: "Decoder Fingerprinting Scalability Comparison"
tags: [comparison, latent-diffusion, fingerprinting, scalability, user-attribution]
related: ["[[fernandez-2023-stable-signature]]", "[[kim-2024-wouaf]]", "[[fei-2025-omnimark]]", "[[yang-2025-stableguard]]", "[[stable-signature-user-identification-degrades-with-scale-and-edits]]", "[[wouaf-generates-user-fingerprinted-models-under-one-second]]", "[[omnimark-generates-fingerprinted-model-copies-under-100-ms]]", "[[stableguard-unifies-watermark-verification-and-tamper-localization]]", "[[decoder-rooted-fingerprinting-scales-through-weight-encoding]]"]
created: 2026-06-09
updated: 2026-07-16
---

# Decoder Fingerprinting Scalability Comparison

## Comparison Question

All three papers use the LDM decoder as the embedding site for a watermark or fingerprint, but they address user scale differently. Stable Signature establishes decoder-rooted watermarking, WOUAF turns a user fingerprint into decoder weight modulation, and OmniMark encodes a fingerprint across multiple weight dimensions.

## Cross-method Comparison

| Method | User-specific mechanism | Reported creation/distribution cost | Quality impact | Main risk |
| --- | --- | --- | --- | --- |
| [[fernandez-2023-stable-signature]] | Fine-tune the latent decoder for each signature | Decoder fine-tuning reported at roughly one minute | Small quality impact across tasks | Threshold rises with user count; identification accuracy drops substantially under combined edits |
| [[kim-2024-wouaf]] | A mapping network converts the user fingerprint into decoder weight modulation | WOUAF-conv and WOUAF-all report `< 1 sec` | CLIP/FID remain close to Original SD; decoder-only outperforms U-Net plus decoder modulation | Autoencoder compression, model purification, and strong blur still reduce attribution |
| [[fei-2025-omnimark]] | OmniMark layers encode a fingerprint across kernel, filter, channel, and spatial dimensions | `<100 ms` to construct fingerprinted convolution layers | About 99% Bit Acc for 48-bit fingerprints with less than one FID point increase | Fine-tuning attacks still threaten the fingerprint and require robustness training and threshold adjustment |

## Current Judgment

Stable Signature is the clearest foundation for showing that an LDM can carry an active provenance signal. For large-scale user attribution, WOUAF and OmniMark are closer to a deployment path because they replace per-user training with weight modulation or encoding.

## Key Differences

- Stable Signature's strength is its statistical detection framework and evidence for decoder-rooted watermarking.
- WOUAF's strength is distributor-oriented attribution and `< 1 sec` user-specific model creation.
- OmniMark's strength is `<100 ms` model-copy generation and multi-dimensional weight encoding.

## Unresolved Issues

None of the three papers fully addresses collusion, decoder replacement, model distillation, LoRA fine-tuning, key leakage, or access to multiple model copies in a realistic platform setting. These issues remain tracked in [[how-to-scale-user-attribution-for-ldm]].

## Adjacent but Distinct Routes

[[yang-2025-stableguard]] also modifies the VAE decoder, but its main task is copyright verification plus [[tamper-localization-for-generated-images]], not creating traceable model copies for many users. It provides evidence for decoder-rooted proactive forensics but should not enter the user-attribution scalability ranking directly. ping-2026-hfrw is post-hoc localized image watermarking and contributes only an external fidelity and robustness comparison.
