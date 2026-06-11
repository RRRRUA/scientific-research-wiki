---
type: reference-database
title: Master Reference Database
tags: [research-wiki, references, citation-mining]
---

# Master Reference Database

_Generated: 2026-06-11_ · Mined from the `# REFERENCES` sections of all parsed papers in `raw/sources/`.

Deduplicated by normalized title (+ author-surname/year). `cited_by` lists the curated wiki sources (or raw folders) whose reference list contains the work; `cited_count` is its citation frequency **within this corpus** (a centrality/depth signal). Fields are faithful to the parses — missing fields are `n/a`, never guessed.

## Summary

- **Parses mined:** 4 `full.md` files → 4 distinct curated/raw papers.
- **Reference strings parsed:** 286.
- **Unique references after dedup:** 265.
- **Cited by >= 2 corpus papers:** 18 (foundational / depth signal).
- **Cited by >= 3 corpus papers:** 0.

## Most-cited references (centrality ranking, cited_count >= 2)

Sorted by in-corpus citation frequency. These are the works the curated corpus leans on most.

| cited_count | Year | Title | Authors | Venue | vol/no/pp | cited_by | curated? |
|---|---|---|---|---|---|---|---|
| 2 | 2023 | n/a | n/a | Guangyu Nie, Changhoon Kim, Yezhou Yang, and Yi Ren. Attributing image generative models using latent fingerprints. arXiv preprint arXiv:2304.09752 | n/a | fernandez-2023-stable-signature, kim-2024-wouaf | no |
| 2 | 2022 | n/a | n/a | Aditya Ramesh, Prafulla Dhariwal, Alex Nichol, Casey Chu, and Mark Chen. Hierarchical text-conditional image generation with clip latents. arXiv preprint arXiv:2204.06125 | n/a | fernandez-2023-stable-signature, kim-2024-wouaf | no |
| 2 | 2022 | n/a | n/a | Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Bjorn Ommer. High-resolution image ¨ synthesis with latent diffusion models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 10684–10695 — Proc. IEEE | n/a | fernandez-2023-stable-signature, kim-2024-wouaf | no |
| 2 | 2022 | n/a | n/a | Ning Yu, Vladislav Skripniuk, Dingfan Chen, Larry Davis, and Mario Fritz. Responsible disclosure of generative models using scalable fingerprinting. In International Conference on Learning Representations (ICLR) | n/a | fernandez-2023-stable-signature, kim-2024-wouaf | no |
| 2 | 2021 | n/a | n/a | Patrick Esser, Robin Rombach, and Bjorn Ommer. Taming transformers for high-resolution image synthesis. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 12873–12883 — Proc. IEEE | n/a | fernandez-2023-stable-signature, kim-2024-wouaf | no |
| 2 | 2021 | n/a | n/a | Ning Yu, Vladislav Skripniuk, Sahar Abdelnabi, and Mario Fritz. Artificial fingerprinting for generative models: Rooting deepfake attribution in training data. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pages 14448–14457 — Proc. IEEE | n/a | fernandez-2023-stable-signature, kim-2024-wouaf | no |
| 2 | 2020 | n/a | n/a | Zhengxue Cheng, Heming Sun, Masaru Takeuchi, and Jiro Katto. Learned image compression with discretized gaussian mixture likelihoods and attention modules. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 7939–7948 — Proc. IEEE | n/a | fernandez-2023-stable-signature, kim-2024-wouaf | no |
| 2 | 2020 | n/a | n/a | Tero Karras, Miika Aittala, Janne Hellsten, Samuli Laine, Jaakko Lehtinen, and Timo Aila. Training generative adversarial networks with limited data. Advances in Neural Information Processing Systems, 33:12104–12114 | n/a | fernandez-2023-stable-signature, kim-2024-wouaf | no |
| 2 | 2020 | n/a | n/a | Tero Karras, Samuli Laine, Miika Aittala, Janne Hellsten, Jaakko Lehtinen, and Timo Aila. Analyzing and improving the image quality of stylegan. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 8110–8119 — Proc. IEEE | n/a | fernandez-2023-stable-signature, kim-2024-wouaf | no |
| 2 | 2020 | n/a | n/a | Jiaming Song, Chenlin Meng, and Stefano Ermon. Denoising diffusion implicit models. arXiv preprint arXiv: | n/a | fernandez-2023-stable-signature, kim-2024-wouaf | no |
| 2 | 2019 | n/a | n/a | Tero Karras, Samuli Laine, and Timo Aila. A style-based generator architecture for generative adversarial networks. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 4401–4410 — Proc. IEEE | n/a | fernandez-2023-stable-signature, kim-2024-wouaf | no |
| 2 | 2018 | n/a | n/a | Johannes Balle, David Minnen, Saurabh Singh, Sung Jin ´ Hwang, and Nick Johnston. Variational image compression with a scale hyperprior. arXiv preprint arXiv:1802.01436 | n/a | fernandez-2023-stable-signature, kim-2024-wouaf | no |
| 2 | 2018 | n/a | n/a | Richard Zhang, Phillip Isola, Alexei A Efros, Eli Shechtman, and Oliver Wang. The unreasonable effectiveness of deep features as a perceptual metric. In CVPR. IEEE | n/a | fernandez-2023-stable-signature, kim-2024-wouaf | no |
| 2 | 2018 | n/a | n/a | Jiren Zhu, Russell Kaplan, Justin Johnson, and Li Fei-Fei. Hidden: Hiding data with deep networks. In ECCV | n/a | fernandez-2023-stable-signature, kim-2024-wouaf | no |
| 2 | 2017 | n/a | n/a | Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, and Sepp Hochreiter. Gans trained by a two time-scale update rule converge to a local nash equilibrium. Advances in neural information processing systems, 30 | n/a | fernandez-2023-stable-signature, kim-2024-wouaf | no |
| 2 | 2017 | n/a | n/a | Yusuke Uchida, Yuki Nagai, Shigeyuki Sakazawa, and Shin’ichi Satoh. Embedding watermarks into deep neural networks. In Proceedings of the | n/a | fernandez-2023-stable-signature, kim-2024-wouaf | no |
| 2 | 2014 | n/a | n/a | Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays, Pietro Perona, Deva Ramanan, Piotr Dollar, and ´ C Lawrence Zitnick. Microsoft coco: Common objects in context. In European conference on computer vision, pages 740–755. Springer | n/a | fernandez-2023-stable-signature, kim-2024-wouaf | no |
| 2 | 2009 | n/a | n/a | Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. Imagenet: A large-scale hierarchical image database. In | n/a | fernandez-2023-stable-signature, kim-2024-wouaf | no |

_Full record set (all 265 unique references, including singletons) lives in the companion `reference-database.json`._
