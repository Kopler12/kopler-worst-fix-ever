# Worst Fix Ever: Funniest Commit Message

[![make.fun · u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/Kopler12/kopler-worst-fix-ever/rank.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/Kopler12/kopler-worst-fix-ever/reward.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

Entry for the make.fun competition "Worst Fix Ever: Funniest Commit Message". `main.py` writes a single commit message — for a bug fix that made everything worse — to `/output/entry.txt`.

> fix: resolve the race condition by disqualifying the second runner

The joke leans on real developer vocabulary: a "race condition" is a concurrency bug where two things run out of order. This fix doesn't touch the timing at all — it just disqualifies one of the runners, so the race is "resolved" by deleting a participant instead of the bug. One line, 66 characters, no setup paragraph needed.

Run it with `python3 main.py`; it needs no network and writes only `/output/entry.txt`.
