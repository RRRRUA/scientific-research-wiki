---
type: overview
title: "项目概览"
tags: [overview, latent-diffusion, watermarking, fingerprinting, user-attribution, tamper-localization]
related: ["[[generative-model-fingerprinting]]", "[[latent-diffusion-watermarking]]", "[[user-attribution]]", "[[watermark-robustness]]", "[[tamper-localization-for-generated-images]]", "[[diffusion-model-fingerprinting-comparison]]", "[[localized-watermarking-for-tamper-localization-comparison]]", "[[decoder-fingerprinting-scalability-comparison]]", "[[anti-collusion-model-distribution-comparison]]", "[[inversion-watermark-robustness-comparison]]", "[[watermark-verification-operands]]", "[[decoder-rooted-fingerprinting-scales-through-weight-encoding]]", "[[latentshield]]", "[[syntag]]", "[[molm]]", "[[genptw]]", "[[robin]]", "[[robin-plus-plus]]", "[[latent-watermark]]"]
created: 2026-06-11
updated: 2026-09-08
---

# 项目概览

这个 wiki 研究生成系统如何在不明显损害图像质量的前提下，嵌入不可见且可验证的 watermarks / fingerprints，用于 generated-image detection、user attribution、model-copy fingerprinting、copyright traceability 和 tamper localization。

## 当前语料

当前语料包含 23 篇去重后的论文，覆盖 latent diffusion / generative provenance、model-copy fingerprinting、inversion robustness、anti-collusion distribution，以及 post-hoc / proactive image watermarking：

其中 AdvMark 的两份 MinerU parse 已归并到同一个 canonical source [[chen-2026-advmark]]，不重复计入论文数量。

- [[fernandez-2023-stable-signature]]：把 signature root 到 latent decoder，用于 generated-image detection 和有限 user identification。
- [[wen-2023-tree-ring-watermarks]]：把 key pattern 写入 initial noise 的 Fourier space，并通过 [[ddim-inversion-for-watermark-detection]] 检测。
- [[kim-2024-wouaf]]：用 user fingerprint 调制 decoder weights，面向 distributor-side user attribution。
- [[pan-2025-ftfaw]]：以 two-stage fine-tuning、adaptive loss weighting 和 dynamic post-processing 改善 decoder weight modulation 的 fidelity / robustness trade-off。
- [[fei-2025-omnimark]]：用 OmniMark layers 在 VAE decoder weights 的多个维度编码 fingerprint，强调快速生成大量 fingerprinted model copies。
- [[yang-2025-stableguard]]：用 MPW-VAE 和 MoE-GFN 把 copyright verification 与 [[tamper-localization-for-generated-images]] 放进 unified diffusion-native framework。
- [[ping-2026-hfrw]]：用 localized invisible watermarking 和 deep reinforcement learning 保护普通高分辨率图像，是 post-hoc / image-level watermarking 的 fidelity 对照路线。
- [[chen-2026-advmark]]：用 AdvMark 的 two-stage defense 处理 distortion、regeneration 和 adversarial attacks，是 post-hoc image watermarking 的 robustness 对照路线。
- [[bui-2023-trustmark]]：用 TrustMark 做 arbitrary-resolution post-hoc watermarking，并用 TrustMark-RM 支持 watermark removal / re-watermarking workflows。
- [[ci-2024-wmadapter]]：用 contextual VAE adapter 在生成时嵌入可变 watermark bits，避免为每条消息单独 fine-tune VAE decoder。
- [[dai-2026-secure-distribution]]：把 Lie-group LoRA watermarking 与 Spectral Weight Modulation 结合，关注 white-box model-copy collusion。
- [[zhang-2026-msat-ldm]]：用 free-generation distribution 训练可迁移的模块化 watermark processor，并面向 fine-tuned / LoRA LDM 的 few-shot adaptation。
- [[sander-2025-watermark-anything]]：把 watermark extraction 做成 pixel-level detection 和 message decoding，支持小区域与多消息。
- [[zhang-2023-editguard]]：以 robust copyright watermark 加 semi-fragile localization watermark 做主动篡改定位。
- [[zhang-2025-omniguard]]：以 adaptive localized watermark 和 degradation-aware extractor 改善 EditGuard 类框架的 fidelity 与 degradation robustness。
- [[meng-2024-latent-watermark]]：在 VAE latent 中注入和恢复 64-bit message，并显示 raw BitAcc 与 thresholded detection 的结论可能不同。
- [[huang-2024-robin]]：在 initial noise 的中频区域嵌入 zero-bit pattern，并用 optimized prompt 隐藏可见影响。
- [[fang-2025-syntag]]：给 inversion-based watermark 加 transformation-sensitive tag、homography predictor 和几何校正。
- [[fares-2026-molm]]：通过 LoRA marker 的组合路由编码用户 key，避免逐 key 重新训练完整模型。
- [[fei-2026-anti-collusion-fingerprinting]]：用 personalized normalization 与 channel transforms 让合谋模型显著失去生成效用，但不直接识别 colluders。
- [[gan-2026-genptw]]：用同一 latent embedding 同时支持 provenance bits 与 tamper localization。
- [[huang-2026-robin-plus-plus]]：把 robust frequency-domain copyright mark 与 fragile spatial localization pattern 联合起来。
- [[bekkari-2026-latentshield]]：通过 adversarial、semantic 和 dynamic-weight objectives 提高 latent payload 的复合攻击恢复能力。

