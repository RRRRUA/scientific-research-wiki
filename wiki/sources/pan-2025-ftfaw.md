---
type: source
title: "FTFAW: A Novel Fingerprinting Method for Latent Diffusion Model Based on Two-Stage Fine-Tuning and Adaptive Loss Weighting"
tags: [latent-diffusion, model-fingerprinting, watermarking, user-attribution, weight-modulation, image-quality]
related: ["[[ftfaw]]", "[[latent-diffusion-watermarking]]", "[[user-attribution]]", "[[watermark-robustness]]", "[[decoder-fingerprinting-scalability-comparison]]", "[[diffusion-model-fingerprinting-comparison]]", "[[ftfaw-improves-fidelity-with-near-perfect-robustness]]", "[[ftfaw-traces-one-million-user-pool]]", "[[ftfaw-dynamic-postprocessing-converges-at-128-bits]]"]
created: 2026-07-20
updated: 2026-07-20
authors: ["Jiajun Pan", "Mouke Mo", "Chuntao Wang", "Shan Bian", "Xinpeng Zhang"]
year: 2025
url: ""
venue: ""
sources: ["Pan 等 - 2025 - FTFAW A Novel Fingerprinting Method for Latent Diffusion Model Based on Two-Stage Fine-Tuning and Adaptive Loss Weighting.pdf-82d05c36-ca8b-42e6-b158-08974805ad25/full.md"]
---

# FTFAW: A Novel Fingerprinting Method for Latent Diffusion Model Based on Two-Stage Fine-Tuning and Adaptive Loss Weighting

## One-line Takeaway

[[ftfaw]] is a fully integrated Stable Diffusion fingerprinting method that uses decoder weight modulation, two-stage fine-tuning, adaptive image-quality loss weighting, and dynamic post-processing to preserve visual fidelity while supporting multi-user attribution.

## Problem

Weight-modulated model fingerprints can distribute many user-specific copies efficiently, but the paper argues that unconstrained fine-tuning causes decoder knowledge forgetting and visible artifacts. FTFAW targets the image-quality versus fingerprint-robustness trade-off in an open-source distribution setting.

## Method

FTFAW converts a binary user fingerprint into modulation factors for every convolutional layer of the Stable Diffusion decoder. Stage 1 freezes the decoder while training the fingerprint mapping network and ConvNeXt-Base extractor; Stage 2 jointly fine-tunes all three once a fingerprint-accuracy threshold is reached.

The training objective combines fingerprint cross-entropy with WatsonVGG and MSE image-quality losses. The quality-loss weights are initially small and increase after fingerprint accuracy reaches the threshold. A bias of one initializes modulation factors near identity, while a dynamic post-processing layer progressively adds and intensifies simulated attacks after the extractor becomes accurate.

## Evidence

For Stable Diffusion v1.4 on MS-COCO, Table II reports FTFAW PSNR `35.19`, SSIM `0.944`, LPIPS `0.0220`, FID `18.28`, clean Bit Acc `0.9993`, attacked Bit Acc `0.9957`, clean TPR `1.0000`, and attacked TPR `0.9999` at the reported 1% FPR. WOUAF-Robust reports `28.51`, `0.759`, `0.0567`, `18.73`, `0.9997`, `0.9987`, `1.0000`, and `0.9993` on the same table.

On LAION-Aesthetics, FTFAW reports PSNR `37.94`, SSIM `0.967`, LPIPS `0.0159`, clean Bit Acc `0.9990`, attacked Bit Acc `0.9912`, and attacked TPR `0.9972`. Table III reports tracing accuracy `1.000` in the reported `10^4`, `10^5`, and `10^6` user pools.

Table IV reports FTFAW at PSNR `35.19`, SSIM `0.944`, Bit Acc `0.9993`, and attacked Bit Acc `0.9957`; removing the two-stage schedule, adaptive weights, MSE, or unit-mean modulation bias reduces at least one of the reported quality or recovery measures. At 128 bits, the static post-processing layer reaches fingerprint accuracy `0.6109` after 55,000 steps, compared with `0.9865` for the dynamic layer.

## Limitations and Caveats

- The reported tracer evaluation samples 1,000 users from each pool, with five images per selected user; it is not a full platform deployment study.
- The paper trains at `256 x 256` and evaluates at `512 x 512`; other resolutions and model families are not established.
- Collusion, decoder replacement, distillation, and LoRA fine-tuning are not evaluated.
- The reported diffusion reconstruction attack reduces Bit Acc to `0.5521`, but also lowers average PSNR to `25.69 dB`; the paper treats this as unusable image quality rather than a successful quality-preserving removal.

## Use in This Project

FTFAW is a direct quality-focused successor comparator to [[kim-2024-wouaf]] within the fully integrated decoder weight-modulation route. It adds evidence that staged optimization and dynamic robustness training can improve fidelity without forfeiting high reported attribution accuracy.

## Raw Sources

- `raw/sources/Pan 等 - 2025 - FTFAW A Novel Fingerprinting Method for Latent Diffusion Model Based on Two-Stage Fine-Tuning and Adaptive Loss Weighting.pdf-82d05c36-ca8b-42e6-b158-08974805ad25/full.md`
- `raw/sources/zotero/Pan 等 - 2025 - FTFAW A Novel Fingerprinting Method for Latent Diffusion Model Based on Two-Stage Fine-Tuning and Adaptive Loss Weighting/full.md` (Zotero mirror)

## Related Pages

- [[ftfaw]]
- [[user-attribution]]
- [[decoder-fingerprinting-scalability-comparison]]
- [[diffusion-model-fingerprinting-comparison]]
