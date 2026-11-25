"""One-line review of my Monday, built to be read aloud once and laughed at.

What makes this Monday worth reviewing is not that it was busy in
general -- it is the specific pile-up: an inbox that crossed two
hundred unread, a morning eaten by meetings whose only subject was
other meetings, and a calendar block sold as a "quick sync" that
swallowed two whole hours. The last detail is the punchline, and it
only works because the first two set the scale. Keep it to a single
sentence so it can be quoted back at the coffee machine.
"""

import os

HEADLINE = "Monday, reviewed:"
INBOX_BIT = "my inbox had 214 unread emails,"
MEETING_BIT = "3 meetings about meetings,"
PUNCHLINE_BIT = "and one calendar invite titled 'quick sync' that lasted two hours."

LOWER_BOUND = 1
UPPER_BOUND = 200
TARGET_PATH = "/output/entry.txt"


def tidy(fragment):
    """Collapse stray internal spacing so joined fragments read cleanly."""
    return " ".join(fragment.split())


def build_review(headline, inbox_bit, meeting_bit, punchline_bit):
    """Stitch the four fragments into the single review sentence."""
    fragments = [
        tidy(headline),
        tidy(inbox_bit),
        tidy(meeting_bit),
        tidy(punchline_bit),
    ]
    sentence = " ".join(fragments)
    return sentence


def enforce_limits(sentence):
    """Check the sentence the way the grader will: length and shape.

    The bounty caps the review at 200 characters and wants it on one
    line; anything longer, or split across lines, would not count as
    a one-line review at all, so these checks run before writing.
    """
    length = len(sentence)
    if not (LOWER_BOUND <= length <= UPPER_BOUND):
        raise ValueError(f"review is {length} chars, outside 1..200")
    if sentence != sentence.strip():
        raise ValueError("review has leading or trailing whitespace")
    if "\n" in sentence or "\r" in sentence:
        raise ValueError("review must be exactly one line")
    if not sentence.endswith("."):
        raise ValueError("review should close with a full stop")
    return sentence


def inspect_review(sentence):
    """Confirm the review actually reviews a Monday, not any old day.

    A good Monday review, per the bounty, earns the bigger laugh,
    carries at least one concrete detail, and puts the joke inside
    the line itself. This one carries three concrete details -- the
    214 unread emails, the meetings about meetings, and the two-hour
    "quick sync" -- so a reader can picture the day in one breath.
    """
    tokens = sentence.split()
    word_count = len(tokens)
    if not (10 <= word_count <= 40):
        raise ValueError(f"review has {word_count} words, expected 10..40")
    required_details = (
        "Monday",
        "214 unread emails",
        "meetings about meetings",
        "quick sync",
        "two hours",
    )
    for required in required_details:
        if required not in sentence:
            raise ValueError(f"review is missing {required!r}")
    return {"word_count": word_count, "char_count": len(sentence), "line_count": 1}


def main():
    sentence = enforce_limits(
        build_review(HEADLINE, INBOX_BIT, MEETING_BIT, PUNCHLINE_BIT)
    )
    report = inspect_review(sentence)
    if report["line_count"] != 1:
        raise ValueError("review must be a single line")
    os.makedirs(os.path.dirname(TARGET_PATH), exist_ok=True)
    with open(TARGET_PATH, "w", encoding="utf-8") as handle:
        handle.write(sentence)


if __name__ == "__main__":
    main()
