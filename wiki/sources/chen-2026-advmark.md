---
type: source
title: "Decoupling Defense Strategies for Robust Image Watermarking"
tags: [image-watermarking, robust-watermarking, adversarial-attacks, regeneration-attacks, watermark-robustness]
related: ["[[advmark]]", "[[post-hoc-image-watermarking]]", "[[watermark-robustness]]", "[[diffusion-model-fingerprinting-comparison]]", "[[advmark-decoupled-training-preserves-clean-accuracy]]", "[[advmark-improves-quality-over-joint-training-baselines]]", "[[advmark-improves-comprehensive-robustness-against-advanced-attacks]]", "[[advmark-ablation-shows-two-defense-stages-are-complementary]]"]
created: 2026-06-17
updated: 2026-06-17
authors: ["Jiahui Chen", "Zehang Deng", "Zeyu Zhang", "Chaoyang Li", "Lianchen Jia", "Lifeng Sun"]
year: 2026
url: ""
venue: ""
sources: ["Chen 等 - 2026 - Decoupling Defense Strategies for Robust Image Watermarking.pdf-8147032b-37f6-4091-8de2-a8ec3a76b5f6/full.md"]
---

# Decoupling Defense Strategies for Robust Image Watermarking

## 一句话结论

[[advmark]] 是一种两阶段 robust image watermarking framework：先用 encoder-focused adversarial fine-tuning 处理 WEvade 等 adversarial attacks，再用 quality-aware direct image optimization 处理 distortion 和 diffusion regeneration attacks；它为本 wiki 提供了一个比 [[hfrw]] 更强调 advanced attacks 的 [[post-hoc-image-watermarking]] 对照路线。

## 问题

论文指出，deep learning-based image watermarking 通常能抵抗 JPEG、noise、blur 等 conventional distortions，但在 diffusion-based regeneration 和 WEvade 等 adversarial attacks 下容易失效。作者认为把 encoder、decoder 和 noise layer 一起 joint adversarial training 会带来两个问题：

- decoder adversarial training 会改变 decision boundary，使 unattacked watermarked images 的 clean accuracy 下降。
- distortion、regeneration 和 adversarial attacks 的机制不同，把三类攻击同时塞进一个 monolithic training process 会导致鲁棒性提升有限。

## 方法

AdvMark 把防御拆成两个阶段。

Stage 1 主要 fine-tune encoder。它构造 defender-tailored adversarial examples，让 decoded message 远离 ground-truth message，而不是靠随机 target message；训练时主要更新 encoder，把 watermarked image 推向 non-attackable region。只有当最终 adversarial bit accuracy 低于阈值时，decoder 才被条件性更新一次，以避免 clean accuracy 被过度牺牲。

Stage 2 直接优化 encoded image。它对 distortion attacks 和 regeneration attack 使用 differentiable attack loss，同时加入 clean-accuracy loss 和 constrained image loss。这个 constrained image loss 同时约束 optimized image 靠近 cover image 和 Stage 1 的 encoded image，用来保留 Stage 1 获得的 adversarial robustness。最后用 quality-aware early stop 和 PSNR budget 替代传统 PGD epsilon-ball projection。

## 证据

Figure 2 的代表性实验中，AdvMark 在 Clean/JPEG/Regen-SD-V1-4/WEvade 上的 bit accuracy 为 1.00/0.99/0.87/0.98；MBRS-JAT 为 0.94/0.98/0.70/0.82，说明 joint adversarial training 提升鲁棒性时损失了 clean accuracy。

Table 1 报告 AdvMark 在 MS-COCO 上的 visual quality。128x128、30-bit 设置下，AdvMark 为 PSNR 37.0、SSIM 0.99、LPIPS 0.01；同设置 MBRS 为 PSNR 32.1、SSIM 0.95、LPIPS 0.09。256x256、100-bit 设置下，AdvMark 在 MS-COCO / DiffusionDB 上分别为 PSNR 38.9 / 38.8、SSIM 0.99 / 0.99、LPIPS 0.01 / 0.01。

Table 2 在 COCO 上报告 AdvMark 的 Clean 1.00、JPEG 0.99、combined distortions 0.83、Regen-SD-V1-4 0.87、Regen-SD-V1-5 0.87、WEvade 0.98、Black-S 1.00、Black-Q 0.73；DiffusionDB 上对应为 Clean 1.00、JPEG 0.98、combined distortions 0.83、Regen-SD-V1-4 0.85、Regen-SD-V1-5 0.85、WEvade 0.96、Black-S 1.00、Black-Q 0.74。论文总结 AdvMark 相比 baselines 在 distortion、regeneration、adversarial attacks 上最高带来 29%、33%、46% accuracy improvement。

Table 3 的 ablation 显示，去掉 Stage 1 后 WEvade accuracy 从 0.98 降到 0.50；去掉 Stage 2 后 combined distortion accuracy 从 0.83 降到 0.65，Regen-SD-V1-4/1-5 从 0.87/0.87 降到 0.54/0.54。

Table 5 报告 AdvMark 在 crop、resize、dropout、salt-pepper、rotation、hue 上均为 1.00，并在 Reg+Adv / Adv+Reg combined attacks 上为 0.87 / 0.81，高于 MBRS 的 0.70 / 0.65。

## 关键结果

- AdvMark 把 adversarial robustness 与 distortion/regeneration robustness 分开优化，而不是用单一 joint adversarial training 同时处理所有攻击。
- Encoder-focused Stage 1 试图维持 clean accuracy，同时获得 WEvade / Black-S 方向的 adversarial robustness。
- Direct image optimization Stage 2 用 constrained image loss 保留 Stage 1 的 adversarial robustness，并补上 distortion / regeneration robustness。
- 在论文评估的 COCO 和 DiffusionDB 设置下，AdvMark 同时报告较高 image quality 和 comprehensive robustness。

## 局限与注意点

- AdvMark 是 post-hoc / image-level watermarking，不是 diffusion-native watermarking，也不直接支持 model-copy user attribution。
- Stage 2 是 per-image optimization，会增加 encoding overhead；论文 Figure 11 报告 AdvMark encoding time 为 1.5s、decoding time 为 0.01s。
- Black-Q attack 的 bit accuracy 仍在论文阈值附近，作者主要强调 AdvMark 会迫使 Black-Q 付出约 15 PSNR 的攻击质量损失。
- `full.md` 中没有解析出 DOI、code URL 或正式 venue，因此本页不补猜这些元数据。

## 对本项目的用途

这篇论文补充了本项目的 robustness 对照维度：[[hfrw]] 强调 local embedding 带来的 fidelity / file-size trade-off，AdvMark 则强调在 ordinary image watermarking 中如何同时对抗 distortion、diffusion regeneration 和 adversarial attacks。它不能替代 LDM-native provenance evidence，但能提醒本项目在设计 benchmark 时需要把 regeneration / adversarial removal 与常规 image transformations 分开评估。

## 原始来源

- `raw/sources/Chen 等 - 2026 - Decoupling Defense Strategies for Robust Image Watermarking.pdf-8147032b-37f6-4091-8de2-a8ec3a76b5f6/full.md`
- `raw/sources/Chen 等 - 2026 - Decoupling Defense Strategies for Robust Image Watermarking.pdf-8147032b-37f6-4091-8de2-a8ec3a76b5f6/2e67c9e1-0e9f-47d0-b921-f7013c3073cd_origin.pdf`

## 相关页面

- [[advmark]]
- [[post-hoc-image-watermarking]]
- [[watermark-robustness]]
- [[diffusion-model-fingerprinting-comparison]]
