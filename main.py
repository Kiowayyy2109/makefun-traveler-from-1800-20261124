"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to someone arriving from 1800, to /output/entry.txt.

The sentence builds only from things a person from 1800 already knows --
a road, a post office, a library -- and uses no word coined after their
time. One comparison carries the whole picture: a single road joining every
library and post office on earth, so a letter crosses the sea in a blink
and a book from any shelf can be read at your table.

Deterministic: no input, no randomness, no network, no clock. The same
bytes are written on every run.
"""

import os

MAX_CHARS = 200

SENTENCE = (
    "Imagine one road joining every library and post office on earth, "
    "so a letter crosses the sea in a blink and a book from any shelf "
    "can be read at your table."
)


def check(text: str) -> None:
    """Gate the sentence the way the sealed scorer does: 1-200 chars."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("sentence must be 1-200 characters")
    if text.count(".") != 1:
        raise ValueError("sentence must be exactly one sentence")
    if not text.strip():
        raise ValueError("sentence must not be only whitespace")


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    check(SENTENCE)
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(SENTENCE)
    # Read it back and prove the file holds exactly the sentence, byte
    # for byte: a silent truncation or newline would fail the gate.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != SENTENCE:
        raise ValueError("entry.txt does not match the sentence")


if __name__ == "__main__":
    main()
