---
type: finding
title: "WOUAF Generates User-Fingerprinted Models under One Second"
tags: [finding, wouaf, scalability, user-attribution, weight-modulation]
related: ["[[kim-2024-wouaf]]", "[[user-attribution]]", "[[generative-model-fingerprinting]]", "[[how-to-scale-user-attribution-for-ldm]]", "[[decoder-fingerprinting-scalability-comparison]]"]
created: 2026-06-09
updated: 2026-07-16
source: "[[kim-2024-wouaf]]"
confidence: high
replicated: false
---

# WOUAF Generates User-Fingerprinted Models under One Second

## Finding

[[kim-2024-wouaf]] turns per-user fingerprint generation from a fine-tuning problem into a weight-modulation forward pass, reporting user-specific model creation in under one second.

## Evidence

Table 1 compares fingerprinting time: 8.4 hr for DAG, `< 1 min` for Stable Signature, and `< 1 sec` for WOUAF-conv and WOUAF-all. The paper also states that after one training stage, WOUAF only needs a lightweight forward pass over the user fingerprint to modulate decoder weights.

## Interpretation

This directly supports the project's hypothesis that large-scale user attribution should create user-specific copies through weight modulation or weight encoding rather than per-user fine-tuning.

## Caveat

`< 1 sec` is the model-creation cost in the paper's environment, not total platform distribution cost. A real system must also account for model storage, download, registry operations, key management, and verifier deployment.
