#!/usr/bin/env python3
"""Rank not-yet-curated references for this research wiki."""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import sys

import wikilib

_IN_SCOPE = re.compile(
    r"diffusion|latent diffusion|stable diffusion|text-to-image|image generation|"
    r"watermark|watermarking|fingerprint|fingerprinting|signature|provenance|"
    r"attribution|traceability|accountability|generated image|synthetic image|"
    r"deepfake|content authenticity|forensic|detection|steganograph|robust|"
    r"vae|decoder|unet|weight modulation|model purification|jpeg|crop|compression",
    re.I,
)
_OUT_SCOPE = re.compile(r"edge computing|mec\b|uav|vehicular|satellite|antenna|circuit|sql|database", re.I)

_TRACKS = [
    (r"latent diffusion|stable diffusion|ldm|text-to-image|diffusion", "Latent diffusion watermarking"),
    (r"fingerprint|fingerprinting|user attribution|traceability|accountability", "Model fingerprinting and user attribution"),
    (r"watermark|signature|steganograph|hidden message", "Image watermarking and signatures"),
    (r"robust|attack|purification|compression|jpeg|crop|post-process|removal", "Robustness and attacks"),
    (r"forensic|detection|deepfake|synthetic image|generated image|authenticity", "Synthetic image detection and provenance"),
    (r"survey|tutorial|overview", "Surveys and foundations"),
]


def infer_scope(rec):
    s = rec.get("scope")
    if s in ("in", "out", "uncertain"):
        return s
    text = (rec.get("title") or "") + " " + (rec.get("venue") or "")
    if _OUT_SCOPE.search(text) and not _IN_SCOPE.search(text):
        return "out"
    if _IN_SCOPE.search(text):
        return "in"
    return "uncertain"


def candidate_track(rec):
    t = rec.get("title") or ""
    for pat, label in _TRACKS:
        if re.search(pat, t, re.I):
            return label
    return "Adjacent methods"


def _tier_rank(tier):
    return {"Q1": 3, "top-conf": 3, "conf": 1}.get(tier, 0)


def score(rec):
    y = rec.get("year")
    recency = 3 if (y or "").isdigit() and int(y) >= 2025 else (2 if (y or "").isdigit() and int(y) >= 2023 else 0)
    scope = 2 if infer_scope(rec) == "in" else (0 if infer_scope(rec) == "out" else 1)
    return recency * 100 + _tier_rank(rec.get("venue_tier")) * 20 + min(rec.get("cited_count", 0), 12) * 5 + scope * 20


def first_author(authors):
    if not authors:
        return "n/a"
    parts = re.split(r",| and ", authors)
    a = parts[0].strip()
    if len(parts) > 1 or "et al" in authors.lower():
        a = re.sub(r"\bet al\.?", "", a).strip() + " et al."
    return a


def parse_uncurated_header(folder):
    fp = os.path.join(wikilib.raw_sources_dir(), folder, "full.md")
    info = {"folder": folder, "title": None, "authors": None, "year": None, "venue": None}
    if not os.path.exists(fp):
        return info
    head = wikilib.read_text(fp)[:2000]
    m = re.search(r"(?m)^#\s+(.+)$", head)
    if m:
        info["title"] = m.group(1).strip()
        for ln in head[m.end():].strip().splitlines():
            ln = ln.strip()
            if ln and "abstract" not in ln.lower():
                info["authors"] = re.sub(r"\s+", " ", ln).split("Abstract")[0].strip()
                break
    ys = re.findall(r"\b(20[0-3][0-9])\b", head)
    if ys:
        info["year"] = max(ys)
    return info


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--top", type=int, default=30)
    ap.add_argument("--json", metavar="PATH")
    args = ap.parse_args(argv)

    refs_dir = os.path.join(wikilib.wiki_dir(), "references")
    db_path = args.db or os.path.join(refs_dir, "reference-database.json")
    out_path = args.out or os.path.join(refs_dir, "recommendations.md")
    if not os.path.exists(db_path):
        print(f"Missing DB: {db_path}. Run mine_refs.py first.")
        return 1

    db = json.load(open(db_path, encoding="utf-8"))
    cur_keys = wikilib.curated_title_keys()
    cands = []
    for r in db.get("records", []):
        if r.get("curated_as") or not r.get("title"):
            continue
        if wikilib.title_match_key(r["title"]) in cur_keys:
            continue
        if infer_scope(r) == "out":
            continue
        cands.append({"rec": r, "track": candidate_track(r), "scope": infer_scope(r), "score": score(r)})
    cands.sort(key=lambda c: (-c["score"], -c["rec"].get("cited_count", 0)))

    slug_map = wikilib.folder_to_slug_map()
    ready = []
    for folder in sorted(set(wikilib.raw_folders()) - set(slug_map)):
        info = parse_uncurated_header(folder)
        info["track"] = candidate_track(info)
        info["scope"] = infer_scope(info)
        ready.append(info)

    today = datetime.date.today().isoformat()
    os.makedirs(refs_dir, exist_ok=True)
    lines = [
        "---",
        "type: recommendations",
        'title: "Reference Recommendations"',
        "tags: [research-wiki, references, recommendations]",
        "related: []",
        f"created: {today}",
        f"updated: {today}",
        "---",
        "",
        "# Reference Recommendations",
        "",
        f"_Generated: {today}_",
        "",
        "Scoring combines recency, venue tier, in-corpus citation frequency, and topic fit for diffusion watermarking / model fingerprinting research.",
        "",
    ]
    if ready:
        lines += ["## Ready to curate now", "", "| Year | Title | Authors | Candidate track | in raw/? |", "|---|---|---|---|---|"]
        for r in ready:
            lines.append(f"| {r.get('year') or 'n/a'} | {r.get('title') or r['folder']} | {first_author(r.get('authors'))} | {r.get('track') or 'n/a'} | yes |")
        lines.append("")
    lines += ["## Top recommendations", "", "| Year | Venue | Title | Authors | cited_count | Candidate track | in raw/? |", "|---|---|---|---|---:|---|---|"]
    for c in cands[: args.top]:
        r = c["rec"]
        venue = r.get("venue_normalized") or r.get("venue") or "n/a"
        lines.append(f"| {r.get('year') or 'n/a'} | {venue} | {r.get('title') or 'n/a'} | {first_author(r.get('authors'))} | {r.get('cited_count', 0)} | {c['track']} | no |")
    lines += ["", "## Notes", "", f"- Candidate records considered: {len(cands)}.", f"- Parsed but uncurated raw folders: {len(ready)}."]
    open(out_path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"recommendations -> {out_path}")

    if args.json:
        out = args.json if os.path.isabs(args.json) else os.path.join(wikilib.scratch_dir(), args.json)
        json.dump({"ready": ready, "candidates": cands[: args.top]}, open(out, "w", encoding="utf-8"), indent=2)
        print(f"report -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
