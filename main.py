#!/usr/bin/env python3
"""Rejected Olympic Sports — entry program.

Writes one funny single-line sport the Olympics turned down
(119 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; no network access; writes only to MAKEFUN_OUTPUT_DIR.
"""

import os
import sys

ENTRY = "Extreme Ironing, live from the cliff edge: athletes press shirts in a gale, scored on creases \u2014 and on not falling off."


def validate_entry(text: str) -> None:
    """Fail loudly if the line breaks the bounty gate (1-200 chars,
    single line, no trailing whitespace) instead of submitting a bad entry."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if "\n" in text or text != text.strip():
        raise ValueError("entry must be a single line with no extra whitespace")


def main() -> int:
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
