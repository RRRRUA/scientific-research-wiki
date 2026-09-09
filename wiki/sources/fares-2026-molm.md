---
type: source
title: "MOLM: Mixture of LoRA Markers"
tags: [latent-diffusion, watermarking, lora, routing, user-attribution, flux]
related: ["[[molm]]", "[[generative-model-fingerprinting]]", "[[user-attribution]]", "[[watermark-capacity-for-user-attribution]]", "[[decoder-fingerprinting-scalability-comparison]]", "[[molm-routes-keys-without-per-key-retraining]]"]
created: 2026-09-08
updated: 2026-09-08
authors: ["Samar Fares", "Nurbek Tastan", "Noor Hussein", "Karthik Nandakumar"]
year: 2026
url: ""
venue: ""
sources: ["Fares 等 - 2026 - MOLM Mixture of LoRA Markers/full.md"]
---

# MOLM: Mixture of LoRA Markers

## One-line Takeaway

[[molm]] treats a binary key as a routing program that selects LoRA adapters across frozen-generator blocks, allowing new keys without key-specific retraining.

## Method

The default design routes 14 VAE-decoder ResNet blocks among four adapter choices per block, yielding a 28-bit key. A perceptual reconstruction loss compares watermarked and unwatermarked outputs generated from the same prompt and latent, while a key extractor supplies bit supervision. The paper evaluates Stable Diffusion v1.5 and FLUX.

## Evidence

On the Stable Diffusion MS-COCO setting, Table 1 reports clean raw bit accuracy `0.98`, crop `0.91`, rotation `0.84`, resize `0.90`, brightness `0.95`, and JPEG `0.89`. The same table reports FID `27.7`, SSIM `0.77`, and PSNR `23.5`; these operands are paired or distributional metrics as defined in the paper and should not be mixed.

Augmentation-trained extraction retains raw bit accuracy `0.82` after the strongest reported 100-step diffusion regeneration and `0.96` at the largest reported PGD budget. The prose reports at least `0.96` raw bit accuracy after sample-averaging removal with up to 5,000 images.

## Limitations and Caveats

- The default capacity is 28 bits. Routing the U-Net raises capacity to 108 bits but produces noticeable generation-quality degradation.
- The averaging experiment combines generated images to estimate a content-independent signal; it is not the model-parameter collusion attack studied by [[dai-2026-secure-distribution]] or [[fei-2026-anti-collusion-fingerprinting]].
- Thresholded TPR at 1% FPR and raw bit accuracy are reported in separate blocks and are not interchangeable.
- Venue, DOI, and a project URL are not present in the parse.

## Raw Source

- `raw/sources/Fares 等 - 2026 - MOLM Mixture of LoRA Markers/full.md`

