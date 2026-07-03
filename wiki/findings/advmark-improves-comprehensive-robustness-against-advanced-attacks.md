---
type: finding
title: "AdvMark Improves Comprehensive Robustness against Advanced Attacks"
tags: [finding, advmark, watermark-robustness, regeneration-attacks, adversarial-attacks]
related: ["[[chen-2026-advmark]]", "[[advmark]]", "[[post-hoc-image-watermarking]]", "[[watermark-robustness]]"]
created: 2026-06-17
updated: 2026-06-17
source: "[[chen-2026-advmark]]"
confidence: high
replicated: false
---

# AdvMark Improves Comprehensive Robustness against Advanced Attacks

## 发现

[[chen-2026-advmark]] 报告 AdvMark 在 distortion、diffusion regeneration、WEvade、Black-S 和 combined advanced attacks 上同时保持较高 bit accuracy，尤其补足了 MBRS 等 baselines 在 regeneration 与 adversarial attacks 下的弱点。

## 证据

Table 2 中，COCO 上 AdvMark 的 Clean/JPEG/combined distortion/Regen-SD-V1-4/Regen-SD-V1-5/WEvade/Black-S/Black-Q 分别为 1.00/0.99/0.83/0.87/0.87/0.98/1.00/0.73。MBRS 对应为 0.93/0.98/0.76/0.70/0.70/0.82/1.00/0.73。

DiffusionDB 上 AdvMark 对应为 1.00/0.98/0.83/0.85/0.85/0.96/1.00/0.74。Table 5 中，AdvMark 在 crop、resize、dropout、salt-pepper、rotation、hue 上均为 1.00，并在 Reg+Adv / Adv+Reg 上为 0.87 / 0.81，高于 MBRS 的 0.70 / 0.65。

## 注意

Black-Q 的 bit accuracy 仍接近攻击阈值；论文的补充解释是 AdvMark 会迫使 Black-Q 产生约 15 PSNR 的质量损失。因此这条 finding 应理解为“在论文定义的攻击质量约束下更稳健”，不是“对所有 query-based attacks 免疫”。
