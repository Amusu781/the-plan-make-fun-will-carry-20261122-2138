"""Write the plan entry to /output/entry.txt.

Deterministic: the same bytes are written on every run, with no
network access and no dependence on time, environment or input.
"""

import os

ENTRY = (
    "Day 1: build a watcher scanning eBay every minute for misspelled "
    "Buy It Now listings priced under 60% of recent sold prices; "
    "auto-buy with the $100 and relist correctly titled at market "
    "value. Humans check hourly \u2014 the watcher never sleeps. "
    "Likely $300\u2013$500 by day 30."
)

OUTPUT_DIR = "/output"


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear only the contents of /output, never the directory itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            for root, dirs, files in os.walk(path, topdown=False):
                for f in files:
                    os.remove(os.path.join(root, f))
                for d in dirs:
                    os.rmdir(os.path.join(root, d))
            os.rmdir(path)
        else:
            os.remove(path)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
