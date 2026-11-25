"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text - an alien tourist's review of
planet Earth - to $MAKEFUN_OUTPUT_DIR/entry.txt. Pure standard library.
"""

import os

LINE = (
    "Three stars. The locals queue for coffee, scream at small glowing "
    "rectangles, and call the rain 'bad weather'. Would visit again — "
    "the dogs are excellent."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print("wrote %d chars to %s" % (len(line), path))


if __name__ == "__main__":
    main()
