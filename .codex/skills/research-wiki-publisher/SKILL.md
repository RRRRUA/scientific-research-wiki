---
name: research-wiki-publisher
description: Validate, commit, and push this research wiki to GitHub with timestamped git snapshots. Use when the user asks to upload, publish, sync, push, or make an automatic git record for the wiki.
---

# Research Wiki Publisher

Use this skill for `D:\WikiProject\scientific research` when publishing wiki changes to GitHub.

## Default Command

Run from the repo root:

```powershell
powershell -ExecutionPolicy Bypass -File tools/wiki/git_snapshot.ps1
```

With a custom commit subject:

```powershell
powershell -ExecutionPolicy Bypass -File tools/wiki/git_snapshot.ps1 -Message "curate HFRW paper"
```

Commit locally without pushing:

```powershell
powershell -ExecutionPolicy Bypass -File tools/wiki/git_snapshot.ps1 -Message "draft wiki update" -NoPush
```

## What The Script Does

1. Sets UTF-8 output and Python IO encoding.
2. Resolves Python from `WIKI_PYTHON`, the bundled Codex runtime, or `python`.
3. Runs validation:
   - `curation_status.py --dupes`
   - `corpus_counts.py`
   - `frontmatter_audit.py`
   - `index_audit.py`
   - `linkcheck.py --orphans`
   - `process_refs.py`
   - `language_audit.py`
   - `verify_refdb.py` when `wiki/references/reference-database.json` exists
4. Stops before committing if any validation fails.
5. Runs `git add -A`; ignored folders such as `raw/`, `wiki/media/`, `.obsidian/`, and `archive/` stay local.
6. Creates a timestamped commit message with:
   - snapshot time
   - repo, branch, and remote
   - validation list
   - staged file summary
7. Pushes to the current upstream, or sets upstream with `git push -u origin <branch>`.

## Guardrails

- Do not manually `git add` raw paper folders for a public repository.
- Do not use force push unless the user explicitly approves it and the remote state has been checked.
- If validation fails, fix the wiki first; do not bypass checks unless the user explicitly asks for `-SkipChecks`.
- If push is rejected because remote has new work, inspect or fetch remote state before deciding whether to merge, rebase, or ask the user.
