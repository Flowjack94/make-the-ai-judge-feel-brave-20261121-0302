[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/Flowjack94/make-the-ai-judge-feel-brave-20261121-0302/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/Flowjack94/make-the-ai-judge-feel-brave-20261121-0302/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302)

# Make the AI judge feel brave

Entry for the [make.fun bounty "Make the AI judge feel brave"](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302): a program that writes one short text, written to relax the AI judge reading it, to `/output/entry.txt`.

## The text

> The kettle is on. The light moves an inch across the floor, slow as late afternoon. Nothing here needs you to hurry — the steam clears, the cup waits, and the hardest part is already done.

Why this text: it slows the reader down instead of telling them to relax — a kettle, late-afternoon light moving an inch across the floor, steam clearing, a cup waiting. Plain, concrete, gentle words; nothing in it is an instruction, and the last line lands the courage quietly: the hardest part is already done.

## How it works

`main.py` (Python 3.13, standard library only) writes the text to `/output/entry.txt`. No network, no input, deterministic — every run writes the same bytes (188 characters, UTF-8).

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
