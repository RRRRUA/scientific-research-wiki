---
type: finding
title: "FTFAW Reports Perfect Tracing in a One-Million-User Pool"
tags: [finding, ftfaw, user-attribution, scalability, model-fingerprinting]
related: ["[[ftfaw]]", "[[pan-2025-ftfaw]]", "[[user-attribution]]", "[[how-to-scale-user-attribution-for-ldm]]"]
created: 2026-07-20
updated: 2026-07-20
source: "[[pan-2025-ftfaw]]"
confidence: high
replicated: false
---

# FTFAW Reports Perfect Tracing in a One-Million-User Pool

## Finding

FTFAW reports tracing accuracy `1.000` for each of its evaluated `10^4`, `10^5`, and `10^6` user fingerprint pools.

## Evidence

Table III gives `1.000` for all three pool sizes. The protocol randomly selects 1,000 users from each pool, generates five images per selected user, extracts fingerprints, and assigns the user with the largest bit match in the fingerprint pool. The paper additionally reports mean per-bit tracing accuracy `0.5136` on 5,000 images from an un-fingerprinted model.

## Interpretation

This is direct scale evidence for a 48-bit, decoder weight-modulation design, but it is an in-paper sampled-pool evaluation rather than a full operational false-attribution study.
