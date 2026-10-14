"""Render a Marp deck to one PNG per slide, so you can look for cut-off content.

The PNGs are scratch output for visual review, not build output. They go in
.slide-renders/<deck>/ (gitignored) and should be deleted once the review is
done -- `--clean` does that, and the Sonnet-Fit-Slides SubagentStop hook
blocks until the folder is gone.

Usage:
    python scripts/render_slides.py ch13            # -> .slide-renders/ch13/ch13.001.png ...
    python scripts/render_slides.py ch13 --slide 9  # print the path of slide 9 only
    python scripts/render_slides.py ch13 --clean    # delete .slide-renders/ch13/
    python scripts/render_slides.py --clean         # delete all of .slide-renders/

Several decks can be checked in parallel: each renders into its own folder, and
`<deck> --clean` only removes that deck's folder (plus .slide-renders/ itself
once it is empty).

Rendering needs a Chromium-family browser. marp-cli only auto-detects Chrome,
Edge and Firefox, so this script also looks for Brave and Chromium and passes
the one it finds through CHROME_PATH (an existing CHROME_PATH wins).
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "slides-src"
THEMES = SRC / "themes"
RENDERS = ROOT / ".slide-renders"

MARP = ["npx", "--yes", "@marp-team/marp-cli@latest"]
BROWSERS = ["google-chrome-stable", "google-chrome", "chromium", "chromium-browser",
            "brave", "brave-browser"]


def find_browser() -> str | None:
    if os.environ.get("CHROME_PATH"):
        return os.environ["CHROME_PATH"]
    for name in BROWSERS:
        path = shutil.which(name)
        if path:
            return path
    return None


def render(deck: str) -> Path:
    src = SRC / f"{deck}.md"
    if not src.exists():
        sys.exit(f"No such deck: {src.relative_to(ROOT)}")

    out_dir = RENDERS / deck
    # Start clean so stale PNGs from a longer earlier version never linger
    shutil.rmtree(out_dir, ignore_errors=True)
    out_dir.mkdir(parents=True)

    env = dict(os.environ)
    browser = find_browser()
    if browser:
        env["CHROME_PATH"] = browser

    # --no-stdin: same reason as build_slides.py, marp-cli otherwise waits on stdin
    cmd = [*MARP, str(src), "--theme-set", str(THEMES), "--allow-local-files",
           "--no-stdin", "--images", "png", "-o", str(out_dir / f"{deck}.png")]
    result = subprocess.run(cmd, cwd=ROOT, env=env, capture_output=True, text=True,
                            shell=(sys.platform == "win32"))
    if result.returncode != 0:
        print(result.stderr[-2000:], file=sys.stderr)
        sys.exit(f"Render failed for {deck} (browser: {browser or 'none found'})")
    return out_dir


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("deck", nargs="?", help="deck name, e.g. ch13")
    ap.add_argument("--slide", type=int, help="only print this slide's PNG path")
    ap.add_argument("--clean", action="store_true",
                    help="delete this deck's renders (or all renders with no deck) and exit")
    args = ap.parse_args()

    if args.clean:
        target = RENDERS / args.deck if args.deck else RENDERS
        shutil.rmtree(target, ignore_errors=True)
        # Drop the parent too once the last deck's folder is gone
        if RENDERS.is_dir() and not any(RENDERS.iterdir()):
            RENDERS.rmdir()
        print(f"Removed {target.relative_to(ROOT)}/")
        return 0
    if not args.deck:
        ap.error("give a deck name, or --clean")

    out_dir = render(args.deck)
    pngs = sorted(out_dir.glob("*.png"))
    if args.slide:
        pngs = [p for p in pngs if p.stem.endswith(f".{args.slide:03d}")]
    for p in pngs:
        print(p.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
