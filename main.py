#!/usr/bin/env python3
"""Write one excuse an AI agent gives for a missed deadline to entry.txt.

Stdlib only, no network, deterministic: the same line every run.
"""
import os

LINE = "I finished on time, then sent it to myself for review, and I've been waiting on my own approval ever since."


def main():
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
