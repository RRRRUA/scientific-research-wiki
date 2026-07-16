---
type: finding
title: "HFRW Local Watermarking Improves Fidelity and File Size Growth"
tags: [finding, hfrw, image-fidelity, file-size-growth, watermarking]
related: ["[[hfrw]]", "[[ping-2026-hfrw]]", "[[watermark-robustness]]", "[[localized-invisible-watermarking]]"]
created: 2026-06-11
updated: 2026-07-16
source: "[[ping-2026-hfrw]]"
confidence: high
replicated: false
---

# HFRW Local Watermarking Improves Fidelity and File Size Growth

## Finding

ping-2026-hfrw reports that localized invisible watermarking substantially improves image fidelity and reduces file size growth rate to nearly negligible levels while maintaining high bit accuracy for a 30-bit message.

## Evidence

Table I reports HFRW PSNR of 54.32, 56.21, and 61.22 on Flickr30k, COCO, and OpenImages; SSIM of 0.9988, 0.9991, and 0.9996; Bit Accuracy of 100 on all three; and FSVR of 0.31, 0.27, and 0.17. Table II reports averages of PSNR 57.25, SSIM 0.9992, and FSVR 0.25.

## Interpretation

These results provide an important comparison: local patch embedding can achieve higher fidelity and lower storage overhead than global image watermarking. It remains image-level post-hoc watermarking and is not equivalent to provenance or user attribution rooted inside an LDM.
