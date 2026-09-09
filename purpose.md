# Project Purpose — Research Deep-Dive

## Research Question

> How can image generation systems embed robust, scalable fingerprints or watermarks for generated-image detection, user attribution, copyright traceability, and tamper localization without significantly harming generation quality?

## Hypothesis / Working Thesis

> Decoder-rooted watermarking is a practical foundation for latent diffusion model provenance, but scalable user attribution likely requires weight modulation or multi-dimensional fingerprint encoding rather than per-user fine-tuning.

## Background

This project currently studies twenty-three papers spanning diffusion-native provenance, scalable model-copy fingerprinting, inversion robustness, anti-collusion distribution, and post-hoc/proactive forensic comparators:

- [[fernandez-2023-stable-signature]] roots invisible watermarks in the latent decoder.
- [[kim-2024-wouaf]] uses weight modulation for distributor-oriented user attribution.
- [[pan-2025-ftfaw]] uses two-stage fine-tuning and adaptive loss weighting to improve the quality-robustness trade-off of decoder weight modulation.
- [[fei-2025-omnimark]] improves scalability by rapidly generating uniquely fingerprinted model copies.
- [[wen-2023-tree-ring-watermarks]] embeds watermark keys into the initial diffusion noise in Fourier space and detects them through DDIM inversion.
- [[yang-2025-stableguard]] integrates a binary watermark into the LDM VAE decoder and uses it for both copyright verification and tamper localization.
- [[ping-2026-hfrw]] uses localized invisible watermarking and deep reinforcement learning to improve fidelity, robustness, and file size growth for ordinary high-resolution image watermarking.
- [[chen-2026-advmark]] decouples adversarial, distortion, and regeneration defenses for robust post-hoc image watermarking.
- [[bui-2023-trustmark]] introduces arbitrary-resolution post-hoc image watermarking and TrustMark-RM for re-watermarking workflows.
- [[ci-2024-wmadapter]] adds a contextual VAE-decoder watermark adapter with flexible message control.
- [[dai-2026-secure-distribution]] studies anti-collusion model distribution through spectral weight modulation.
- [[zhang-2026-msat-ldm]] trains a transferable modular watermark module on internally generated latents.
- [[sander-2025-watermark-anything]] localizes watermarked areas and decodes several messages from small image regions.
- [[zhang-2023-editguard]] pairs copyright recovery with semi-fragile tamper-localization evidence.
- [[zhang-2025-omniguard]] augments versatile watermarking with blind, degradation-aware tamper extraction.
- [[meng-2024-latent-watermark]] injects and decodes 64-bit messages directly in the latent space and exposes the distinction between raw bit recovery and thresholded detection.
- [[huang-2024-robin]] hides a robust frequency-domain pattern with prompt optimization and verifies it through inversion.
- [[fang-2025-syntag]] adds a geometric synchronization tag and correction module to inversion-based watermarks.
- [[fares-2026-molm]] composes binary fingerprints by routing generation through mixtures of LoRA markers.
- [[fei-2026-anti-collusion-fingerprinting]] combines personalized normalization with function-invariant transforms to deter model-copy collusion.
- [[gan-2026-genptw]] uses one latent embedding route for provenance tracing and tamper localization.
- [[huang-2026-robin-plus-plus]] couples robust copyright verification with fragile spatial tamper evidence in two domains.
- [[bekkari-2026-latentshield]] optimizes latent payload robustness with adversarial, semantic, and dynamically weighted objectives.

The motivating gap is accountability for AI-generated images: platforms and model providers need to detect generated content and, in some settings, trace misuse to a specific user or model copy.

## Sub-questions

1. How do decoder-level watermarks compare with post-hoc image watermarking?
2. How does the number of users affect false-positive thresholds and attribution accuracy?
3. Which method best balances image quality, robustness, and deployment scalability?
4. How vulnerable are these methods to white-box model attacks such as fine-tuning or purification?
5. When does watermarking need to support pixel-level tamper localization rather than only image-level detection or user attribution?
6. What trade-offs appear when comparing diffusion-native watermarking with post-hoc localized image watermarking?
7. How should arbitrary-resolution deployment, watermark removal, and re-watermarking be evaluated alongside robustness?
8. Can model distribution remain accountable under white-box collusion, and does the design identify colluders or merely make colluded copies unusable?
9. When is a localized watermark mask evidence of provenance, and when is it a defensible tamper-localization mask?
10. How should geometric synchronization be evaluated separately from ordinary photometric robustness in inversion-based watermarks?
11. Which metric operand is actually reported: raw BitAcc, exact recovery, zero-bit accuracy/AUC, TPR at a fixed FPR, candidate-pool attribution, or localization quality?

## Scope

**In scope:**
- Latent diffusion and Stable Diffusion-style image generation.
- Watermarking, fingerprinting, user attribution, and generated-image provenance.
- Tamper localization for generated images when it is grounded in watermarking or proactive forensics.
- Post-hoc image watermarking papers when they clarify fidelity, robustness, file-size, advanced-attack, or deployment trade-offs for the main LDM question.
- Robustness against image post-processing and model-level attacks.
- Literature-review synthesis across related papers.

**Out of scope:**
- Legal policy design for AI-generated media.
- Full implementation or reproduction of all experiments.
- Non-image modalities unless added as future reading.

## Methodology

- Read each paper into a structured source page.
- Extract reusable concepts into concept pages.
- Maintain research questions in `wiki/queries/`.
- Write synthesis pages that compare methods across mechanisms, results, limitations, and open gaps.
- Link every claim back to source pages or raw paper markdown when possible.

## Success Criteria

- The wiki can distinguish fixed signatures, flexible adapters, scalable model-copy fingerprints, anti-collusion distribution, and post-hoc/localized watermarking routes.
- The wiki can support a related-work paragraph on diffusion model watermarking and fingerprinting.
- The wiki can identify open research gaps around scalability and white-box robustness.
- New papers can be added using the same source/concept/query/synthesis structure.

## Current Status

> Started on 2026-06-07. Twenty-three distinct papers have been imported, summarized, and linked into the wiki; duplicate parses are counted once.

## Language Policy

The wiki is now English-first for agent-facing knowledge pages. Source, concept, entity, finding, comparison, synthesis, query, thesis, and reference pages should use concise English prose and canonical English technical names. Chinese is reserved for human-facing orientation and navigation pages such as README, purpose, overview, index, and log. Avoid bilingual duplication. Greek, Dutch, Indonesian, or other non-English/non-Chinese generated prose should be treated as language drift and moved to archive/language-review/ before rebuilding.
