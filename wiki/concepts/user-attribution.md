---
type: concept
title: "User Attribution"
tags: [attribution, accountability, model-distribution]
related: ["[[generative-model-fingerprinting]]", "[[latent-diffusion-watermarking]]", "[[watermark-robustness]]", "[[watermark-capacity-for-user-attribution]]", "[[watermark-verification-operands]]", "[[how-to-scale-user-attribution-for-ldm]]", "[[pan-2025-ftfaw]]", "[[dai-2026-secure-distribution]]", "[[fei-2025-omnimark]]", "[[fares-2026-molm]]", "[[fei-2026-anti-collusion-fingerprinting]]", "[[meng-2024-latent-watermark]]"]
created: 2026-06-07
updated: 2026-09-08
---

# User Attribution

## Definition
User attribution links generated content to the specific user, customer, or model copy that produced it.

## Typical Workflow
1. A provider or distributor assigns a unique fingerprint to each user.
2. Generated images carry that fingerprint invisibly.
3. A verifier extracts a candidate fingerprint from a suspicious image.
4. A statistical test compares the extracted bits with registered user fingerprints.

## Why It Is Harder Than Detection
Detection asks whether an image came from a model family. Attribution asks which user among many candidates generated it. As the user population grows, false-positive control becomes stricter and the matching threshold generally must increase.

## Related Papers
- [[fernandez-2023-stable-signature]] models detection and identification with binomial tests.
- [[kim-2024-wouaf]] focuses on distributor-oriented attribution.
- [[fei-2025-omnimark]] focuses on scalable per-user fingerprint generation.
- [[pan-2025-ftfaw]] adds a quality-focused two-stage optimization schedule and reports perfect tracing in its sampled `10^4`, `10^5`, and `10^6` user-pool evaluations.
- [[dai-2026-secure-distribution]] adds a collusion-defense mechanism: user copies remain functionally equivalent before collusion, while the evaluated merges damage usability when traceability is removed.
- [[fares-2026-molm]] uses 28-bit LoRA routing for new keys without per-key retraining, but does not evaluate model-parameter collusion.
- [[fei-2026-anti-collusion-fingerprinting]] evaluates 48-bit personalized normalization up to a sampled `10^4`-user set and makes merged copies unusable through ACT.
- [[meng-2024-latent-watermark]] demonstrates why thresholded detection and exact payload recovery must remain separate in attribution claims.

## Collusion Boundary

Fast copy generation and high bit accuracy do not establish collusion resistance. A distribution protocol must state whether it seeks to identify colluders, make colluded copies unusable, or merely preserve a watermark after a merge. [[secure-distribution]] and [[fei-2026-anti-collusion-fingerprinting]] supply evidence for the second objective, not the first. See [[anti-collusion-model-distribution-comparison]].

## Boundary Cases

[[tree-ring-watermark]] and [[stableguard]] support provenance or copyright verification, but they are not primary evidence for large-scale user attribution. Tree-Ring has not established multi-key capacity, while StableGuard primarily targets tamper localization.
