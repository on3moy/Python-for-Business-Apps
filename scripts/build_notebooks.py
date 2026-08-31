"""Build chapter practice notebooks from notebook-src/*.md via Jupytext.

Usage:
    uv run python scripts/build_notebooks.py            # every notebook-src/ch*.md
    uv run python scripts/build_notebooks.py ch1 ch3     # just these chapters

Converts notebook-src/ch<N>.md (Jupytext plain-Markdown format: text outside
```python fences becomes a markdown cell, each fenced block becomes a code
cell) to docs/notebooks/ch<N>.ipynb, overwriting whatever is there, with a
python3 kernelspec set so it opens cleanly in Jupyter/VS Code.

Build through THIS script, not by shelling out to `jupytext`/`jupyter nbconvert`
directly. On at least one Windows/cp1252 environment, an ad-hoc `jupyter
nbconvert --execute --inplace` run after this script (as an extra manual
"double check it runs" step) silently corrupted every non-ASCII character
(em dashes, emoji) in the output into U+FFFD replacement characters, even
though this script's own build was clean. If you need to confirm a notebook
executes without error, prefer `scripts/build_solution_notebooks.py`'s
`--execute` path (already exercised and known clean) over an ad-hoc command.
"""

import subprocess
import sys
from pathlib import Path

SRC_DIR = Path("notebook-src")
OUT_DIR = Path("docs/notebooks")


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
        print("no notebook-src/ch*.md files found", file=sys.stderr)
        return 1

    ok = True
    for name in names:
        if not build_one(name):
            ok = False

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
