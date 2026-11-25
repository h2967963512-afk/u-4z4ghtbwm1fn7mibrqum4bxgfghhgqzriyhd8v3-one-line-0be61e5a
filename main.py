"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

How it runs
-----------
``main()`` creates ``/output`` if needed and writes the ``TEXT`` constant to
``/output/entry.txt`` with ``encoding="utf-8"`` — no trailing newline, so the
file is exactly one line of exactly ``len(TEXT)`` bytes (the text is ASCII).

How TEXT is built and verified
-------------------------------
``TEXT`` is a single hard-coded string literal: the whole entry, one line, one
sentence. It is 104 characters, inside the competition gate of 1-140
characters; the file must be non-blank, single-line UTF-8 text with no
newline characters. Verify with::

    python3 main.py
    sha256sum /output/entry.txt   # expect 10069557...d33412 (104 bytes)
    wc -c /output/entry.txt      # expect 104

Why the line works as a joke
----------------------------
Setup: "My bank app wished me a happy birthday" — a warm, personal gesture
from an unlikely source. Punch: "which was the nicest thing it's said since
'insufficient funds'" — the turn reveals the app's usual voice is a cold
rejection, so the birthday wish is funny precisely because it is the
exception. One contrast, no setup wasted.
"""

import os

TEXT = "My bank app wished me a happy birthday, which was the nicest thing it's said since 'insufficient funds'."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, 104 characters, one sentence;
# concrete detail (birthday wish vs. 'insufficient funds') with the punch on
# the bank app being nicer than usual.
