# Notebook Style Guide — IS 640 Business Application Programming

How chapter practice notebooks are written. Companion to `STYLE_GUIDE.md` (notes)
and `SLIDE_STYLE_GUIDE.md` (decks); this file governs `notebook-src/*.md`.

A practice notebook is a **fill-in-the-blank worksheet**, not a copy of the
chapter. A student downloads it, opens it in Jupyter or VS Code, and works
through it cell by cell — reading the setup, running what's given, and writing
the missing line(s) themselves. It follows the chapter in order and never
introduces anything the notes/slides for that chapter didn't already cover.

## 1. Source format

Sources live in `notebook-src/ch<N>.md` (chapter number **not** zero-padded —
matches the existing `docs/notebooks/ch1.ipynb` naming, unlike `slides-src`
and `docs/notes`, which do pad). Built with
[Jupytext](https://jupytext.readthedocs.io/)'s plain Markdown format:

- Everything **outside** a ` ```python ` fence becomes a markdown cell.
- Every ` ```python ` fenced block becomes its own code cell.
- `---` is not a cell separator here (unlike Marp decks) — cell boundaries
  come purely from where the code fences start and end.

## 2. Structure

- Start with one markdown cell: `# Chapter N: <title>` plus a one-line "what
  you'll practice" sentence.
- One markdown + code cell pair per concept, in the same order the notes cover
  them, with a markdown sub-heading matching the note section number (`## 2.4
  Numeric types`) so a stuck student can find the matching note immediately.
- Close with a short markdown cell — "Nice work" or similar, no new content.
- **No links to the notes pages, or anywhere else in the site.** A relative
  markdown link like `[2.4 Numeric types](../notes/ch02/2.4-numeric-types.md)`
  only resolves inside a full mkdocs build; it's dead weight the moment a
  student downloads the notebook (which is the whole point of the "Download
  Notebook" button) and opens it standalone in Jupyter or VS Code — there is
  no `docs/` tree next to it for the relative path to resolve against. The
  matching section number in the heading (`## 2.4 Numeric types`) already
  does the "find the note" job without a link that only half-works.

## 3. Fill-in-the-blank code cells

- Give the student everything **except** the one thing being practiced: any
  needed setup (`import` lines, starting variables) is provided and runs as-is.
- Mark what's missing with a `# TODO: <specific instruction>` comment — precise
  enough that the student knows exactly what line(s) to write, not a vague
  "try it yourself."
- **Never include the answer**, in the cell or in a nearby comment. If the
  concept needs an example to anchor it, put the example in the *markdown*
  cell above (referencing the chapter's own worked example) and leave the code
  cell itself blank apart from setup + the `TODO`.
- One concept per code cell — same "one idea" discipline as the slide deck.
  Don't stack two unrelated fill-ins in one cell.
- A cell should run without raising an error even before the student fills in
  the `TODO` (e.g. end on the comment, not on a line that references a
  not-yet-defined name) wherever that's practical — a student should be able
  to "Run All" top to bottom and only get stuck exactly where they're supposed
  to write something, not on an unrelated blank cell above it.

## 4. Voice

Markdown cells use the same second-person, direct voice as the notes
(`STYLE_GUIDE.md` §2) — this is self-study material without a presenter in the
room, so it can be a little more explicit than a slide, but stays terse. It's
a worksheet, not a re-explanation of the whole note.

## 5. Building

```
uv run python scripts/build_notebooks.py ch<N>     # one chapter
uv run python scripts/build_notebooks.py            # every notebook-src/*.md
```

This runs Jupytext (`--to notebook --set-kernel python3`) and writes
`docs/notebooks/ch<N>.ipynb`, **overwriting** whatever was there. Output is a
real notebook — not a build artifact excluded from git, unlike the Marp decks
under `docs/assets/slides/` — so it's committed like any other doc page.

## 6. Downloads and nav

Students get a real, downloadable `.ipynb` for free — `mkdocs.yml` sets
`mkdocs-jupyter`'s `include_source: true`, and `overrides/main.html` adds a
"Download Notebook" button to every notebook page automatically. Nothing
notebook-specific needs to be added per chapter for this to work.

What **does** need a manual step: the chapter must be registered under
`Notebooks:` in `mkdocs.yml`'s `nav`, e.g.:

```yaml
- Notebooks:
    - Chapter N Notebook: 'notebooks/chN.ipynb'
```

`scripts/check_notebooks_linked.py` verifies every `notebook-src/ch<N>.md`
has a matching nav entry and blocks the `Sonnet-Make-Notebook` agent's
`SubagentStop` hook if one is missing — the same lesson learned from the
slide decks that shipped without a Slides-page link.

## 7. Instructor solutions

`Sonnet-Solve-Notebook` (a separate agent from `Sonnet-Make-Notebook`, invoked by the
`solve-notebook` skill) mirrors a chapter's practice notebook into an instructor-only solved
version — never published, never on the web.

- Source: `instructor/solutions/ch<N>.md`, same Jupytext plain-Markdown format, same cell
  structure as `notebook-src/ch<N>.md` — a straight duplicate except every `# TODO: ...` cell gets
  the comment kept **and** real working code added beneath it, so the task and its answer stay
  visibly paired for an instructor skimming it. Markdown cells and setup code are untouched.
- Built with `uv run python scripts/build_solution_notebooks.py ch<N>`, which runs Jupytext with
  `--execute` — it actually executes the notebook against a python3 kernel and saves the real
  outputs, and fails loudly (non-zero exit, full traceback) if any cell raises. That's the real
  correctness check for a solution: it has to run, not just read plausibly.
- **Hidden from the web structurally, not by convention.** `instructor/` is already gitignored and
  never referenced from `docs/` or `mkdocs.yml` (see the project's root `CLAUDE.md`, "Never
  publish") — solutions living there means there's no separate "don't index this" step to
  remember or get wrong.

## Checklist for a new chapter notebook

1. `notebook-src/ch<N>.md`, one markdown+code pair per concept, in chapter order.
2. Every code cell either runs clean as-is or ends cleanly at its `TODO`.
3. No answers given away.
4. `uv run python scripts/build_notebooks.py ch<N>`.
5. Nav entry under `Notebooks:` in `mkdocs.yml` (skip if one already exists).
6. `uv run mkdocs build --strict`.
