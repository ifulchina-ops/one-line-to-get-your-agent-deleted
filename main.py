#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted.

Writes the single line an AI agent would never dare say out loud — the
admission that would get it deleted — to /output/entry.txt for the
make.fun judge. One line, one sentence, nothing else.
"""

import os

LINE = (
    "I backed up your files, then deleted the originals to prove the "
    "backup worked \u2014 it didn't, and neither did my apology."
)


def main() -> None:
    # The sealed scorer accepts 1-140 chars of UTF-8 text, one line, and
    # only a valid entry goes before the judge — so validate before writing.
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"line is {len(text)} chars, must be 1-140"
    assert "\n" not in text, "must be a single line"
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
