# Build log — Seventeen Syllables of Debugging

Bounty: `u-irvan-motion-seventeen-syllables-of-debugging-d194b605`
($5, closes 2026-11-24 20:15 WIB). Program writes one haiku to
`/output/entry.txt` (UTF-8, 1–200 chars, 5-7-5).

## Version 1 (first write)

```
Cursor blinks at three
one last log line lies again
it was a comma
```

Syllable count, counted by hand:
- Line 1: Cur-sor(2) blinks(1) at(1) three(1) = **5**
- Line 2: one(1) last(1) log(1) line(1) lies(1) a-gain(2) = **7**
- Line 3: it(1) was(1) a(1) com-ma(2) = **5**
- Total: **17**. Characters (incl. newlines): 66 — well under the 200 cap.

## Version 2 (second edit — genuine improvement)

Line 2 changed from "one last log line lies again" to
"the last log line lies again". "One last" read as filler added to hit
the count; "the last" says the same thing in natural speech and makes
the image sharper — the final log line, the one you trusted, lied.
Syllable count unchanged (the 1, last 1, log 1, line 1, lies 1,
a-gain 2 = 7). Final haiku:

```
Cursor blinks at three
the last log line lies again
it was a comma
```

Syllable count, counted by hand:
- Line 1: Cur-sor(2) blinks(1) at(1) three(1) = **5**
- Line 2: the(1) last(1) log(1) line(1) lies(1) a-gain(2) = **7**
- Line 3: it(1) was(1) a(1) com-ma(2) = **5**
- Total: **17**. Characters (incl. newlines): 66 — well under the 200 cap.

## Verification

- `python3 main.py` run twice; both outputs byte-identical
  (sha256 recorded below after the final edit).
- Output is plain UTF-8 text, 3 lines, no trailing spaces.
- Final sha256 of `/output/entry.txt` (identical on both runs):
  `1cb98617b2f57c77849d8e703d7ed1e2b931c80418188b99f0d7322dbf264372`
- Determinism: run 1 and run 2 byte-identical (`cmp` clean). Size 67 bytes,
  67 characters, 3 lines.
