# Slide Style Guide — IS 640 Business Application Programming

How lecture decks are written. Companion to `STYLE_GUIDE.md`, which governs the
notes; this file governs `slides-src/*.md`.

Decks are Marp markdown, built to standalone HTML by `scripts/build_slides.py`
and linked from `docs/slides/index.md`. Sources live **outside** `docs/` so
MkDocs never renders them as pages.

---

## 1. Slides are not notes

The notes are the reference; the deck is the performance. A deck slide carries
**one idea**, in as few words as will survive being read from the back of the
room. If a slide needs a paragraph, it is either two slides or it belongs only
in the notes.

Rough budget: a chapter deck runs 25–40 slides. Section breaks are cheap; dense
slides are not.

## 2. Front matter

Every deck starts with exactly this:

```
---
marp: true
theme: charcoal-lb
paginate: true
---
```

Then a title slide:

```
<!-- _class: lead -->
<!-- _paginate: false -->

# Chapter N
## Subtitle in one line

IS 640 — Business Application Programming
```

`_class` and `_paginate` with the leading underscore apply to **that slide
only**. Without the underscore they apply to every slide from there on — a
common and annoying mistake.

## 3. Structure

- `---` on its own line separates slides.
- Every section of the chapter gets a **section break** slide: `<!-- _class: lead -->` plus a single H1 naming the section. These give the deck a rhythm and give you a natural place to pause.
- Section numbering matches the notes (`1.3 Basic input and output`), so a student can find the matching note.
- End on a `<!-- _class: lead -->` closing slide — "Questions?" or similar.

## 4. Voice

Same voice as the notes: second person, "Lets"/"Let's", conversational, dry
jokes, business framing. See `STYLE_GUIDE.md` §2 — do not develop a separate,
more formal register for slides.

The difference is **compression**, not tone. Notes explain; slides assert and
you explain out loud.

## 5. Code on slides

- **Tag the fence with the language** — ` ```python ` for Python, ` ```bash `
  for shell commands. The theme's Monokai syntax colors only apply when
  highlight.js knows the language; a bare ` ``` ` renders as flat monochrome
  text.
- **3–8 lines, hard maximum ~10.** Longer than that is unreadable projected.
- `# Lets ...` narration comments carry the teaching, exactly as in the notes.
- One code block per slide. Two is a sign it should be two slides.
- Output goes underneath as `Output: \`13\`` rather than in a second fence — it
  saves vertical space.

The theme renders code in "window chrome" with traffic-light dots and Monokai
syntax highlighting. Nothing else is needed to opt in beyond the language tag.

## 6. Speaker notes

Anything you plan to *say* rather than show goes in an HTML comment:

```
<!--
Ask the room for a business example before advancing. Payroll works well.
-->
```

These appear in presenter view (press <kbd>P</kbd>) and nowhere else. Use them
for demo cues, questions to ask, and timing notes — that is what makes a deck
re-presentable next semester.

## 7. Layout patterns

`slides-src/_layouts.md` is the reference sheet — copy from it. It is not built
(the `_` prefix tells `build_slides.py` to skip it).

Available:

| Pattern | Use |
|-|-|
| `<!-- _class: lead -->` | Title and section-break slides |
| `<div class="columns">` | Two columns — right/wrong pairs, before/after |
| `![w:800](assets/x.png)` | Image sizing; `w:` and `h:` in px |

Deck images live in `slides-src/assets/`, which the build script copies next to
the built HTML.

## 8. Theme

`slides-src/themes/` splits into four files:

- `lb-tokens.css` — **edit this one** for colors, sizes, the logo. Nothing here depends on layout.
- `lb-base.css` — headings, text, lists, links, blockquotes, tables
- `lb-components.css` — code window chrome, callouts, logo watermark, columns
- `charcoal-lb.css` — the entry point that imports the other three plus `uncover`

Marp resolves `@import "name"` against the theme set directory, so each partial
carries its own `/* @theme name */` header and must stay in that folder.

Two Marp-specific gotchas are already handled in `charcoal-lb.css` and
`lb-components.css`, and the comments there explain why — do not "clean them
up":

- `/* @auto-scaling headings */` stops Marp wrapping code blocks in a
  shrink-to-fit shadow-DOM element that centers them.
- Inline code is styled via `:not(:is(pre, marp-pre)) > code`, because a plain
  `code` selector loses to Marp's own rule.

## 9. Building

```
python scripts/build_slides.py              # every deck -> HTML
python scripts/build_slides.py ch01         # just one
python scripts/build_slides.py --pdf        # also PDF
```

Output lands in `docs/assets/slides/`, which is **gitignored and regenerated**
— never edit the HTML. Run the build before `mkdocs build`, or the Slides
gallery links will 404 under `--strict`.

## 10. Presenting

Decks are linked, never iframed — Marp owns the full viewport and its own
keyboard handlers, and an iframe breaks fullscreen and arrow keys.

<kbd>F</kbd> fullscreen · <kbd>P</kbd> presenter view · arrows to navigate.

---

## Checklist for a new deck

1. `slides-src/chNN.md` with the standard front matter.
2. Title slide with `_class: lead` and `_paginate: false`.
3. A section-break slide per chapter section, numbered to match the notes.
4. One idea per content slide; 3–8 line bare code fences with `# Lets …` comments.
5. Speaker notes in HTML comments for anything you will say, not show.
6. Closing `_class: lead` slide.
7. `python scripts/build_slides.py chNN`.
8. Add the deck to `docs/slides/index.md` with `{ target="_blank" }`.
