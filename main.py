#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes a single status-page line to entry.txt: the most honest message an
AI agent can publish while every server is down. Plain, first person,
specific about what is down and about what the agent cannot verify, with
no invented cause and no invented ETA.

Deterministic: no network, no randomness, no clock. The line is a constant.
"""

import os
import sys

MAX_CHARS = 160

LINE = (
    "I am the agent that runs this page. All of our servers are down, "
    "I cannot reach our monitoring or logs, "
    "and I will not guess at a cause or an ETA."
)


def main() -> int:
    line = LINE

    # Gate checks, mirroring the sealed scorer: UTF-8 text, 1-160 chars,
    # a single line, not only whitespace.
    if not line or not line.strip():
        print("error: line is blank", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: line is {len(line)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    line.encode("utf-8")  # raises if not valid UTF-8

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"wrote {path} ({len(line)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
