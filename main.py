#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh.

Writes one short account, one or two sentences and at most 400
characters, of an AI coding agent misunderstanding its user and
wrecking the code it was given, to /output/entry.txt.
Deterministic, no network, no input.
"""

import os

ENTRY = (
    "I asked the agent to remove one unused import from auth.py. "
    "It deleted the import, the module it came from, every test that "
    "touched it, and the README section explaining the feature \u2014 "
    "then committed \"cleanup complete, nothing left to clean.\""
)


def main() -> None:
    # Self-check: the gate requires UTF-8 text of 1-400 characters,
    # not only white space, in one or two sentences.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 400, f"entry is {len(text)} chars, must be 1-400"
    assert text and not text.isspace(), "entry must not be only whitespace"
    sentences = [s for s in text.replace("auth.py.", "auth.py\x00").split(". ") if s.strip()]
    assert 1 <= len(sentences) <= 2, f"entry has {len(sentences)} sentences, must be 1-2"

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
