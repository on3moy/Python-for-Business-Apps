"""Verify every slide deck under slides-src/ is linked from docs/slides/index.md.

Usage: uv run python scripts/check_slides_linked.py

Exits 0 when every non-reference deck (files starting with "_" are reference
sheets, e.g. _layouts.md, and are skipped -- same convention as build_slides.py
and check_slide_density.py) has its built HTML filename linked from the slides
index page. Exits 1 with the list of unlinked decks otherwise.
"""

import os
import sys

SLIDES_SRC = "slides-src"
INDEX = "docs/slides/index.md"


def main():
    with open(INDEX, "r", encoding="utf-8") as f:
        index_text = f.read()

    missing = []
    for name in sorted(os.listdir(SLIDES_SRC)):
        if not name.endswith(".md") or name.startswith("_"):
            continue
        deck = name[:-3]
        if f"{deck}.html" not in index_text:
            missing.append(deck)

    if missing:
        print(f"Built deck(s) not linked from {INDEX}:")
        for deck in missing:
            print(f"  - {deck} (expected a link to assets/slides/{deck}.html)")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
