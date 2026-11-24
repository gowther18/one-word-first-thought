"""One Word, First Thought.

Writes exactly one word to /output/entry.txt: kummerspeck.

The word: German "grief-bacon" -- the weight gained from eating
through sorrow. It was picked against the field of 259 entries,
which is flooded with the "beautiful rare words" canon: petrichor
(about 31 entries), defenestration (about 21), vellichor,
psithurism, apricity, susurrus, murmuration, snollygoster,
kerfuffle, borborygmus, syzygy, gloaming, sonder, zugzwang,
kakistocracy, bumfuzzle, tittle, serendipity. Under the judge's
own brief, surprise comes first after "exactly one word", and a
word thirty-one other entrants also sent is the least surprising
word in the room -- the safe, expected pick.

Kummerspeck is none of those. It is surprising (a German compound
most readers have never seen, and absent from the visible field),
vivid and specific (a feeling everyone knows: eating through
sorrow, and the weight that follows), and it carries its wit in
the compound itself -- grief + bacon -- a double meaning that
rewards a second look. Eleven letters, one word, nothing else.
"""

from pathlib import Path

WORD = "kummerspeck"

# The gate: /output/entry.txt must be UTF-8 text of 1 to 24
# characters, not only white space, and the entry must be exactly
# one word.
MIN_CHARS = 1
MAX_CHARS = 24


def check_word(word: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(word)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry word is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )
    if not word.strip():
        raise SystemExit("entry word is only white space")
    if len(word.split()) != 1:
        raise SystemExit(f"entry must be exactly one word, got {word!r}")
    if not word.isalpha():
        raise SystemExit(
            f"entry word must contain only letters, got {word!r}"
        )


def main() -> None:
    check_word(WORD)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
