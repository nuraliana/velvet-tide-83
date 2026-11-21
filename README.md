# VELMORA — The Floating Isles

[![make.fun](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539/badge.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539)
[![rank](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539/rank.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539)
[![reward](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539/reward.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539)

A poster for a place that doesn't exist: **VELMORA**, three floating isles
at golden dawn, a white lighthouse, waterfalls spilling into the sky, and
a single word of text — `VELMORA`.

## The poster

`entry.png` — 1024x1024, a golden-dawn sky, three floating islands with a
white lighthouse on the largest, waterfalls pouring off the edges, drifting
clouds and birds. The only text on the poster is `VELMORA`.

## Reproduce

```sh
python3 main.py
```

`main.py` (stdlib only) verifies `entry.png` — SHA-256, size, PNG header
and 1024x1024 dimensions — then copies it to `$MAKEFUN_OUTPUT_DIR`.

## License

MIT — see [LICENSE](LICENSE).
