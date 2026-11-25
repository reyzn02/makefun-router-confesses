#!/usr/bin/env python3
"""The Router Confesses -- make.fun entry.

Writes the router's one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Python 3 standard library only.
"""

import os
import sys
from pathlib import Path

ENTRY = "I cut the Wi-Fi at the climax because the dog dies in this one \u2014 and I'm not sitting here while you cry into the cushions."

MAX_CHARS = 200


def validate_entry(line: str) -> str | None:
    """Return an error message if the line breaks the gate, else None."""
    if not line.strip():
        return "entry is empty or whitespace only"
    if "\n" in line or "\r" in line:
        return "entry must be a single line"
    if len(line) >= MAX_CHARS:
        return "entry is %d chars, must be under %d" % (len(line), MAX_CHARS)
    return None


def main() -> int:
    line = ENTRY
    error = validate_entry(line)
    if error is not None:
        print("error: " + error, file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(line, encoding="utf-8")
    if out_path.read_text(encoding="utf-8") != line:
        print("error: written entry does not match the validated line", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
