---
type: finding
title: "TrustMark Noise Simulation Improves Robustness across Perturbations"
tags: [finding, trustmark, watermark-robustness, noise-simulation, adversarial-attacks]
related: ["[[bui-2023-trustmark]]", "[[trustmark]]", "[[watermark-robustness]]", "[[post-hoc-image-watermarking]]"]
created: 2026-07-06
updated: 2026-07-06
source: "[[bui-2023-trustmark]]"
confidence: high
replicated: false
---

# TrustMark Noise Simulation Improves Robustness across Perturbations

## Finding

[[bui-2023-trustmark]] reports that broad differentiable noise simulation helps TrustMark preserve bit accuracy under diverse image perturbations and increases resistance to I-FGSM-style adversarial attacks.

## Evidence

The TrustMark noise module uses three geometric transformations plus fifteen optional perturbation sources, and all eighteen transforms are differentiable. Table 1 reports noised bit accuracy around `0.95-0.97` for TrustMark-Q/B on CLIC, DIV2K, and MetFace.

Table 2 evaluates the ImageNet-C configuration on CLIC. TrustMark reports noised bit accuracy `0.95 +- 0.08`, compared with RoSteALS `0.94 +- 0.07`, StegaStamp `0.88 +- 0.13`, SSL `0.62 +- 0.14`, RivaGAN `0.77 +- 0.16`, and dwtDctSvd `0.61 +- 0.20`.

Figure 4 reports that high-severity noise simulation reduces PSNR from `53.2 dB` to `40.2 dB`, but bit accuracy drops by only `3%`. It also reports that, with high-level noise training, `32%` of watermarked images require more than `3000` I-FGSM iterations for a successful attack, while training without noise simulation requires fewer than `50` iterations for any watermarked image.

## Caveat

This is robustness against the paper's simulated perturbations and I-FGSM setup. It should not be treated as evidence for robustness against diffusion-native model attacks such as fine-tuning, distillation, or decoder replacement.
