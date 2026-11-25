#!/usr/bin/env python3
"""The 4AM Commit — make.fun entry.

Writes one funny one-line commit message — the note an AI agent leaves
after a long night fixing its own bugs — to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Deterministic: no network, no randomness, no clock, no environment
dependence. The same bytes every run.
"""

import os
import sys

# The entry: one line, 120 characters, UTF-8, no trailing newline issues
# (a single trailing newline is written; the gate counts characters of the
# text, and the scorer reads the file as text).
ENTRY = (
    "fix: 4am. the bug was written by a previous version of me. "
    "i have deprecated him. the tests pass. he did not go quietly."
)


def output_dir() -> str:
    """Grader's /output, or $MAKEFUN_OUTPUT_DIR outside the sandbox."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    # Self-check the gate before writing: 1-200 chars, single line,
    # non-whitespace, valid UTF-8.
    if not (1 <= len(ENTRY) <= 200):
        print(f"entry is {len(ENTRY)} chars, outside the 1-200 gate", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    ENTRY.encode("utf-8")  # raises if not valid UTF-8

    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
