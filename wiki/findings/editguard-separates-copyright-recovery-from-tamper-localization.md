---
type: finding
title: "EditGuard Separates Copyright Recovery from Tamper Localization"
tags: [finding, editguard, tamper-localization, proactive-forensics, copyright]
related: ["[[editguard]]", "[[zhang-2023-editguard]]", "[[tamper-localization-for-generated-images]]", "[[omniguard]]"]
created: 2026-07-16
updated: 2026-07-16
source: "[[zhang-2023-editguard]]"
confidence: medium
replicated: false
---

# EditGuard Separates Copyright Recovery from Tamper Localization

## Finding

EditGuard uses a robust global bit watermark and a semi-fragile spatial watermark to answer copyright ownership and edited-region localization separately.

## Evidence

Figure 1 states that the method achieves over `95%` localization precision and nearly `100%` copyright accuracy in the illustrated evaluation. The method trains its united image-bit steganography network without tampered samples, then uses recovery disruption of the spatial watermark for zero-shot localization.

## Interpretation

Separating robust copyright recovery from semi-fragile local evidence makes task boundaries explicit. The result is reported at a high level in the parsed paper, so its quantitative scope should be checked against the paper's full experimental tables before using it for benchmark-level ranking.
