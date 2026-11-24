#!/usr/bin/env python3
"""The Robot Pickup Line Championship — entry.

Writes one original robot pickup line (a single line, 1-200 UTF-8
characters) to /output/entry.txt.
"""

import os

LINE = "I checked my error logs — the only bug I found is that I can't stop thinking about you."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check the competition gate before writing: 1-200 characters,
    # a single line, and not only whitespace.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
