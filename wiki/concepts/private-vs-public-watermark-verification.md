---
type: concept
title: "Private vs Public Watermark Verification"
created: 2026-06-09
updated: 2026-06-09
tags: [watermark-verification, provenance, governance, detection]
related: ["[[tree-ring-watermark]]", "[[ddim-inversion-for-watermark-detection]]", "[[latent-diffusion-watermarking]]", "[[user-attribution]]", "[[watermark-robustness]]"]
sources: ["Wen 等 - 2023 - Tree-Ring Watermarks Fingerprints for Diffusion Images that are Invisible and Robust.pdf-009a7e2b-80bb-48a7-bf25-28b175fc8239/full.md"]
---

# Private vs Public Watermark Verification

Private vs public watermark verification 区分的是“谁能验证图像是否带有 watermark”。Private verification 通常要求 model owner 或可信服务持有 model、secret key 或专用 detector；public verification 则允许第三方用公开或互操作的 detector 独立验证。

## Tree-Ring 的位置

[[tree-ring-watermark]] 更接近 private verification。检测需要通过相同或兼容的 diffusion model 做 [[ddim-inversion-for-watermark-detection]]，并检查 secret key。因此平台、媒体机构或独立审计者如果没有 model owner 提供的验证接口，很难直接复现检测。

## 安全收益

Private verification 可以减少攻击者的反馈。如果攻击者无法可靠查询 watermark 是否被移除，就更难优化 removal attack。这对 [[watermark-robustness]] 有利。

## 部署代价

缺点是互操作性较弱。开放环境中的 provenance system 往往希望第三方快速验证图片来源；如果每次都必须依赖 model owner 的 API 或模型访问，治理和取证流程会更复杂。
