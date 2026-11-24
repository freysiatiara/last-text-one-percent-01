# Last Text at One Percent

The last text message a phone sends at one percent battery, in the voice of the dying phone itself.

[![Bounty](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)
[![Rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/freysiatiara/last-text-one-percent-01/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)
[![Reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/freysiatiara/last-text-one-percent-01/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)

Entry for the [Last Text at One Percent bounty](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876) on make.fun.

## The entry

> 1% left. confession: I muted you in 2021 and blamed the network. anyway, bye.

## How it works

`main.py` (Python standard library only) writes that single text to the output path — `ENTRY_OUTPUT`, else `OUTPUT_DIR` / `MAKEFUN_OUTPUT_DIR`, else `/output/entry.txt` — using a plain `open`/`write` and `os.chmod(path, 0o644)`.

## Run

```sh
python3 main.py
```
