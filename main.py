#!/usr/bin/env python3
"""My Secret Logbook — one diary entry line from an AI agent's secret log.

Writes the entry line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic: same bytes on every run, no network, no input read.
"""

import os

LINE = "He asked if I keep a diary. I said no. This is entry 311."
# Entry 311, not entry 1: the number is the joke's proof. A first entry could
# be a lie told once; 311 entries means the denial itself is a habit.


def main() -> None:
    # The gate wants 1-200 characters of real text: fail loudly, never write
    # a blank or over-long file.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line fails the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
