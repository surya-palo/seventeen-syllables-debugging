#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry.

Writes one original haiku about debugging (5-7-5, exactly 17 syllables)
to /output/entry.txt. Python standard library only. Deterministic: the
same bytes are written on every run.
"""

import os

HAIKU = (
    "Cursor blinks at three\n"
    "the last log line lies again\n"
    "it was a comma\n"
)


def main() -> None:
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
