# IS 640 — Business Application Programming

Course site for IS 640, CSULB. Lecture notes, Marp slide decks, and notebooks,
published with MkDocs Material at
<https://on3moy.github.io/Python-for-Business-Apps/>.

The notes are structured as a linked vault rather than a linear textbook: every
section is its own note, notes wikilink to each other, and a tag index lets
students browse by topic across chapters.

## Layout

```
docs/            the MkDocs site
  notes/chNN/    lecture notes, one topic per file, plus an index.md hub
  slides/        deck gallery page
  course/        install guide, how-to-use, reference
  notebooks/     Jupyter notebooks
  assets/slides/ BUILT decks (gitignored, regenerate with build_slides.py)
slides-src/      Marp deck sources + modular theme (outside docs/ by design)
scripts/         build_slides.py
instructor/      gitignored: zyBooks ingests, labs, derived problems
.claude/         STYLE_GUIDE.md, SLIDE_STYLE_GUIDE.md, agents, skills
```

## Working on it

```bash
uv sync                                 # install
python scripts/build_slides.py          # build the decks first
uv run mkdocs serve                     # then serve the site
uv run mkdocs build --strict            # what CI should run
```

Build the decks before building the site — the Slides gallery links to files
that `build_slides.py` produces, and `--strict` fails if they are missing.

## Authoring

`.claude/STYLE_GUIDE.md` is the contract for notes; `.claude/SLIDE_STYLE_GUIDE.md`
for decks. Read them before adding a chapter — the site's consistency is the
point.

The Claude Code commands in `.claude/commands/` run the chapter pipeline:

| Command | Does |
|-|-|
| `/ingest-chapter N` | zyBooks chapter → `instructor/zybooks-raw/` |
| `/write-notes N` | ingest → notes in the author's voice, with wikilinks |
| `/make-slides N` | notes → Marp deck, built and linked |
| `/make-lab N` | labs → original in-class problems (instructor-only) |

Two rules that are easy to trip over:

- **Every new page must be added to `nav:` in `mkdocs.yml`.**
- **Cross-references are relative markdown links** — `[text](2.8-module-basics.md)`
  in-chapter, `[text](../ch02/2.3-objects.md)` across. `mkdocs build --strict`
  fails on a broken one.

## Site plugins

Deliberately few — each third-party plugin is a maintenance liability.

- `search` — Material's built-in full-text search
- `mkdocs-jupyter` — renders the notebooks
