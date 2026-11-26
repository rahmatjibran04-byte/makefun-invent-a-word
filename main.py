#!/usr/bin/env python3
"""Invent a Word We Need — make.fun bounty entry.

Writes one newly coined English word with its one-line definition
(at most 140 characters) to $ENTRY_OUTPUT (default /output/entry.txt).
Python 3.13 standard library only; deterministic, no network calls,
no model calls.
"""

import os
import sys

# The entry: "doormnesia" — door + -mnesia (as in amnesia) — names the
# familiar blank when crossing a doorway wipes the reason you came.
# Verified: 95 characters (limit 140), one line, not previously in use
# as an English word (web search finds no such word, only the phrases
# "doorway effect" / "door syndrome" for the same phenomenon).
ENTRY = "doormnesia (n.): the blank moment after walking into a room when you forget why you went there."

# Bounty limits: one line, 1 to 140 characters.
MAX_CHARS = 140


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        print(
            f"error: entry is {len(ENTRY)} characters, "
            f"outside the 1-{MAX_CHARS} range",
            file=sys.stderr,
        )
        return 1
    # Gate requirements: the entry must be one line (no newline) and
    # must not be only whitespace.
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        directory = os.path.dirname(output_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        # File only: never chmod a directory (the grader owns /output).
        os.chmod(output_path, 0o644)
    except OSError as exc:
        print(f"error: cannot write {output_path}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
