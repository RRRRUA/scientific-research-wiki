---
type: finding
title: "HFRW RL Patch Selection Improves Embedding Quality"
tags: [finding, hfrw, deep-reinforcement-learning, patch-selection, watermarking]
related: ["[[ping-2026-hfrw]]", "[[hfrw]]", "[[localized-invisible-watermarking]]"]
created: 2026-06-11
updated: 2026-06-11
source: "[[ping-2026-hfrw]]"
confidence: high
replicated: false
---

# HFRW RL Patch Selection Improves Embedding Quality

## 发现

HFRW 的 dueling DQN patch selection 比随机选择 patch 更能降低嵌入失真，同时略微改善 message extraction error。

## 证据

Table III 报告在 test dataset 上，RL-optimized patches 相比 random patches 将 PSNR 从 41.15 提高到 43.33，RMSE(Xco, Xen) 从 0.0175 降到 0.0136，RMSE(M, M') 从 0.0879 降到 0.0811。Fig. 8 的单图示例中，最终优化位置相对初始随机位置将 PSNR 从 39.89 提高到 47.44，RMSE(Xco, Xen) 从 0.0202 降到 0.0084。

## 解释

这条 finding 说明 HFRW 的强化学习模块不是装饰性组件，而是在局部嵌入设置中实际承担“选择低失真区域”的作用。
