---
type: source
title: "HFRW: High Fidelity and Robust Watermarking using Deep Reinforcement Learning"
tags: [image-watermarking, post-hoc-watermarking, localized-watermarking, reinforcement-learning, image-fidelity]
related: ["[[hfrw]]", "[[localized-invisible-watermarking]]", "[[post-hoc-image-watermarking]]", "[[watermark-robustness]]", "[[diffusion-model-fingerprinting-comparison]]", "[[hfrw-local-watermarking-improves-fidelity-and-file-size-growth]]", "[[hfrw-rl-patch-selection-improves-embedding-quality]]", "[[hfrw-localized-embedding-trades-cropping-robustness-for-fidelity]]"]
created: 2026-07-16
updated: 2026-07-16
authors: ["Ping Ping", "Ruixuan Jiang", "Bobiao Guo", "Xiaohui Yang", "Feng Xu"]
year: 2026
url: ""
venue: ""
sources: ["Ping 等 - 2026 - HFRW High Fidelity and Robust Watermarking using Deep Reinforcement Learning/full.md"]
---

# HFRW: High Fidelity and Robust Watermarking using Deep Reinforcement Learning

## One-line Takeaway

[[hfrw]] is a post-hoc localized invisible watermarking method that uses dueling deep Q-learning to choose a `128 x 128` embedding patch, CBAM-enhanced encoder/decoder networks, and synchronization for geometric attacks.

## Problem

Global invisible watermarking can change every pixel and substantially increase file size for high-resolution assets. The paper targets high fidelity, low file-size growth, and recovery after common geometric and non-geometric operations.

## Method

A dueling DQN searches an observed image region for an embedding patch using image features, position, and action history. A CBAM-enhanced encoder embeds the message into that patch. At extraction time, a localization and synchronization module locates and rectifies the patch before the decoder recovers the message.

## Evidence

The abstract reports PSNR above `54 dB` across tested datasets and FSVR below `0.5`. Table III compares random with RL-optimized patches: PSNR rises from `41.15` to `43.33`, image RMSE falls from `0.0175` to `0.0136`, and message RMSE falls from `0.0879` to `0.0811`.

Table V reports that CBAM raises patch PSNR from `34.34` to `41.24` and improves bit accuracy under JPEG, color, resize, and picture-in-picture attacks. Table IV shows the payload trade-off: at 30 effective bits, bit accuracy is `98.17%`, `99.77%`, `98.87%`, and `96.03%` under JPEG, color, resize, and PIP; the values decline as payload increases to 120 bits.

## Limitations and Caveats

- Severe cropping is a stated weakness because the watermark is localized.
- Reported effective capacity relies on four-fold replication of a 120-bit embedded message.
- HFRW is an ordinary-image, post-hoc method and does not tie provenance to a generator, user, or model copy.

## Use in This Project

HFRW is the high-fidelity and storage-overhead comparator for diffusion-native provenance methods and for broader localized watermarking approaches.

## Raw Sources

- `raw/sources/Ping 等 - 2026 - HFRW High Fidelity and Robust Watermarking using Deep Reinforcement Learning/full.md`

## Related Pages

- [[hfrw]]
- [[localized-invisible-watermarking]]
- [[post-hoc-image-watermarking]]
