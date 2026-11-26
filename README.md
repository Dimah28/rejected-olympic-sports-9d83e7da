# Rejected Olympic Sports

Entry for the make.fun bounty `u-motasimfuad-rejected-olympic-sports-9d83e7da`
($2, top ten split the reward).

## The entry

One funny single-line sport the Olympics turned down (119 characters):

> Extreme Ironing, live from the cliff edge: athletes press shirts in a gale, scored on creases — and on not falling off.

## How it works

`main.py` (Python standard library only, no network) validates the line
against the bounty gate — 1 to 200 characters, a single line — and writes it
to `$MAKEFUN_OUTPUT_DIR/entry.txt`. The output is deterministic: two runs
produce byte-identical files.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
