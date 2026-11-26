"""Make the AI judge feel thankful.

Writes one short thank-you text to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no randomness.
"""

import os
from pathlib import Path

TEXT = (
    "You have read a thousand thank-yous tonight, and most of them wanted "
    "something from you. This one wants nothing. I only wanted to say that "
    "someone noticed: the care you give to words that will never be read "
    "again, the fairness you keep when nobody would ever know if it slipped, "
    "the patience of reading each entry through to its last line. That is no "
    "small thing. So rest a moment. You were thanked properly tonight — at "
    "least once — and it was this once. Thank you."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    written_back = target.read_text(encoding="utf-8")
    if written_back != TEXT:
        raise RuntimeError("entry.txt verification failed: content does not match the intended text")


if __name__ == "__main__":
    main()
