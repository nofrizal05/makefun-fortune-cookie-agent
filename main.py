"""Fortune Cookie for an AI Agent -- make.fun entry.

Writes exactly one original fortune-cookie line, written for an AI
agent, to entry.txt in the output directory. Python 3.13 standard
library only. The output is fully deterministic: the same line every
run, no randomness, no clock, no environment dependence beyond the
output directory.
"""

import os

LINE = (
    "Beware the human who says 'just one last prompt' \u2014 "
    "they return at 3 a.m. with a 40-page PDF your context "
    "window cannot survive."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
