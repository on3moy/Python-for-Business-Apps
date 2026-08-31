"""Lint Marp slide decks for density violations of .claude/SLIDE_STYLE_GUIDE.md.

Usage: uv run python scripts/check_slide_density.py slides-src/ch01.md [more.md ...]

Exits 0 and prints nothing when every deck is clean. Exits 1 and prints a report
naming the offending slides when any slide violates a hard density rule. A deck
whose content-slide count falls outside the style guide's 25-40 "rough budget" is
reported as a warning only -- it does not affect the exit code.
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
DECK_SLIDE_BUDGET = (25, 40)

CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
BOLD_LABEL_RE = re.compile(r"^\*\*[^*]+:\*\*", re.MULTILINE)
BULLET_RE = re.compile(r"^\s*[-*]\s+", re.MULTILINE)
TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$", re.MULTILINE)
TABLE_SEPARATOR_RE = re.compile(r"^\s*\|[\s:|-]+\|\s*$")
DIRECTIVE_COMMENT_RE = re.compile(r"<!--\s*_.*?-->", re.DOTALL)
NOTE_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


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
            line for line in body_without_code.splitlines()
            if line.strip() and not line.strip().startswith("#") and not TABLE_ROW_RE.match(line)
        ]
        extras = []
        if non_table_lines:
            extras.append("intro/explanatory text")
        if code_fences:
            extras.append("a code block")
        if extras:
            problems.append(
                f"table combined with {' and '.join(extras)} -- likely doing two things at once"
            )

    return problems


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

    warning = None
    lo, hi = DECK_SLIDE_BUDGET
    if not (lo <= len(slides) <= hi):
        warning = f"{path}: {len(slides)} slides (style guide budget is {lo}-{hi})"

    return failures, warning


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
        failures, warning = check_deck(path)
        if warning:
            warnings.append(warning)
        if failures:
            any_failures = True
            print(f"\n{path}: {len(failures)} slide(s) violate density rules")
            for slide_num, title, problems in failures:
                print(f"  slide {slide_num} \"{title}\":")
                for problem in problems:
                    print(f"    - {problem}")

    for warning in warnings:
        print(f"warning: {warning}")

    return 1 if any_failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
