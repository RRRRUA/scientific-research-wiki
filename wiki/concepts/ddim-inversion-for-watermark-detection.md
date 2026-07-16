---
type: concept
title: "DDIM Inversion for Watermark Detection"
created: 2026-06-09
updated: 2026-07-16
tags: [ddim-inversion, diffusion-models, watermark-detection]
related: ["[[tree-ring-watermark]]", "[[fourier-noise-watermarking]]", "[[latent-diffusion-watermarking]]", "[[watermark-robustness]]", "[[private-vs-public-watermark-verification]]"]
sources: ["Wen 等 - 2023 - Tree-Ring Watermarks Fingerprints for Diffusion Images that are Invisible and Robust.pdf-009a7e2b-80bb-48a7-bf25-28b175fc8239/full.md"]
---

# DDIM Inversion for Watermark Detection

DDIM inversion for watermark detection approximately maps a final image back to the initial noise used in diffusion sampling. In [[tree-ring-watermark]], the watermark key is stored in the Fourier space of the initial noise rather than in final-image pixels, so detection must first recover or estimate that noise.

## Role in Tree-Ring

Tree-Ring writes a key into the initial noise during generation. Detection starts from a candidate image, estimates the initial noise by reversing the diffusion process, transforms the estimate into Fourier space, and checks the designated mask for the secret key pattern. The paper also uses a statistical test to control false positive rate.

## Advantages

- Detection does not require the original text prompt; the paper uses an empty prompt for inversion in its Stable Diffusion setting.
- The watermark does not need to be overlaid on the image as a post-hoc pattern.
- When inversion is accurate enough, detection can verify a hidden key from the generation process.

## Limitations

Detection quality depends directly on inversion quality. Strong image edits, combined transformations, sampler changes, or lack of access to a compatible model can weaken this path. It is therefore generally better suited to private verification by the model owner than to fully open public verification.
