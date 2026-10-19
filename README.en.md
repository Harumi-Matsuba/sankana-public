# Decipherment of the 1916 three-kana telegrams (JACAR B03050089100)

[日本語版 README](README.md)

This repository records a full reading of two cipher telegrams to Huang Xing (黄興), probably dated 20 May 1916. The Japanese Foreign Ministry copied them at the time. They are read here with the known conversion formula.
- **Source**: Japanese Foreign Ministry records, 特定人ノ発受郵便物取調 vol. 3, JACAR B03050089100.
  - Frames 0076–0078: the romanized cipher text.
  - Frames 0079–0081: worksheets by Japanese analysts of the time.
- **System**: the "three-kana code". Each Chinese character becomes its 4-digit standard telegraph code. Each code becomes three kana, and the kana are sent in romaji.
- **Conversion formula**: identified by Satoshi Tomokiyo (Cryptiana).

The detailed documents in `docs/` and the notes in `data/` are written in Japanese. This English README summarizes them.

## Status
All 229 groups are tabulated in `data/groups.csv`.

| Category | Telegram 1 (groups 0–107) | Telegram 2 (groups 108–228) |
|---|---|---|
| Read by the formula as written | 60 | 73 |
| Read after correcting a word's spelling | 43 | 43 |
| Filled from the printed text | 5 | 0 |
| Inferred | 0 | 4 |
| End marker (オワリ, "end") | 0 | 1 |

- **Telegram 1**: from the ten members of the Military Affairs Council (軍務院, Junwuyuan) to Huang Xing.
  - Its plaintext was printed in 1916 in 『護國軍紀事』 no. 5. The print was identified by the prior repository listed below. **This is not a new decipherment; it is a check against the print.**
  - The final table matches 102 of the 107 printed characters (see `docs/VERIFICATION.md`).
- **Telegram 2**: from six people at Zhaoqing (肇慶) to Huang Xing. They are proposed to be Lin Hu 林虎, Li Genyuan 李根源, Cheng Zikai 程子楷, Wen Qun 文羣, Yang Yongtai 楊永泰 and Zhang Shizhao 章士釗.
  - No printed text has been found. This table is an independent reading from the formula.
  - The signatories were identified using the addressees 隱印崧詔鬯行. These come from the cipher text of Huang Xing's reply (JACAR B03050731500).
- Inferred readings, medium-certainty corrections and the prior repository's caveats are discussed in `docs/OPEN.md`.

## What is new in this decipherment
**Prior work this relies on**
- The three-kana conversion formula and partial readings from the worksheets: Satoshi Tomokiyo.
- The plaintext of Telegram 1 (identification of the print): the prior repository saberwatchmanga/sun-circle-cipher-1916.

**What this work adds**
1. **A complete reading of Telegram 2**
   - The prior repository left many groups of Telegram 2 blank, e.g. 0274, watuno, kutena, tathe, caose, 6381 and akuso.
   - This work proposes 僅・恐・發・卿・兵・贑・代・謀・舊部・楷・粤・出 for them, and the whole telegram reads as continuous text.
   - Inferred and medium-certainty readings are listed, with their grounds, in `data/corrections.csv` and `docs/OPEN.md`.
2. **Identification of the six signatories**
   - Decoding the cipher text of Huang Xing's reply (B03050731500) with the formula gives the addressees 隱印崧詔鬯行. This does not depend on any handwritten copy, and it matches the printed text in 『近代史資料』 no. 50.
   - The Japanese handwritten translation 隱印崧蕘邕行 appears to be a copying error. It is quoted in D. Bourdeau's repository dbourdeau/cyphersolver, targets/sunyatsen/HUANG_NOTES.md.
   - Matching these characters with courtesy names (字) and art names (号) gives the six signatories above. Four of these courtesy names (隱青, 印泉, 崧生, 行嚴) are also confirmed in the 1916 staff lists of 『軍務院考實』.
   - The editorial footnote in 『近代史資料』 gives the 4th and 5th addressees as Zeng Qiheng 曾其衡 and Zhao Zhengping 趙正平. However, Zhao Zhengping's courtesy name is 厚生, which does not match 鬯. The kana for 衡 do not match the signature either.
