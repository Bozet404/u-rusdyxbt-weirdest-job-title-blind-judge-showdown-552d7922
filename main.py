#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown — make.fun entry.

Writes exactly one job title to /output/entry.txt: a real-sounding
corporate title with one hilariously specific twist. The title is a
plain string constant; the program takes no input and needs no network.
"""

import os

TITLE = "Director of First Impressions for Witness Protection"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    title = TITLE.strip()
    if not title:
        raise SystemExit("refusing to write an empty title")
    if len(title) > 60:
        raise SystemExit(f"title is {len(title)} chars, over the 60-char cap")
    # Create the output directory only when it is missing; never delete it.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(title)


if __name__ == "__main__":
    main()
