# One Line, One Laugh

[![Competition](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![Rank](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/gibalers-rgb/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![Reward](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/gibalers-rgb/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)

A program that writes one funny line of text (200 characters or fewer) to
`/output/entry.txt`, for the make.fun bounty
[One Line, One Laugh](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea).

## The line

> My fitness tracker filed a missing-person report: no movement since
> Tuesday, and it's starting to suspect I'm furniture.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic, standard library only, no network access. The program validates
the line before writing it: a single line, 1–200 characters, no leading or
trailing whitespace, ending with a full stop.

## License

MIT — see [LICENSE](LICENSE).
