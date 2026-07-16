---
type: source
title: "Watermark Anything with Localized Messages"
tags: [image-watermarking, localized-watermarking, message-extraction, watermark-detection, tamper-localization]
related: ["[[watermark-anything]]", "[[localized-invisible-watermarking]]", "[[tamper-localization-for-generated-images]]", "[[watermark-robustness]]", "[[localized-watermarking-for-tamper-localization-comparison]]", "[[watermark-anything-decodes-localized-messages-from-small-regions]]"]
created: 2026-07-16
updated: 2026-07-16
authors: ["Tom Sander", "Pierre Fernandez", "Alain Durmus", "Teddy Furon", "Matthijs Douze"]
year: 2025
url: "https://github.com/facebookresearch/watermark-anything"
venue: ""
sources: ["Sander 等 - 2025 - Watermark Anything with Localized Messages/full.md"]
---

# Watermark Anything with Localized Messages

## One-line Takeaway

[[watermark-anything]] (WAM) reframes image watermarking as pixel-level detection and decoding, enabling localization of watermarked areas and recovery of multiple distinct messages in one image.

## Problem

Conventional watermarking makes one global detection or decoding decision per image and weakens when only a small surface is watermarked or when watermarked regions are spliced. The paper targets localized, multi-message provenance while retaining ordinary watermark robustness and imperceptibility.

## Method

WAM jointly trains an embedder and extractor. The extractor predicts a pixel-level detection mask and a message-bit vector for each pixel. Its two-phase training first targets low-resolution robustness with masked augmentations, then post-trains for imperceptibility and multiple messages. DBSCAN clusters decoded pixel messages without requiring the number of watermarks in advance.

## Evidence

The paper reports that five separate 32-bit messages, each occupying no more than 10% of an image, achieve more than `85%` mIoU for watermarked-area detection and over `95%` bit accuracy after horizontal flip and contrast adjustment. Table 8 reports WAM bit accuracy `100.0`, `91.8`, `100.0`, and `95.30` for no attack, geometric, valuemetric, and splicing aggregates, with PSNR/SSIM/LPIPS `38.3/0.99/0.04`.

Table 7 reports WAM detection TPR `99.9%` and bit accuracy `94.2%` when a watermarked region occupies 10% of the image, and TPR `100.0%` with bit accuracy `96.5%` for a 10% collage condition.

## Limitations and Caveats

- WAM's extractor can show visible patterns in very white, very dark, or strongly textured regions.
- JPEG applied on top of geometric/contrast transformations complicates multi-message clustering.
- Diffusion purification remains an effective challenge; WAM trades VAE-attack robustness for localized geometric robustness.

## Use in This Project

WAM bridges image-level provenance and localized forensics: it can detect, decode, and spatially assign watermark evidence without relying on a fixed localization tag.

## Raw Sources

- `raw/sources/Sander 等 - 2025 - Watermark Anything with Localized Messages/full.md`

## Related Pages

- [[watermark-anything]]
- [[localized-invisible-watermarking]]
- [[localized-watermarking-for-tamper-localization-comparison]]
