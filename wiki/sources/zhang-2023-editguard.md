---
type: source
title: "EditGuard: Versatile Image Watermarking for Tamper Localization and Copyright Protection"
tags: [image-watermarking, tamper-localization, proactive-forensics, copyright-protection, steganography]
related: ["[[editguard]]", "[[tamper-localization-for-generated-images]]", "[[localized-invisible-watermarking]]", "[[watermark-robustness]]", "[[localized-watermarking-for-tamper-localization-comparison]]", "[[editguard-separates-copyright-recovery-from-tamper-localization]]"]
created: 2026-07-16
updated: 2026-07-16
authors: ["Xuanyu Zhang", "Runyi Li", "Jiwen Yu", "Youmin Xu", "Weiqi Li", "Jian Zhang"]
year: 2023
url: "https://xuanyuzhang21.github.io/project/editguard/"
venue: ""
sources: ["Zhang 等 - 2023 - EditGuard Versatile image watermarking for tamper localization and copyright protection/full.md"]
---

# EditGuard: Versatile Image Watermarking for Tamper Localization and Copyright Protection

## One-line Takeaway

[[editguard]] is a proactive forensic watermarking system that sequentially embeds a semi-fragile 2D localization watermark and a robust copyright bit string, then decodes them in parallel.

## Problem

Copyright watermarking normally identifies ownership but does not identify edited regions. Passive localization networks often depend on seen tampering types. The paper targets zero-shot localization of AIGC edits while preserving copyright recovery under degradation.

## Method

EditGuard converts dual forensics into a united image-bit steganography network (IBSN). Its image-hiding and revealing modules use invertible blocks for a spatial localization watermark; separate bit-encryption and recovery modules handle the robust copyright message. A prompt-based posterior estimation module improves recovery after degradation.

## Evidence

The paper's Figure 1 states that EditGuard achieves over `95%` localization precision and nearly `100%` copyright accuracy in the illustrated evaluation. It evaluates localization, copyright recovery, and generalization to AIGC-based editing after training the image-bit steganography system without tampered samples or tamper labels.

## Limitations and Caveats

- The reported localization mechanism relies on the fragility and locality of recovered image-into-image steganography.
- The paper's quality, robustness, and localization measures are not directly equivalent to user attribution or generator-bound provenance.
- Later work in this corpus, [[zhang-2025-omniguard]], identifies fixed localization watermarks and severe degradations as important limitations of this design.

## Use in This Project

EditGuard provides a clear proactive baseline for separating robust global copyright recovery from semi-fragile local tamper evidence.

## Raw Sources

- `raw/sources/Zhang 等 - 2023 - EditGuard Versatile image watermarking for tamper localization and copyright protection/full.md`

## Related Pages

- [[editguard]]
- [[tamper-localization-for-generated-images]]
- [[localized-watermarking-for-tamper-localization-comparison]]
