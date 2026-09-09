---
type: overview
title: "Wiki Index"
tags: [index, research-wiki]
related: ["[[overview]]", "[[diffusion-model-fingerprinting-comparison]]", "[[localized-watermarking-for-tamper-localization-comparison]]", "[[decoder-fingerprinting-scalability-comparison]]", "[[anti-collusion-model-distribution-comparison]]", "[[inversion-watermark-robustness-comparison]]", "[[watermark-verification-operands]]", "[[latentshield]]", "[[syntag]]", "[[molm]]", "[[genptw]]", "[[robin]]", "[[robin-plus-plus]]", "[[latent-watermark]]"]
created: 2026-06-11
updated: 2026-09-08
---

# Wiki Index

## Overview

- [[overview]] — 项目概览、阅读路径、当前结论和待跟踪问题。
- [[log]] — wiki 维护日志。

## Entities

- [[stable-signature]] — Stable Signature 方法实体。
- [[tree-ring-watermark]] — Tree-Ring Watermarking 方法实体。
- [[wouaf]] — WOUAF 方法实体。
- [[omnimark]] — OmniMark 方法实体。
- [[stableguard]] — StableGuard 方法实体。
- [[advmark]] — AdvMark 方法实体。
- [[trustmark]] — TrustMark 方法实体。
- [[wmadapter]] — WMAdapter 方法实体。
- [[secure-distribution]] — Secure Distribution 方法实体。
- [[msat-ldm]] — MSAT-LDM 方法实体。
- [[hfrw]] — HFRW 方法实体。
- [[watermark-anything]] — Watermark Anything 方法实体。
- [[editguard]] — EditGuard 方法实体。
- [[omniguard]] — OmniGuard 方法实体。
- [[ftfaw]] — FTFAW 方法实体。
- [[latentshield]] — LatentShield 多目标 latent watermarking 方法实体。
- [[syntag]] — SynTag 几何同步增强方法实体。
- [[molm]] — MOLM compositional LoRA marker 方法实体。
- [[genptw]] — GenPTW provenance tracing 与 tamper localization 方法实体。
- [[robin]] — ROBIN inversion-based zero-bit watermarking 方法实体。
- [[robin-plus-plus]] — ROBIN++ dual-domain copyright 与 localization 方法实体。
- [[latent-watermark]] — Latent Watermark latent-space payload 方法实体。

## Concepts

- [[generative-model-fingerprinting]] — 生成模型指纹识别，用于检测、溯源和归因。
- [[latent-diffusion-watermarking]] — Latent Diffusion Models 中的 watermark / fingerprint 嵌入机制。
- [[user-attribution]] — 将生成图像追溯到具体用户、key 或模型副本。
- [[watermark-robustness]] — 水印或指纹对图像变换、模型攻击和退化的鲁棒性。
- [[ddim-inversion-for-watermark-detection]] — 用 DDIM inversion 恢复 initial noise 并检测 watermark key。
- [[fourier-noise-watermarking]] — 在 initial noise 的 Fourier coefficients 中嵌入 watermark。
- [[private-vs-public-watermark-verification]] — 私有验证与公开验证的部署差异。
- [[watermark-capacity-for-user-attribution]] — 多 key / 多用户归因容量与 false positive control。
- [[tamper-localization-for-generated-images]] — 生成图像中的篡改区域定位。
- [[post-hoc-image-watermarking]] — 后处理图像水印路线，以及它和 diffusion-native provenance 的边界。
- [[arbitrary-resolution-image-watermarking]] — 任意分辨率图像水印及 original-resolution evaluation 问题。
- [[localized-invisible-watermarking]] — 局部不可见水印、空间证据与 fidelity/cropping trade-off。

## Sources

