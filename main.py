#!/usr/bin/env python3
"""The Houseplant Out-of-Office - make.fun bounty entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Pure standard library, deterministic: the same line every run.
"""
import os
import sys

LINE = "Out of office. Nobody watered me since March and I'm still alive, purely out of spite. Your email can wait too. - Fern"

def main() -> int:
    if not 1 <= len(LINE) <= 120:
        print(f"entry is {len(LINE)} characters, must be 1-120", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != LINE:
            print("verification failed: entry.txt differs", file=sys.stderr)
            return 1
    print(f"wrote {len(LINE)} characters to {path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
