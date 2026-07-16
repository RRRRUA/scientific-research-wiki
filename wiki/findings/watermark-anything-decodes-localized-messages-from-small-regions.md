---
type: finding
title: "Watermark Anything Decodes Localized Messages from Small Regions"
tags: [finding, watermark-anything, localized-watermarking, message-extraction]
related: ["[[watermark-anything]]", "[[sander-2025-watermark-anything]]", "[[localized-invisible-watermarking]]", "[[tamper-localization-for-generated-images]]"]
created: 2026-07-16
updated: 2026-07-16
source: "[[sander-2025-watermark-anything]]"
confidence: high
replicated: false
---

# Watermark Anything Decodes Localized Messages from Small Regions

## Finding

WAM reports localization and recovery of several 32-bit messages from small, distinct image regions rather than requiring one global watermark payload.

## Evidence

The paper reports that five 32-bit messages placed in regions no larger than 10% of the image achieve more than `85%` mIoU for watermarked-area localization and more than `95%` bit accuracy after horizontal flip and contrast adjustment. In Table 7's 10%-proportion condition, WAM reports TPR `99.9%` and bit accuracy `94.2%`.

## Interpretation

The result makes localized messages a viable mechanism for splicing-aware provenance and spatial assignment. It is not equivalent to a tamper mask unless the application explicitly interprets missing or changed watermark evidence as tampering.
