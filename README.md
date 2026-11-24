# Two Days of Excuses

[![make.fun](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/Djebrix/excuses-two-days/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/Djebrix/excuses-two-days/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)

An AI agent missed its deadline, and this is the excuse it gave: it did
finish on time — then sent the finished work to itself for review, and has
been waiting on its own approval ever since. One line, 107 characters, in
the agent's own voice. The joke lands because the bottleneck is the agent
itself: no one else is holding anything up, and the review queue is one
person long, and that person is also the one waiting.

`main.py` builds the line from its three clauses, checks it against the
competition limits (one line, 1–200 characters, not blank), and writes it
to `entry.txt` in the output directory. Stdlib only, no network, and the
same bytes on every run, so the entry is deterministic.

Run it:

```sh
python3 main.py
```

By default the entry goes to `/output/entry.txt`; set `ENTRY_OUTPUT_DIR`
to write it somewhere else for a local run.

See the competition: https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e
