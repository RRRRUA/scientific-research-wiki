---
type: source
title: "Decoupling Defense Strategies for Robust Image Watermarking"
tags: [image-watermarking, robust-watermarking, adversarial-attacks, regeneration-attacks, watermark-robustness]
related: ["[[advmark]]", "[[post-hoc-image-watermarking]]", "[[watermark-robustness]]", "[[diffusion-model-fingerprinting-comparison]]", "[[advmark-decoupled-training-preserves-clean-accuracy]]", "[[advmark-improves-quality-over-joint-training-baselines]]", "[[advmark-improves-comprehensive-robustness-against-advanced-attacks]]", "[[advmark-ablation-shows-two-defense-stages-are-complementary]]"]
created: 2026-06-17
updated: 2026-07-16
authors: ["Jiahui Chen", "Zehang Deng", "Zeyu Zhang", "Chaoyang Li", "Lianchen Jia", "Lifeng Sun"]
year: 2026
url: ""
venue: ""
sources: ["Chen 等 - 2026 - Decoupling Defense Strategies for Robust Image Watermarking.pdf-8147032b-37f6-4091-8de2-a8ec3a76b5f6/full.md"]
---

# Decoupling Defense Strategies for Robust Image Watermarking

## One-sentence Summary

[[advmark]] is a two-stage robust image watermarking framework. Encoder-focused adversarial fine-tuning first addresses attacks such as WEvade, then quality-aware direct image optimization addresses distortions and diffusion regeneration. It provides a [[post-hoc-image-watermarking]] comparator that emphasizes advanced attacks more strongly than hfrw.

## Problem

Deep-learning image watermarking often resists conventional distortions such as JPEG, noise, and blur but fails under diffusion-based regeneration and adversarial attacks such as WEvade. The authors identify two problems with joint adversarial training of the encoder, decoder, and noise layer:

- Adversarial training of the decoder changes its decision boundary and reduces clean accuracy on unattacked watermarked images.
- Distortion, regeneration, and adversarial attacks operate differently, so combining all three in a monolithic training process yields limited robustness gains.

## Method

AdvMark separates defense into two stages.

Stage 1 primarily fine-tunes the encoder. It constructs defender-tailored adversarial examples that push the decoded message away from the ground-truth message instead of using a random target. Training mainly updates the encoder to move watermarked images toward a non-attackable region. The decoder receives one conditional update only when final adversarial bit accuracy falls below a threshold, limiting the sacrifice of clean accuracy.

Stage 2 directly optimizes the encoded image. It uses differentiable attack losses for distortion and regeneration together with clean-accuracy and constrained-image losses. The constrained-image loss keeps the optimized image close to both the cover image and the Stage 1 encoded image, preserving adversarial robustness from Stage 1. A quality-aware early stop and PSNR budget replace conventional PGD epsilon-ball projection.

## Evidence

In the representative Figure 2 experiment, AdvMark scores 1.00/0.99/0.87/0.98 bit accuracy on Clean/JPEG/Regen-SD-V1-4/WEvade, while MBRS-JAT scores 0.94/0.98/0.70/0.82, showing that joint adversarial training loses clean accuracy while improving robustness.

Table 1 reports AdvMark visual quality on MS-COCO. Under the 128x128, 30-bit setting, AdvMark reaches PSNR 37.0, SSIM 0.99, and LPIPS 0.01, while MBRS reaches 32.1, 0.95, and 0.09. Under the 256x256, 100-bit setting, AdvMark reaches PSNR 38.9/38.8, SSIM 0.99/0.99, and LPIPS 0.01/0.01 on MS-COCO/DiffusionDB.

Table 2 reports AdvMark on COCO at Clean 1.00, JPEG 0.99, combined distortions 0.83, Regen-SD-V1-4 0.87, Regen-SD-V1-5 0.87, WEvade 0.98, Black-S 1.00, and Black-Q 0.73. On DiffusionDB, the corresponding scores are 1.00, 0.98, 0.83, 0.85, 0.85, 0.96, 1.00, and 0.74. The paper summarizes maximum accuracy improvements over baselines of 29%, 33%, and 46% under distortion, regeneration, and adversarial attacks.

The Table 3 ablation shows that removing Stage 1 lowers WEvade accuracy from 0.98 to 0.50. Removing Stage 2 lowers combined-distortion accuracy from 0.83 to 0.65 and Regen-SD-V1-4/1-5 from 0.87/0.87 to 0.54/0.54.

Table 5 reports 1.00 under crop, resize, dropout, salt-pepper, rotation, and hue, and 0.87/0.81 under Reg+Adv/Adv+Reg combined attacks, above MBRS at 0.70/0.65.

## Key Results

- AdvMark optimizes adversarial robustness separately from distortion and regeneration robustness instead of using one joint adversarial training process for all attacks.
- Encoder-focused Stage 1 preserves clean accuracy while gaining robustness against WEvade and Black-S.
- Direct image optimization in Stage 2 uses a constrained-image loss to retain Stage 1 adversarial robustness and add distortion and regeneration robustness.
- AdvMark reports both high image quality and comprehensive robustness in the evaluated COCO and DiffusionDB settings.

## Limitations and Caveats

- AdvMark is post-hoc image-level watermarking, not diffusion-native watermarking, and does not directly support model-copy user attribution.
- Stage 2 is per-image optimization and adds encoding overhead. Figure 11 reports 1.5 s encoding time and 0.01 s decoding time.
- Black-Q bit accuracy remains near the paper's threshold; the authors mainly argue that AdvMark forces Black-Q to incur about 15 PSNR of attack-quality loss.
- The parsed `full.md` contains no DOI, code URL, or formal venue, so this page does not infer those fields.

## Use in This Project

This paper adds a robustness comparator to the project. hfrw emphasizes the fidelity and file-size trade-off of local embedding, while AdvMark emphasizes defenses against distortion, diffusion regeneration, and adversarial attacks in ordinary image watermarking. It cannot replace LDM-native provenance evidence, but it shows that benchmark design should evaluate regeneration and adversarial removal separately from conventional image transformations.

## Original Sources

- `raw/sources/Chen 等 - 2026 - Decoupling Defense Strategies for Robust Image Watermarking.pdf-8147032b-37f6-4091-8de2-a8ec3a76b5f6/full.md`
- `raw/sources/Chen 等 - 2026 - Decoupling Defense Strategies for Robust Image Watermarking.pdf-8147032b-37f6-4091-8de2-a8ec3a76b5f6/2e67c9e1-0e9f-47d0-b921-f7013c3073cd_origin.pdf`

## Related Pages

- [[advmark]]
- [[post-hoc-image-watermarking]]
- [[watermark-robustness]]
- [[diffusion-model-fingerprinting-comparison]]
