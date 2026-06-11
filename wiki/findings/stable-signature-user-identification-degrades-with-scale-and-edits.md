---
type: finding
title: "Stable Signature User Identification Degrades with Scale and Edits"
tags: [finding, stable-signature, user-identification, scalability, false-positive-rate]
related: ["[[fernandez-2023-stable-signature]]", "[[user-attribution]]", "[[how-to-scale-user-attribution-for-ldm]]", "[[decoder-fingerprinting-scalability-comparison]]"]
created: 2026-06-09
updated: 2026-06-09
source: "[[fernandez-2023-stable-signature]]"
confidence: high
replicated: false
---

# Stable Signature User Identification Degrades with Scale and Edits

## 发现

[[fernandez-2023-stable-signature]] 支持 user identification，但用户规模和图像编辑会明显压低 identification accuracy。

## 证据

论文用 48-bit signatures，fine-tune `N' = 1000` 个模型，每个模型生成 100 张图像，再外推到更大的用户集合。raw parse 中报告：在 `N = 10^5` 用户规模下，未修改图像的 identification accuracy 约为 98%；combined edit 下约为 40%。论文还指出，随着用户数 N 增加，为控制全局 FPR，阈值必须提高，因此 detection/identification accuracy 会被交换掉。

## 解释

这个 finding 是本项目“scalable user attribution”问题的起点：Stable Signature 可以把固定 signature root 到 decoder，但如果每个用户都需要一个单独 fine-tuned model copy，并且阈值随用户数收紧，它更像基础方案而不是最终平台级方案。

## 注意

论文报告的 identification 结果部分依赖外推，并且没有覆盖真实平台中的重复生成、用户合谋、模型再分发和长期漂移。