## 阅读路径

先读 [[generative-model-fingerprinting]]、[[latent-diffusion-watermarking]] 和 [[watermark-robustness]]，建立任务和指标框架。随后读 source pages，重点比较嵌入位置：decoder、initial noise、weight modulation、multi-dimensional weight encoding、VAE adapter + forensic network、post-hoc local patch、post-hoc robust image optimization、post-hoc residual scaling。

如果目标是大规模 user attribution，继续读 [[user-attribution]]、[[watermark-capacity-for-user-attribution]]、[[how-to-scale-user-attribution-for-ldm]] 和 [[decoder-fingerprinting-scalability-comparison]]；模型合谋证据看 [[anti-collusion-model-distribution-comparison]]。如果目标是 inversion 与几何攻击，读 [[inversion-watermark-robustness-comparison]]。如果目标是 forensic localization，读 [[tamper-localization-for-generated-images]] 和 [[localized-watermarking-for-tamper-localization-comparison]]。跨论文抄录指标前先读 [[watermark-verification-operands]]，避免把 raw BitAcc、TPR@FPR、zero-bit accuracy 与定位指标混为一谈。

## 当前结论

Decoder-rooted watermarking 是 LDM provenance 的实用起点，但大规模 user attribution 更可能依赖 weight modulation 或 multi-dimensional weight encoding，而不是为每个用户单独 fine-tune decoder。FTFAW 进一步说明这条路线的核心优化目标不只在 distribution speed，也在于先稳定 fingerprint learning、再恢复 image-quality optimization。Tree-Ring 说明 initial-noise watermarking 可以在不训练模型的情况下提供强 provenance detection，但多 key capacity 仍是开放问题。StableGuard 说明同一个 watermark signal 可以进一步服务 tamper localization。

WMAdapter 和 MSAT-LDM 说明 adapter / modular route 可以把 flexible message control、training-data alignment 与 model-variant transfer 单独优化；Secure Distribution 进一步把 white-box collusion 加入分发模型的 threat model。现有证据表明“抗合谋”需要单独区分：让 colluded model 不可用不等于识别全部 colluders。

HFRW、AdvMark、TrustMark、WAM、EditGuard 和 OmniGuard 说明 post-hoc / proactive image watermarking 仍然有重要参考价值：HFRW 展示 local embedding 对 fidelity 和 file-size growth 的改善，TrustMark 展示 arbitrary-resolution deployment 与 re-watermarking workflow，WAM 把 local messages 变成 pixel-level evidence，EditGuard 与 OmniGuard 将 copyright recovery 和 tamper localization 分离。但这类方法通常不能替代 diffusion-native provenance，因为它们缺少与用户、模型副本或生成过程的内生绑定。

