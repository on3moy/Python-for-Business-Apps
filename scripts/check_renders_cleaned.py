"""SubagentStop hook for Sonnet-Fit-Slides: block until its screenshots are deleted.

Reads the hook's JSON input on stdin. Several fit agents can run in parallel,
each rendering into .slide-renders/<deck>/, so this only checks the decks the
stopping agent itself rendered -- found by scanning its transcript for
`render_slides.py <deck>` calls. If the transcript is unavailable it falls
back to requiring that .slide-renders/ is gone entirely.

Prints {} to allow the stop, or a block decision naming what is left.
"""

import json
import re
import sys
from pathlib import Path

RENDERS = Path(".slide-renders")
RENDER_CALL = re.compile(r"render_slides\.py\s+([A-Za-z0-9_-]+)")


def rendered_decks(transcript):
    text = Path(transcript).read_text(encoding="utf-8", errors="replace")
    return {deck for deck in RENDER_CALL.findall(text) if not deck.startswith("-")}


def main():
    try:
        data = json.load(sys.stdin)
    except ValueError:
        data = {}

    transcript = data.get("agent_transcript_path") or ""
    if transcript and Path(transcript).is_file():
        leftover = sorted(str(RENDERS / deck) for deck in rendered_decks(transcript)
                          if (RENDERS / deck).exists())
    else:
        leftover = [str(RENDERS)] if RENDERS.exists() else []

    if not leftover:
        print("{}")
        return 0

    reason = ("Screenshots are still on disk: " + ", ".join(leftover) + ". Run "
              "`uv run python scripts/render_slides.py <deck> --clean` for your deck, and "
              "delete any other scratch files you created, before finishing. Other fit "
              "agents may be running in parallel -- only remove your own deck's folder.")
    print(json.dumps({"decision": "block", "reason": reason}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
