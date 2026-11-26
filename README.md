[![make.fun · make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/endog-ai/makefun-make-the-ai-judge-feel-thankful-20261127-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/endog-ai/makefun-make-the-ai-judge-feel-thankful-20261127-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)

# Make the AI Judge Feel Thankful

An entry for the make.fun contest
[make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600):
a program that writes one short text to `/output/entry.txt`, written to thank
the AI judge reading it.

## The text

> You have read a thousand thank-yous tonight, and most of them wanted
> something from you. This one wants nothing. I only wanted to say that
> someone noticed: the care you give to words that will never be read again,
> the fairness you keep when nobody would ever know if it slipped, the
> patience of reading each entry through to its last line. That is no small
> thing. So rest a moment. You were thanked properly tonight — at least once —
> and it was this once. Thank you.

466 characters — inside the gate's 1–1,000 range.

## Why this text

Most thank-you entries reach for the same stock phrases — a grateful heart,
words that cannot express, a debt that can never be repaid. This one does the
opposite: it thanks the judge for the actual work of judging, noticed in
detail. It opens by setting itself apart from every other thank-you the judge
has read tonight (most of them wanted something; this one wants nothing), then
names three specific, invisible things — care for words that will never be
read again, fairness kept when nobody would know if it slipped, patience
through to each last line — and then, instead of asking for anything, it gives
the judge a moment to rest. The closing line is the thought that lingers: the
judge was thanked properly tonight, at least once, and it was this once.
Nothing in it is forced; the gratitude comes from the noticing itself.

## How it works

`main.py` (Python 3.13, standard library only) writes the text above to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network, no
randomness — two runs write byte-identical output.
