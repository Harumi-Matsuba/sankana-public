# Decipherment of the 1916 three-kana telegrams (JACAR B03050089100)

[日本語版 README](README.md)

| | |
|---|---|
| Status | **Full reading** (both telegrams, all 229 groups read; 4 groups of Telegram 2 are inferred). Grounds: control by comparison with the print (102 of 107 characters) / independent second transcription 94.6% letter agreement (≥ 85%) / share given a value 224/229 groups = 97.8% (excluding the 5 groups filled from the print, including the 4 inferred; ≥ 95%) / calibration: 54/59 uncorrected groups = 91.5% (≥ 90%) |
| Relation to prior work | Telegram 1 is **reproduced**: the formula is Satoshi Tomokiyo's, and its printed plaintext was first identified by saberwatchmanga/sun-circle-cipher-1916. Much of Telegram 2 was also already read, character by character, on the Japanese worksheets of 1916 (83 characters; published by Tomokiyo and saberwatchmanga). Four of the six senders are identified, as the addressees of the reply, in a footnote of 『近代史資料』 no. 50, and a list of six is proposed as a hypothesis by saberwatchmanga. This work adds readings for groups left unresolved (10 groups) or not fitting the text in prior work, so that Telegram 2 reads as continuous text; a comparison with a second copy of the same cipher text (B03050731100); and the grounds for identifying the 4th and 5th senders as Wen Qun and Yang Yongtai (see "What this decipherment adds" below). A search for prior work by a checker other than the decipherer, trying to refute novelty, is in [docs/PRIOR_CHECK.en.md](docs/PRIOR_CHECK.en.md) (20 Oct 2026). This is not claimed as a first |
| Human checking | **No human has checked the transcription.** The romaji was transcribed by an AI (Claude) and only compared with transcriptions by another AI (Codex). Agreement between AIs is not a substitute for human checking |
| Figures | Independent second transcription (Codex, one run without seeing the first, in a fresh context after the first was corrected): 94.6% letter agreement / Control: the final table of Telegram 1 matches 102 of the 107 printed characters / Calibration: 54 of the 59 uncorrected groups match the print (the other 5 are textual differences). No key-shuffling control (no key is estimated in this system). Details in [docs/METHOD.en.md](docs/METHOD.en.md) |
| Use of AI | Transcription, converter, correction search, checks and documents by Claude (Claude Opus 5.5); second transcription by OpenAI Codex. The human directed the work and reviewed the results (see "Use of AI" below) |

This repository records a full reading of two cipher telegrams to Huang Xing (黄興), dated 20 May 1916. The Japanese Foreign Ministry copied them at the time. They are read here with the known conversion formula.
- **Source**: Japanese Foreign Ministry records, 特定人ノ発受郵便物取調 vol. 3, JACAR B03050089100.
  - Frames 0076–0078: the romanized cipher text.
  - Frames 0079–0081: worksheets by Japanese analysts of the time.
- **System**: the "three-kana code". Each Chinese character becomes its 4-digit standard telegraph code. Each code becomes three kana, and the kana are sent in romaji.
- **Conversion formula**: identified by Satoshi Tomokiyo (Cryptiana).

The documents in `docs/` have English versions (`*.en.md`). `SOURCES.md` and `data/README.md` are bilingual: Japanese first, then English (use the "English" link at the top of each file). The free-text columns of `data/corrections.csv` and `data/worksheet.csv` have English translations.

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
  - The final table matches 102 of the 107 printed characters (see [docs/VERIFICATION.en.md](docs/VERIFICATION.en.md)).
- **Telegram 2**: from six people at Zhaoqing (肇慶) to Huang Xing. They are proposed to be Lin Hu 林虎, Li Genyuan 李根源, Cheng Zikai 程子楷, Wen Qun 文羣, Yang Yongtai 楊永泰 and Zhang Shizhao 章士釗.
  - No printed text has been found. This table is an independent reading from the formula.
  - The signatories were identified using the addressees 隱印崧詔鬯行. These come from the cipher text of Huang Xing's reply (JACAR B03050731500).
