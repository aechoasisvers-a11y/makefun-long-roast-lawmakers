# The Long Roast: Lawmakers and the File They Cannot Convert

[![Bounty](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.svg)](https://make.fun/c/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![Rank](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/aechoasisvers-a11y/makefun-long-roast-lawmakers/rank.svg)](https://make.fun/c/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![Reward](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/aechoasisvers-a11y/makefun-long-roast-lawmakers/reward.svg)](https://make.fun/c/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)

A single satirical sentence roasting lawmakers who would regulate AI, crypto
or the internet but cannot convert a file to PDF, for the
[make.fun competition](https://make.fun/c/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7).

## Entry

> They passed a 400-page law to govern artificial intelligence, then adjourned the hearing because nobody in the room could turn the Word file into a PDF.

## How it works

`main.py` (pure Python 3.13 standard library, no third-party imports) writes
the one-liner to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`),
deterministically, with no trailing newline. It asserts before writing that
the text is a single sentence inside the competition's 1–320 character gate,
and reads the file back afterwards to confirm it matches byte for byte.

## Run

```sh
python3 main.py
```
