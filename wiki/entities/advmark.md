---
type: entity
title: AdvMark
aliases: ["Decoupling Defense Strategies for Robust Image Watermarking"]
tags: [method, image-watermarking, robust-watermarking, adversarial-training, post-hoc-image-watermarking]
related: ["[[chen-2026-advmark]]", "[[post-hoc-image-watermarking]]", "[[watermark-robustness]]", "[[advmark-decoupled-training-preserves-clean-accuracy]]", "[[advmark-improves-quality-over-joint-training-baselines]]", "[[advmark-improves-comprehensive-robustness-against-advanced-attacks]]", "[[advmark-ablation-shows-two-defense-stages-are-complementary]]"]
created: 2026-06-17
updated: 2026-07-16
sources: ["Chen 等 - 2026 - Decoupling Defense Strategies for Robust Image Watermarking.pdf-8147032b-37f6-4091-8de2-a8ec3a76b5f6/full.md", "Chen 等 - 2026 - Decoupling Defense Strategies for Robust Image Watermarking.pdf-8147032b-37f6-4091-8de2-a8ec3a76b5f6/2e67c9e1-0e9f-47d0-b921-f7013c3073cd_origin.pdf"]
---

# AdvMark

AdvMark is a robust post-hoc image watermarking method and two-stage framework introduced by [[chen-2026-advmark]] in 2026. It targets ordinary image watermarking and [[post-hoc-image-watermarking]], not provenance watermarking internal to Latent Diffusion Models.

AdvMark's central idea is to decouple defense strategies. Instead of jointly training the encoder and decoder against all attacks, it uses two distinct defense stages for adversarial robustness and distortion/regeneration robustness.

## Architecture

| Stage | Objective | Mechanism |
| --- | --- | --- |
| Stage 1 | Improve adversarial robustness while protecting clean accuracy | Encoder-focused adversarial fine-tuning |
| Stage 2 | Improve distortion and regeneration robustness | Quality-aware direct image optimization |
| Quality-aware early stop | Enforce a lower bound on image quality | Replace conventional PGD epsilon-ball projection with a PSNR budget |

## Stage 1: Encoder-Focused Adversarial Fine-Tuning

Stage 1 primarily fine-tunes the encoder for adversarial robustness. Defender-tailored adversarial examples train the encoder to move watermarked images into a more stable region of input space without aggressively changing the decoder's decision boundary.

The decoder is updated conditionally only when adversarial bit accuracy falls below a threshold. This protects clean bit accuracy and avoids sacrificing unattacked decoding performance excessively for resistance to adversarial examples.

## Stage 2: Quality-Aware Direct Image Optimization

Stage 2 directly optimizes the encoded image to improve robustness to conventional distortions and regeneration attacks.

Its loss constrains the optimized image to remain close to both:

- The original cover image
- The encoded image produced by Stage 1

This constrained image loss limits quality degradation while retaining the adversarial robustness obtained in Stage 1.

## Attack and Robustness Scope

AdvMark argues that robustness for ordinary image watermarking cannot be evaluated only with conventional distortions such as JPEG, blur, and noise. Stronger attack types must be separated, including:

- diffusion regeneration attacks
- WEvade
- Black-Q
- Black-S
- Other adversarial attacks

AdvMark is therefore an important comparator for advanced-attack benchmarks in [[watermark-robustness]].

## Role in This Wiki

AdvMark is a strong comparator for [[post-hoc-image-watermarking]]. It does not directly address scalable [[user-attribution]] in Latent Diffusion Models or model-copy fingerprinting.

Its main value is to broaden the robustness analysis: AdvMark shows that watermark robustness can improve by separating defense objectives and helps define finer attack categories and benchmark dimensions for [[watermark-robustness]].
