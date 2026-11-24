#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes a single line — the excuse a developer gives when code breaks in
production — to /output/entry.txt.

Entry for make.fun competition
u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.
The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
"""

import os

LINE = (
    "I deleted the bug at 2 a.m. Turns out it was load-bearing "
    "\u2014 the entire feature was standing on it."
)


def main() -> None:
    # The gate refuses anything outside 1..200 characters, so fail loudly
    # here instead of writing an entry that can never be judged.
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-200")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Verify the round trip: what the grader reads must be exactly what
    # we validated above, with no trailing newline or encoding surprise.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt round-trip mismatch")
    print(f"wrote {len(written)}-character entry to /output/entry.txt")


if __name__ == "__main__":
    main()
