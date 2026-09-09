---
type: source
title: "Latent Watermark: Inject and Detect Watermarks in Latent Diffusion Space"
tags: [latent-diffusion, watermarking, latent-space, user-attribution, robustness]
related: ["[[latent-watermark]]", "[[latent-diffusion-watermarking]]", "[[user-attribution]]", "[[watermark-robustness]]", "[[watermark-verification-operands]]", "[[latent-watermark-separates-thresholded-detection-from-bit-recovery]]"]
created: 2026-09-08
updated: 2026-09-08
authors: ["Zheling Meng", "Bo Peng", "Jing Dong"]
year: 2024
url: ""
venue: ""
sources: ["Meng 等 - 2024 - Latent Watermark Inject and Detect Watermarks in Latent Diffusion Space/full.md"]
---

# Latent Watermark: Inject and Detect Watermarks in Latent Diffusion Space

## One-line Takeaway

[[latent-watermark]] injects and decodes messages in VAE latent space and uses three-stage progressive training to weaken the usual coupling between pixel-space watermark strength and visible distortion.

## Method

A message encoder and coupler fuse bits into the first channel of the final diffusion latent. At verification, the ordinary VAE encoder maps the received image back to latent space, where a decoupler and message decoder recover the bits. The frozen Stable Diffusion v1.4 model is not fine-tuned.

The training sequence first learns message encoding and decoding, then initializes the coupler near an identity mapping, and finally optimizes latent distance, LPIPS, and message recovery jointly. The main run uses 50,000 LAION-Aesthetics images without augmentation or a noise layer.

## Evidence

The paper evaluates 5,000 COCO captions and 5,000 Flickr30k captions. For the 64-bit COCO setting, Table 1 reports clean raw bit accuracy `99.95%`, average single-attack raw bit accuracy `99.04%`, and all-attack raw bit accuracy `90.00%`. The corresponding thresholded TPR@0.01FPR values are `100%`, `100%`, and `100%`.

Under the nine individual COCO attacks, Table 2 reports 64-bit raw bit accuracy from `97.44%` to `99.93%`, including reconstruction by Stable Diffusion v2.1 and two learned VAEs.

## Limitations and Caveats

- A `90%` average bit recovery rate is not exact recovery of a 64-bit user identifier. The simultaneous `100%` TPR reflects thresholded presence detection, not perfect attribution.
- FID is defined between watermarked and same-prompt vanilla generations in this paper, rather than between generated and real-image distributions; it should not be compared blindly with conventional FID.
- The experiments use one Stable Diffusion version and do not evaluate white-box model replacement, collusion, or extractor-aware attacks.
- Venue, DOI, and code URL are not present in this parse.

## Raw Source

- `raw/sources/Meng 等 - 2024 - Latent Watermark Inject and Detect Watermarks in Latent Diffusion Space/full.md`

