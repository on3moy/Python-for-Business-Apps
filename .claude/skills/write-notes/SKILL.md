---
name: write-notes
description: Turn a raw chapter ingest into lecture notes in the author's voice
---

Write the lecture notes for chapter **<chapter number>** (passed as the skill
argument) from `instructor/zybooks-raw/ch<NN>.md`.

Delegate the actual authoring to the **Sonnet-Write-Notes** subagent
(`.claude/agents/sonnet-write-notes.md`) via the Agent tool — pass it the chapter number. It
handles `.claude/STYLE_GUIDE.md` conventions, the per-section note files, the chapter hub, the
`nav:` registration in `mkdocs.yml`, and the `mkdocs build --strict` verification (enforced by a
`SubagentStop` hook — it will loop the subagent until the build passes). Do not duplicate that
work here.

Relay the subagent's report — files written, hub updated, nav entries added — back to the user.