新增证据把原有结论拆成三条更清楚的路线。MOLM 展示了 compositional LoRA routing 的容量优势；Fei et al. (2026) 与 Secure Distribution 都把 anti-collusion 表述为 merged model 的 utility destruction，而不是 colluder identification；SynTag、ROBIN 与 ROBIN++ 则说明 inversion-based detection 的几何同步、可逆轨迹和多重攻击需要独立评估。GenPTW 与 ROBIN++ 扩展了 joint provenance-localization 路线，但它们的 F1/IoU 不能替代 payload 或 attribution 指标。

## 关键证据

- Stable Signature 支持低 FPR generated-image detection，但 user identification 会随用户规模和 image edits 下降。
- WOUAF 和 OmniMark 把用户差异编码到权重或权重层中，明显更接近平台分发场景。
- FTFAW 在其采样的 `10^4`、`10^5`、`10^6` user pools 上报告 `1.000` tracing accuracy，并在相同 Table II 中以更高 PSNR/SSIM 和更低 LPIPS 对比 WOUAF-Robust。
- Tree-Ring 把 watermark 放进 sampling process，强化 private provenance verification。
- StableGuard 把 proactive watermarking 与 tamper localization 结合，在 AIGC tampering benchmark 上报告高 F1/AUC/IoU。
- HFRW 在 ordinary image watermarking 中报告高 PSNR/SSIM、低 FSVR 和常见攻击下较高 bit accuracy，但 severe cropping 是局部嵌入弱点。
- AdvMark 把 encoder-focused adversarial fine-tuning 与 quality-aware direct image optimization 分开，报告更好的 clean accuracy、image quality 和 advanced-attack robustness。
- TrustMark 在 CLIC、DIV2K 和 MetFace 上报告高 PSNR/SSIM 与较高 noised bit accuracy，并用 residual-based Resolution Scaling 支持 original-resolution evaluation。
- Secure Distribution 在报告的 nonlinear collusion 下把 Bit Acc 降到约 random guessing，同时 PSNR 低于 `7 dB`，将 anti-collusion 表述为 utility destruction。
- WAM、EditGuard 和 OmniGuard 的核心指标除了 bit recovery 还包括 watermarked-area localization 或 tamper-mask F1/AUC/IoU。
- MOLM 的默认 28-bit 方案通过 LoRA 组合路由免除逐 key 训练；论文中的 generated-image sample averaging 不是 model-parameter collusion。
- Fei et al. (2026) 的两方平均合谋让 ACT 模型 FID 升至 `79.51`，说明其防御代价主要体现为效用破坏。
- SynTag 在几何攻击下显著恢复 GauShad/Tree-Ring 检测，但主实验只有 50 张图，1,000 个 negative samples 也不足以直接验证 `10^-6` 级 FPR。
- Latent Watermark 的复合攻击 raw BitAcc 为 `90.00%`，同时 thresholded TPR@1%FPR 为 `100%`；这不是 exact 64-bit recovery。
- GenPTW 与 ROBIN++ 报告高 localization F1/AUC/IoU，但跨架构结果和 zero-bit classification accuracy 需要按各自实验操作数解释。

## 待跟踪问题

- 多用户 false positive control 和 traitor tracing。
- White-box fine-tuning、distillation、decoder replacement、purification 和 collusion attacks。
- Colluder identification、utility destruction 与 false-positive control 的联合评估。
- Regeneration / adversarial removal 与常规 image transformations 应该在同一 benchmark 中分开报告。
- Arbitrary-resolution evaluation、watermark removal 和 re-watermarking 应该与 robustness 指标分开记录。
- Public verification 与 private verification 的部署取舍。
- 同一 benchmark 中联合评估 detection、user attribution、tamper localization、fidelity 和 storage cost 的 protocol。
- 低 FPR 声明所需的 negative-set 规模、置信区间，以及 candidate-pool sampling 规则。
- 在相同攻击强度下分别报告 payload recovery、zero-bit verification、exact attribution 与 localization，避免跨 protocol 排名。