- [[fernandez-2023-stable-signature]] — Stable Signature: Rooting watermarks in latent diffusion models。
- [[wen-2023-tree-ring-watermarks]] — Tree-Ring Watermarks: Fingerprints for Diffusion Images that are Invisible and Robust。
- [[kim-2024-wouaf]] — WOUAF: Weight Modulation for User Attribution and Fingerprinting。
- [[pan-2025-ftfaw]] — FTFAW: Two-Stage Fine-Tuning and Adaptive Loss Weighting for LDM Fingerprinting。
- [[yang-2025-stableguard]] — StableGuard: Copyright protection and tamper localization in LDMs。
- [[chen-2026-advmark]] — AdvMark: Decoupling Defense Strategies for Robust Image Watermarking。
- [[bui-2023-trustmark]] — TrustMark: Universal Watermarking for Arbitrary Resolution Images。
- [[ci-2024-wmadapter]] — WMAdapter: Adding WaterMark Control to Latent Diffusion Models。
- [[dai-2026-secure-distribution]] — Secure Distribution: Anti-Collusion Watermarking via Spectral Weight Modulation in Latent Diffusion Models。
- [[ping-2026-hfrw]] — HFRW: High Fidelity and Robust Watermarking using Deep Reinforcement Learning。
- [[sander-2025-watermark-anything]] — Watermark Anything with Localized Messages。
- [[zhang-2023-editguard]] — EditGuard: Versatile Image Watermarking for Tamper Localization and Copyright Protection。
- [[zhang-2025-omniguard]] — OmniGuard: Hybrid Manipulation Localization via Augmented Versatile Deep Image Watermarking。
- [[zhang-2026-msat-ldm]] — MSAT-LDM: Transferable High-Fidelity Watermarking for LDMs。
- [[fei-2025-omnimark]] — OmniMark: Efficient and Scalable Latent Diffusion Model Fingerprinting。
- [[meng-2024-latent-watermark]] — Latent Watermark: Inject and Detect Watermarks in Latent Diffusion Space。
- [[huang-2024-robin]] — ROBIN: Robust and Invisible Watermarks for Diffusion Models with Adversarial Optimization。
- [[fang-2025-syntag]] — SynTag: Geometric Robustness for Inversion-based Generative Image Watermarking。
- [[fares-2026-molm]] — MOLM: Mixture of LoRA Markers。
- [[fei-2026-anti-collusion-fingerprinting]] — Efficient, Robust, and Anti-Collusion Fingerprinting of Image Diffusion Models。
- [[gan-2026-genptw]] — GenPTW: Provenance Tracing and Tamper Localization。
- [[huang-2026-robin-plus-plus]] — ROBIN++: Dual-Domain Copyright Protection and Tamper Localization。
- [[bekkari-2026-latentshield]] — LatentShield: Multi-Objective Robust Latent Watermarking。

## Queries

- [[how-to-scale-user-attribution-for-ldm]] — LDM 的用户归因如何扩展到大规模用户？

## Comparisons

- [[decoder-fingerprinting-scalability-comparison]] — Decoder / weight personalization 的 user-attribution scalability 对比。
- [[localized-watermarking-for-tamper-localization-comparison]] — HFRW、WAM、EditGuard 与 OmniGuard 的局部水印和篡改定位边界。
- [[anti-collusion-model-distribution-comparison]] — Secure Distribution 与 personalized-normalization ACT 的模型合谋边界。
- [[inversion-watermark-robustness-comparison]] — Tree-Ring、ROBIN、SynTag 与 ROBIN++ 的 inversion robustness 对比。

## Methodology

- [[watermark-verification-operands]] — 区分 raw BitAcc、exact recovery、TPR@FPR、zero-bit classification、candidate-pool attribution 与 localization metrics。

## Synthesis

- [[diffusion-model-fingerprinting-comparison]] — 当前论文的方法谱系、任务边界和证据索引。

## Thesis

- [[decoder-rooted-fingerprinting-scales-through-weight-encoding]] — 大规模 user attribution 更可能依赖 weight modulation 或 multi-dimensional weight encoding。

## Findings

