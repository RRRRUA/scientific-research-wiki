---
type: source
title: "StableGuard: Towards Unified Copyright Protection and Tamper Localization in Latent Diffusion Models"
tags: [latent-diffusion-models, watermarking, tamper-localization, copyright-protection, generative-ai-safety]
related: ["[[stableguard]]", "[[latent-diffusion-watermarking]]", "[[watermark-robustness]]", "[[tamper-localization-for-generated-images]]", "[[diffusion-model-fingerprinting-comparison]]"]
created: 2026-06-11
updated: 2026-06-11
authors: ["Haoxin Yang", "Bangzhen Liu", "Xuemiao Xu", "Cheng Xu", "Yuyang Yu", "Zikai Huang", "Yi Wang", "Shengfeng He"]
year: 2025
url: "https://github.com/Harxis/StableGuard"
venue: "NeurIPS 2025"
sources: ["Yang 等 - 2025 - StableGuard Towards Unified Copyright Protection and Tamper Localization in Latent Diffusion Model.pdf-d8a32816-0fa0-4c8d-934e-e96205ef30ed/full.md"]
---

# StableGuard: Towards Unified Copyright Protection and Tamper Localization in Latent Diffusion Models

## 一句话结论

StableGuard 把 holistic binary watermark 嵌入 Latent Diffusion Models 的 VAE decoder，并训练 MoE-GFN 从同一信号中同时做 copyright verification 和 tamper localization；它扩展了本项目从“检测/用户归因”到“篡改区域定位”的方法谱系。

## 问题

已有 post-hoc watermarking 需要在生成后额外处理图像，可能增加开销并损害图像质量。Stable Signature、WOUAF、WaDiff 等 diffusion-native watermarking 改善了嵌入方式，但通常不处理 tampering localization。EditGuard、OmniGuard、WAM 等统一版权保护与篡改定位的方法仍偏 post-hoc，generation 与 forensics 不是同一个端到端优化过程。

## 方法

StableGuard 包含两个核心组件：

- Multiplexing Watermark VAE (MPW-VAE)：在 pretrained VAE decoder 中加入 lightweight latent residual-based watermark adapter，可开关 watermark，生成同一 latent code 的 watermarked / watermark-free paired images。
- Mixture-of-Experts Guided Forensic Network (MoE-GFN)：基于 UNet，在 decoder 中加入 Mixture-of-Forensic-Experts (MoFE) block。专家分支分别处理全局 watermark extraction、local tampering traces 和 frequency-domain boundary cues，并由 Dynamic Soft Router 自适应融合。

训练数据通过把 watermarked image 与 watermark-free counterpart 用 random masks 或 SAM-generated semantic masks 融合生成，不需要人工 tamper annotations。MPW-VAE 与 MoE-GFN 以 self-supervised, end-to-end 方式联合优化。

## 证据

论文在 COCO training set 上训练，在 COCO test set、custom T2I dataset 和 35,000 张图像的 AIGC tampering benchmark 上评估。AIGC benchmark 包含 25,000 张 COCO 图像和 10,000 张 T2I 图像，并使用 Stable Diffusion Inpainting、SDXL、Kandinsky、ControlNet、LaMa 等方法编辑 SAM masks 对应区域。

Table 1 报告 32-bit StableGuard 在 COCO 上达到 PSNR 40.50、SSIM 0.970、LPIPS 0.062、FID 19.5、Bit Acc 99.97；在 T2I dataset 上达到 PSNR 40.53、SSIM 0.972、LPIPS 0.060、FID 19.4、Bit Acc 99.98。

Table 2 报告 StableGuard 在 AIGC tampering dataset 的五类编辑方法上，F1 约 0.979-0.981、AUC 约 0.991-0.993、IoU 约 0.960-0.963，整体高于 EditGuard、OmniGuard、WAM 和 passive localization baselines。

Table 4 的 ablation 显示，去掉 MPW-VAE 后 F1/AUC/IoU 降到 0.811/0.796/0.774；完整 decoder placement 版本为 0.980/0.992/0.961，Bit Acc 为 99.98。

## 关键结果

- 将 copyright protection 和 tamper localization 放进同一个 diffusion-native framework。
- MPW-VAE 可生成 paired watermarked / clean samples，支撑无人工标注的 tamper training。
- MoE-GFN 用专家分支融合 holistic watermark、local traces 和 boundary cues。
- 在 bit accuracy、image fidelity、AIGC tamper localization 和 degradation robustness 上都报告强于主要对比方法。

## 局限与注意点

- 论文明确说 StableGuard 主要针对 image latent diffusion models；迁移到 video latent diffusion models 是未来方向。
- Forensic accuracy 在 image degradation 下仍会下降，尤其 tamper localization 比 watermark extraction 更依赖 local consistency。
- 方法假设图像在生成时已经被 watermark；没有 watermark 的 clean images 不在系统操作范围内，论文将其保守视为 fully tampered。
- 该工作不主打大规模 user attribution，因此不能直接回答 WOUAF / OmniMark 关注的 per-user model-copy attribution。

## 对本项目的用途

StableGuard 是当前语料中最明确连接“diffusion-native watermarking”和“pixel-level tamper localization”的论文。它适合用于区分三类任务：generated-image detection、user attribution、tamper localization。

## 原始来源

- `raw/sources/Yang 等 - 2025 - StableGuard Towards Unified Copyright Protection and Tamper Localization in Latent Diffusion Model.pdf-d8a32816-0fa0-4c8d-934e-e96205ef30ed/full.md`
- `raw/sources/Yang 等 - 2025 - StableGuard Towards Unified Copyright Protection and Tamper Localization in Latent Diffusion Model.pdf-d8a32816-0fa0-4c8d-934e-e96205ef30ed/f2b07f79-3754-4fa0-9210-8643b5d674eb_origin.pdf`

## 相关页面

- [[stableguard]]
- [[latent-diffusion-watermarking]]
- [[watermark-robustness]]
- [[tamper-localization-for-generated-images]]
- [[diffusion-model-fingerprinting-comparison]]
