---
description: Turn a raw chapter ingest into lecture notes in the author's voice
argument-hint: <chapter number>
---

Write the lecture notes for chapter **$1** from
`instructor/zybooks-raw/ch<NN>.md`.

## Read first

- `.claude/STYLE_GUIDE.md` — the authoring contract. Follow it exactly; new
  pages must be indistinguishable from the existing ones.

## Produce

One file per section at `docs/notes/ch<NN>/<n>.<s>-kebab-case-title.md`, plus
the chapter hub `docs/notes/ch<NN>/index.md`.

Each note needs:

1. No front matter — the file starts at the `# H1`, which supplies the title.
2. The content, in the author's voice: `**term:**` / definition pairs,
   `??? example "🦖 Example"`, `??? question "<a real student question>"`,
   `!!! quote "Zybooks"` for textbook definitions, bare code fences with
   `# Lets …` comments, `(1)` + `{ .annotate }` footnotes, ✅/❌ marks.
3. 2–4 inline `[[basename|display text]]` wikilinks, each target linked once, on
   first mention. Never inside code fences, backticks, headings, or **pipe
   tables** — a `|` in a wikilink breaks the table.

The hub `index.md` gets a sentence or two of intro, and one bullet per section
in order — each a wikilink plus one short clause.

## Rules

- Write **original prose in the author's voice**. The only sanctioned verbatim
  quotation is a short attributed definition inside `!!! quote "Zybooks"`.
- Two trailing spaces at the end of nearly every line. They are load-bearing.
- Err short. No summaries, no learning objectives, no exercises, **no "See also" footer** — just stop.
- LF line endings, UTF-8.

## Then

Register every new page in `nav:` in `mkdocs.yml` — the chapter's bare
`'notes/ch<NN>/index.md'` entry first, then each section.

Finish with `uv run mkdocs build --strict` and fix anything it reports.