- [[stable-signature-detects-generated-images-at-low-fpr]] — Stable Signature 在低 false positive rate 下检测生成图像。
- [[stable-signature-user-identification-degrades-with-scale-and-edits]] — Stable Signature 的 user identification 会随用户规模和 image edits 下降。
- [[wouaf-generates-user-fingerprinted-models-under-one-second]] — WOUAF 报告小于 1 秒生成用户指纹模型。
- [[wouaf-decoder-only-modulation-preserves-quality-better]] — WOUAF decoder-only modulation 比 U-Net + decoder modulation 更保质量。
- [[omnimark-generates-fingerprinted-model-copies-under-100-ms]] — OmniMark 报告小于 100 ms 生成 fingerprinted model copies。
- [[omnimark-maintains-high-bit-accuracy-with-low-quality-impact]] — OmniMark 在 48-bit fingerprints 下保持高 Bit Acc 与低质量影响。
- [[stableguard-unifies-watermark-verification-and-tamper-localization]] — StableGuard 统一 copyright verification 与 tamper localization。
- [[stableguard-mpw-vae-enables-self-supervised-tamper-training]] — StableGuard 的 MPW-VAE 支撑 self-supervised tamper training。
- [[stableguard-maintains-watermark-accuracy-under-degradation-and-tampering]] — StableGuard 在 tampering ratio 与 image degradation 下保持较高 watermark accuracy。
- [[latentshield-multi-objective-training-improves-composite-attack-recovery]] — LatentShield 多目标训练提高复合攻击下的 payload recovery，但论文有结果叙述与 FPR 分辨率问题。
- [[syntag-restores-geometric-robustness-to-inversion-watermarks]] — SynTag 通过预测和校正几何变换恢复 inversion watermark detection。
- [[molm-routes-keys-without-per-key-retraining]] — MOLM 通过 LoRA marker 组合路由编码 key，无需逐 key 训练。
- [[act-makes-colluded-fingerprint-models-unusable]] — ACT 让参数合谋模型严重失去生成质量，但不识别 colluders。
- [[genptw-unifies-provenance-recovery-and-tamper-localization]] — GenPTW 用同一 latent embedding 联合支持 provenance bits 与 localization。
- [[robin-active-hiding-improves-inversion-watermark-quality]] — ROBIN 用 active hiding 改善 inversion watermark 的同 seed 图像质量。
- [[robin-plus-plus-dual-domain-synergy-improves-joint-verification]] — ROBIN++ 的 dual-domain synergy 同时改善 copyright verification 与 localization。
- [[latent-watermark-separates-thresholded-detection-from-bit-recovery]] — Latent Watermark 显示 thresholded detection 与 raw payload recovery 必须分开解释。
- [[hfrw-local-watermarking-improves-fidelity-and-file-size-growth]] — HFRW 的局部水印显著改善 fidelity 和 file size growth。
- [[hfrw-rl-patch-selection-improves-embedding-quality]] — HFRW 的 RL patch selection 提升嵌入质量。
- [[hfrw-localized-embedding-trades-cropping-robustness-for-fidelity]] — HFRW 用 cropping robustness 换取高 fidelity 和低 FSVR。
- [[advmark-decoupled-training-preserves-clean-accuracy]] — AdvMark 通过 decoupled training 保护 clean accuracy。
- [[advmark-improves-quality-over-joint-training-baselines]] — AdvMark 比 joint-training baselines 保持更高 image quality。
- [[advmark-improves-comprehensive-robustness-against-advanced-attacks]] — AdvMark 提升对 distortion、regeneration 和 adversarial attacks 的综合鲁棒性。
- [[advmark-ablation-shows-two-defense-stages-are-complementary]] — AdvMark ablation 显示两个防御阶段互补。
- [[trustmark-achieves-high-quality-watermarking-on-arbitrary-resolution-benchmarks]] — TrustMark 在 arbitrary-resolution benchmarks 上兼顾 image quality 和 watermark recovery。
- [[trustmark-noise-simulation-improves-robustness-across-perturbations]] — TrustMark 的 noise simulation 提升多扰动鲁棒性。
- [[trustmark-rm-supports-high-quality-re-watermarking]] — TrustMark-RM 支持高质量 re-watermarking。
- [[trustmark-architecture-components-improve-visual-quality]] — TrustMark 的 GAN、FFL 和 post-process components 提升视觉质量。
- [[wmadapter-hybrid-finetuning-improves-image-quality]] — WMAdapter 的 hybrid finetuning 提升图像质量。
- [[secure-distribution-collusion-removal-destroys-model-utility]] — Secure Distribution 在报告的 collusion 中以模型可用性下降换取可追溯性保护。
- [[watermark-anything-decodes-localized-messages-from-small-regions]] — WAM 从小区域定位并解码多个 watermark messages。
- [[editguard-separates-copyright-recovery-from-tamper-localization]] — EditGuard 分离 copyright recovery 与 tamper localization。
- [[omniguard-improves-localization-under-degradation]] — OmniGuard 在 reported degradation 下改善 localization F1。
- [[ftfaw-improves-fidelity-with-near-perfect-robustness]] — FTFAW 在报告的鲁棒性下提升 fingerprinted image fidelity。
- [[ftfaw-traces-one-million-user-pool]] — FTFAW 在采样的百万用户池上报告完美 tracing accuracy。
- [[ftfaw-dynamic-postprocessing-converges-at-128-bits]] — FTFAW 的 dynamic post-processing 支持 128-bit fingerprint training convergence。

## References

- [[reference-database]] — 从论文 raw parses 抽取的参考文献数据库。
- [[recommendations]] — 后续阅读建议；仅保留可靠、可解释的推荐。
