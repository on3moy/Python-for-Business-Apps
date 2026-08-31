# IS 640 — Business Application Programming

Course site for IS 640, CSULB. Lecture notes, Marp slide decks, and notebooks,
published with MkDocs Material at
<https://on3moy.github.io/Python-for-Business-Apps/>.

The notes are structured as a linked tree rather than a linear textbook: every
section is its own page, each chapter has an `index.md` hub, and pages
cross-reference each other with plain relative links. Chapters 1–4 are live
(~40 note pages).

## Layout

```
docs/               the MkDocs site
  notes/chNN/       lecture notes, one topic per file, plus an index.md hub
  slides/index.md   deck gallery (links to the built HTML)
  course/           install guide, how-to-use, MkDocs reference
  notebooks/        Jupyter notebooks
  img/              images used by the notes
  stylesheets/      extra.css
  assets/slides/    BUILT decks (gitignored, regenerate with build_slides.py)
slides-src/         Marp deck sources + modular theme (outside docs/ by design)
notebook-src/       notebook sources, built into docs/notebooks/
scripts/            deck + notebook builders, link and density checks
instructor/         gitignored: zyBooks ingests, labs, derived problems
.claude/            the three STYLE_GUIDEs, skills/, agents/
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

`build_slides.py` shells out to `marp-cli` through `npx`, so it needs Node on
the first run. It takes a deck name to build just one (`build_slides.py ch01`)
and `--pdf` / `--pptx` to export those formats alongside the HTML.

## Authoring

`.claude/STYLE_GUIDE.md` is the contract for notes, `.claude/SLIDE_STYLE_GUIDE.md`
for decks, and `.claude/NOTEBOOK_STYLE_GUIDE.md` for notebooks. Read them
before adding a chapter — the site's consistency is the point.

The Claude Code skills in `.claude/skills/` run the chapter pipeline. Each one
dispatches to a matching agent in `.claude/agents/`, and the build and link
checks are enforced by `SubagentStop` hooks rather than by remembering to run
them:

| Skill | Does |
|-|-|
| `/ingest-chapter N` | zyBooks chapter → `instructor/zybooks-raw/` |
| `/write-notes N` | ingest → notes in the author's voice |
| `/make-slides N` | notes → Marp deck, built and linked |
| `/clean-slides N` | split slides that drifted past one idea each |
| `/make-notebook N` | notes → fill-in-the-blank practice notebook |
| `/solve-notebook N` | practice notebook → solved instructor copy |

Rules that are easy to trip over:

- **Every new page must be added to `nav:` in `mkdocs.yml`**, and each chapter's
  bare `'notes/chNN/index.md'` entry must come first in its block — that is what
  makes it the section landing page.
- **Cross-references are relative markdown links** — `[text](2.8-module-basics.md)`
  in-chapter, `[text](../ch02/2.3-objects.md)` across. `mkdocs build --strict`
  fails on a broken one, so the build is the check.
- **Two trailing spaces are load-bearing** in notes — they are hard line breaks,
  and the `**term:**` / definition pairs render wrong without them.
  `.gitattributes` pins LF so they stay diffable.
- **Code fences differ by medium.** Notes use bare, untagged fences; slides tag
  the language, because Marp only colorizes what highlight.js recognizes.
- **Never edit the built HTML in `docs/assets/slides/`** — edit `slides-src/`
  and rebuild. Decks are linked, never iframed; Marp owns its own viewport and
  key handling.
- **`instructor/` never ships.** Raw zyBooks captures, lab prompts, and
  solutions are copyrighted course material: gitignored, outside `docs/`, never
  in `nav:`.

## Site plugins

Deliberately few — each third-party plugin is a maintenance liability.

- `search` — Material's built-in full-text search
- `mkdocs-jupyter` — renders the notebooks
