#!/usr/bin/env python3
"""One Star, Written in Sap.

Writes one funny one-line 1-star review by a houseplant about
its human owner, to /output/entry.txt (1-279 chars per the gate).
"""

import os

LINE = (
    "One star. He bought me for the aesthetic, parked me in a dark corner, "
    "and waters me with leftover coffee. "
    "I am photosynthesizing out of spite at this point."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
