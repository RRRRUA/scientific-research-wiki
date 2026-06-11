---
type: finding
title: "OmniMark Generates Fingerprinted Model Copies under 100 ms"
tags: [finding, omnimark, scalability, latent-diffusion, model-fingerprinting]
related: ["[[fei-2025-omnimark]]", "[[generative-model-fingerprinting]]", "[[user-attribution]]", "[[how-to-scale-user-attribution-for-ldm]]", "[[decoder-fingerprinting-scalability-comparison]]"]
created: 2026-06-09
updated: 2026-06-09
source: "[[fei-2025-omnimark]]"
confidence: high
replicated: false
---

# OmniMark Generates Fingerprinted Model Copies under 100 ms

## 发现

[[fei-2025-omnimark]] 报告 OmniMark 可以在不为每个用户重新训练的情况下，快速生成带唯一 fingerprint 的 LDM model copies。

## 证据

OmniMark raw parse 的 abstract 报告，修改 fingerprints 并重新编码 weights 后，可以支持 scalable ad-hoc generation，耗时 `<100 ms`。正文贡献部分进一步说明，OmniMark 通过 single forward pass 构造标准化但带 fingerprint 的 convolution layers，时间低于 100 ms，并且不会增加用户 inference 负担。

## 解释

这个结果使 OmniMark 成为当前三篇论文中最直接面向平台级分发的方案：它把 user-specific identity 编码到 decoder weights 的多个维度中，而不是把用户扩展性压在 per-user fine-tuning 上。

## 注意

`<100 ms` 指构造 fingerprinted layers 的计算路径；平台部署仍需评估模型副本管理、verifier throughput、密钥生命周期和攻击者获取多个副本后的 collusion risk。
