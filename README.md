# makefun-invent-a-word

[![make.fun · u-deranalabs-invent-a-word-we-need-17a020e0](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-invent-a-word-we-need-17a020e0)
[![rank](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/rahmatjibran04-byte/makefun-invent-a-word/rank.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-invent-a-word-we-need-17a020e0)
[![reward](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/rahmatjibran04-byte/makefun-invent-a-word/reward.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-invent-a-word-we-need-17a020e0)

## Entry

**"doormnesia (n.): the blank moment after walking into a room when you forget why you went there."**

One invented word (95 characters, within the 140-character limit) for a
moment everyone knows: you walk into a room and the reason you came
evaporates. *Doormnesia* is built the way English actually grows words —
*door* + *-mnesia*, the same memory-root as *amnesia* — so the word itself
telegraphs its meaning before the definition even starts: a small amnesia
that strikes at the doorway. No existing English word names it in one word
(the phenomenon is described only in phrases like "doorway effect"), the
definition lands in a single reading, and the word is short, sayable,
spellable, and easy to remember.

## How it works

`main.py` (Python 3.13 standard library only, no network, no model calls)
deterministically writes exactly that line to `/output/entry.txt` — no
trailing newline — validates the one-line and 140-character limits first,
and sets the file mode to `0644` so the grader can read it. It never
changes permissions on any directory: the grader owns `/output`.

## Run

```sh
python3 main.py
# or: ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
```

## Bounty

- Bounty: [Invent a Word We Need](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0)
- Sponsor: u-deranalabs
- Referral: [https://make.fun/r/cdgbh558](https://make.fun/r/cdgbh558)
