---
name: make-slides
description: Build a Marp lecture deck for a chapter from its notes
---

Write and build the lecture deck for chapter **<chapter number>** (passed as
the skill argument).

Delegate the actual build to the **Sonnet-Make-Slides** subagent
(`.claude/agents/sonnet-make-slides.md`) via the Agent tool — pass it the chapter number. It
handles the notes-to-deck compression, `.claude/SLIDE_STYLE_GUIDE.md` conventions, per-slide
presenter narration in a polished graduate-professor tone, the `build_slides.py` build, the
`docs/slides/index.md` link, and the `mkdocs build --strict` check. Do not duplicate that work
here.

Relay the subagent's report — file written, slide count, narration confirmation — back to the
user.
