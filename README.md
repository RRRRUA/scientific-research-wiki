# Scientific Research Wiki

A long-running research deep-dive on **watermarking, fingerprinting, provenance,
user attribution, and tamper localization for generative image systems**,
especially Latent Diffusion Models (LDMs).

The current center of gravity is diffusion-model watermarking and generative
model fingerprinting: where the signal is embedded, how it survives edits and
attacks, whether it can identify users or model copies, and how it can support
copyright verification or tamper localization. Adjacent image-watermarking
papers are also included when they provide useful baselines or design contrasts.

This wiki is meant to grow over time. It is not just a paper list: sources are
curated into structured notes, linked into reusable concepts, distilled into
grounded findings, and then compared through synthesis pages and working theses.

Built and indexed with [LLM Wiki](https://github.com/llm-wiki). Wikilinks
(`[[page-slug]]`) form the graph; YAML frontmatter typing is enforced by
`schema.md`.

## Layout

```text
purpose.md          Research question, hypothesis, scope, methodology
schema.md           Page-type / frontmatter / cross-link conventions
wiki/               Curated knowledge graph (markdown + wikilinks)
  overview.md       Project state at a glance
  index.md          Type-grouped page directory
  log.md            Reverse-chronological activity log
  entities/         Named things: methods, systems, datasets, techniques
  concepts/         Ideas, mechanisms, metrics, threat models
  sources/          Papers and articles (curated)
  methodology/      Research methods and protocols
  findings/         Individual evidence-backed claims
  thesis/           Working hypotheses and their evolution
  queries/          Open research questions
  comparisons/      Side-by-side analyses
  synthesis/        Cross-cutting summaries
  references/       Mined citation database and reading recommendations
tools/wiki/         Validation, curation, and reference-mining scripts
.codex/             Project-local agents, skills, and language policy
raw/sources/        Local-only primary documents (PDFs, parsed markdown, images)
                   — ignored by Git in this public repository
```

See `schema.md` for naming and frontmatter rules. See `purpose.md` for the
higher-level research framing.

## Source Pipeline

A source has three states:

1. **Raw** — present locally under `raw/sources/<slug>/` with parsed markdown,
   original PDF, and extracted images, but not yet reviewed or linked into the
   graph.
2. **Curated** — has a corresponding `wiki/sources/<author-year-slug>.md` with
   frontmatter, summary, method notes, limitations, and outbound wikilinks to
   the entities / concepts / findings it introduces.
3. **Synthesized** — its evidence has been cross-linked from at least one
   finding, comparison, synthesis, thesis, or query page.

The local `raw/sources/` directory can grow over time, but it is intentionally
not tracked in Git by default. The public repository records the research map
and curation layer, not copyrighted source PDFs or full paper parses.

## Working With The Wiki

The local LLM Wiki desktop app indexes `wiki/**/*.md` and local
`raw/sources/**`, then serves a JSON API on `http://127.0.0.1:19828`.
Wikilinks (`[[page-slug]]`) are graph edges; frontmatter `related:` lists are
explicit cross-references.

To curate a raw source:

1. Confirm the parsed markdown lives at `raw/sources/<slug>/full.md`.
2. Skim it and decide whether it is in scope for `purpose.md`. If marginal,
   leave it raw and note why in `wiki/log.md`.
3. Write `wiki/sources/<author-year-slug>.md` following `schema.md`.
4. Add or extend `wiki/concepts/`, `wiki/entities/`, and `wiki/findings/` only
   when the corpus justifies them.
5. Update `wiki/index.md`, `wiki/overview.md`, and `wiki/log.md`.
6. Run the validation tools and rescan in LLM Wiki.

## Common Checks

```powershell
python tools/wiki/curation_status.py --dupes
python tools/wiki/corpus_counts.py
python tools/wiki/frontmatter_audit.py
python tools/wiki/index_audit.py
python tools/wiki/linkcheck.py --orphans
python tools/wiki/process_refs.py
python tools/wiki/language_audit.py
```

## Reference Mining

```powershell
python tools/wiki/mine_refs.py --merge wiki/references/reference-database.json
python tools/wiki/verify_refdb.py
python tools/wiki/render_refdb.py --min 2
python tools/wiki/recommend_refs.py --top 30
python tools/wiki/language_audit.py
```

## Language Policy

Agent-facing wiki pages are written primarily in concise English:
`wiki/sources`, `wiki/concepts`, `wiki/entities`, `wiki/findings`,
`wiki/comparisons`, `wiki/synthesis`, `wiki/queries`, `wiki/thesis`, and
`wiki/references`.

Chinese is reserved for human-facing orientation and navigation, such as this
README, `purpose.md`, `wiki/overview.md`, `wiki/index.md`, and `wiki/log.md`.

Official paper titles, method names, datasets, metrics, formulas, code
identifiers, venues, and URLs stay in their canonical English form. Avoid
bilingual duplication: do not write a full Chinese explanation and then repeat
the same content in English.
