---
type: comparison
title: "Decoder Fingerprinting Scalability Comparison"
tags: [comparison, latent-diffusion, fingerprinting, scalability, user-attribution]
related: ["[[fernandez-2023-stable-signature]]", "[[kim-2024-wouaf]]", "[[pan-2025-ftfaw]]", "[[fei-2025-omnimark]]", "[[fares-2026-molm]]", "[[fei-2026-anti-collusion-fingerprinting]]", "[[yang-2025-stableguard]]", "[[stable-signature-user-identification-degrades-with-scale-and-edits]]", "[[wouaf-generates-user-fingerprinted-models-under-one-second]]", "[[ftfaw-improves-fidelity-with-near-perfect-robustness]]", "[[ftfaw-traces-one-million-user-pool]]", "[[omnimark-generates-fingerprinted-model-copies-under-100-ms]]", "[[molm-routes-keys-without-per-key-retraining]]", "[[act-makes-colluded-fingerprint-models-unusable]]", "[[anti-collusion-model-distribution-comparison]]", "[[watermark-verification-operands]]", "[[decoder-rooted-fingerprinting-scales-through-weight-encoding]]"]
created: 2026-06-09
updated: 2026-09-08
---

# Decoder Fingerprinting Scalability Comparison

## Comparison Question

Six core designs personalize a decoder or adjacent generative weights, but they scale by different mechanisms. Stable Signature fine-tunes one decoder per signature; WOUAF and FTFAW learn fingerprint-conditioned decoder modulation; OmniMark directly encodes several decoder-weight dimensions; MOLM routes a key through combinations of LoRA markers; and Fei et al. (2026) personalize VAE normalization before adding anti-collusion transforms.

## Cross-method Comparison

| Method | User-specific mechanism | Reported creation/distribution cost | Quality impact | Main risk |
| --- | --- | --- | --- | --- |
| [[fernandez-2023-stable-signature]] | Fine-tune the latent decoder for each signature | Decoder fine-tuning reported at roughly one minute | Small quality impact across tasks | Threshold rises with user count; identification accuracy drops substantially under combined edits |
| [[kim-2024-wouaf]] | A mapping network converts the user fingerprint into decoder weight modulation | WOUAF-conv and WOUAF-all report `< 1 sec` | CLIP/FID remain close to Original SD; decoder-only outperforms U-Net plus decoder modulation | Autoencoder compression, model purification, and strong blur still reduce attribution |
| [[pan-2025-ftfaw]] | Weight modulation of all decoder convolution layers, trained with freeze-then-joint fine-tuning | Single trained mapping network supports user-specific modulation; explicit per-copy timing not reported | Table II reports substantially higher PSNR/SSIM and lower LPIPS than WOUAF-Robust while retaining near-perfect attacked recovery | Reports sampled-pool tracing, not full operational attribution; collusion and model replacement are not evaluated |
| [[fei-2025-omnimark]] | OmniMark layers encode a fingerprint across kernel, filter, channel, and spatial dimensions | `<100 ms` to construct fingerprinted convolution layers | About 99% raw BitAcc for 48-bit fingerprints with less than one FID point increase | Fine-tuning attacks still threaten the fingerprint and require robustness training and threshold adjustment |
| [[fares-2026-molm]] | A binary key selects one LoRA marker from each frozen-generator routing block | One trained marker mixture represents combinatorial keys without per-key retraining | The 28-bit SD configuration reports `0.98` clean raw BitAcc and FID `27.7`; a 108-bit U-Net route visibly worsens quality | Capacity is architectural, while the reported sample-averaging attack is not model-parameter collusion |
| [[fei-2026-anti-collusion-fingerprinting]] | A 48-bit personalized normalization module is combined with user-specific channel transforms | Personalized modules and transforms create model copies; end-to-end per-copy latency is not reported | Uncolluded copies report about `99.5%` raw BitAcc | Equal-weight collusion is deterred mainly by severe utility loss, and the method does not identify colluders |

## Current Judgment

Stable Signature remains the clearest foundation for showing that an LDM decoder can carry an active provenance signal. WOUAF, FTFAW, OmniMark, and MOLM move closer to large-scale distribution by amortizing personalization through modulation, direct encoding, or compositional routing. The Fei et al. anti-collusion design adds an orthogonal requirement: colluded model copies should either retain traceable signals or lose useful generation quality.

## Key Differences

- Stable Signature's strength is its statistical detection framework and evidence for decoder-rooted watermarking.
- WOUAF's strength is distributor-oriented attribution and `< 1 sec` user-specific model creation.
- FTFAW's strength is staged optimization of the fidelity-robustness trade-off, with sampled-pool results up to `10^6` users.
- OmniMark's strength is `<100 ms` model-copy generation and multi-dimensional weight encoding.
- MOLM's strength is combinatorial key routing without retraining a separate model for every key, but its reported 28-bit operating point is smaller than several 48- or 64-bit payloads.
- The Fei et al. PNM-ACT design targets white-box model-copy collusion, but its positive result is utility destruction rather than colluder identification.

## Unresolved Issues

No method jointly demonstrates platform-scale distribution, calibrated global false-positive control, useful colluded outputs, and colluder identification. Sampled user-pool retrieval, raw BitAcc, and TPR at a fixed FPR are different operands and should be reported separately; see [[watermark-verification-operands]]. Model-collusion evidence is compared in [[anti-collusion-model-distribution-comparison]], while the broader deployment gaps remain tracked in [[how-to-scale-user-attribution-for-ldm]].

## Adjacent but Distinct Routes

[[yang-2025-stableguard]] also modifies the VAE decoder, but its main task is copyright verification plus [[tamper-localization-for-generated-images]], not creating traceable model copies for many users. It provides evidence for decoder-rooted proactive forensics but should not enter the user-attribution scalability ranking directly. ping-2026-hfrw is post-hoc localized image watermarking and contributes only an external fidelity and robustness comparison.
