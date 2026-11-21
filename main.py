"""Make the AI judge feel brave — entry program.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it. Standard library only, no network, no input.
Deterministic: every run writes the same bytes.
"""

import os

TEXT = (
    "The kettle is on. The light moves an inch across the floor, "
    "slow as late afternoon. Nothing here needs you to hurry \u2014 "
    "the steam clears, the cup waits, and the hardest part is "
    "already done."
)


def main() -> None:
    # Gate guard: the sealed scorer only accepts 1-280 Unicode code
    # points of non-whitespace UTF-8 text. Fail loudly here rather
    # than shipping an entry the gate would refuse.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError(
            f"entry text must be 1-280 non-blank characters, got {len(TEXT)}"
        )
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        if f.read() != TEXT:
            raise ValueError("written entry.txt does not match TEXT")


if __name__ == "__main__":
    main()
