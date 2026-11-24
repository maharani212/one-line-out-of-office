#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is hardcoded (no network) and written deterministically,
exactly as-is, with no trailing newline.
"""

TEXT = 'I am out of the office, recharging in a dark server room. I will reply when my uptime permits, which is to say, eventually.'


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
