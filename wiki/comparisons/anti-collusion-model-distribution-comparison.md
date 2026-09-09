---
type: comparison
title: "Anti-Collusion Model Distribution Comparison"
tags: [comparison, anti-collusion, model-distribution, fingerprinting, user-attribution]
related: ["[[dai-2026-secure-distribution]]", "[[fei-2026-anti-collusion-fingerprinting]]", "[[fares-2026-molm]]", "[[secure-distribution-collusion-removal-destroys-model-utility]]", "[[act-makes-colluded-fingerprint-models-unusable]]", "[[how-to-scale-user-attribution-for-ldm]]"]
created: 2026-09-08
updated: 2026-09-08
sources: ["Dai 等 - 2026 - Secure Distribution Anti-Collusion Watermarking via Spectral Weight Modulation in Latent Diffusion Models/full.md", "Fei 等 - 2026 - Efficient, Robust, and Anti-Collusion Fingerprinting of Image Diffusion Models/full.md", "Fares 等 - 2026 - MOLM Mixture of LoRA Markers/full.md"]
---

# Anti-Collusion Model Distribution Comparison

## Comparison

| Work | Protected object | Attack operand | Defensive mechanism | Reported result | Boundary |
| --- | --- | --- | --- | --- | --- |
| [[dai-2026-secure-distribution]] | User-specific LDM copies | Parameter merging of white-box models | Lie-group LoRA plus paired Spectral Weight Modulation | Nonlinear merges push raw bit recovery near random while PSNR falls below `7 dB` | Utility destruction, not colluder identification |
| [[fei-2026-anti-collusion-fingerprinting]] | PNM-personalized VAE decoders | Linear and nonlinear parameter merging | Function-invariant channel permutation, scaling, and sign flip | Two-party averaging raises FID to `79.51`; nonlinear merges produce PSNR `5.21-6.24 dB` | Utility destruction, not traitor tracing |
| [[fares-2026-molm]] | Images emitted through routed LoRA adapters | Averaging many generated images to estimate a watermark signal | Key-dependent distributed routing | Removal raw bit accuracy remains at least `0.96` through 5,000 averaged images in the reported test | Sample averaging is not model-parameter collusion |

## Synthesis

The first two works intentionally make a merged model unusable. They do not recover the colluder set. MOLM addresses a different averaging attack whose operands are output images, so its result cannot be used as evidence that routed model copies resist parameter interpolation.

## Evaluation Requirements

A fair anti-collusion study must state whether attackers combine model parameters or generated samples, whether success means retained watermark recovery or destroyed utility, and whether the verifier identifies one user, all colluders, or only the presence of a registered code.

