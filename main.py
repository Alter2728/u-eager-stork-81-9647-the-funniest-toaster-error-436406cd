#!/usr/bin/env python3
"""Entry for make.fun bounty u-eager-stork-81-9647-the-funniest-toaster-error-436406cd:
"The Funniest Toaster Error Message".

Writes one line — the funniest error message a kitchen toaster would show
its owner — to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Python 3.13, standard library only. Deterministic: same bytes every run.

Revision note (thinking_revised): the draft's ending — "pretend this
never happened" — is a shrug the reader has heard before. The final keeps
the same setup (the toaster has decided to become a smoke machine) but
lands on a small heroic epitaph instead: "tell the others I went out
bravely." The appliance stays deadpan and dignified about its own
breakdown, which is where the laugh comes from.
"""

import os

ENTRY = (
    "ERROR 04: I have decided to become a smoke machine. Please unplug "
    "me and tell the others I went out bravely."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
