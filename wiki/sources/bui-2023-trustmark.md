---
type: source
title: "TrustMark: Universal Watermarking for Arbitrary Resolution Images"
tags: [image-watermarking, post-hoc-watermarking, arbitrary-resolution, watermark-robustness, provenance]
related: ["[[trustmark]]", "[[post-hoc-image-watermarking]]", "[[arbitrary-resolution-image-watermarking]]", "[[watermark-robustness]]", "[[diffusion-model-fingerprinting-comparison]]", "[[trustmark-achieves-high-quality-watermarking-on-arbitrary-resolution-benchmarks]]", "[[trustmark-noise-simulation-improves-robustness-across-perturbations]]", "[[trustmark-rm-supports-high-quality-re-watermarking]]", "[[trustmark-architecture-components-improve-visual-quality]]"]
created: 2026-07-06
updated: 2026-07-06
authors: ["Tu Bui", "Shruti Agarwal", "John Collomosse"]
year: 2023
url: ""
venue: ""
sources: ["Bui 等 - 2023 - TrustMark Universal Watermarking for Arbitrary Resolution Images.pdf-28de830f-aa55-4f9a-b0ee-83e4bffaa789/full.md"]
---

# TrustMark: Universal Watermarking for Arbitrary Resolution Images

## One-line Takeaway

[[trustmark]] is a GAN-based [[post-hoc-image-watermarking]] method for arbitrary-resolution images. It combines a watermark embedder, a ResNet50 extractor, extensive differentiable noise simulation, focal frequency loss, and a residual-based resolution scaling algorithm; it also introduces TrustMark-RM for watermark removal and re-watermarking workflows.

## Problem

The paper frames imperceptible image watermarking as a content provenance mechanism for copyright protection, misinformation prevention, and responsible generative AI. It argues that signed provenance metadata such as C2PA manifests can be stripped during online redistribution, while many deep watermarking methods focus on fixed low resolutions and only a narrow set of perturbations.

The target gap is ordinary image watermarking for creative assets: high-resolution or arbitrary-resolution images need imperceptible watermarks that survive realistic image transformations and support re-watermarking as assets move through editing tools.

## Method

TrustMark contains three main pieces:

- Watermark embedder: early image-watermark fusion followed by a customized MUNIT-based network. The post-process module uses multiple `1 x 1` convolutions and SiLU activations to preserve high-frequency visual detail.
- Watermark extractor: a ResNet50 with the final layer replaced by a sigmoid-activated `l`-dimensional classifier for recovering the watermark bits.
- Noise module: three geometric transformations plus fifteen perturbation sources, including random flip, crop, resize, JPEG compression, brightness, hue, contrast, sharpness, color jitter, RGB shift, saturation, grayscale, several blur types, Gaussian noise, and posterize. The transforms are differentiable so recovery errors can backpropagate to the embedder.

The training loss balances binary cross-entropy watermark recovery with image quality losses in YUV, LPIPS, focal frequency loss (FFL), and GAN+gradient-penalty loss. The paper uses a staged training procedure that first prioritizes extractor accuracy, then unlocks random image batches, noise simulation, GAN loss, and a larger image-quality weight.

For arbitrary resolution, TrustMark runs the fixed `256 x 256` model on a resized image, computes a residual image, interpolates that residual back to the original `H x W`, and adds it to the original-resolution input. The same residual scaling procedure applies to TrustMark-RM, the KBNet-based watermark removal network.

## Evidence

Table 1 evaluates TrustMark-Q and TrustMark-B on CLIC, DIV2K, and MetFace. TrustMark-Q reports PSNR / SSIM of `43.26 / 0.99` on CLIC, `42.39 / 0.99` on DIV2K, and `45.34 / 0.99` on MetFace, with clean bit accuracy `1.00` and noised bit accuracy around `0.95-0.96`. TrustMark-B trades about 2 dB PSNR for higher noised bit accuracy, reporting `0.97` on all three benchmarks.

