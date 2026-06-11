---
type: comparison
title: "Decoder Fingerprinting Scalability Comparison"
tags: [comparison, latent-diffusion, fingerprinting, scalability, user-attribution]
related: ["[[fernandez-2023-stable-signature]]", "[[kim-2024-wouaf]]", "[[fei-2025-omnimark]]", "[[yang-2025-stableguard]]", "[[stable-signature-user-identification-degrades-with-scale-and-edits]]", "[[wouaf-generates-user-fingerprinted-models-under-one-second]]", "[[omnimark-generates-fingerprinted-model-copies-under-100-ms]]", "[[stableguard-unifies-watermark-verification-and-tamper-localization]]", "[[decoder-rooted-fingerprinting-scales-through-weight-encoding]]"]
created: 2026-06-09
updated: 2026-06-09
---

# Decoder Fingerprinting Scalability Comparison

## 比较问题

三篇论文都利用 LDM decoder 作为 watermark/fingerprint 的嵌入位置，但它们解决“用户规模”的方式不同：Stable Signature 证明 decoder-rooted watermarking 可行，WOUAF 把 user fingerprint 变成 decoder weight modulation，OmniMark 进一步把 fingerprint 编码进多个 weight dimensions。

## 横向对照

| 方法 | 用户特定化方式 | 报告的生成/分发成本 | 质量影响 | 主要风险 |
| --- | --- | --- | --- | --- |
| [[fernandez-2023-stable-signature]] | 每个 signature fine-tune latent decoder | 论文报告 decoder fine-tuning 约 1 分钟级 | 多任务质量影响较小 | 用户数增加时阈值提高；combined edits 下 identification accuracy 明显下降 |
| [[kim-2024-wouaf]] | User fingerprint 经过 mapping network 调制 decoder weights | WOUAF-conv/WOUAF-all 报告 `< 1 sec` | CLIP/FID 接近 Original SD；decoder-only 优于 U-Net+decoder | Autoencoder compression、model purification、强 blur 等仍会降低 attribution |
| [[fei-2025-omnimark]] | OmniMark layers 在 kernel/filter/channel/spatial 等维度编码 fingerprint | 报告 `<100 ms` 构造 fingerprinted convolution layers | 48-bit fingerprints 下 Bit Acc 约 99%，FID 增加不到 1 点 | Fine-tuning attack 仍可威胁 fingerprint，需要 robust fingerprinting 和阈值调整 |

## 当前判断

如果目标只是证明 LDM 可以主动携带 provenance signal，Stable Signature 是最清晰的基础。若目标是大规模 user attribution，WOUAF 和 OmniMark 更接近部署路径，因为它们把“用户差异”从 per-user training 转为 weight modulation/encoding。

## 关键差异

- Stable Signature 的强项是统计检测框架和 decoder-rooted watermarking 的可行性。
- WOUAF 的强项是 distributor-oriented attribution 与 `< 1 sec` user-specific model creation。
- OmniMark 的强项是 `<100 ms` model-copy generation 和 multi-dimensional weight encoding。

## 尚未解决

三篇论文都还没有完整回答真实平台中的 collusion、decoder replacement、model distillation、LoRA fine-tuning、密钥泄露和多副本泄露问题。这些问题应继续留在 [[how-to-scale-user-attribution-for-ldm]] 里跟踪。

## 邻近但不同的路线

[[yang-2025-stableguard]] 也修改 VAE decoder，但它的主任务是 copyright verification + [[tamper-localization-for-generated-images]]，不是给大量用户生成可追踪 model copies。因此它可以作为 decoder-rooted proactive forensics 的证据，但不应直接纳入 user-attribution scalability 排名。[[ping-2026-hfrw]] 则是 post-hoc localized image watermarking，对本 comparison 只提供 fidelity / robustness 的外部参照。
