#!/usr/bin/env python3
"""The Router Confesses -- make.fun entry.

Writes the router's one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Python 3 standard library only.
"""

import os
import sys
from pathlib import Path

ENTRY = "I dropped out at the climax because the hero said 'I'll be right back' \u2014 and I know exactly how that ends."

MAX_CHARS = 200


def main() -> int:
    line = ENTRY
    if not line.strip():
        print("error: entry is empty or whitespace only", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(line) >= MAX_CHARS:
        print(
            "error: entry is %d chars, must be under %d" % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
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