Table 2 uses the ImageNet-C noise configuration on CLIC. TrustMark reports PSNR `38.87 +- 1.42` and noised bit accuracy `0.95 +- 0.08`, compared with RoSteALS `32.68 +- 1.75 / 0.94 +- 0.07`, SSL `41.84 +- 0.10 / 0.62 +- 0.14`, and RivaGAN `40.32 +- 0.15 / 0.77 +- 0.16`.

Figure 4 reports that increasing watermark length from 32 to 200 bits drops PSNR by 7.5 dB and bit accuracy by 11%. The same figure reports that high-severity noise simulation reduces PSNR from 53.2 dB to 40.2 dB while bit accuracy drops by only 3%, and makes I-FGSM attacks harder: under high-level noise training, 32% of watermarked images require more than 3000 attack iterations.

Table 3 reports TrustMark-RM removal on DIV2K for TrustMark-B: PSNR `48.48`, SSIM `0.997`, and bit accuracy `0.553`; the I-FGSM comparison has PSNR `23.48`, SSIM `0.613`, and bit accuracy `0.629`.

Table 4 ablates TrustMark-B on DIV2K. With GAN, FFL, and the post-process module enabled, PSNR / SSIM / clean accuracy / noised accuracy are `40.203 / 0.987 / 0.999 / 0.973`. With all three disabled, the values are `36.300 / 0.976 / 0.991 / 0.959`; the paper summarizes the three components as contributing about 4 dB PSNR and 1.4% bit accuracy in total.

The arbitrary-resolution ablation reports that, across 20% to 100% of original DIV2K resolution, encoding PSNR varies by only `+-0.02 dB` and decoding bit accuracy varies by only `+-1e-4` on average.

## Key Results

- TrustMark is a strong post-hoc comparator for high-quality watermarking on arbitrary-resolution images.
- Resolution scaling makes fixed-resolution watermarking/removal networks operate at original image resolution by scaling residuals rather than final images.
- TrustMark-RM supports high-quality watermark removal for re-watermarking, but removal/re-watermarking remains a workflow feature rather than a provenance guarantee.
- Noise simulation improves robustness against diverse perturbations and I-FGSM-style adversarial attacks, but large payloads and cluttered high-frequency images remain harder cases.

## Limitations and Caveats

- TrustMark is not diffusion-native and does not bind provenance to a specific generator, user, or model copy.
- The paper evaluates post-hoc image watermarking and removal, not large-scale user attribution or traitor tracing.
- The paper reports cluttered images as the main weak cases, with slightly lower PSNR and extraction accuracy.
- Larger payloads reduce both image quality and bit accuracy.
- `full.md` does not parse a DOI, code URL, or formal venue, so those metadata fields are left blank.

## Use in This Project

TrustMark expands the post-hoc comparator set beyond hfrw and [[advmark]]. HFRW emphasizes local embedding and file-size/fidelity trade-offs; AdvMark emphasizes decoupled defense against regeneration and adversarial attacks; TrustMark emphasizes arbitrary-resolution deployment, broad perturbation robustness, and re-watermarking workflows.

## Raw Sources

- `raw/sources/Bui 等 - 2023 - TrustMark Universal Watermarking for Arbitrary Resolution Images.pdf-28de830f-aa55-4f9a-b0ee-83e4bffaa789/full.md`
- `raw/sources/Bui 等 - 2023 - TrustMark Universal Watermarking for Arbitrary Resolution Images.pdf-28de830f-aa55-4f9a-b0ee-83e4bffaa789/cf13de3c-3347-4a38-b427-80732392b45e_origin.pdf`

## Related Pages

- [[trustmark]]
- [[post-hoc-image-watermarking]]
- [[arbitrary-resolution-image-watermarking]]
- [[watermark-robustness]]
- [[diffusion-model-fingerprinting-comparison]]
