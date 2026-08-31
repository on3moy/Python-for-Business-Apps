---
name: solve-notebook
description: Create the instructor-only solved version of a chapter's practice notebook
---

Write the solution notebook for chapter **<chapter number>** (passed as the skill argument), from
`notebook-src/ch<N>.md`.

Delegate the actual work to the **Sonnet-Solve-Notebook** subagent
(`.claude/agents/sonnet-solve-notebook.md`) via the Agent tool — pass it the chapter number. It
duplicates the practice notebook's structure into `instructor/solutions/ch<N>.md`, fills in every
`# TODO` cell with real working code, and builds + executes it via
`scripts/build_solution_notebooks.py` (enforced by a `SubagentStop` hook that actually re-runs the
notebook and blocks until every cell executes without error). `instructor/` is gitignored and
never published — this is instructor-only material. Do not duplicate that work here.

Relay the subagent's report — file written, TODOs solved, execution confirmation — back to the
user.
