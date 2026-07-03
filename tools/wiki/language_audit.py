from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


BLOCKED_SCRIPTS = {
    "Greek": re.compile(r"[\u0370-\u03FF\u1F00-\u1FFF]"),
    "Cyrillic": re.compile(r"[\u0400-\u04FF]"),
    "Arabic": re.compile(r"[\u0600-\u06FF]"),
    "Hebrew": re.compile(r"[\u0590-\u05FF]"),
    "Thai": re.compile(r"[\u0E00-\u0E7F]"),
    "Devanagari": re.compile(r"[\u0900-\u097F]"),
}


def audit(root: Path) -> list[tuple[Path, str, int]]:
    rows: list[tuple[Path, str, int]] = []
    for path in sorted((root / "wiki").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for name, pattern in BLOCKED_SCRIPTS.items():
            count = len(pattern.findall(text))
            if count:
                rows.append((path.relative_to(root), name, count))
    return rows


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

    parser = argparse.ArgumentParser(
        description="Audit wiki pages for scripts outside the Chinese/English language policy."
    )
    parser.add_argument("--root", default=".", help="Project root. Defaults to current directory.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    rows = audit(root)
    if args.json:
        print(
            json.dumps(
                {
                    "ok": not rows,
                    "violations": [
                        {"path": rel.as_posix(), "script": script, "count": count}
                        for rel, script, count in rows
                    ],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0 if not rows else 1

    if not rows:
        print("LANGUAGE AUDIT: CLEAN")
        return 0

    print("LANGUAGE AUDIT: BLOCKED SCRIPT FOUND")
    for rel, script, count in rows:
        print(f"{rel}\t{script}\t{count}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
