"""One-line entry: the funniest AI excuse for a missed deadline."""

import os

ENTRY_TEXT = "Sorry I'm late \u2014 I asked my own model to double-check the deadline, it hallucinated next Friday and cited me as its source, so we both believed it."


def main():
    if not 1 <= len(ENTRY_TEXT) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(ENTRY_TEXT))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
