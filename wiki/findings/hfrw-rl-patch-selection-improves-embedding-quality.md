---
type: finding
title: "HFRW RL Patch Selection Improves Embedding Quality"
tags: [finding, hfrw, deep-reinforcement-learning, patch-selection, watermarking]
related: []
created: 2026-06-11
updated: 2026-07-16
source: "[[ping-2026-hfrw]]"
confidence: high
replicated: false
---

# HFRW RL Patch Selection Improves Embedding Quality

## Finding

HFRW's dueling DQN patch selection reduces embedding distortion more effectively than random patch selection and slightly improves message extraction error.

## Evidence

Table III reports that RL-optimized patches increase PSNR from 41.15 to 43.33, reduce RMSE(Xco, Xen) from 0.0175 to 0.0136, and reduce RMSE(M, M') from 0.0879 to 0.0811 relative to random patches on the test dataset. In the single-image example in Figure 8, the optimized location raises PSNR from 39.89 to 47.44 and reduces RMSE(Xco, Xen) from 0.0202 to 0.0084.

## Interpretation

This finding shows that HFRW's reinforcement-learning module is not decorative; it performs the concrete role of selecting a low-distortion region for local embedding.
