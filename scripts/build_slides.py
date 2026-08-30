"""Build the Marp decks in slides-src/ into docs/assets/slides/.

Marp sources deliberately live outside docs/ so MkDocs never tries to render
them as ordinary pages. This script compiles each deck to a standalone HTML
file (optionally PDF/PPTX) inside the docs tree, where MkDocs copies it
verbatim and the Slides gallery links to it.

Usage:
    python scripts/build_slides.py              # all decks -> HTML
    python scripts/build_slides.py ch01         # just one deck
    python scripts/build_slides.py --pdf        # also export PDF
    python scripts/build_slides.py --pptx       # also export PPTX

Requires Node (marp-cli is fetched via npx on first run).
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "slides-src"
THEMES = SRC / "themes"
ASSETS = SRC / "assets"
OUT = ROOT / "docs" / "assets" / "slides"

MARP = ["npx", "--yes", "@marp-team/marp-cli@latest"]


def decks(names: list[str]) -> list[Path]:
    """Deck sources to build. Files starting with '_' are shared partials."""
    if names:
        found = []
        for n in names:
            p = SRC / f"{n.removesuffix('.md')}.md"
            if not p.exists():
                sys.exit(f"No such deck: {p.relative_to(ROOT)}")
            found.append(p)
        return found
    return sorted(p for p in SRC.glob("*.md") if not p.name.startswith("_"))


def build(deck: Path, fmt: str) -> bool:
    out = OUT / f"{deck.stem}.{fmt}"
    # --no-stdin matters: run non-interactively, marp-cli otherwise decides it
    # should read the deck from stdin and hangs waiting for input.
    cmd = [*MARP, str(deck), "--theme-set", str(THEMES),
           "--allow-local-files", "--no-stdin"]
    if fmt == "html":
        cmd.append("--html")
    else:
        cmd.append(f"--{fmt}")
    cmd += ["-o", str(out)]

    print(f"  {deck.name} -> {out.relative_to(ROOT)}")
    result = subprocess.run(cmd, cwd=ROOT, shell=(sys.platform == "win32"))
    if result.returncode != 0:
        print(f"  !! failed: {deck.name} ({fmt})", file=sys.stderr)
        return False
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("decks", nargs="*", help="deck names, e.g. ch01 (default: all)")
    ap.add_argument("--pdf", action="store_true", help="also export PDF")
    ap.add_argument("--pptx", action="store_true", help="also export PPTX")
    args = ap.parse_args()

    targets = decks(args.decks)
    if not targets:
        print(f"No decks found in {SRC.relative_to(ROOT)}/")
        return 0

    OUT.mkdir(parents=True, exist_ok=True)

    # The theme inlines url("assets/...") against the built deck, so the asset
    # folder has to sit next to the output HTML.
    if ASSETS.is_dir():
        shutil.copytree(ASSETS, OUT / "assets", dirs_exist_ok=True)

    formats = ["html"] + (["pdf"] if args.pdf else []) + (["pptx"] if args.pptx else [])
    print(f"Building {len(targets)} deck(s) as {', '.join(formats)}:")

    failed = 0
    for deck in targets:
        for fmt in formats:
            if not build(deck, fmt):
                failed += 1

    if failed:
        print(f"\n{failed} build(s) failed.", file=sys.stderr)
        return 1
    print(f"\nDone. Decks are in {OUT.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