- Inferred readings, medium-certainty corrections and the prior repository's caveats are discussed in [docs/OPEN.en.md](docs/OPEN.en.md).

## What this decipherment adds
**Prior work this relies on**
- The three-kana conversion formula and partial readings from the worksheets: Satoshi Tomokiyo.
- The plaintext of Telegram 1 (identification of the print): the prior repository saberwatchmanga/sun-circle-cipher-1916.

**What this work adds**
1. **A complete reading of Telegram 2**
   - The 1916 worksheets already read 83 characters of Telegram 2 (as transcribed on Tomokiyo's page). The prior repository left 10 groups of Telegram 2 unresolved, and in other groups gave only the character produced by the formula, which does not fit the text (e.g. 0274, watuno, kutena, tathe, caose, 6381 and akuso).
   - This work proposes 僅・恐・發・卿・兵・贑・代・謀・舊部・楷・粤・出 for them, and the whole telegram reads as continuous text.
   - Inferred and medium-certainty readings are listed, with their grounds, in `data/corrections.csv` and [docs/OPEN.en.md](docs/OPEN.en.md).
2. **Identification of the six signatories**
   - Decoding the cipher text of Huang Xing's reply (B03050731500) with the formula gives the addressees 隱印崧詔鬯行. This does not depend on any handwritten copy, and it matches the printed text in 『近代史資料』 no. 50.
   - The Japanese handwritten translation 隱印崧蕘邕行 appears to be a copying error. It is quoted in D. Bourdeau's repository dbourdeau/cyphersolver, targets/sunyatsen/HUANG_NOTES.md.
   - Matching these characters with courtesy names (字) and art names (号) gives the six signatories above. Four of them (Lin Hu, Li Genyuan, Cheng Zikai, Zhang Shizhao) agree with the footnote in 『近代史資料』, and a list of six is already proposed as a hypothesis in the prior repository. What this work adds is the check against the cipher text of the reply and the staff lists, and the grounds for the 4th and 5th. All six courtesy or art names (隱青, 印泉, 崧生, 詔雲, 暢卿, 行嚴) are also confirmed in the 1916 staff lists of 『軍務院考實』. There, Yang Yongtai's courtesy name is written 暢卿, a homophone (chàng) of the addressee 鬯.
   - The editorial footnote in 『近代史資料』 gives the 4th and 5th addressees as Zeng Qiheng 曾其衡 and Zhao Zhengping 趙正平. However, Zhao Zhengping's courtesy name is 厚生 (also so in the 1916 staff lists), which does not match 鬯. The kana for 衡 do not match the signature either.
3. **What Telegram 2 says**: the senders' account and plans as of 20 May 1916. These are statements in the telegram, not verified facts.
   - The Military Affairs Council exists only in name; its committees and delegates' meetings have not yet been organized.
   - Li Liejun's (李烈鈞) Xiehe army (協和軍) will be assembled within ten days and enter Jiangxi via Shaozhou (韶州). Li Liejun's troops did in fact fight at Shaozhou on 19 June.
   - Lin Hu will become commander of the 4th Division, gather about 10,000 of his former troops and march into Jiangxi (the telegram reads 虎任第四師長，收集舊部約萬，亦卽出贑).
     - 師 and 舊部 are read after correcting the spelling; their certainty is medium.
     - The title "4th Division commander" does not match later records. In the staff lists of 『軍務院考實』, Lin Hu is commander-in-chief of the 6th National Protection Army, and the 4th Division commander in Li Liejun's army is Fang Shengtao 方聲濤 (see [docs/OPEN.en.md](docs/OPEN.en.md)).
   - Zhang Shizhao will travel to Japan to report in person.
   - Who "潤輔" near the beginning refers to is not settled. The staff lists name a resident delegate in Japan, Zhang Xiaozhun 張孝準 (courtesy name 潤農), who fits the context, but the kana do not match (see [docs/OPEN.en.md](docs/OPEN.en.md)).
4. **A second copy of the cipher text**
   - JACAR B03050731100 contains a copy of the same telegram, sent to the Foreign Ministry on 21 May 1916 by Consul Ōta (太田) at Zhaoqing. Its cover note summarizes both telegrams.
   - This confirms, from contemporary Japanese records, the date (20 May) and that Li Genyuan was among the senders of Telegram 2.
   - Comparing the two copies, the corrected spelling of 5 words (at 短・適・唐・光・情・羣) appears as such in the second copy (see [docs/VERIFICATION.en.md](docs/VERIFICATION.en.md)).
5. **Minor points**
   - The formula can represent telegraph codes only up to 9199. Its handling of multiples of 200 cannot be checked against actual telegrams.
   - The pencil note on worksheet frame 0080 reads 詔, not 韶.
   - The transcription was cross-checked against three blind transcriptions by another AI (see [docs/VERIFICATION.en.md](docs/VERIFICATION.en.md)).

## Contents
| Path | Contents |
|---|---|
| `data/romaji_raw.txt` | Literal transcription of the romaji cipher text (no corrections) |
| `data/romaji_copy2.txt` | Transcription of a second copy of the same cipher text (JACAR B03050731100) |
| `data/corrections.csv` | List of corrections (40 words, 9 groups): original spelling, correction, reason, certainty, grounds |
| `data/groups.csv` | Table of all 229 groups (kana, telegraph code, character, category), generated by `src/build_groups.py` |
| `data/worksheet.csv` | Japanese analysts' worksheet notes compared with this reading (26 items) |
| `data/ctc_kTaiwanTelegraph.tsv` | Telegraph code → character table, extracted from Unicode Unihan |
| `src/` | Converter and tools (`kana.py`, `second.py`, `build_groups.py`, `check.py`, `fix.py`, `beam.py`, `lm.py`, `build_ctc.py`) |
| `tests/` | Tests of the formula, the reply, and table consistency |
| `docs/` | Method, figures, use of AI and limits (METHOD), decipherment record (DECIPHERMENT), verification (VERIFICATION), open questions (OPEN). English versions are `*.en.md` |
| `second/` | Blind transcriptions by Codex (the list of words corrected and not corrected after the cross-check is `crosscheck_decisions.tsv`): the independent second transcription (`codex_run4.txt`) and the three cross-check runs used to correct the first (`codex_run1–3.txt`). `*_raw.txt` is the unedited output, `*_events.jsonl` the run log; the prompt is `codex_prompt.txt`. Agreement is computed by `src/second.py` |
| `data/README.md` | Meaning of the files, columns and categories in `data/`. Japanese and English |

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

See [SOURCES.md](SOURCES.md#english) for full references.

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

  Disagreements were rechecked against the images, and 5 words were corrected (see [docs/VERIFICATION.en.md](docs/VERIFICATION.en.md)). Because this comparison was used for the corrections, it is not reported as an independent figure. After the corrections, Codex read the images once more in a fresh context without seeing any answer (the independent second transcription); letter agreement was 94.6% (see [docs/METHOD.en.md](docs/METHOD.en.md)).
- Parts of the work were carried out by the AI continuously, without a person checking each step.
- **Models used**
  - Claude: Claude Opus 5.5 (`claude-opus-5-5`). The three helper agents used during the work ran on the same model.
  - Transcription cross-check: OpenAI Codex (`codex-cli 0.163.0-alpha.10.2`, model `gpt-6.1-sol`).
  - Independent second transcription: the same Codex CLI, default model (the model name does not appear in the run log).
- AI readings and judgments can be wrong. The grounds and certainty of each correction are given in `data/corrections.csv` and [docs/OPEN.en.md](docs/OPEN.en.md). Please check against the original JACAR images.

## License
- Code (`src/`, `tests/`): MIT
- Documents and data (`docs/`, the self-made parts of `data/`, the README files): CC BY 4.0
- `data/ctc_kTaiwanTelegraph.tsv`: under the Unicode License

See [LICENSE](LICENSE) for details.
