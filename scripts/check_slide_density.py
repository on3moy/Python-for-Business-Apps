"""Lint Marp slide decks for density violations of .claude/SLIDE_STYLE_GUIDE.md.

Usage: uv run python scripts/check_slide_density.py slides-src/ch01.md [more.md ...]

Exits 0 and prints nothing when every deck is clean. Exits 1 and prints a report
naming the offending slides when any slide violates a hard density rule.

Two kinds of rule live here, and the distinction matters:

  * Per-slide caps (code blocks, bold labels, bullets, body lines) push *toward*
    splitting a slide in two.
  * The per-section cap and the flat 30-slide deck cap push *back*. Without them
    every rule in this file pointed the same direction, decks ratcheted upward
    with nothing to stop them, and the old fixed 25-40 deck budget -- a warning
    that never affected the exit code -- was routinely waved off. Both caps are
    blocking precisely because they are the only counterweight.

MAX_SLIDES_PER_DECK is flat rather than scaled: a chapter does not get more class
time for having more sections. The scaled range in deck_budget() remains a warning
for decks that are bloated for their shape while still under the flat cap.
"""

import os
import re
import sys

MAX_CODE_FENCE_LINES = 8  # style guide's target ceiling ("3-8 lines"); ~10 is an
                          # escape valve for exceptional cases, not the enforced default
MAX_CODE_BLOCKS_PER_SLIDE = 1
MAX_BOLD_LABELS_PER_SLIDE = 1
MAX_BULLET_ITEMS_PER_SLIDE = 5
MAX_BODY_LINES_PER_SLIDE = 8
MAX_CONTENT_SLIDES_PER_SECTION = 4
MAX_SLIDES_PER_DECK = 30     # blocking; see deck_budget() for why it is a flat number
MAX_TABLE_CAVEAT_LINES = 1   # one short footnote may share a table slide
MAX_TABLE_CAVEAT_CHARS = 70  # ...as long as it is genuinely a footnote

CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
BOLD_LABEL_RE = re.compile(r"^\*\*[^*]+:\*\*", re.MULTILINE)
BULLET_RE = re.compile(r"^\s*[-*]\s+", re.MULTILINE)
TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$", re.MULTILINE)
TABLE_SEPARATOR_RE = re.compile(r"^\s*\|[\s:|-]+\|\s*$")
DIRECTIVE_COMMENT_RE = re.compile(r"<!--\s*_.*?-->", re.DOTALL)
NOTE_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
LEAD_DIRECTIVE_RE = re.compile(r"<!--\s*_class:\s*lead\s*-->")
H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)


def split_slides(text):
    # Drop the frontmatter block (--- ... --- at the very top).
    text = text.strip()
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4:]
    slides = re.split(r"\n---\n", text)
    return [s.strip() for s in slides if s.strip()]


def strip_notes_and_directives(slide):
    visible = DIRECTIVE_COMMENT_RE.sub("", slide)
    visible = NOTE_COMMENT_RE.sub("", visible)
    return visible.strip()


def slide_title(visible):
    match = re.search(r"^#{1,3}\s+(.+)$", visible, re.MULTILINE)
    return match.group(1).strip() if match else "(untitled)"


def is_section_break(slide, visible):
    """A lead-class slide carrying an H1 -- title, section break, or closing."""
    return bool(LEAD_DIRECTIVE_RE.search(slide)) and bool(H1_RE.search(visible))


def check_slide(visible):
    problems = []

    code_fences = CODE_FENCE_RE.findall(visible)
    if len(code_fences) > MAX_CODE_BLOCKS_PER_SLIDE:
        problems.append(f"{len(code_fences)} code blocks (max {MAX_CODE_BLOCKS_PER_SLIDE})")
    for fence in code_fences:
        line_count = fence.count("\n") - 1
        if line_count > MAX_CODE_FENCE_LINES:
            problems.append(f"code block has {line_count} lines (max {MAX_CODE_FENCE_LINES})")

    body_without_code = CODE_FENCE_RE.sub("", visible)

    bold_labels = BOLD_LABEL_RE.findall(body_without_code)
    if len(bold_labels) > MAX_BOLD_LABELS_PER_SLIDE:
        problems.append(
            f"{len(bold_labels)} bold-label definitions (max {MAX_BOLD_LABELS_PER_SLIDE}) -- "
            "likely two ideas on one slide"
        )

    bullets = BULLET_RE.findall(body_without_code)
    if len(bullets) > MAX_BULLET_ITEMS_PER_SLIDE:
        problems.append(f"{len(bullets)} bullet items (max {MAX_BULLET_ITEMS_PER_SLIDE})")

    body_lines = [
        line for line in body_without_code.splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]
    if len(body_lines) > MAX_BODY_LINES_PER_SLIDE:
        problems.append(f"{len(body_lines)} body lines (max {MAX_BODY_LINES_PER_SLIDE})")

    table_rows = [
        line for line in body_without_code.splitlines()
        if TABLE_ROW_RE.match(line) and not TABLE_SEPARATOR_RE.match(line)
    ]
    if len(table_rows) >= 2:  # header + at least one data row
        non_table_lines = [
            line.strip() for line in body_without_code.splitlines()
            if line.strip() and not line.strip().startswith("#") and not TABLE_ROW_RE.match(line)
        ]
        # A single short line beside a table is a footnote-style caveat (e.g.
        # "the = always goes second"), not a second idea. Forbidding it outright
        # just exiled those caveats onto slides of their own, which is exactly
        # the bloat this linter exists to prevent.
        caveat = (
            len(non_table_lines) <= MAX_TABLE_CAVEAT_LINES
            and all(len(line) <= MAX_TABLE_CAVEAT_CHARS for line in non_table_lines)
        )
        extras = []
        if non_table_lines and not caveat:
            extras.append("intro/explanatory text")
        if code_fences:
            extras.append("a code block")
        if extras:
            problems.append(
                f"table combined with {' and '.join(extras)} -- likely doing two things at once"
            )

    return problems