3. **Content of Telegram 2**: the situation on the Zhaoqing side as of 20 May 1916.
   - The Military Affairs Council exists only in name; its committees and delegates' meetings have not yet been organized.
   - Li Liejun's (李烈鈞) Xiehe army (協和軍) will be assembled within ten days and enter Jiangxi via Shaozhou (韶州). Li Liejun's troops did in fact fight at Shaozhou on 19 June.
   - Lin Hu will gather about 10,000 of his former troops and march into Jiangxi.
   - Zhang Shizhao will travel to Japan to report in person.
   - According to the staff lists in 『軍務院考實』, Li Liejun's army had a "4th Division" (commander: Fang Shengtao 方聲濤), and the Military Affairs Council had a resident delegate in Japan, Zhang Xiaozhun 張孝準 (courtesy name 潤農). These are clues to "虎任第四師長" and "潤輔" in the telegram, but neither is settled (see `docs/OPEN.md`).
4. **Minor points**
   - The formula can represent telegraph codes only up to 9199. Its handling of multiples of 200 cannot be checked against actual telegrams.
   - The pencil note on worksheet frame 0080 reads 詔, not 韶.
   - The transcription was cross-checked against three blind transcriptions by another AI (see `docs/VERIFICATION.md`).

## Contents
| Path | Contents |
|---|---|
| `data/romaji_raw.txt` | Literal transcription of the romaji cipher text (no corrections) |
| `data/corrections.csv` | List of corrections (40 words, 9 groups): original spelling, correction, reason, certainty, grounds |
| `data/groups.csv` | Table of all 229 groups (kana, telegraph code, character, category), generated by `src/build_groups.py` |
| `data/worksheet.csv` | Japanese analysts' worksheet notes compared with this reading (26 items) |
| `data/ctc_kTaiwanTelegraph.tsv` | Telegraph code → character table, extracted from Unicode Unihan |
| `src/` | Converter and tools (`kana.py`, `build_groups.py`, `check.py`, `fix.py`, `beam.py`, `lm.py`, `build_ctc.py`) |
| `tests/` | Tests of the formula, the reply, and table consistency |
| `docs/` | Decipherment record (DECIPHERMENT), verification (VERIFICATION), open questions (OPEN). In Japanese |

## Usage
Everything except `fix.py` and `beam.py` runs with the Python 3 standard library only.

```
python3 src/build_groups.py                      # builds data/groups.csv and outputs/romaji_corrected.txt
python3 src/check.py outputs/romaji_corrected.txt
python3 -m unittest discover -s tests
```

`fix.py` and `beam.py` use a frequency model to rank candidates. How to obtain its inputs is described at the top of `src/lm.py`; the inputs are not included in this repository.

## Prior work and credits
- **Satoshi Tomokiyo**, "Solution of Two Chinese Cipher Telegrams Archived in Japan (1916)" (Cryptiana)
  - Identified the three-kana conversion formula (added 23 September 2026).
  - Identified this telegram and its worksheets, and published partial readings.
  - This decipherment is built on his formula.
- **saberwatchmanga/sun-circle-cipher-1916** (GitHub)
  - A work record of 7–10 October 2026. It identified the print of Telegram 1.
  - It keeps a transcription that separates the source and worksheet layers, along with points and careful caveats about Telegram 2.
  - Comparing with its transcription revealed two errors in mine (groups 39 and 188), which I fixed after rechecking the images.
- **D. Bourdeau** (cyphersolver): survey of the telegrams in this file series.

See `SOURCES.md` for full references (in Japanese).

## Use of AI
- Most of this work was done by Claude (Claude Code), an AI by Anthropic:
  - transcribing the romaji from the images
  - writing the converter
  - searching for correction candidates
  - checking against historical sources
  - writing the documents
- The publisher directed the work and reviewed it.
- **How the transcription was made**: Claude read `data/romaji_raw.txt` letter by letter from enlarged JACAR images. The publisher did not check it letter by letter. Instead, it was compared with:
  - three blind transcriptions by another AI (OpenAI Codex), and
  - the prior repository's transcription.

  Disagreements were rechecked against the images, and 5 words were corrected (see `docs/VERIFICATION.md`).
- Parts of the work were run automatically until a goal was reached, using Claude Code's /goal feature.
- **Models used**
  - Claude: Claude Opus 5.5 (`claude-opus-5-5`). The three helper agents used during the work ran on the same model.
  - Transcription cross-check: OpenAI Codex (`codex-cli 0.163.0-alpha.10.2`, model `gpt-6.1-sol`).
- AI readings and judgments can be wrong. The grounds and certainty of each correction are given in `data/corrections.csv` and `docs/OPEN.md`. Please check against the original JACAR images.

## License
- Code (`src/`, `tests/`): MIT
- Documents and data (`docs/`, the self-made parts of `data/`, the README files): CC BY 4.0
- `data/ctc_kTaiwanTelegraph.tsv`: under the Unicode License

See [LICENSE](LICENSE) for details.
