#!/usr/bin/env python3
"""Everyday Wonder entry: a coin sinking through green fountain water.

Writes one sentence to entry.txt inside the directory named by the
MAKEFUN_OUTPUT_DIR environment variable (default /output).
All paths are resolved from this script's own location, never from the
current working directory. No network, no reads outside this repository.
"""

import os
import stat
from pathlib import Path

SENTENCE = (
    "My coin sank so slowly through the green fountain water "
    "that my wish reconsidered halfway down."
)


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    _ = script_dir  # paths are anchored here, not on the working directory
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(SENTENCE + "\n", encoding="utf-8")
    os.chmod(out_path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
