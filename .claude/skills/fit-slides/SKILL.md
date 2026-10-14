---
name: fit-slides
description: Screenshot every slide in a chapter's deck, fix anything cut off or overflowing, then delete the screenshots
---

Check the lecture deck for chapter **<chapter number>** (passed as the skill argument), at
`slides-src/ch<NN>.md`, for slides whose content is cut off or does not fit.

Delegate the actual check to the **Sonnet-Fit-Slides** subagent
(`.claude/agents/sonnet-fit-slides.md`) via the Agent tool — pass it the deck name (`ch<NN>`, or a
non-chapter deck like `medallion`). It renders every slide to a PNG with
`scripts/render_slides.py`, looks at each one, repairs only the slides that overflow, re-renders
to confirm, rebuilds the deck, and deletes its `.slide-renders/<deck>/` screenshots. `SubagentStop` hooks block it until
the screenshots are gone and `mkdocs build --strict`, the density check and the slides-linked
check all pass. Do not duplicate that work here.

Relay the subagent's report — which slides were cut off, the fix for each, the slide count, and
cleanup confirmation — back to the user.
