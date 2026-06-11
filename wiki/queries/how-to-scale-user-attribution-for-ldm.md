---
type: query
title: "LDM 的用户归因如何扩展到大规模用户？"
tags: [user-attribution, scalability, latent-diffusion, fingerprinting]
related: ["[[user-attribution]]", "[[generative-model-fingerprinting]]", "[[latent-diffusion-watermarking]]", "[[watermark-capacity-for-user-attribution]]", "[[diffusion-model-fingerprinting-comparison]]", "[[decoder-fingerprinting-scalability-comparison]]", "[[decoder-rooted-fingerprinting-scales-through-weight-encoding]]"]
created: 2026-06-07
updated: 2026-06-09
---

# LDM 的用户归因如何扩展到大规模用户？

## 当前回答

大规模用户归因（user attribution）需要同时解决三个问题：每个用户的模型副本如何快速生成、指纹空间是否足够大、验证阈值如何控制 false positive rate。三篇论文给出了递进关系：

- [[fernandez-2023-stable-signature]] 证明 decoder-rooted watermarking 可以把稳定签名嵌入 LDM 输出，但面向大规模用户时仍接近 per-user fine-tuning。
- [[kim-2024-wouaf]] 用 decoder weight modulation 让用户指纹进入权重，降低为每个用户重新训练完整模型的成本。
- [[fei-2025-omnimark]] 用 OmniMark layers 和多维权重编码，把生成带指纹模型副本的时间压到很低，更接近平台级分发。

更细的横向判断见 [[decoder-fingerprinting-scalability-comparison]]。当前 working thesis 见 [[decoder-rooted-fingerprinting-scales-through-weight-encoding]]。

[[wen-2023-tree-ring-watermarks]] 和 [[yang-2025-stableguard]] 是重要边界案例：Tree-Ring 强化了 provenance detection，但多 key capacity 仍是开放问题；StableGuard 强化了 copyright verification 与 tamper localization，但不以 per-user attribution 为主目标。[[ping-2026-hfrw]] 更偏 ordinary image copyright traceability，不直接回答 LDM user attribution。

## 关键约束

1. 指纹容量：bit length 越短，用户规模上升时误归因风险越高；bit length 越长，训练和检测难度可能上升。
2. 验证阈值：平台级部署不能只报告平均 bit accuracy，还要明确 false positive rate、true positive rate 和多用户检索策略。
3. 模型攻击：white-box fine-tuning、purification、quantization 和 pruning 都可能削弱指纹。
4. 质量保持：归因能力不能靠明显降低图像质量换来，否则用户和攻击者都能察觉。

## 后续阅读

优先补充 traitor tracing codes、collusion-resistant fingerprinting 和 statistical verification 相关论文，用来回答多用户合谋和平台级误报控制问题。
