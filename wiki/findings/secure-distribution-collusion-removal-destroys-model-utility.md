---
type: finding
title: "Secure Distribution Collusion Removal Destroys Model Utility"
tags: [finding, secure-distribution, anti-collusion, latent-diffusion, watermarking]
related: ["[[secure-distribution]]", "[[dai-2026-secure-distribution]]", "[[user-attribution]]", "[[watermark-robustness]]"]
created: 2026-07-16
updated: 2026-07-16
source: "[[dai-2026-secure-distribution]]"
confidence: high
replicated: false
---

# Secure Distribution Collusion Removal Destroys Model Utility

## Finding

In the reported nonlinear collusion experiments, Secure Distribution reduces watermark recovery to near random guessing only together with severe output-quality degradation.

## Evidence

Table 4 reports watermark extraction accuracies from `49.11%` to `52.04%` after random, power-mean, and max-absolute-value collusion. The same attacks yield PSNR from `5.98` to `6.72 dB` and LPIPS about `0.84-0.85`. The paper treats those quality levels as unusable outputs.

## Interpretation

This is anti-collusion deterrence rather than traitor tracing: it argues that watermark removal by the evaluated merges forfeits model utility, but does not identify the colluding users.
