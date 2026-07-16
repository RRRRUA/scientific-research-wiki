---
type: source
title: "StableGuard: Towards Unified Copyright Protection and Tamper Localization in Latent Diffusion Models"
tags: [latent-diffusion-models, watermarking, tamper-localization, copyright-protection, generative-ai-safety]
related: ["[[stableguard]]", "[[latent-diffusion-watermarking]]", "[[watermark-robustness]]", "[[tamper-localization-for-generated-images]]", "[[diffusion-model-fingerprinting-comparison]]"]
created: 2026-06-11
updated: 2026-07-16
authors: ["Haoxin Yang", "Bangzhen Liu", "Xuemiao Xu", "Cheng Xu", "Yuyang Yu", "Zikai Huang", "Yi Wang", "Shengfeng He"]
year: 2025
url: "https://github.com/Harxis/StableGuard"
venue: "NeurIPS 2025"
sources: ["Yang 等 - 2025 - StableGuard Towards Unified Copyright Protection and Tamper Localization in Latent Diffusion Model.pdf-d8a32816-0fa0-4c8d-934e-e96205ef30ed/full.md"]
---

# StableGuard: Towards Unified Copyright Protection and Tamper Localization in Latent Diffusion Models

## One-sentence Summary

StableGuard embeds a holistic binary watermark in the VAE decoder of Latent Diffusion Models and trains MoE-GFN to perform copyright verification and tamper localization from the same signal. It extends the project's scope from detection and user attribution to localized tamper forensics.

## Problem

Existing post-hoc watermarking requires extra processing after generation, which can add overhead and degrade image quality. Diffusion-native methods such as Stable Signature, WOUAF, and WaDiff improve embedding but generally do not address tamper localization. Methods such as EditGuard, OmniGuard, and WAM unify copyright protection with localization but remain post-hoc, so generation and forensics are not optimized end to end.

## Method

StableGuard contains two core components:

- Multiplexing Watermark VAE (MPW-VAE): adds a lightweight latent residual-based watermark adapter to a pretrained VAE decoder. The watermark is switchable, allowing the same latent code to produce paired watermarked and watermark-free images.
- Mixture-of-Experts Guided Forensic Network (MoE-GFN): adds Mixture-of-Forensic-Experts (MoFE) blocks to a UNet decoder. Expert branches process global watermark extraction, local tampering traces, and frequency-domain boundary cues, then a Dynamic Soft Router fuses them adaptively.

Training images combine a watermarked image and its watermark-free counterpart with random or SAM-generated semantic masks, requiring no manual tamper annotations. MPW-VAE and MoE-GFN are optimized jointly in a self-supervised, end-to-end process.

## Evidence

The paper trains on the COCO training set and evaluates on the COCO test set, a custom T2I dataset, and a 35,000-image AIGC tampering benchmark. The benchmark contains 25,000 COCO images and 10,000 T2I images, with SAM-masked regions edited by Stable Diffusion Inpainting, SDXL, Kandinsky, ControlNet, and LaMa.

Table 1 reports that 32-bit StableGuard reaches PSNR 40.50, SSIM 0.970, LPIPS 0.062, FID 19.5, and Bit Acc 99.97 on COCO; on the T2I dataset it reaches 40.53, 0.972, 0.060, 19.4, and 99.98.

Table 2 reports F1 around 0.979-0.981, AUC around 0.991-0.993, and IoU around 0.960-0.963 across five editing methods on the AIGC tampering dataset, generally above EditGuard, OmniGuard, WAM, and passive localization baselines.

In the Table 4 ablation, removing MPW-VAE reduces F1/AUC/IoU to 0.811/0.796/0.774; the full decoder-placement version reaches 0.980/0.992/0.961 with Bit Acc 99.98.

## Key Results

- Combines copyright protection and tamper localization in one diffusion-native framework.
- MPW-VAE generates paired watermarked and clean samples for tamper training without manual annotations.
- MoE-GFN fuses holistic watermark, local-trace, and boundary cues through expert branches.
- Reports stronger bit accuracy, image fidelity, AIGC tamper localization, and degradation robustness than major comparison methods.

## Limitations and Caveats

- StableGuard targets image latent diffusion models; transfer to video latent diffusion models is future work.
- Forensic accuracy still declines under image degradation, especially because tamper localization depends more on local consistency than watermark extraction.
- The method assumes images were watermarked during generation. Unwatermarked clean images are outside its operational scope and are conservatively treated as fully tampered.
- The work does not target large-scale user attribution and cannot directly answer per-user model-copy attribution studied by WOUAF and OmniMark.

## Use in This Project

StableGuard is the clearest paper in the corpus connecting diffusion-native watermarking with pixel-level tamper localization. It helps distinguish generated-image detection, user attribution, and tamper localization.

## Original Sources

- `raw/sources/Yang 等 - 2025 - StableGuard Towards Unified Copyright Protection and Tamper Localization in Latent Diffusion Model.pdf-d8a32816-0fa0-4c8d-934e-e96205ef30ed/full.md`
- `raw/sources/Yang 等 - 2025 - StableGuard Towards Unified Copyright Protection and Tamper Localization in Latent Diffusion Model.pdf-d8a32816-0fa0-4c8d-934e-e96205ef30ed/f2b07f79-3754-4fa0-9210-8643b5d674eb_origin.pdf`

## Related Pages

- [[stableguard]]
- [[latent-diffusion-watermarking]]
- [[watermark-robustness]]
- [[tamper-localization-for-generated-images]]
- [[diffusion-model-fingerprinting-comparison]]
