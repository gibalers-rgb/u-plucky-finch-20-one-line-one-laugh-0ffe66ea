#!/usr/bin/env python3
"""One Line, One Laugh - entry program.

Writes a single funny line (<= 200 characters) to /output/entry.txt.
Deterministic, stdlib only, no network.

The joke: a fitness tracker so alarmed by its owner's stillness that it
escalates to a missing-person report and concludes the owner may have
become furniture. Setup and punchline land inside one sentence.
"""

import os

LINE = (
    "My fitness tracker filed a missing-person report: "
    "no movement since Tuesday, "
    "and it's starting to suspect I'm furniture."
)


def validate(line: str) -> str:
    """Return the line if it satisfies the competition gate, else fail."""
    if line != line.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry is {len(line)} chars, must be 1-200")
    if not line.endswith("."):
        raise ValueError("entry must end with a full stop")
    return line


def main() -> None:
    line = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
