---
name: clean-slides
description: Review an existing chapter's slide deck for density "leakage" and split overloaded slides
---

Review and repair the lecture deck for chapter **<chapter number>** (passed as the skill
argument), at `slides-src/ch<NN>.md`.

Delegate the actual review to the **Sonnet-Clean-Slides** subagent
(`.claude/agents/sonnet-clean-slides.md`) via the Agent tool — pass it the chapter number. It runs
the automated `scripts/check_slide_density.py` check, reads the deck itself for leakage the
mechanical check can't catch (a demo bundled with an unrelated generalization, a stacked
enumeration, etc.), splits only the slides that need it, rebuilds, and relies on the
`SubagentStop` hooks (`mkdocs build --strict`, then the density check scoped to this deck) to
verify. Do not duplicate that work here.

Relay the subagent's report — which slides were split and why, the new slide count, narration
confirmation — back to the user.
