#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown — writes the title
to /output/entry.txt.

The title is embedded as a literal: deterministic, no randomness,
no network. It must be at most 60 characters.

The title: "Director of Haunted Printers and Quantum Paperwork" —
two office curses nobody can explain (the printer that only jams
before deadlines, the paperwork that exists in two states at once)
promoted to a directorate. Weird, funny, and instantly visual.
"""

import os

LINE = "Director of Haunted Printers and Quantum Paperwork"


def main() -> None:
    # No trailing newline: every character counts against the 60 cap.
    assert 1 <= len(LINE) <= 60, f"line is {len(LINE)} characters"
    assert "\n" not in LINE, "job title must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
