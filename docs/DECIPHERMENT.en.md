# Decipherment record

[日本語](DECIPHERMENT.md) ｜ **English**

## Sources
- Japanese Foreign Ministry records, 各国内政関係雑纂／支那ノ部／革命党関係（亡命者ヲ含ム）／特定人ノ発受郵便物取調, vol. 3 (JACAR B03050089100)
  - Frames 0076–0078: the romanized cipher text (5 sheets, 126 words)
  - Frames 0079–0081: worksheets by Japanese analysts of the time (the cipher text rewritten in katakana, with some kanji notes)
- Images are not included in this repository; they are referred to by frame number.

- A second copy of the same telegram is in JACAR B03050731100, images 24–26 (Consul Ōta at Zhaoqing, telegram no. 42, sent 21 May 1916). Its cover note summarizes both telegrams. The comparison is in [VERIFICATION.md](VERIFICATION.en.md), section 3.

## System: the three-kana code
Each Chinese character is turned into its 4-digit standard telegraph code, the code is replaced by three kana, and the kana are sent in romaji.
The formula from code to three kana was identified by Satoshi Tomokiyo (Cryptiana) (see [SOURCES.md](../SOURCES.md#english)).

```
kana 1 = S1[c // 200]             S1 = アカサタナハマヤラワイキシチニヒミリヰウクスツヌフムユルエケセテネヘメレヱオコソトノホモヨロ
kana 2 = S2[(c - 1) % 10]         S2 = アイウエオカキクケコ
kana 3 = S3[((c - 1) // 10) % 20] S3 = ホヘフヒハノネヌニナトテツチタソセスシサ
```

This decipherment applies the formula in reverse (`src/kana.py`):
- split the romaji into kana and group them in threes;
- turn each group back into a telegraph code, and the code into a character with Unicode Unihan kTaiwanTelegraph.

The formula gives strong constraints:
- the 2nd kana can only be ア–オ or カ–コ;
- the 3rd kana can only be one of the 20 kana of the サ, タ, ナ and ハ rows.

These constraints were used to find and repair corrupted places.

## Procedure
1. **Transcription of the romaji** (`data/romaji_raw.txt`)
   - Copied letter by letter from the images, with no corrections.
   - Romaji cannot distinguish エ from ヱ, or イ from ヰ.
2. **Re-reading corrupted words** (`data/corrections.csv`)
   - For groups that break the rules or make no sense, the spelling of the word was rechecked on the images.
   - Common confusions:
     - cursive h/k, wa/ha, n/u, a/o, m/n, ss/sh
     - エ/ヱ
   - 40 of the 126 words were corrected. The reason, certainty and grounds of each are given one per line in `corrections.csv`.
3. **Groups that cannot be read from the text**
   - 5 groups of Telegram 1 were filled from the printed text.
   - 4 groups of Telegram 2 were inferred from context and Huang Xing's reply.
4. **Building the table**: `python3 src/build_groups.py` builds the table of all 229 groups, `data/groups.csv`.

## Results
### Telegram 1 (groups 0–107)
From the ten members of the Military Affairs Council (軍務院) to Huang Xing, welcoming his arrival in Japan and asking for his guidance.

> 黃克強先生鑒奉删電知公抵日歡躍逾恆堯等碌碌庸才勉起討賊正慮綆短適逢公歸願承不遺俯賜提挈公首倡共和富有方略各國情勢考查復殷將來內政外交諸賴指導大局所繫惟公圖之唐繼堯岑春煊梁啓超劉顯世陸榮廷龍濟光呂公望蔡鍔李烈鈞陳炳焜哿

- Its plaintext was printed in 1916 in 『護國軍紀事』 no. 5 as 「軍政府歡迎黃克強電」. The print was identified by the prior repository.
- **This telegram is not a new decipherment; it is treated as a check against the print.** The comparison is in [VERIFICATION.md](VERIFICATION.en.md).
- The 5 characters 富・有・方・各・復 cannot be read from the spelling of the text and were filled from the print.

### Telegram 2 (groups 108–228)
From six people at Zhaoqing (肇慶) to Huang Xing, proposed to be Lin Hu 林虎, Li Genyuan 李根源, Cheng Zikai 程子楷, Wen Qun 文羣, Yang Yongtai 楊永泰 and Zhang Shizhao 章士釗. That Li Genyuan was among the senders is also confirmed by the cover note of Consul Ōta's telegram ("李根源等ヨリ黄興ニ宛テタルモノ").

> 公抵日喜甚潤輔當告公近形以定進行方略軍務院僅擁虛名委員代表等會皆未組織協和軍旬內可齊卽由韶入贑非俟幹卿協和兵入湘贑吾人恐難發言馮段調停此間暫置代理參謀事源專任之虎任第四師長收集舊部約萬亦卽出贑楷調粤中湘軍卽出湘釗擬來東面達近情虎源楷羣泰釗哿（オワリ）

- No printed text of this telegram has been found. The prior repository also discusses points and hypotheses about it; this table is a separate, independent reading from the formula.
- Content (summary):
  - The Military Affairs Council exists only in name; its committees and delegates' meetings have not yet been organized.
  - The Xiehe army (協和軍; Li Liejun 李烈鈞, whose courtesy name is 協和) will be assembled within ten days and enter Jiangxi via Shaozhou.
  - Lin Hu, as commander of the 4th Division, will gather about 10,000 of his former troops and march into Jiangxi.
  - Zhang Shizhao will travel to Japan to report in person.
- 4 groups rely on inference:
  - 164 贑
  - 211 出
  - 223 楷
  - 225 泰

  Some corrections are also rated "medium" in certainty. Both are discussed in [OPEN.md](OPEN.en.md).

### Signatures and Huang Xing's reply
Huang Xing's reply (25 May 1916, JACAR B03050731500) was sent in the same three-kana code.
- Decoding its cipher text (romaji from Tomokiyo's page) with the formula gives the opening 「隱印崧詔鬯行諸兄鑒正寄函」.
- This matches the opening of 「致肇慶軍務院電」 in 『近代史資料』 no. 50, p.123 (隱、印、崧、詔、鬯、行諸兄鑒). The check is reproduced in `tests/test_formula.py`.
- Reading the six addressee characters as courtesy names (字) or art names (号), they correspond to the six signature characters of Telegram 2:

| Addressee in the reply | Person (courtesy / art name) | Signature in Telegram 2 | Status of the signature group |
|---|---|---|---|
| 隱 | Lin Hu 林虎 (隱青) | 虎 | read by the formula as written |
| 印 | Li Genyuan 李根源 (印泉) | 源 | corrected reading |
| 崧 | Cheng Zikai 程子楷 (崧生) | 楷 | inferred (text ヌクヘ; differs from ニクヘ = 楷 only in the 1st kana) |
| 詔 | Wen Qun 文羣 (art name 詔雲) | 羣 | corrected reading (text nukufu read as mukufu) |
| 鬯 | Yang Yongtai 楊永泰 (鬯卿) | 泰 | inferred (text ヌアタ; differs from ヒアタ = 泰 only in the 1st kana) |
| 行 | Zhang Shizhao 章士釗 (行嚴) | 釗 | read by the formula as written |

The courtesy and art names follow Wikipedia. All six were also confirmed in the staff lists of the 1916 『軍務院考實』:
- Vol. 1: Lin Hu (隱青), Li Genyuan (印泉), Zhang Shizhao (行嚴), Cheng Zikai (崧生) (PDF pp. 250, 254, 259)
- Vol. 2 (appendix 『兩廣都司令部考實』): Wen Qun (詔雲), Yang Yongtai (暢卿) (PDF pp. 230, 236, 237). In the staff list, Yang Yongtai's courtesy name is written 暢卿, a different character with the same sound as the addressee 鬯. Addressees of a reply are not necessarily the signers of Telegram 2; this is discussed in [OPEN.md](OPEN.en.md).

## Relation to the Japanese analysts' worksheets
- `data/worksheet.csv` lists, in my reading, 26 kanji notes on the worksheets (frames 0079–0081) that relate to this decipherment.
  - Agree with this decipherment: 21
  - Disagree: 5
- The notes include contemporary guesses, so they are not treated as independent evidence. Where they are cited as grounds for a correction, they are supporting evidence only.
