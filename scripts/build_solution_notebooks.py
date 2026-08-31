"""Build and execute instructor solution notebooks from instructor/solutions/*.md.

Usage:
    uv run python scripts/build_solution_notebooks.py            # every instructor/solutions/ch*.md
    uv run python scripts/build_solution_notebooks.py ch1 ch3     # just these chapters

Same Jupytext plain-Markdown source format as scripts/build_notebooks.py, but
these sources have every practice notebook's `# TODO` cell filled in with real
code. Unlike the student-facing build, this one runs with --execute: Jupytext
actually runs the notebook against a python3 kernel and saves real cell
outputs into the .ipynb (so an instructor can see expected output without
re-running it themselves) and, critically, exits non-zero if any cell raises
-- that's the real correctness check for a solutions notebook, not a static
read-through.

instructor/ is gitignored (see project CLAUDE.md, "Never publish") and never
referenced from docs/ or mkdocs.yml, so anything built here is never part of
the published site.
"""

import subprocess
import sys
from pathlib import Path

SRC_DIR = Path("instructor/solutions")
OUT_DIR = Path("instructor/solutions")


def build_one(name):
    src = SRC_DIR / f"{name}.md"
    if not src.exists():
        print(f"error: {src} does not exist", file=sys.stderr)
        return False

    out = OUT_DIR / f"{name}.ipynb"
    result = subprocess.run(
        [
            "jupytext",
            "--to", "notebook",
            "--set-kernel", "python3",
            "--execute",
            str(src),
            "-o", str(out),
        ]
    )
    return result.returncode == 0


def main(argv):
    if argv:
        names = argv
    else:
        names = sorted(p.stem for p in SRC_DIR.glob("ch*.md"))

    if not names:
        print("no instructor/solutions/ch*.md files found", file=sys.stderr)
        return 1

    ok = True
    for name in names:
        if not build_one(name):
            ok = False

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
