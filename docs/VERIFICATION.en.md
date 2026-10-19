# Verification

[日本語](VERIFICATION.md) ｜ **English**

## 1. Telegram 1 against the printed text
- **Print**: 『護國軍紀事』 no. 5 (1916), 「軍政府歡迎黃克強電」 (107 characters).
  - The print was identified by the prior repository saberwatchmanga/sun-circle-cipher-1916.
  - The comparison used that repository's manual transliteration. I did not reread the image of the print myself.
  - The printed text is not included in this repository. See [SOURCES.md](../SOURCES.md#english).
- **Method**: the characters of the first 107 decoded groups of Telegram 1 were aligned with the 107 printed characters using Python's difflib.SequenceMatcher, and the matching characters were counted.

| Transcription | Characters matching the print |
|---|---|
| The romaji read as written (`data/romaji_raw.txt`) | 26 / 107 (note) |
| Final table (`data/groups.csv`) | 102 / 107 |

(Note) Read as written, the hi at the start of word 46 (hiuchitaka) joins the c at the end of the previous word to form chi (チ). One kana is lost and every later group shifts. My transcription before the correction (which misread this word as huuchitaka) matched 40 characters.

Breakdown of the final table (the 107 groups of Telegram 1):

| Category | Groups | Matching the print |
|---|---|---|
| Read by the formula as written | 59 | 54 |
| Corrected reading | 43 | 43 |
| Filled from the print | 5 | 5 (filled with the printed characters, so they match by definition) |

The print differs in these 4 places. The 5 groups on the telegram side (28, 41–43, 57) are all read by the formula as written.

| Group | Telegram | Print | Interpretation |
|---|---|---|---|
| between 9 and 10 | (none) | 我 | only in the print |
| 28 | 慮 (1982) | 憂 (1992) | codes differ in the tens digit; cannot tell a transmission error from an editorial change |
| 41–43 | 提挈公 | 教言 | different wording |
| 57 | 查 | 察 | different wording |

**Caution**: that all 43 "corrected reading" groups match the print does not independently show the accuracy of the corrections, since some corrections in Telegram 1 were made with the print available. The closest to an independent check is the uncorrected groups: 54 of 59 match the print, and the remaining 5 characters are the wording differences above.

## 2. Checking the transcription (independent transcriptions by another AI)
The romaji was transcribed from the images by Claude. No human checked it letter by letter. Instead, it was checked as follows (19 October 2026).

- **Method**
  - OpenAI Codex (model gpt-6.1-sol) was given only the images of frames 0076–0078 and asked for a literal transcription, three separate times.
  - It was not shown my transcription or the prior repository's. In all three runs there were no file reads or command executions (confirmed in the run logs).
  - The three results were combined by majority vote, word by word.
  - The three transcriptions and the prompt are in `second/`. Letter agreement with the corrected `data/romaji_raw.txt` is 94.0%, 94.3% and 94.2% (`src/second.py`, [METHOD.en.md](METHOD.en.md)).

- **Agreement by word** (126 words)

| Codex results | Words |
|---|---|
| all 3 the same | 60 |
| 2 the same | 55 |
| all different | 11 |

- **Differences by letter** (1,266 letters, counted on my transcription before correction, at the time of the check)

| Compared | Letters that differ |
|---|---|
| my transcription vs the prior repository's | 21 |
| my transcription vs each Codex run | 81 / 77 / 77 |
| the prior repository's vs each Codex run | 85 / 82 / 86 |

- **The 42 words where the Codex majority differed from my transcription**
  - For 5 words, after rechecking the images, I judged that I had misread them, and corrected `data/romaji_raw.txt`:
    - 46 huuchitaka → hiuchitaka
    - 58 nikochitak → rikochitak
    - 63 echiuashit → echinashit
    - 96 takaonomie → takaononie
    - 116 esatefumika → esatefmika
  - For 4 of these (58, 63, 96, 116), the prior repository's transcription also agreed with the Codex majority.
  - 46, 58 and 96 now have the same spelling I had previously reached by correction, so they were removed from the list of corrections.
  - For 63 and 116 the literal spelling changed, so the readings used for decoding were moved into the list of corrections.
  - For 121 (wakataekat), I confirmed on the image a small o written above the a, and added it to the grounds of the correction (wakatoekat).
  - For the remaining 36 words, applying the Codex reading gave the following results, so I kept my reading:

| Result of applying the Codex reading | Words |
|---|---|
| later groups shift | 13 |
| groups that break the rules appear | 7 |
| characters that matched the print change (e.g. 鑒奉→鑤克, 光→儕) | 4 |
| characters that make no sense in Telegram 2 (e.g. 馮段→馬段, 第四→笫四) | 11 |
| no change in characters (in the section filled from the print) | 1 |

- **Limits**
  - The prior repository also transcribed mainly with Codex, so agreement between Codex and the prior repository is not fully independent support.
  - A single Codex transcription has many discrepancies. I judged a word to be my misreading only when I agreed after rechecking the image.
  - This check compares AIs with each other and does not replace a human check.

## 3. The second copy of the cipher text (JACAR B03050731100)
### The copy
- Japanese Foreign Ministry records 「袁世凱帝制計画一件（極秘）／反袁動乱及各地状況」, vol. 15, item "1 大正5年4月29日から大正5年5月22日" (JACAR B03050731100), images 24–26.
- Consul Ōta (太田) at Zhaoqing to Foreign Minister Ishii, **telegram no. 42** (sent 21 May 1916, received 22 May). It forwards the telegram to Huang Xing at Cen Chunxuan's request, and after the cover note comes "（以下支那側暗號）" with the full romaji cipher text (42 lines, 126 words).
- It is a copy of the same telegram, separate from frames 0076–0078 (`data/romaji_raw.txt`). Its transcription is `data/romaji_copy2.txt` (read from the images by Claude; no human checked it letter by letter).

### Summary in the cover note (my reading)
- The telegram consists of two telegrams.
- The first is from Cen Chunxuan together with the governors and commanders of Yunnan, Guizhou, Guangdong/Guangxi and Zhejiang, to Huang Xing. It thanks him for working together with them and says that, since he advocated the republic, is rich in strategy and has studied the situation of the powers, they will rely on his guidance in domestic and foreign affairs.
- The second is from Li Genyuan and others to Huang Xing. It states that they will soon organize the Xiehe army and enter Hunan and Jiangxi.

**What this shows**
- That both telegrams are dated 20 May 1916 (哿) is confirmed by Japanese records (section 6).
- That Li Genyuan was among the senders of Telegram 2 is confirmed by contemporary Japanese records.
- The summary agrees with this decipherment (Telegram 1 as in the print; 「協和軍旬內可齊，卽由韶入贑」 in Telegram 2).

### Comparing the romaji
The two copies were compared word by word. Even the superscript additions (at°akitets, wakat°ekat) are the same, so they are copies of the same text.

| Result | Words |
|---|---|
| same spelling in both copies | 114 |
| different spelling | 12 |

The 12 differing words:

| Type | Words |
|---|---|
| the spelling corrected in this decipherment is written as such in the second copy | 17 noheenihek (短・適), 43 hifuketaha (唐), 52 aitataitek (光), 121 wakatoekat (情), 123 hemukufunu (羣) |
| partly agrees with this decipherment's correction | 20 kotoakushoh (final h), 35 usawakteae (te), 45 ietoriasac (ie), 108 eyuniheiso (initial e and h) |
| applying the second copy's spelling makes the group unreadable | 5 kahakaasei, 34 sakaosokik, 57 coteriatsu (possibly my misreading; not checked) |

- Of the 40 corrected words, 5 have their corrected spelling independently supported by the second copy.
- For 30, the second copy has the same corrupted spelling as the transcription of frames 0076–0078. The corruption probably arose before the copies were made, at transmission.
- In the sections filled from the print (groups 48–52 and 58 of Telegram 1) and the 4 inferred groups (164, 211, 223, 225), the second copy has the same spelling and gives no new reading.

## 4. Confirming the signatures with Huang Xing's reply
- Decoding the first 8 words of the cipher text of Huang Xing's reply (JACAR B03050731500) with the formula gives 「隱印崧詔鬯行諸兄鑒正寄函」.
- This matches the opening of 「致肇慶軍務院電」 in 『近代史資料』 no. 50, p.123.
- Reproduced by `test_huang_reply_addressees` in `tests/test_formula.py`.

### The full text of the reply
- **Method**: the full cipher text of the reply (31 words; romaji from Tomokiyo's page) was decoded with the formula. Only the following two corrections, both given in Tomokiyo's article, were applied:
  - "O HI" can be corrected to "CHI" (KONUOHIKE → KONUCHIKE). Without this, every group from 35 on shifts.
  - YE in this romaji is read as エ in the 2nd and 3rd positions (the 2nd kana can only be ア–オ or カ–コ).
- **Result**: all 46 groups read.

  > 隱印崧詔鬯行諸兄鑒正寄函間適接哿電敬悉一切護國軍能速入湘贑甚好行嚴何日東渡望速啓行先電示興徑

  Reproduced by `test_huang_reply_full_text` in `tests/test_formula.py`.
- **Three witnesses compared**

| Place | Decoded from the cipher text | Print in 『近代史資料』 | Contemporary Japanese copy (transliteration on Bourdeau's page) |
|---|---|---|---|
| 4th and 5th addressees | 詔・鬯 | 詔・鬯 | 誥・邕 |
| opening | 正寄函間 | 正寄函間 | 正發書 (in the paraphrase on the same page, 「正發書翰之際」) |
| 護國軍… | 能**速**入湘贑 | 能入湘贛 (no 速) | 能**速**入湘贛 |

- **What this shows**
  - For the addressees 詔・鬯 and the opening 寄函, the print is correct, and the Japanese copy's 誥・邕 and 發書 appear to be copying errors. This confirms the addressees 「隱印崧詔鬯行」 from the side of the original telegram.
  - 速 is in both the cipher text and the Japanese copy, so the print appears to have dropped it. That 速 is present was already known from Bourdeau's page.
- **Caution**: only Tomokiyo's romaji and his own corrections were used, so this is not a new decipherment. I did not recheck the romaji against the image of the cipher text.

## 5. Reproducing the formula
`tests/test_formula.py` checks the following:
- For codes 1–9199, encoding and decoding agree.
  - Since the 1st-kana table has 46 characters, codes up to 9199 can be represented.
  - For the handling of multiples of 200, see [OPEN.md](OPEN.en.md).
- The kana and characters of 15 groups from Tomokiyo's list (一 = アアホ, 印 = タウホ, 哿 = タカス, etc.) are reproduced by the formula and the Unihan table.
- `data/groups.csv` is identical to the table regenerated from the transcription and the list of corrections.
- The codes in the table agree with both the kana and the characters.
- The second copy has 126 words, 12 of which differ, and the 5 words with corrected spellings are written as such in it.

How to run:

```
python3 -m unittest discover -s tests
```

## 6. Date
In the rhyme-day system, 删 means the 15th and 哿 the 20th. The Military Affairs Council was established on 8 May 1916. Huang Xing's reply is dated the 25th and answers Telegram 2. In addition, the same telegram was sent to the Foreign Ministry by Consul Ōta at Zhaoqing on 21 May 1916 (section 3). The two telegrams were therefore sent on **20 May 1916**.
