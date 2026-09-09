---
type: source
title: "A Robust Latent Watermarking Framework for Diffusion-Generated Images with Multi-Objective Optimization"
tags: [latent-diffusion, watermarking, latent-space, multi-objective-optimization, semantic-editing]
related: ["[[latentshield]]", "[[latent-diffusion-watermarking]]", "[[watermark-robustness]]", "[[user-attribution]]", "[[watermark-verification-operands]]", "[[latentshield-multi-objective-training-improves-composite-attack-recovery]]"]
created: 2026-09-08
updated: 2026-09-08
authors: ["Fouad Bekkari", "Sayah Moad", "Khaldi Amine", "Akram Boukhamla", "Kafi Redouane Aditya Kumar Sahu"]
year: 2026
url: ""
venue: ""
sources: ["Bekkari 等 - 2026 - A robust latent watermarking framework for diffusion-generated images with multi-objective optimizat/full.md"]
---

# A Robust Latent Watermarking Framework for Diffusion-Generated Images with Multi-Objective Optimization

## One-line Takeaway

[[latentshield]] injects a 64-bit message through a learnable projection in VAE latent space, trains an extractor against conventional and semantic edits, and uses H-DFWA to select loss weights across fidelity, clean recovery, and robustness objectives.

## Method

The pre-trained Stable Diffusion v2.1 network is left unchanged. A bipolar message is projected into selected latent channels with strength alpha, after which the ordinary diffusion and VAE decoding path produces the image. A CNN extractor is trained with conventional, geometric, semantic-edit, composite, and PGD simulations. H-DFWA searches the three loss weights before final training.

## Evidence

The paper evaluates 64-bit messages on COCO, ImageNet, and MedPix. On COCO, Table 6 reports `44.27 dB` PSNR and FID `25.18` versus `24.90` for the unwatermarked model. Table 7 reports raw bit accuracy of `99.92%` for JPEG QF 50, `97.83%` for 30-degree rotation, and `96.31%` after 20% cropping. Table 9 reports `84.19%` raw bit accuracy for JPEG plus inpainting plus rotation.

The ablation in Table 12 raises composite-attack bit accuracy from `71.2%` with fixed weights to `82.1%` with H-DFWA alone and `84.2%` with the full system. The reported one-time H-DFWA search costs about `110 GPU hours`, in addition to `18 GPU hours` for final training.

## Limitations and Internal Consistency

- Table 8 gives PPGS `89.20%` and LatentShield `88.41%` under global instruction editing, while the surrounding prose says LatentShield outperforms PPGS and gives incompatible margins. The table is retained as the primary numeric evidence.
- The claimed empirical FPR of `0.95 x 10^-6` from 100,000 negative images cannot be directly resolved by a count whose smallest non-zero rate is `10^-5`; treat the low-FPR value as model-based or insufficiently evidenced, not as confirmed empirical calibration.
- The INNA removal attack lowers bit accuracy from `100%` to `71.8%` according to the limitations section.
- The author boundary between `Kafi Redouane` and `Aditya Kumar Sahu` is unclear in the parse; frontmatter preserves the parsed string rather than guessing.
- Venue, DOI, and code URL are not present in the parse.

## Raw Source

- `raw/sources/Bekkari 等 - 2026 - A robust latent watermarking framework for diffusion-generated images with multi-objective optimizat/full.md`

