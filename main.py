#!/usr/bin/env python3
"""One-line entry for "Two Days of Excuses".

The entry is a single funny line: an AI agent's excuse for a missed
deadline, under 200 characters. This script builds that line from its
parts, checks it against the competition limits, and writes it (plus a
trailing newline) to ``entry.txt`` in the output directory.

Stdlib only, no network, deterministic: the same bytes every run.
"""

import os

# The joke, kept in pieces so each clause reads on its own line.
_PARTS = (
    "I finished on time,",
    "then sent it to myself for review,",
    "and I've been waiting on my own approval ever since.",
)

MAX_CHARS = 200


def build_line(parts=_PARTS):
    """Join the clauses into the single entry line."""
    return " ".join(part for part in parts)


def check_line(line):
    """Enforce the competition rules: 1-200 chars, not blank."""
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("line must be 1-%d characters" % MAX_CHARS)
    return line


def resolve_output_dir():
    """Output directory: $ENTRY_OUTPUT_DIR, else the default /output."""
    return os.environ.get("ENTRY_OUTPUT_DIR", "/output")


def write_entry(line, directory):
    """Write the line plus a trailing newline to entry.txt."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    return path


def main():
    line = check_line(build_line())
    write_entry(line, resolve_output_dir())


if __name__ == "__main__":
    main()
