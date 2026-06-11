---
type: overview
title: "项目概览"
tags: [overview, latent-diffusion, watermarking, fingerprinting, user-attribution, tamper-localization]
related: ["[[generative-model-fingerprinting]]", "[[latent-diffusion-watermarking]]", "[[user-attribution]]", "[[watermark-robustness]]", "[[localized-invisible-watermarking]]", "[[tamper-localization-for-generated-images]]", "[[diffusion-model-fingerprinting-comparison]]", "[[decoder-fingerprinting-scalability-comparison]]", "[[decoder-rooted-fingerprinting-scales-through-weight-encoding]]"]
created: 2026-06-11
updated: 2026-06-11
---

# 项目概览

这个 wiki 研究生成系统如何在不明显损害图像质量的前提下，嵌入不可见且可验证的 watermarks / fingerprints，用于 generated-image detection、user attribution、model-copy fingerprinting、copyright traceability 和 tamper localization。

## 当前语料

当前语料包含五篇 latent diffusion / generative provenance 论文，以及一篇 image watermarking 对照论文：

- [[fernandez-2023-stable-signature]]：把 signature root 到 latent decoder，用于 generated-image detection 和有限 user identification。
- [[wen-2023-tree-ring-watermarks]]：把 key pattern 写入 initial noise 的 Fourier space，并通过 [[ddim-inversion-for-watermark-detection]] 检测。
- [[kim-2024-wouaf]]：用 user fingerprint 调制 decoder weights，面向 distributor-side user attribution。
- [[fei-2025-omnimark]]：用 OmniMark layers 在 VAE decoder weights 的多个维度编码 fingerprint，强调快速生成大量 fingerprinted model copies。
- [[yang-2025-stableguard]]：用 MPW-VAE 和 MoE-GFN 把 copyright verification 与 [[tamper-localization-for-generated-images]] 放进 unified diffusion-native framework。
- [[ping-2026-hfrw]]：用 localized invisible watermarking 和 deep reinforcement learning 保护普通高分辨率图像，是 post-hoc / image-level watermarking 的对照路线。

## 阅读路径

先读 [[generative-model-fingerprinting]]、[[latent-diffusion-watermarking]] 和 [[watermark-robustness]]，建立任务和指标框架。随后读 source pages，重点比较嵌入位置：decoder、initial noise、weight modulation、multi-dimensional weight encoding、VAE adapter + forensic network、post-hoc local patch。

如果目标是大规模 user attribution，继续读 [[user-attribution]]、[[watermark-capacity-for-user-attribution]]、[[how-to-scale-user-attribution-for-ldm]] 和 [[decoder-fingerprinting-scalability-comparison]]。如果目标是 forensic localization，读 [[tamper-localization-for-generated-images]]、[[stableguard]] 以及 StableGuard 的 findings。如果目标是理解普通图像水印的 fidelity / file-size trade-off，读 [[localized-invisible-watermarking]]、[[hfrw]] 和 HFRW findings。

## 当前结论

Decoder-rooted watermarking 是 LDM provenance 的实用起点，但大规模 user attribution 更可能依赖 weight modulation 或 multi-dimensional weight encoding，而不是为每个用户单独 fine-tune decoder。Tree-Ring 说明 initial-noise watermarking 可以在不训练模型的情况下提供强 provenance detection，但多 key capacity 仍是开放问题。StableGuard 说明同一个 watermark signal 可以进一步服务 tamper localization。HFRW 说明 post-hoc local embedding 能显著降低 fidelity 和 file-size 代价，但不能替代 diffusion-native provenance。

## 关键证据

- Stable Signature 支持低 FPR generated-image detection，但 user identification 会随用户规模和 image edits 下降。
- WOUAF 和 OmniMark 把用户差异编码到权重或权重层中，明显更接近平台分发场景。
- Tree-Ring 把 watermark 放进 sampling process，强化 private provenance verification。
- StableGuard 把 proactive watermarking 与 tamper localization 结合，在 AIGC tampering benchmark 上报告高 F1/AUC/IoU。
- HFRW 在 ordinary image watermarking 中报告高 PSNR/SSIM、低 FSVR 和常见攻击下较高 bit accuracy，但 severe cropping 是局部嵌入弱点。

## 待跟踪问题

- 多用户 false positive control 和 traitor tracing。
- White-box fine-tuning、distillation、decoder replacement、purification 和 collusion attacks。
- Public verification 与 private verification 的部署取舍。
- 同一 benchmark 中联合评估 detection、user attribution、tamper localization、fidelity 和 storage cost 的 protocol。
