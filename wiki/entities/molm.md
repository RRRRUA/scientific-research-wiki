---
type: entity
title: "MOLM"
tags: [method, lora, routing, model-fingerprinting]
related: ["[[fares-2026-molm]]", "[[generative-model-fingerprinting]]", "[[user-attribution]]", "[[decoder-fingerprinting-scalability-comparison]]"]
created: 2026-09-08
updated: 2026-09-08
sources: ["Fares 等 - 2026 - MOLM Mixture of LoRA Markers/full.md"]
---

# MOLM

Mixture of LoRA Markers (MOLM) embeds a binary key by routing generation through selected LoRA adapters in frozen-model blocks. Its default VAE-decoder configuration uses 14 routing layers and four paths per layer for a 28-bit key without per-key retraining.

