# Method, figures, use of AI and limits

[日本語](METHOD.md) ｜ **English**

The full procedure is in [DECIPHERMENT.en.md](DECIPHERMENT.en.md) and the details of each check in [VERIFICATION.en.md](VERIFICATION.en.md). This document summarizes their main points and figures.

## 1. Method
1. **Transcription (first pass)**: Claude read the romaji letter by letter from enlarged images of JACAR B03050089100, frames 0076–0078 (`data/romaji_raw.txt`, 126 words, 1,265 letters).
2. **Conversion**: decoded with Satoshi Tomokiyo's formula (romaji → three kana → 4-digit telegraph code → character) (`src/kana.py`). Code → character uses kTaiwanTelegraph from Unicode Unihan.
3. **Corrections**: groups that break the rules or do not make sense were treated as garbled spellings; candidates were ranked and corrected (`data/corrections.csv`: 40 words and 9 groups, each with reason, certainty and grounds).
4. **Checks**: against the printed text (Telegram 1), a second copy of the cipher text, Huang Xing's reply, and the Japanese analysts' worksheets of the time.

## 2. Figures
| Item | Result | Where |
|---|---|---|
| Independent second transcription (another model, without seeing the first) | OpenAI Codex, one run (run 4, 20 Oct 2026), made in a fresh context after the first transcription had been corrected. Letter agreement with `data/romaji_raw.txt`: 94.6% (68 differing letters out of 1,265); 76 of 126 words spelled the same | `second/codex_run4.txt`, `src/second.py` |
| Cross-check record (the comparison used to correct the first transcription) | Codex, three runs (runs 1–3, 19 Oct 2026). Letter agreement with the corrected `romaji_raw.txt`: 94.0%, 94.3%, 94.2% (76, 72, 74 differing letters). By word: all three agree on 60, two on 55, all differ on 11. Of the 115 words with a majority reading, 78 equal `romaji_raw.txt` and 37 differ | `second/codex_run1–3.txt`, [VERIFICATION.en.md](VERIFICATION.en.md) §2 |
| Control (against plaintext) | The final table of Telegram 1 matches 102 of the 107 printed characters | [VERIFICATION.en.md](VERIFICATION.en.md) §1 |
| Calibration (only the part that does not depend on the answer) | Of the 59 groups read by the formula with no correction, 54 match the print. The other 5 are textual differences from the print (慮/憂, 提挈公/教言, 查/察) | same |
| Control (second copy) | 114 of 126 words are spelled the same in both copies. For 5 of the 40 corrected words, the corrected spelling is written as such in the second copy | [VERIFICATION.en.md](VERIFICATION.en.md) §3 |
| Control (reply) | Decoding the cipher text of Huang Xing's reply (Tomokiyo's romaji) with the same formula reads all 46 groups, and the addressees 隱印崧詔鬯行 match the print in 『近代史資料』 | [VERIFICATION.en.md](VERIFICATION.en.md) §4, `tests/` |

- **Why the cross-check record and the independent second transcription are kept apart**: all 42 words where the majority of Codex runs 1–3 differed from the first pass (at the time of the check) were rechecked on the images. 5 were judged to be misreadings in the first pass and corrected; for the other 37 the first reading was kept, because the Codex reading shifts the groups, breaks the rules, or no longer matches the print (see [VERIFICATION.en.md](VERIFICATION.en.md) §2). Since the first transcription was corrected after seeing this comparison, agreement with runs 1–3 is not an independent figure. A further run (run 4) was therefore made in a fresh context after the corrections, and its agreement is reported as the independent second transcription. All 5 corrected words are spelled as corrected in run 4 as well.
- **Caveat on calibration**: some of the 43 "corrected" groups of Telegram 1 were corrected while the print was available. Their agreement with the print is therefore not counted as calibration. Telegram 2 has no printed text and no calibration.
- No key-shuffling control (1000 runs) was done: the system is fixed by a published formula and no key was estimated. Comparisons with the plaintext (print), the second copy and the reply serve as controls instead.

## 3. Use of AI
- Claude (Anthropic, Claude Opus 5.5, `claude-opus-5-5`): transcription from the images, the converter, searching for correction candidates, checking against historical sources, and writing the documents. Three helper agents on the same model were used during the work. Parts of the work were run automatically until a goal was reached, using Claude Code's /goal feature.
- OpenAI Codex (`codex-cli 0.163.0-alpha.10.2`): three cross-check runs (runs 1–3, model `gpt-6.1-sol`) and one independent second transcription (run 4, default model; the model name does not appear in the run log). All four runs were given only the same five images and the same prompt (`second/codex_prompt.txt`), each in a separate run. Run 4 was started from an empty folder with `codex exec --ephemeral -s read-only` (the exact invocation of runs 1–3 was not recorded). The run logs (`second/codex_run*_events.jsonl`) show no file reads or commands. Where a row of the output was split into more than three words, neighbouring pieces were joined to make three (compare with `*_raw.txt`).
- The publisher (a human): directed the work and reviewed the results. **No human has checked the romaji transcription letter by letter.**

## 4. Limits
- Agreement between AI transcriptions is not a substitute for human checking. Codex also underlies the prior repository's transcription, so agreement between Codex and the prior repository is not independent support.
- Telegram 2 has no printed text; it is an independent reading from the formula and includes 4 inferred groups and some medium-certainty corrections (see [OPEN.en.md](OPEN.en.md)).
- The comparison with the print used the prior repository's manual transliteration; the print images were not re-read.
- The second copy (`data/romaji_copy2.txt`) was also transcribed by Claude, without a second transcription.
