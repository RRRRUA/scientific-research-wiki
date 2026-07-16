# Wiki maintenance toolkit

Reusable, version-controlled scripts shared by the research-wiki agents:
`research-wiki-curator`, `research-wiki-auditor`, `research-wiki-synthesizer`,
and `research-reference-scout`.

## Rule

- Reusable logic lives here, tracked in git.
- `.curation-out/` is gitignored scratch for reports and transient state only.
- Run scripts from the repo root. They import `wikilib`, which discovers the repo root.

## Scripts

| Script | Purpose | Common flags |
|---|---|---|
| `wikilib.py` | Shared library: repo paths, markdown enumeration, wikilink parsing, raw/sources reference parsing, title normalization, folder-to-curated-slug map, and venue classifier. | - |
| `linkcheck.py` | Wikilink integrity; exits 1 on dangling links. | `--orphans`, `--json` |
| `curation_status.py` | Reconcile `raw/sources/` against curated pages and detect duplicate MinerU ingests. | `--dupes`, `--near-ratio`, `--json` |
| `make_batches.py` | Split genuinely new papers or explicit lists into batches. | `--size`, `--input`, `--json` |
| `corpus_counts.py` | Exact page counts per wiki type plus raw/sources count and log size. | `--json` |
| `process_refs.py` | Find process narration that leaked into pages other than `wiki/log.md`. | `--json` |
| `language_audit.py` | Block wrong-language wiki pages; agent-facing prose must be English, while exact filenames in frontmatter/code literals and Chinese navigation pages remain allowed. | `--json` |
| `index_audit.py` | Reconcile wiki page inventory against `wiki/index.md`. | `--ignore`, `--json` |
| `frontmatter_audit.py` | Lint frontmatter structure, required keys, type-directory consistency, H1, and self-references. | `--type`, `--show-soft`, `--ignore`, `--json` |
| `entity_roster_audit.py` | Advisory cross-check for author/tool entity rosters against source pages. | `--input`, `--json` |
| `mine_refs.py` | Mine `# References` blocks into `wiki/references/reference-database.json`. | `--json`, `--merge` |
| `verify_refdb.py` | Integrity gate for mined reference DB. | `--db`, `--min-year`, `--max-year`, `--flag-year`, `--json` |
| `render_refdb.py` | Render `wiki/references/reference-database.md` from JSON. | `--db`, `--out`, `--min` |
| `recommend_refs.py` | Rank not-yet-curated references for diffusion watermarking / model fingerprinting research. | `--top`, `--db`, `--out`, `--json` |
| `git_snapshot.ps1` | Validate the wiki, create a timestamped git commit, and push to the configured remote. | `-Message`, `-NoPush`, `-Remote`, `-Branch`, `-SkipChecks` |

## Typical flows

```powershell
python tools/wiki/curation_status.py --dupes --json status.json
python tools/wiki/corpus_counts.py
python tools/wiki/index_audit.py
python tools/wiki/frontmatter_audit.py
python tools/wiki/linkcheck.py --orphans
python tools/wiki/process_refs.py
python tools/wiki/language_audit.py
```

```powershell
python tools/wiki/mine_refs.py --merge wiki/references/reference-database.json
python tools/wiki/verify_refdb.py
python tools/wiki/render_refdb.py --min 2
python tools/wiki/recommend_refs.py --top 30
python tools/wiki/language_audit.py
```

```powershell
powershell -ExecutionPolicy Bypass -File tools/wiki/git_snapshot.ps1
powershell -ExecutionPolicy Bypass -File tools/wiki/git_snapshot.ps1 -Message "curate new paper"
powershell -ExecutionPolicy Bypass -File tools/wiki/git_snapshot.ps1 -NoPush
```
