---
type: finding
title: "Stable Signature Detects Generated Images at Low FPR"
tags: [finding, stable-signature, detection, false-positive-rate, latent-diffusion]
related: ["[[fernandez-2023-stable-signature]]", "[[latent-diffusion-watermarking]]", "[[watermark-robustness]]", "[[decoder-rooted-fingerprinting-scales-through-weight-encoding]]"]
created: 2026-06-09
updated: 2026-07-16
source: "[[fernandez-2023-stable-signature]]"
confidence: high
replicated: false
---

# Stable Signature Detects Generated Images at Low FPR

## Finding

[[fernandez-2023-stable-signature]] reports that Stable Signature can detect text-to-image generated images at a very low false positive rate (FPR).

## Evidence

The paper generates images from MS-COCO prompts and performs detection with a 48-bit signature and a binomial statistical test. It reports about 99% detection for unmodified images at `FPR = 10^-9`, about 84% when cropping retains only 10% of the image, and about 65% under combined transformations.

## Interpretation

This result supports the foundational value of decoder-rooted watermarking. The latent decoder writes the watermark directly during generation instead of adding it afterward, making it better suited than passive forensic detection or post-hoc watermarking as a provenance signal under low-FPR requirements.

## Caveat

These are reported paper results, not project reproductions. The extreme low-FPR range depends mainly on the binomial model and the paper's empirical check; platform deployment still requires independent validation of bit independence and threshold stability.
