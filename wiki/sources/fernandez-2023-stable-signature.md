---
type: source
title: "The Stable Signature: Rooting Watermarks in Latent Diffusion Models"
tags: [latent-diffusion-models, watermarking, stable-diffusion, detection, user-identification, generative-ai-safety]
related: ["[[latent-diffusion-watermarking]]", "[[user-attribution]]", "[[watermark-robustness]]", "[[generative-model-fingerprinting]]", "[[diffusion-model-fingerprinting-comparison]]"]
created: 2026-06-07
updated: 2026-07-16
authors: ["Pierre Fernandez", "Guillaume Couairon", "Herve Jegou", "Matthijs Douze", "Teddy Furon"]
year: 2023
url: ""
venue: ""
sources: ["Fernandez 等 - 2023 - The Stable Signature Rooting Watermarks in Latent Diffusion Models/full.md"]
---

# The Stable Signature: Rooting Watermarks in Latent Diffusion Models

## One-sentence Summary
Stable Signature fine-tunes the latent decoder to embed an invisible binary signature in every image produced by a latent diffusion model, supporting detection and user identification without post-generation watermarking.

## Problem
Post-generation watermarks are easy to remove or bypass, especially when users can access open-source generation pipelines. Passive forensic detection also struggles under extremely low false-positive requirements and usually cannot identify the model copy that generated an image reliably.

## Method
The method first pre-trains a watermark extractor and then fine-tunes only the latent decoder of the latent diffusion model so generated images contain a fixed binary signature. Bit matching and binomial statistical tests perform detection and identification.

## Evidence
The paper evaluates 48-bit signatures on Stable-Diffusion-like models with MS-COCO prompts across text-to-image, image editing, inpainting, and super-resolution. It reports high detection rates at very low false positive rates and evaluates robustness under cropping, brightness shifts, JPEG compression, and combined transformations.

## Key Results
- Detects most unmodified generated images at extremely low false-positive rates.
- Reports about 98% identification for unmodified images across 100,000 users, with lower accuracy under combined image edits.
- Has limited impact on generation quality across multiple LDM tasks.
- Rooting the signature in generation provides stronger security and efficiency than post-hoc watermarking.

## Limitations and Caveats
- Each new signature requires fine-tuning a model copy, creating scalability pressure at large user counts.
- Strong combined transformations and informed attacks reduce robustness.
- Under strong assumptions, model-level purification can reduce watermark accuracy while preserving acceptable image quality.

## Use in This Project
This paper is the foundational source for decoder-rooted LDM watermarking and provides the statistical framework for detection and identification. WOUAF and OmniMark can be compared against it on scalability and robustness.

## Original Sources
- `raw/sources/Fernandez 等 - 2023 - The Stable Signature Rooting Watermarks in Latent Diffusion Models/full.md`

## Related Pages
- [[latent-diffusion-watermarking]]
- [[user-attribution]]
- [[watermark-robustness]]
- [[generative-model-fingerprinting]]
- [[diffusion-model-fingerprinting-comparison]]
