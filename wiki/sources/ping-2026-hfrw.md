---
type: source
title: "HFRW: High Fidelity and Robust Watermarking using Deep Reinforcement Learning"
tags: [image-watermarking, robust-watermarking, deep-reinforcement-learning, local-watermarking, copyright-protection]
related: ["[[hfrw]]", "[[localized-invisible-watermarking]]", "[[watermark-robustness]]", "[[diffusion-model-fingerprinting-comparison]]"]
created: 2026-06-11
updated: 2026-06-11
authors: ["Ping Ping", "Ruixuan Jiang", "Bobiao Guo", "Xiaohui Yang", "Feng Xu"]
year: 2026
url: ""
venue: ""
sources: ["HFRW_High_Fidelity_and_Robust_Watermarking_using_Deep_Reinforcement_Learning.pdf-1d97070b-78d6-4eb4-a7a0-f24fbfba014c/full.md"]
---

# HFRW: High Fidelity and Robust Watermarking using Deep Reinforcement Learning

## 一句话结论

HFRW 是一种 localized invisible watermarking 方法：它用 dueling Q-learning 选择局部嵌入 patch，用 CBAM-enhanced encoder / decoder 嵌入和恢复消息，并用 watermark localization and synchronization module 抵抗几何攻击；它不是 LDM-native watermarking，而是本 wiki 中 post-hoc / local image watermarking 的重要对照。

## 问题

论文关注高分辨率图像的大规模版权保护场景：用户希望水印方案同时满足 high fidelity、低 file size growth rate 和对常见攻击的 robustness。作者认为 visible watermark 容易被图像编辑工具移除，而许多 deep learning-based invisible watermarking 方法使用 global embedding，处理任意分辨率图像时会带来明显质量下降和文件体积增长。

## 方法

HFRW 的流程包含三个模块：

- Self-optimization module：把 watermark embedding patch selection 建模为 Markov decision process，用 dueling DQN 在 observed region 中移动 128x128 bounding box，选择对图像质量影响较小的嵌入区域。
- CBAM-enhanced encoder / decoder：在 encoder 和 decoder 中加入 Convolutional Block Attention Module (CBAM)，强化 spatial 和 frequency domain feature learning。
- Watermark localization and synchronization module：用 U2-Net 定位被水印化的局部区域，并根据 mask 估计几何变换，用 inverse transformation 同步 patch 后再解码。

## 证据

论文在 COCO 上训练 watermarking model 和 segmentation model，并用 COCO、Flickr30k、OpenImages 做 fidelity 和 file size growth rate 评估。对比方法包括 HiDDeN、MBRS 和 SSL，统一以 30-bit copyright message 做比较；HFRW 内部实际输入 120-bit sequence，通过四重复、bit-wise averaging 和 threshold classification 得到最终 30-bit message。

Table I 报告 HFRW 在 Flickr30k、COCO、OpenImages 上的 PSNR 分别为 54.32、56.21、61.22，SSIM 分别为 0.9988、0.9991、0.9996，Bit Accuracy 均为 100，FSVR 分别为 0.31、0.27、0.17。Table II 报告三数据集平均 PSNR 57.25、SSIM 0.9992、FSVR 0.25。

Fig. 7 报告 HFRW 在 JPEG、color jitter、Gaussian noise、Gaussian blur、crop、resize、padding、PIP 等攻击下的 bit accuracy。论文总结其 non-geometric attacks 下通常超过 90% 或接近 100%，resize 和 padding 接近 100%，PIP 高于 93%；但 severe crop 下性能下降，crop ratio 0.35 时约 84。

Table III 显示 RL-optimized patches 相比 random patches 将 PSNR 从 41.15 提高到 43.33，并把 RMSE(Xco, Xen) 从 0.0175 降到 0.0136。Table V 显示加入 CBAM 后 PSNR 从 34.34 提升到 41.24，并改善 JPEG、Color、Resize、PIP 下的 bit accuracy。

## 局限与注意点

- HFRW 是 post-hoc / image-level watermarking，不是 diffusion-native，也不直接支持 model-copy user attribution。
- 由于水印只嵌入 128x128 local patch，严重 cropping 可能直接移除嵌入区域。论文明确承认这是 localized embedding 的固有限制。
- 论文把 file size growth rate 作为重要指标，这对大规模高分辨率图像存储有意义，但不能替代 LDM provenance 中的 false positive control、multi-key capacity 或 white-box model attack 评估。

## 对本项目的用途

HFRW 给本项目提供一个清晰的 non-LDM 对照：通过局部嵌入可以显著改善 fidelity 和 FSVR，但其部署边界和 LDM-native watermarking 不同。它适合用于比较 post-hoc local image watermarking 与 decoder/noise/weight-rooted diffusion watermarking 的取舍。

## 原始来源

- `raw/sources/HFRW_High_Fidelity_and_Robust_Watermarking_using_Deep_Reinforcement_Learning.pdf-1d97070b-78d6-4eb4-a7a0-f24fbfba014c/full.md`
- `raw/sources/HFRW_High_Fidelity_and_Robust_Watermarking_using_Deep_Reinforcement_Learning.pdf-1d97070b-78d6-4eb4-a7a0-f24fbfba014c/c7433e92-82e3-4618-94f3-5cb74011b7e5_origin.pdf`

## 相关页面

- [[hfrw]]
- [[localized-invisible-watermarking]]
- [[watermark-robustness]]
- [[diffusion-model-fingerprinting-comparison]]
