---
description: Derive original in-class problems from a chapter's zyBooks labs
argument-hint: <chapter number>
---

Build in-class problems for chapter **$1**.

## Everything here stays in `instructor/`

`instructor/` is gitignored and lives outside `docs/`. Nothing this command
produces goes near the published site. Do not add any of it to `nav:`.

## Steps

1. Capture the chapter's lab prompts to `instructor/labs/ch<NN>/`. Raw capture,
   no rewriting — this is copyrighted zyBooks material held only as a source.

2. For each lab worth covering in class, write an **original** problem to
   `instructor/problems/ch<NN>/<n>-short-name.md`:

   - Same concept and roughly the same difficulty as the lab it shadows.
   - **Different scenario, different numbers, different variable names.** It
     must teach the same skill without being the zyBooks problem with the serial
     numbers filed off. If you cannot restate it originally, skip it and say so.
   - Business framing, matching the course: salary, taxes, invoices, inventory,
     report formatting.
   - Note which lab it corresponds to, so it can be paired during lecture.

3. Include a worked solution in the same file under a `## Solution` heading,
   with the code in a bare fence and `# Lets …` comments — you will be walking
   the room through it.

## Report

List the problems written, the lab each shadows, and any lab you skipped
because it could not be restated as original work.
