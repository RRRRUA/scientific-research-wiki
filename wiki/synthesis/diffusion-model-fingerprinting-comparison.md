---
type: synthesis
title: "Diffusion Model Fingerprinting Comparison"
tags: [synthesis, latent-diffusion, watermarking, fingerprinting, user-attribution, tamper-localization]
related: ["[[fernandez-2023-stable-signature]]", "[[wen-2023-tree-ring-watermarks]]", "[[kim-2024-wouaf]]", "[[fei-2025-omnimark]]", "[[yang-2025-stableguard]]", "[[ping-2026-hfrw]]", "[[user-attribution]]", "[[watermark-robustness]]", "[[localized-invisible-watermarking]]", "[[tamper-localization-for-generated-images]]", "[[decoder-fingerprinting-scalability-comparison]]", "[[decoder-rooted-fingerprinting-scales-through-weight-encoding]]"]
created: 2026-06-07
updated: 2026-06-11
---

# Diffusion Model Fingerprinting Comparison

## 对比摘要

当前 wiki 的核心问题仍是 diffusion / generative model provenance，但语料现在包含一个重要外部对照：[[ping-2026-hfrw]]。前五篇论文试图把 provenance signal 放进 diffusion generation workflow；HFRW 则展示 post-hoc localized image watermarking 如何在高分辨率图像上优化 fidelity、file size growth 和 robustness。

## 方法谱系

| 方法 | 嵌入机制 | 主要任务 | 扩展性判断 |
| --- | --- | --- | --- |
| [[fernandez-2023-stable-signature]] | fine-tune LDM decoder，使输出带固定 binary signature | generated-image detection 与有限 user identification | 基础方法清晰，但 per-signature training 不适合大规模用户分发 |
| [[wen-2023-tree-ring-watermarks]] | 在 initial noise 的 Fourier space 写入 key，再用 DDIM inversion 检测 | provenance detection / model-owner verification | 不需要训练，但多 key user-attribution capacity 未证明 |
| [[kim-2024-wouaf]] | 用 user fingerprint 调制 decoder weights | distributor-side user attribution | 比 per-user training 更可扩展，报告 `< 1 sec` 生成用户模型 |
| [[fei-2025-omnimark]] | OmniMark layers + multi-dimensional decoder weight encoding | scalable model-copy fingerprinting | 当前最强调快速分发，报告 `<100 ms` 生成 fingerprinted model copy |
| [[yang-2025-stableguard]] | MPW-VAE decoder adapter + MoE-GFN forensic network | copyright verification + tamper localization | 扩展到 proactive forensics，但不是主打大规模 user attribution |
| [[ping-2026-hfrw]] | post-hoc localized invisible watermarking + dueling DQN patch selection | ordinary image copyright traceability | 高 fidelity / 低 FSVR 的对照路线，但不是 diffusion-native |

## 共同评价维度

- 指纹/水印检测：bit accuracy、attribution accuracy、false positive rate。
- 生成或图像质量：FID、CLIP score、PSNR、SSIM、LPIPS。
- 图像后处理鲁棒性：crop、blur、JPEG compression、noise、editing、color changes、resize、padding。
- 模型级攻击鲁棒性：fine-tuning、purification、pruning、quantization、collusion。
- 若目标是 tamper localization，还需要 F1、AUC、IoU、mask quality 和 degradation 下的定位稳定性。
- 若目标是高分辨率图像存储，还需要 file size variation rate (FSVR)。

## 任务边界

本 wiki 需要明确区分四类问题：

1. Generated-image detection：判断图像是否来自带水印的生成流程。Stable Signature 和 Tree-Ring 是核心证据。
2. User attribution：判断图像来自哪个用户、key 或模型副本。WOUAF 和 OmniMark 是核心证据。
3. Tamper localization：判断图像哪些区域被修改。StableGuard 是当前核心证据。
4. Ordinary image copyright traceability：保护普通高分辨率图像。HFRW 是 post-hoc local watermarking 对照。

这些任务可以共享 watermarking 技术，但部署指标不同。把 StableGuard 的 localization F1 当作 user attribution evidence，或把 HFRW 的 post-hoc fidelity / FSVR 结果当作 diffusion-native provenance 证据，都会混淆结论。

## 当前研究缺口

现有结果还需要更强的平台级验证：更大的用户数量、更明确的 false positive control、更真实的 white-box attacker、多用户合谋场景下的 traitor tracing，以及统一 benchmark 中同时评估 detection、attribution、localization、fidelity 和 storage cost 的 protocol。

## 证据索引

- Detection / identification 基础：[[stable-signature-detects-generated-images-at-low-fpr]]、[[stable-signature-user-identification-degrades-with-scale-and-edits]]。
- 扩展性路径：[[wouaf-generates-user-fingerprinted-models-under-one-second]]、[[omnimark-generates-fingerprinted-model-copies-under-100-ms]]。
- 质量与鲁棒性：[[wouaf-decoder-only-modulation-preserves-quality-better]]、[[omnimark-maintains-high-bit-accuracy-with-low-quality-impact]]、[[stableguard-maintains-watermark-accuracy-under-degradation-and-tampering]]、[[hfrw-local-watermarking-improves-fidelity-and-file-size-growth]]。
- Tamper localization：[[stableguard-unifies-watermark-verification-and-tamper-localization]]、[[stableguard-mpw-vae-enables-self-supervised-tamper-training]]。
- Local post-hoc watermarking trade-off：[[hfrw-rl-patch-selection-improves-embedding-quality]]、[[hfrw-localized-embedding-trades-cropping-robustness-for-fidelity]]。
- 横向判断：[[decoder-fingerprinting-scalability-comparison]] 和 [[decoder-rooted-fingerprinting-scales-through-weight-encoding]]。
