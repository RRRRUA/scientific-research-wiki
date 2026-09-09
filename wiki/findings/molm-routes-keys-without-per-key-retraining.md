---
type: finding
title: "MOLM Routes Keys without Per-Key Retraining"
tags: [finding, molm, lora, routing, scalability]
related: ["[[fares-2026-molm]]", "[[molm]]", "[[user-attribution]]", "[[watermark-capacity-for-user-attribution]]", "[[decoder-fingerprinting-scalability-comparison]]"]
created: 2026-09-08
updated: 2026-09-08
source: "[[fares-2026-molm]]"
confidence: high
replicated: false
---

# MOLM Routes Keys without Per-Key Retraining

## Finding

MOLM encodes a 28-bit key through adapter-path selection after one training process, avoiding a new optimization run for every key.

## Evidence

The default configuration uses 14 VAE-decoder routing blocks with four LoRA paths per block. On Stable Diffusion and MS-COCO, Table 1 reports clean raw bit accuracy `0.98` and FID `27.7`, a change of `-1.4` relative to the paper's vanilla reference. The paper reports training in about one day on one A100 and no added generator inference overhead.

## Interpretation

Routing provides combinatorial key assignment, but usable capacity is constrained by fidelity: the reported 108-bit U-Net route visibly degrades generation quality.

