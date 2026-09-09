---
type: source
title: "SynTag: Enhancing the Geometric Robustness of Inversion-based Generative Image Watermarking"
tags: [latent-diffusion, watermarking, inversion, geometric-robustness, synchronization]
related: ["[[syntag]]", "[[ddim-inversion-for-watermark-detection]]", "[[watermark-robustness]]", "[[inversion-watermark-robustness-comparison]]", "[[syntag-restores-geometric-robustness-to-inversion-watermarks]]"]
created: 2026-09-08
updated: 2026-09-08
authors: ["Han Fang", "Kejiang Chen", "Zehua Ma", "Jiajun Deng", "Yicong Li", "Weiming Zhang", "Ee-Chien Chang"]
year: 2025
url: ""
venue: ""
sources: ["Fang 等 - 2025 - SynTag Enhancing the Geometric Robustness of Inversion-based Generative Image Watermarking/full.md"]
---

# SynTag: Enhancing the Geometric Robustness of Inversion-based Generative Image Watermarking

## One-line Takeaway

[[syntag]] augments inversion-based watermarks with a deliberately transformation-sensitive template so a predictor can estimate and reverse geometric distortion before watermark extraction.

## Method

A fine-tuned VAE decoder injects an imperceptible SynTag feature. A predictor estimates four transformed corner points, which define a homography for geometric correction. Pixel-level and latent-level dither compensation then search a small neighborhood before the original inversion watermark is extracted. The paper instantiates the wrapper with Gaussian Shading and Tree-Ring Watermarks.

## Evidence

Across Stable Diffusion v1.4 and v2.1, Table 1 reports GauShad-SynTag geometric TPR `0.980/0.988` and raw bit accuracy `0.938/0.940`; TreeRings-SynTag reports geometric TPR `0.928/0.932`. Table 6 raises geometric TPR from `0.016` without the predictor to `0.990` with the predictor and both compensation stages, while raw bit accuracy rises from `0.633` to `0.935`.

## Limitations and Caveats

- The main evaluation uses only 50 generated images, so the reported averages and very-low-FPR claims need larger held-out validation.
- The dither false-positive check uses 1,000 non-watermarked images and therefore does not empirically establish an FPR of `10^-6`.
- SynTag requires a fine-tuned decoder, a learned predictor, candidate search, and inversion; it is a compatibility layer for inversion-based methods rather than a standalone watermark payload.
- Strong purification eventually breaks detection: at noise strength `0.5`, TPR falls to `0.580`, and at `0.7` it reaches `0.000`, although attacked-image PSNR is also very low.
- Venue, DOI, and code URL are not present in the parse.

## Raw Source

- `raw/sources/Fang 等 - 2025 - SynTag Enhancing the Geometric Robustness of Inversion-based Generative Image Watermarking/full.md`

