---
description: Build a Marp lecture deck for a chapter from its notes
argument-hint: <chapter number>
---

Write and build the lecture deck for chapter **$1**.

## Read first

- `.claude/SLIDE_STYLE_GUIDE.md` — deck conventions.
- `slides-src/_layouts.md` — copy the slide patterns from here.
- `docs/notes/ch<NN>/` — the notes this deck presents.

## Produce

`slides-src/ch<NN>.md`:

- Standard front matter (`marp: true`, `theme: charcoal-lb`, `paginate: true`).
- Title slide with `_class: lead` and `_paginate: false`.
- A `_class: lead` section-break slide per chapter section, numbered to match
  the notes so students can find the matching page.
- One idea per content slide. Compress the notes — do not paste them.
- Bare code fences, 3–8 lines, `# Lets …` narration comments.
- Speaker notes in `<!-- -->` comments for anything you would say rather than
  show: demo cues, questions to ask the room, timing.
- Closing `_class: lead` slide.

## Then

```
python scripts/build_slides.py ch<NN>
```

Add the deck to `docs/slides/index.md` as a `{ target="_blank" }` link — never
an iframe; Marp needs the full viewport for fullscreen and arrow keys.

Verify with `uv run mkdocs build --strict`, which will fail if the deck link
points at a file the build script did not produce.
