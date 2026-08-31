"""Verify every notebook-src/ch<N>.md has a nav entry in mkdocs.yml.

Usage: uv run python scripts/check_notebooks_linked.py

mkdocs build --strict already fails if a nav entry points at a file that
doesn't exist, but it does NOT fail if a built notebook exists with no nav
entry at all -- exactly the gap that let the chapter 3/4 slide decks ship
without a link on the Slides page. This is the notebook equivalent of
check_slides_linked.py.

Exits 0 when every notebook-src/ch<N>.md's built docs/notebooks/ch<N>.ipynb
is referenced somewhere in mkdocs.yml. Exits 1 with the list of unlinked
chapters otherwise.
"""

import sys
from pathlib import Path

SRC_DIR = Path("notebook-src")
NAV_FILE = Path("mkdocs.yml")


def main():
    nav_text = NAV_FILE.read_text(encoding="utf-8")

    missing = []
    for src in sorted(SRC_DIR.glob("ch*.md")):
        name = src.stem
        needle = f"notebooks/{name}.ipynb"
        if needle not in nav_text:
            missing.append(name)

    if missing:
        print("Notebook(s) built but not registered in mkdocs.yml nav:")
        for name in missing:
            print(f"  - {name} (expected a 'notebooks/{name}.ipynb' entry under Notebooks:)")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
