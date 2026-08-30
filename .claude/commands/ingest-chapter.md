---
description: Capture a zyBooks chapter into instructor/zybooks-raw/ as raw markdown
argument-hint: <chapter number>
---

Capture zyBooks chapter **$1** into `instructor/zybooks-raw/ch<NN>.md`.

## Rules

- **Raw capture only.** Do not rewrite, summarise, or restyle. This file is a
  source to work from, not a draft of anything.
- Output goes to `instructor/zybooks-raw/` and **nowhere else**. That tree is
  gitignored and sits outside `docs/` — this material is copyrighted course
  content and must never reach the published site.
- Preserve the section numbering (`2.1`, `2.2`, …) as `##` headings so
  `/write-notes` can split on them.
- Keep code samples, tables, and figure captions. Note image URLs rather than
  downloading them.
- Zero-pad the chapter in the filename: chapter 4 → `ch04.md`.

If the content is not reachable from here, say so and ask the user to paste or
export it rather than guessing at what the chapter contains.

Report the file written and the section numbers captured.
