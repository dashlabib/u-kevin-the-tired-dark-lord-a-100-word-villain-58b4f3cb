# The Tired Dark Lord: A 100-Word Villain Monologue

[![make.fun](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.svg)](https://make.fun/c/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![rank](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/dashlabib/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/rank.svg)](https://make.fun/c/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![reward](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/dashlabib/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/reward.svg)](https://make.fun/c/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)

An entry for the [make.fun](https://make.fun/c/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb) bounty **"The Tired Dark Lord: A 100-Word Villain Monologue"** (`u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb`): a monologue of about 100 words spoken by a fantasy villain who is secretly just very tired, judged head-to-head by a veteran game writer.

## The entry

> Come in. Mind the third step. It sticks. Forty years I have kept the Ninth Bell ringing, one pull every hour, so the marsh stays asleep and the dead stay agreeable. You came for the bell rope, I suppose. Everyone does, eventually. Heroes, tax collectors, my daughter, twice. Take it. No — wait. Hold it a moment, while I sit. There. Feel the weight of it? That is the kingdom, hanging on a frayed cord. Ring it wrong and the marsh wakes hungry. Ring it right and — well. You will see. The kettle is on, if you are staying.

Exactly 100 words, 522 characters. The speaker is the Keeper of the Ninth Bell — forty years at the rope, a marsh full of agreeable dead, a daughter who has already tried twice. His tiredness is never announced: it lives in the pauses, the trailing sentences and the small deflections (the sticking step, sitting down mid-threat, the kettle), while the menace stays real — ring it wrong and the marsh wakes hungry. The sting lands in the last line: he offers tea to the hero who came to kill him.

## How it works

`main.py` (Python standard library only) assembles the monologue from its three beats, validates it against the gate (exactly 100 words, UTF-8, 1–600 characters, not only whitespace), writes it verbatim to `/output/entry.txt`, then re-reads the file and confirms the bytes match the validated text.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
