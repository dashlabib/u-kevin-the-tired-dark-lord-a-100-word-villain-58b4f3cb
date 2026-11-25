#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue — make.fun entry.

This program does exactly one small thing: it writes a single original
100-word monologue, spoken by a fantasy villain who is secretly just very
tired, to /output/entry.txt (and prints it to standard output).

The speaker is the Keeper of the Ninth Bell: forty years he has pulled the
bell rope once an hour so the marsh stays asleep and the dead stay
agreeable. The hero has come for the rope, as heroes, tax collectors and
his own daughter have before. His tiredness is never announced — it lives
in the pauses, the trailing sentences and the small deflections (the
sticking third step, sitting down mid-threat, the kettle) — while the
menace stays real: ring the bell wrong and the marsh wakes hungry.

Standard library only. No arguments, no network, no randomness, no side
effects beyond the one output file.
"""

import os
import sys

# The monologue is held as three beats and joined with spaces, so the entry
# is assembled from its movements rather than stored as one blob.
OPENING = (
    "Come in. Mind the third step. It sticks. "
    "Forty years I have kept the Ninth Bell ringing, one pull every hour, "
    "so the marsh stays asleep and the dead stay agreeable."
)
MIDDLE = (
    "You came for the bell rope, I suppose. Everyone does, eventually. "
    "Heroes, tax collectors, my daughter, twice. Take it. No — wait. "
    "Hold it a moment, while I sit. There. Feel the weight of it? "
    "That is the kingdom, hanging on a frayed cord."
)
CLOSE = (
    "Ring it wrong and the marsh wakes hungry. "
    "Ring it right and — well. You will see. "
    "The kettle is on, if you are staying."
)

MONOLOGUE = OPENING + " " + MIDDLE + " " + CLOSE

# The competition's gate: /output/entry.txt is UTF-8 text of 1 to 600
# characters, not only white space. The monologue is exactly 100 words.
MAX_CHARS = 600
WORD_TARGET = 100

# The entry text shipped in the repository beside this program. When the
# program runs from the repository, its output must agree with that file
# byte for byte, so the text reviewers read is the text the program writes.
REPO_ENTRY_TXT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "entry.txt"
)


def main() -> int:
    text = MONOLOGUE
    words = text.split()
    if len(words) != WORD_TARGET:
        print(
            f"monologue is {len(words)} words, expected {WORD_TARGET}",
            file=sys.stderr,
        )
        return 1
    if not (1 <= len(text) <= MAX_CHARS) or not text.strip():
        print(
            f"monologue is {len(text)} characters, gate is 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if os.path.exists(REPO_ENTRY_TXT):
        with open(REPO_ENTRY_TXT, "r", encoding="utf-8") as f:
            shipped = f.read().strip()
        if shipped != text:
            print(
                "monologue differs from the entry.txt shipped in the repository",
                file=sys.stderr,
            )
            return 1
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Re-read and confirm the stored file matches the validated text.
    with open(out_path, "r", encoding="utf-8") as f:
        stored = f.read()
    if stored != text + "\n":
        print("stored entry does not match the validated text", file=sys.stderr)
        return 1
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
