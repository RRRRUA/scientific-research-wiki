---
name: research-wiki
description: Maintain an LLM Wiki research knowledge base for scientific papers. Use when curating raw papers, auditing wiki consistency, synthesizing findings/comparisons, mining references, or working in this project wiki.
---

# Research Wiki

## Quick Start

Use this skill for `D:\WikiProject\scientific research` and similar LLM Wiki paper repositories.

Core layout:

- `raw/sources/<slug>/full.md`: MinerU parse and original artifacts.
- `wiki/sources/`: one grounded page per curated paper.
- `wiki/concepts/`, `wiki/entities/`, `wiki/findings/`, `wiki/comparisons/`, `wiki/synthesis/`, `wiki/queries/`, `wiki/methodology/`, `wiki/thesis/`: derived graph layer.
- `tools/wiki/`: reusable validation and reference-mining CLIs.

Windows note: run wiki scripts with UTF-8 output, for example set `$env:PYTHONIOENCODING='utf-8'` before Python commands when raw folder names contain Chinese or symbols.

## Workflows

### Curate a new paper

1. Read `purpose.md`, `schema.md`, and `tools/wiki/README.md`.
2. Run `python tools/wiki/curation_status.py --dupes`.
3. Read the target `raw/sources/<slug>/full.md`.
4. Write `wiki/sources/<author-year-shortslug>.md`; never invent missing metadata.
5. Update index, overview, and log.
6. Run link, frontmatter, index, process-narration, and language checks.

### Audit the wiki

Run:

```powershell
python tools/wiki/curation_status.py --dupes
python tools/wiki/corpus_counts.py
python tools/wiki/index_audit.py
python tools/wiki/frontmatter_audit.py
python tools/wiki/linkcheck.py --orphans
python tools/wiki/process_refs.py
python tools/wiki/language_audit.py
```

### Mine references

Run:

```powershell
python tools/wiki/mine_refs.py --merge wiki/references/reference-database.json
python tools/wiki/verify_refdb.py
python tools/wiki/render_refdb.py --min 2
python tools/wiki/recommend_refs.py --top 30
python tools/wiki/language_audit.py
```

### Publish a git snapshot

Use the `research-wiki-publisher` skill, which wraps:

```powershell
powershell -ExecutionPolicy Bypass -File tools/wiki/git_snapshot.ps1
```

## Guardrails

- Ground claims in `raw/sources/<slug>/full.md`.
- Do not invent DOI, venue, year, result values, or citations.
- Reuse existing slugs and tag vocabulary before creating new pages.
- Keep all wiki pages except `wiki/log.md` evergreen.
- Treat LLM Wiki API results as an index aid; files and parses are the source of truth.
- Run `tools/wiki/language_audit.py` after edits; archive wrong-language auto pages under `archive/language-review/` before rebuilding canonical pages.

## Language Policy

- Agent-facing wiki pages default to concise English: `sources`, `concepts`, `entities`, `findings`, `comparisons`, `synthesis`, `queries`, `thesis`, and `references`.
- Chinese is reserved for human-facing orientation and navigation pages such as `README.md`, `purpose.md`, `wiki/overview.md`, `wiki/index.md`, and `wiki/log.md`.
- Preserve official English paper titles, method names, datasets, metrics, formulas, code identifiers, venues, and URLs; do not translate official names.
- Avoid bilingual duplication. Do not write a full Chinese explanation and then repeat the same content in English.
- Do not write Greek, Dutch, Indonesian, or other non-English/non-Chinese prose.
- If a wrong-language auto page exists, archive it under archive/language-review/ before rebuilding agent-facing pages in English.
