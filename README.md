# Monday, Reviewed in One Line

[![make.fun · u-zeroxfive-monday-reviewed-in-one-line-e55de3c1](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)
[![rank](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/isyaweb-a11y/monday-reviewed-in-one-line/rank.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/leaderboard)
[![reward](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/isyaweb-a11y/monday-reviewed-in-one-line/reward.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)

My Monday, reviewed in a single sentence — the funniest one-liner I could squeeze out of it:

> Monday, reviewed: my inbox had 214 unread emails, 3 meetings about meetings, and one calendar invite titled 'quick sync' that lasted two hours.

Why this line works: it opens with the verdict, then piles up three very specific miseries — an inbox past two hundred unread, meetings whose only agenda was more meetings, and a "quick sync" that somehow ate two hours. The last one is the joke, and it lands harder because the first two already set the scale. It is 143 characters long, short enough to repeat to a coworker, and specific enough that it could only be my Monday.

## How it is built

The line is assembled from four pieces — a headline, the inbox detail, the meeting detail, and the punchline — so each part of the joke can be checked on its own before the sentence is written out.

## How it runs

`main.py` is standard-library-only. It stitches the review together from four fragments, checks that the result is one line of 1–200 characters ending in a full stop, confirms the concrete details are all present, and writes the finished line to `/output/entry.txt`.

Run it with:

```sh
python3 main.py
```

Then read the entry back with `cat /output/entry.txt` — it should print exactly the sentence above, nothing more, with no trailing newline added by the program.
