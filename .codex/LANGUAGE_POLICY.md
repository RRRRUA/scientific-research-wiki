# Language Policy

This project uses automatic Chinese/English writing only:

- Default explanatory prose: Simplified Chinese.
- Paper titles, method names, datasets, metrics, code identifiers, venues, and formulas: keep official English.
- First mention of important terms: use Chinese plus the official English term when helpful, for example: 用户归因（user attribution）.
- Do not generate Greek, Dutch, Indonesian, or any other non-Chinese/non-English prose.
- If an upstream LLM Wiki auto-page is generated in the wrong language, archive it under archive/language-review/ and rebuild the wiki page in Chinese/English.
- Run `python tools/wiki/language_audit.py` after wiki edits; it is a required gate for curator, synthesizer, and auditor workflows.
