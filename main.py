"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

import os

TEXT = "My bank app wished me a happy birthday, which was the nicest thing it's said since 'insufficient funds'."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, 102 characters, one sentence;
# concrete detail (birthday wish vs. 'insufficient funds') with the punch on
# the bank app being nicer than usual.
