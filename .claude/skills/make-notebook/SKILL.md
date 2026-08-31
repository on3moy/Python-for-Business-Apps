---
name: make-notebook
description: Write a fill-in-the-blank Jupyter practice notebook for a chapter from its published notes
---

Write the practice notebook for chapter **<chapter number>** (passed as the skill argument), from
`docs/notes/ch<NN>/`.

Delegate the actual authoring to the **Sonnet-Make-Notebook** subagent
(`.claude/agents/sonnet-make-notebook.md`) via the Agent tool — pass it the chapter number. It
handles `.claude/NOTEBOOK_STYLE_GUIDE.md` conventions, the fill-in-the-blank cell discipline
(carried over from the same leakage lessons as `Sonnet-Clean-Slides`), the
`scripts/build_notebooks.py` build, the `mkdocs.yml` nav entry, and the `mkdocs build --strict` /
`scripts/check_notebooks_linked.py` verification (enforced by `SubagentStop` hooks that loop the
subagent back until both pass). Do not duplicate that work here.

Relay the subagent's report — file written, concept-cell count, no-answers-given confirmation —
back to the user.
