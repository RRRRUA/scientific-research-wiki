---
type: finding
title: "AdvMark Improves Comprehensive Robustness against Advanced Attacks"
tags: [finding, advmark, watermark-robustness, regeneration-attacks, adversarial-attacks]
related: ["[[chen-2026-advmark]]", "[[advmark]]", "[[post-hoc-image-watermarking]]", "[[watermark-robustness]]"]
created: 2026-06-17
updated: 2026-07-16
source: "[[chen-2026-advmark]]"
confidence: high
replicated: false
---

# AdvMark Improves Comprehensive Robustness against Advanced Attacks

## Finding

[[chen-2026-advmark]] reports that AdvMark maintains high bit accuracy under distortions, diffusion regeneration, WEvade, Black-S, and combined advanced attacks, addressing weaknesses of baselines such as MBRS under regeneration and adversarial attacks.

## Evidence

In Table 2, AdvMark scores 1.00/0.99/0.83/0.87/0.87/0.98/1.00/0.73 on COCO for Clean/JPEG/combined distortion/Regen-SD-V1-4/Regen-SD-V1-5/WEvade/Black-S/Black-Q. MBRS scores 0.93/0.98/0.76/0.70/0.70/0.82/1.00/0.73.

On DiffusionDB, AdvMark scores 1.00/0.98/0.83/0.85/0.85/0.96/1.00/0.74. In Table 5, it scores 1.00 under crop, resize, dropout, salt-pepper, rotation, and hue, and 0.87/0.81 under Reg+Adv/Adv+Reg, above MBRS at 0.70/0.65.

## Caveat

Black-Q bit accuracy remains near the attack threshold. The paper's additional argument is that AdvMark forces Black-Q to incur about 15 PSNR of quality loss. This finding therefore means more robust under the paper's attack-quality constraint, not immune to all query-based attacks.
