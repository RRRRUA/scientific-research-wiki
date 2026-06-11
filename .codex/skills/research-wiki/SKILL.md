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

## Guardrails

- Ground claims in `raw/sources/<slug>/full.md`.
- Do not invent DOI, venue, year, result values, or citations.
- Reuse existing slugs and tag vocabulary before creating new pages.
- Keep all wiki pages except `wiki/log.md` evergreen.
- Treat LLM Wiki API results as an index aid; files and parses are the source of truth.
- Run `tools/wiki/language_audit.py` after edits; archive wrong-language auto pages under `archive/language-review/` before rebuilding canonical pages.

## Language Policy

- Default output language for wiki pages is Simplified Chinese.
- Preserve official English paper titles, method names, datasets, metrics, formulas, code identifiers, venues, and URLs.
- Use Chinese plus the official English term for important technical terms on first mention, for example: 用户归因（user attribution）.
- Do not write Greek, Dutch, Indonesian, or other non-Chinese/non-English prose.
- If a wrong-language auto page exists, archive it under archive/language-review/ before rebuilding the page in Chinese/English.
