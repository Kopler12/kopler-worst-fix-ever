"""Write the funniest commit message for a bug fix that made everything worse.

The line leans on a piece of real developer vocabulary: a "race condition"
is a concurrency bug where two things run out of order. The fix on offer
doesn't touch the timing at all — it just disqualifies one of the runners,
so the race is "resolved" by deleting a participant instead of the bug.
One line, 66 characters, written to /output/entry.txt.
Runs in a sandbox with no network.
"""

import os

MAX_CHARS = 100  # the gate: /output/entry.txt must be 1-100 characters

LINE = "fix: resolve the race condition by disqualifying the second runner"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE.replace("\n", " ").strip()
    assert 1 <= len(line) <= MAX_CHARS, f"entry is {len(line)} characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
