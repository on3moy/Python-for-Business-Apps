---
name: ingest-chapter
description: Capture a zyBooks chapter into instructor/zybooks-raw/ as raw markdown
---

Capture zyBooks chapter **<chapter number>** (passed as the skill argument) into
`instructor/zybooks-raw/ch<NN>.md`.

Delegate the actual capture to the **Haiku-Chapter-Ingest** subagent
(`.claude/agents/haiku-chapter-ingest.md`) via the Agent tool — pass it the chapter number and
any source material or URL the user gave you. It handles the raw-capture rules, filename
zero-padding, and the ingestion timestamp; do not duplicate that work here.

If the content is not reachable, say so and ask the user to paste or export it rather than
guessing at what the chapter contains, before invoking the subagent.

Relay the subagent's report of the file written and the section numbers captured back to the user.