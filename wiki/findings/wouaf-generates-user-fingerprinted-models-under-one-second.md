---
type: finding
title: "WOUAF Generates User-Fingerprinted Models under One Second"
tags: [finding, wouaf, scalability, user-attribution, weight-modulation]
related: ["[[kim-2024-wouaf]]", "[[user-attribution]]", "[[generative-model-fingerprinting]]", "[[how-to-scale-user-attribution-for-ldm]]", "[[decoder-fingerprinting-scalability-comparison]]"]
created: 2026-06-09
updated: 2026-06-09
source: "[[kim-2024-wouaf]]"
confidence: high
replicated: false
---

# WOUAF Generates User-Fingerprinted Models under One Second

## 发现

[[kim-2024-wouaf]] 把 per-user fingerprint generation 从 fine-tuning 问题转成 weight modulation forward pass，因此报告的 user-specific model creation 时间低于 1 秒。

## 证据

WOUAF raw parse 的 Table 1 比较了 fingerprinting time：DAG 为 8.4 hr，Stable Signature 为 `< 1 min`，WOUAF-conv 和 WOUAF-all 都为 `< 1 sec`。论文正文还说明，WOUAF 在一次训练后只需为用户 fingerprint 运行轻量 forward pass，即可调制 decoder weights。

## 解释

这个结果直接支撑本项目 hypothesis：大规模 user attribution 不应依赖每个用户重新 fine-tune，而应通过 weight modulation 或 weight encoding 生成用户特定副本。

## 注意

`< 1 sec` 是论文环境中的模型生成成本，不等于完整平台分发成本。真实系统还要考虑模型存储、下载、数据库登记、密钥管理和 verifier 部署。
