---
type: concept
title: "User Attribution"
tags: [attribution, accountability, model-distribution]
related: ["[[generative-model-fingerprinting]]", "[[latent-diffusion-watermarking]]", "[[watermark-robustness]]", "[[watermark-capacity-for-user-attribution]]", "[[how-to-scale-user-attribution-for-ldm]]"]
created: 2026-06-07
updated: 2026-06-09
---

# User Attribution

## 定义
用户归因（user attribution）是把生成内容回溯到产生它的具体用户、客户或模型副本。

## 典型流程
1. Provider 或 distributor 为每个用户分配唯一 fingerprint。
2. 生成图像以不可见方式携带该 fingerprint。
3. Verifier 从可疑图像中提取候选 fingerprint。
4. 系统用 statistical test 把提取结果与已注册用户 fingerprints 比对。

## 为什么比检测更难
Detection 只问图像是否来自某个 model family；attribution 要问大量候选用户中的哪一个生成了图像。用户数量越大，false positive control 越严格，匹配阈值通常也要更高。

## 相关论文
- [[fernandez-2023-stable-signature]] 用 binomial tests 建模 detection 和 identification。
- [[kim-2024-wouaf]] 聚焦 distributor-oriented attribution。
- [[fei-2025-omnimark]] 聚焦 scalable per-user fingerprint generation。

## 边界案例

[[tree-ring-watermark]] 和 stableguard 都能支持 provenance 或 copyright verification，但它们当前不是大规模 user attribution 的主要证据：前者的多 key capacity 尚未证明，后者主要面向 tamper localization。
