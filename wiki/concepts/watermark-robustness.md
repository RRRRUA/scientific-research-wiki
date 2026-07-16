---
type: concept
title: "Watermark Robustness"
tags: [watermarking, robustness, adversarial-attacks]
related: ["[[generative-model-fingerprinting]]", "[[latent-diffusion-watermarking]]", "[[user-attribution]]", "[[tree-ring-watermark]]", "[[stableguard]]", "[[hfrw]]", "[[advmark]]", "[[trustmark]]", "[[secure-distribution]]", "[[watermark-anything]]", "[[omniguard]]", "[[localized-invisible-watermarking]]", "[[post-hoc-image-watermarking]]", "[[arbitrary-resolution-image-watermarking]]", "[[tamper-localization-for-generated-images]]", "[[diffusion-model-fingerprinting-comparison]]"]
created: 2026-06-07
updated: 2026-07-06
---

# Watermark Robustness

## Definition

Watermark robustness is the ability of an embedded signature, watermark, or fingerprint to remain detectable after transformations, quality degradation, editing, regeneration, or adversarial removal attempts.

## Image-level Transformations

Common evaluations include cropping, JPEG compression, brightness/contrast shifts, rotation, blur, noise, text overlay, resizing, erasing, color changes, and combinations of these transformations.

## Model-level Attacks

For model fingerprinting, white-box users may try to weaken a fingerprint through pruning, quantization, parameter noise, model compression, fine-tuning, model purification, distillation, decoder replacement, or collusion.

## Patterns in the Current Corpus

- [[fernandez-2023-stable-signature]] shows that decoder-rooted watermarks can survive many image edits, but remain vulnerable to informed image/model-level attacks.

- [[wen-2023-tree-ring-watermarks]] shows that initial-noise Fourier watermarking can maintain high AUC under many common image transformations without post-hoc image editing.

- [[kim-2024-wouaf]] improves robustness to image post-processing relative to Stable Signature in its evaluation.

- [[fei-2025-omnimark]] uses noise-layer training and sharpness-aware robustness to improve resistance to image attacks and model attacks.

- [[yang-2025-stableguard]] uses a holistic watermark as a forensic cue. It reports high Bit Acc under tampering ratios, compression, and noise, while noting that localization accuracy declines under degradation.

- [[ping-2026-hfrw]] uses local patch embedding, DQN patch selection, and a localization/synchronization module to improve ordinary image watermarking fidelity, FSVR, and common-attack robustness; severe cropping remains its main weakness.

- [[chen-2026-advmark]] decouples adversarial defense from distortion/regeneration defense. Stage 1 targets adversarial robustness, while Stage 2 uses direct image optimization to recover conventional distortion and diffusion regeneration robustness.

- [[bui-2023-trustmark]] expands the post-hoc robustness frame to arbitrary-resolution images, broad differentiable noise simulation, and re-watermarking. Its evidence distinguishes perturbation robustness from removal and replacement workflows.

- [[dai-2026-secure-distribution]] treats collusion as a model-level threat. Its evaluated linear and nonlinear merges reduce recovered bits to random levels only while also degrading model outputs severely.

- [[sander-2025-watermark-anything]] prioritizes recovery from small watermarked regions and splicing; its robustness profile differs from global watermarking and from purification resistance.

- [[zhang-2025-omniguard]] uses a learned mask extractor to preserve localization under ordinary degradation, but reports a boundary where very severe degradation reduces proactive localization to passive-detection behavior.

## Research Tensions

Stronger robustness often trades off against image quality, payload length, compute overhead, public verifiability, and scalable user attribution. The post-hoc comparators add another caution: robustness to ordinary perturbations, diffusion regeneration, adversarial removal, and watermark replacement should not be collapsed into a single aggregate score.