def check_sections(slides):
    """Group content slides under the section break that precedes them.

    Returns (failures, section_count). Any content slides before the first
    section break are attributed to a pseudo-section so they are still counted.
    """
    sections = []  # (name, [slide_numbers])
    current = ("(before first section break)", [])

    for i, slide in enumerate(slides, start=1):
        visible = strip_notes_and_directives(slide)
        if is_section_break(slide, visible):
            if current[1]:
                sections.append(current)
            current = (slide_title(visible), [])
        else:
            current[1].append(i)

    if current[1]:
        sections.append(current)

    failures = []
    for name, slide_numbers in sections:
        if len(slide_numbers) > MAX_CONTENT_SLIDES_PER_SECTION:
            nums = ", ".join(str(n) for n in slide_numbers)
            failures.append(
                (name, f"{len(slide_numbers)} content slides "
                       f"(max {MAX_CONTENT_SLIDES_PER_SECTION}) -- slides {nums}")
            )

    return failures, len(sections)


def deck_budget(section_count):
    """Slide budget scaled to the chapter's shape, under a flat blocking ceiling.

    Two bounds do different jobs here, and the distinction matters:

    * MAX_SLIDES_PER_DECK is a flat, blocking 30 -- a lecture-length constraint,
      not a content one. A chapter does not get more class time for having more
      sections, so scaling the *ceiling* with section count was the loophole that
      let a 17-section chapter justify 73 slides. The fix for a chapter that does
      not fit is bundling sections under one break and pushing the rest into the
      notes and the speaker notes, which is exactly what ch06 did going 57 -> 30.
    * The scaled range below stays a warning and catches the opposite drift: a
      6-section chapter at 28 slides is under the flat cap but still bloated for
      its shape. Its upper bound is clamped so it can never contradict the cap.

    The scaled upper bound targets an *average* of 3.5 content slides per section,
    deliberately tighter than the per-section hard cap of 4: some sections earn
    the fourth slide, but a deck where most of them do has drifted. The figure is
    calibrated against ch01, the deck written before the counts started climbing.

    Each section also costs its own section-break slide, so the per-section
    allowance is 3.5 content + 1 break. Leaving the break out made the warning
    fire on decks that were legally under the content cap -- and a warning that
    fires on compliant decks is one nobody reads, which is how the old fixed
    25-40 budget stopped working.
    """
    lo = section_count * 2
    hi = section_count * 9 // 2 + 2  # (3.5 content + 1 break)/section; +2: title, closing
    return lo, min(hi, MAX_SLIDES_PER_DECK)


def check_deck(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    slides = split_slides(text)
    failures = []

    for i, slide in enumerate(slides, start=1):
        visible = strip_notes_and_directives(slide)
        problems = check_slide(visible)
        if problems:
            failures.append((i, slide_title(visible), problems))

    section_failures, section_count = check_sections(slides)

    deck_failure = None
    if len(slides) > MAX_SLIDES_PER_DECK:
        deck_failure = (
            f"{len(slides)} slides (max {MAX_SLIDES_PER_DECK}) -- bundle sections under "
            f"one break and move what you would say out loud into speaker notes"
        )

    warning = None
    lo, hi = deck_budget(section_count)
    if section_count and not deck_failure and not (lo <= len(slides) <= hi):
        warning = (
            f"{path}: {len(slides)} slides across {section_count} sections "
            f"(budget {lo}-{hi} at this section count)"
        )

    return failures, section_failures, deck_failure, warning


def main(argv):
    if not argv:
        print("usage: check_slide_density.py <deck.md> [more.md ...]", file=sys.stderr)
        return 2

    any_failures = False
    warnings = []

    for path in argv:
        # Files with a leading underscore (e.g. _layouts.md) are reference
        # sheets, not built decks -- build_slides.py skips them the same
        # way, and their nested example code fences confuse the naive
        # '---' slide splitter here.
        if os.path.basename(path).startswith("_"):
            continue
        failures, section_failures, deck_failure, warning = check_deck(path)
        if warning:
            warnings.append(warning)
        if deck_failure:
            any_failures = True
            print(f"\n{path}: deck exceeds the slide cap")
            print(f"    - {deck_failure}")
        if failures:
            any_failures = True
            print(f"\n{path}: {len(failures)} slide(s) violate density rules")
            for slide_num, title, problems in failures:
                print(f"  slide {slide_num} \"{title}\":")
                for problem in problems:
                    print(f"    - {problem}")
        if section_failures:
            any_failures = True
            print(f"\n{path}: {len(section_failures)} section(s) exceed the slide cap")
            for name, problem in section_failures:
                print(f"  section \"{name}\":")
                print(f"    - {problem}")

    for warning in warnings:
        print(f"warning: {warning}")

    return 1 if any_failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
