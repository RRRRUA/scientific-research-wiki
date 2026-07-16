# Language Policy

This project uses an English-first writing policy for agent-facing knowledge:

- Agent-facing wiki pages (`wiki/sources`, `wiki/concepts`, `wiki/entities`, `wiki/findings`, `wiki/comparisons`, `wiki/synthesis`, `wiki/queries`, `wiki/thesis`, and `wiki/references`) default to concise English prose.
- Chinese is reserved for human-facing orientation and navigation such as `README.md`, `purpose.md`, `wiki/overview.md`, `wiki/index.md`, and `wiki/log.md`.
- Keep official paper titles, method names, datasets, metrics, code identifiers, venues, formulas, and URLs in their canonical English form; do not translate official names.
- Preserve exact source filenames as metadata or code literals even when an imported filename contains Chinese characters such as `等`; this exception does not permit Chinese explanatory prose in agent-facing pages.
- Avoid bilingual duplication. Do not write a full Chinese explanation and then repeat the same content in English.
- Do not generate Greek, Dutch, Indonesian, or any other non-English/non-Chinese prose.
- If an upstream LLM Wiki auto-page is generated in the wrong language, archive it under archive/language-review/ and rebuild agent-facing pages in English.
- Run `python tools/wiki/language_audit.py` after wiki edits; it is a required gate for curator, synthesizer, and auditor workflows.
