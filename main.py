"""Vacuum's Alibi, v3: the dust has a lawyer.

One line, under 200 characters. The vacuum reports the spot
it skipped, in its own deadpan log voice: low battery, a tenant
with seniority, and a decision made out of respect.
"""

from pathlib import Path

LINE = (
    "Battery at 9%. The dust under the bed has seniority, "
    "a lease, and a lawyer. I cleaned around it out of respect."
)
# 111 characters: one line, one excuse, punch at the end.

DEST = Path("/output/entry.txt")


def main() -> None:
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
