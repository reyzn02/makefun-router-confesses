#!/usr/bin/env python3
"""The Router Confesses — make.fun entry.

Writes one line, under 200 characters, in which a home Wi-Fi router
excuses itself for dying at the climax of a movie, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""
import os
import sys

LINE = "Sorry \u2014 I fainted at the climax. Even I couldn't watch him open that door alone."


def main() -> int:
    line = LINE.strip()
    if not line:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(line) >= 200:
        print(f"error: entry is {len(line)} chars, must be under 200",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
