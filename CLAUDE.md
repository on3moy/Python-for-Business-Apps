# IS 640 — Business Application Programming

Course site for CSULB IS 640, published to GitHub Pages via MkDocs Material.
Author: Moy Patel (`on3moy`).

## Content pipeline

```
zyBooks chapter
  -> /ingest-chapter N  -> instructor/zybooks-raw/chNN.md   (raw, gitignored)
  -> /write-notes N     -> docs/notes/chNN/*.md             (published notes)
  -> /make-slides N     -> slides-src/chNN.md -> docs/assets/slides/chNN.html
  -> /make-lab N        -> instructor/problems/chNN/        (gitignored)
```

Slash commands live in `.claude/commands/`.

## Commands

```
uv run mkdocs serve                    # preview site at localhost:8000
uv run mkdocs build                    # build site/
python scripts/build_slides.py         # build all Marp decks -> docs/assets/slides/
python scripts/build_slides.py ch01    # just one deck
```

**Build the slides before building the site.** `docs/assets/slides/` is
gitignored build output; if it is empty, the Slides gallery links 404.

## Never publish

- **`instructor/`** — raw zyBooks captures, lab prompts, solutions. Copyrighted
  course material. Gitignored, lives outside `docs/`, never goes in `nav:`.

## Conventions

- **Style guides are the contract.** `.claude/STYLE_GUIDE.md` for notes,
  `.claude/SLIDE_STYLE_GUIDE.md` for decks. Read the relevant one before writing
  content; new pages should be indistinguishable from existing ones.
- **No YAML front matter.** Pages start at the `# H1`, which supplies the title.
- **Nav is manual.** Every new note page must be registered in `nav:` in
  `mkdocs.yml`. Each chapter's bare `'notes/chNN/index.md'` entry must come
  first in its block — that is what makes it the section landing page.
- **Two trailing spaces are load-bearing** in notes. They are hard line breaks;
  the `**term:**` / definition pairs render wrong without them. `.gitattributes`
  enforces LF so these stay diffable.
- **Code fences differ by medium.** Notes use bare, untagged triple-backtick
  fences (house style). Slides tag the language (`python`, `bash`) — Marp only
  applies the theme's Monokai colors when highlight.js knows the language.
- **Cross-references are plain relative markdown links** —
  `[module basics](2.8-module-basics.md)` in-chapter,
  `[objects](../ch02/2.3-objects.md)` across. `mkdocs build --strict` fails on a
  broken one, so the build is the check.
- **Marp sources live outside `docs/`** (`slides-src/`) so MkDocs never renders
  them as pages. Never edit the built HTML in `docs/assets/slides/`.
- Decks are **linked, never iframed** — Marp owns the viewport and its own
  keyboard handlers.
