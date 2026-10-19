# 検証

**日本語** ｜ [English](#english)

## 1. 第1電と刊本の照合
- **刊本**：『護國軍紀事』第5期（1916年）「軍政府歡迎黃克強電」（107字）。
  - 刊本を特定したのは、先行リポジトリ saberwatchmanga/sun-circle-cipher-1916。
  - 照合には、同リポジトリの手作業の翻字を使った。刊本の画像を私自身が読み直したわけではない。
  - 刊本の本文は、このリポジトリに含めていない。出典は [SOURCES.md](../SOURCES.md)。
- **方法**：解読した第1電の先頭107組の字の列と刊本の107字を、Python の difflib.SequenceMatcher で並べ、一致する字を数えた。

| 転写 | 刊本と一致した字 |
|---|---|
| ローマ字原文をそのまま読んだもの（`data/romaji_raw.txt`） | 26 / 107（注） |
| 最終の表（`data/groups.csv`） | 102 / 107 |

（注）原文をそのまま読むと、46語目（hiuchitaka）の先頭の hi が、直前の語の末尾の c とつながって chi（チ）になる。そのため仮名が1つ減り、後ろの組がすべてずれる。修正の前の私の転写（この語を huuchitaka と読み違えていた）では40字が一致していた。

最終の表の内訳（第1電の107組）：

| 区分 | 組数 | 刊本と一致 |
|---|---|---|
| 変換式どおり | 59 | 54 |
| 修正読み | 43 | 43 |
| 刊本で補う | 5 | 5（刊本の字を入れたので、一致は当然） |

刊本と違うのは次の4か所。電報側の5組（28・41〜43・57）は、いずれも変換式どおりの組。

| 組 | 電報 | 刊本 | 見方 |
|---|---|---|---|
| 9と10の間 | （なし） | 我 | 刊本にだけある字 |
| 28 | 慮（1982） | 憂（1992） | 電碼が十の位で1桁違う。送信時の誤りか、刊本の改変かは決められない |
| 41〜43 | 提挈公 | 教言 | 文の違い |
| 57 | 查 | 察 | 文の違い |

**注意**：「修正読み」43組がすべて刊本と一致するのは、修正の精度を独立に示すものではない。第1電の修正には、刊本を参照できる状態で行ったものが含まれる。独立に近い検証は、修正を入れていない「変換式どおり」の組で、59組中54組が刊本と一致し、残る5字は上の文の違いだった。

## 2. 原文の転写の照合（別の AI による独立の転写）
ローマ字原文は、Claude が画像から書き起こした。人による1字ずつの確認はしていない。代わりに、次の照合をした（2026年10月19日）。

- **方法**
  - OpenAI の Codex（モデル gpt-6.1-sol）に、コマ0076〜0078の画像だけを渡して、字どおりの転写を3回、別々に作らせた。
  - こちらの転写や先行リポジトリの転写は見せていない。3回とも、ファイルの読み込みやコマンドの実行はなかった（実行記録で確認）。
  - 3回の結果を、語ごとに多数決した。

- **語ごとの一致**（126語）

| Codex 3回の結果 | 語数 |
|---|---|
| 3回とも同じ | 60 |
| 2回が同じ | 55 |
| 3回ともばらばら | 11 |

- **字ごとの食い違い**（1,266字。照合した時点の、修正前の私の転写で数えた）

| 比べたもの | 違う字の数 |
|---|---|
| 私の転写と先行リポジトリの転写 | 21 |
| 私の転写と Codex の各回 | 81 / 77 / 77 |
| 先行リポジトリの転写と Codex の各回 | 85 / 82 / 86 |

- **Codex の多数の読みが、私の転写と違った42語**
  - 5語は、画像を見直して、私の読み違いと判断し、`data/romaji_raw.txt` を直した。
    - 46 huuchitaka → hiuchitaka
    - 58 nikochitak → rikochitak
    - 63 echiuashit → echinashit
    - 96 takaonomie → takaononie
    - 116 esatefumika → esatefmika
  - このうち4語（58・63・96・116）は、先行リポジトリの転写も Codex の多数と同じだった。
  - 46・58・96 は、私がもともと修正で直していた綴りと同じになった。そのため、修正の一覧から外した。
  - 63・116 は、字どおりの綴りを直したので、解読のための読み替えを修正の一覧に移した。
  - 121（wakataekat）は、画像で a の上に小さく o が書き足されていることを確かめた。修正（wakatoekat）の根拠に加えた。
  - 残る36語は、Codex の読みを当てると、解読が次のようになった。そのため、私の読みを残した。

| Codex の読みを当てた結果 | 語数 |
|---|---|
| 後ろの組がずれる | 13 |
| 規則外の組が出る | 7 |
| 刊本と一致していた字が別の字になる（例：鑒奉→鑤克、光→儕） | 4 |
| 第2電で、文の通らない字になる（例：馮段→馬段、第四→笫四） | 11 |
| 字が変わらない（刊本で補った区間） | 1 |

- **限界**
  - 先行リポジトリも、Codex を中心に転写している。Codex と先行リポジトリの一致は、完全に独立した裏付けではない。
  - Codex 単独の転写は食い違いが多い。私の読み違いと判断したのは、画像を見直して同意できた語だけ。
  - この照合は AI どうしの比較で、人による確認の代わりにはならない。

## 3. 暗号文の第二の写し（JACAR B03050731100）との照合
### 見つかった写し
- 外務省記録「袁世凱帝制計画一件（極秘）／反袁動乱及各地状況」の第十五巻の件名「1 大正5年4月29日から大正5年5月22日」（JACAR B03050731100）、画像24〜26ページ。
- 肇慶の太田領事から石井外務大臣への電報 **第四二號**（大正5年5月21日発、22日本省着）。岑春煊から頼まれた黄興宛ての電報を伝えるもので、表書きの後ろに「（以下支那側暗號）」として、ローマ字の暗号文の全文（42行・126語）が付いている。
- コマ0076〜0078（`data/romaji_raw.txt`）とは別の、同じ電文の写し。転写は `data/romaji_copy2.txt`（Claude が画像から読んだもの。人による1字ずつの確認はしていない）。

### 表書きの要旨（私の判読）
- 電報は2通からなる。
- 1通目は、岑春煊をはじめ、雲南・貴州・両広・浙江の各都督と各司令官らの連名で、黄興に宛てたもの。黄興が協同して事に当たることに感謝し、公は共和を首唱し、方略に富み、各国の情勢も調べたので、今後の内政・外交はただ公の指導を頼む、という内容。
- 2通目は、李根源らから黄興に宛てたもの。近日中に協和軍を組織して、湖南と江西に入ることを述べている。

**分かること**
- 2通が1916年5月20日（哿）付であることが、日本側の記録で確かめられた（第6節）。
- 第2電の差出人に李根源が入っていることが、当時の日本側の記録で確かめられた。
- 要旨は、この解読の内容（第1電は刊本どおり。第2電の「協和軍旬內可齊，卽由韶入贑」）と合う。

### ローマ字の照合
2つの写しを語ごとに比べた。上付きの書き足し（at°akitets、wakat°ekat）まで同じで、同じ電文の写しである。

| 結果 | 語数 |
|---|---|
| 2つの写しで綴りが同じ | 114 |
| 綴りが違う | 12 |

綴りが違う12語の内訳：

| 内訳 | 語 |
|---|---|
| この解読で直した綴りが、第二の写しではそのまま書かれている | 17 noheenihek（短・適）、43 hifuketaha（唐）、52 aitataitek（光）、121 wakatoekat（情）、123 hemukufunu（羣） |
| この解読の修正と、一部だけ合う | 20 kotoakushoh（末尾の h）、35 usawakteae（te）、45 ietoriasac（ie）、108 eyuniheiso（先頭の e と h） |
| 第二の写しの綴りを当てると、読めなくなる | 5 kahakaasei、34 sakaosokik、57 coteriatsu（私の判読の誤りの可能性があり、確かめていない） |

- 直した40語のうち、5語は、第二の写しによって、修正後の綴りが独立に裏付けられた。
- 30語は、第二の写しも、原文の転写と同じ崩れた綴りだった。崩れは、写しを作る段階より前（送信の段階）で起きたとみられる。
- 刊本で補った第1電の48〜52・58組目と、推定の4組（164・211・223・225）の区間は、第二の写しでも同じ綴りで、新しい読みは出ない。

## 4. 黄興の返電による署名の確認
- 黄興の返電（JACAR B03050731500）の暗号文の冒頭8語を変換式で戻すと、「隱印崧詔鬯行諸兄鑒正寄函」が出る。
- 『近代史資料』総50号 p.123「致肇慶軍務院電」の冒頭と一致する。
- 再現：`tests/test_formula.py` の `test_huang_reply_addressees`。

### 返電の全文の照合
- **方法**：返電の暗号文の全文（31語。ローマ字は友清氏のページによる）を変換式で戻した。直したのは、友清氏が記事で示している次の2点だけ。
  - 「O HI」は「CHI」に直せる（KONUOHIKE → KONUCHIKE）。直さないと、35組目から後ろがすべてずれる。
  - このローマ字の YE は、2字目・3字目ではエと読む（2字目に入るのはア〜オ・カ〜コだけ）。
- **結果**：全46組が読めた。

  > 隱印崧詔鬯行諸兄鑒正寄函間適接哿電敬悉一切護國軍能速入湘贑甚好行嚴何日東渡望速啓行先電示興徑

  再現：`tests/test_formula.py` の `test_huang_reply_full_text`。
- **3つの写しの比較**

| 箇所 | 暗号文を変換式で戻したもの | 『近代史資料』の活字 | 当時の日本側の写し（Bourdeau 氏のページの翻字） |
|---|---|---|---|
| 宛先の4・5字目 | 詔・鬯 | 詔・鬯 | 誥・邕 |
| 書き出し | 正寄函間 | 正寄函間 | 正發書（同ページの意訳の文では「正發書翰之際」） |
| 護國軍… | 能**速**入湘贑 | 能入湘贛（「速」がない） | 能**速**入湘贛 |

- **分かること**
  - 宛先の「詔・鬯」と書き出しの「寄函」は、活字が正しく、日本側の写しの「誥・邕」「發書」は写し誤りとみられる。宛先「隱印崧詔鬯行」を、元の電文の側から確かめたことになる。
  - 「速」は暗号文にも日本側の写しにもあり、活字が落としたものとみられる。「速」があること自体は、Bourdeau 氏のページですでに分かっていた。
- **注意**：使ったのは友清氏のローマ字と、友清氏自身の直し方だけで、新しい解読ではない。暗号文の画像で、ローマ字を私が確かめ直したわけではない。

## 5. 変換式の再現
`tests/test_formula.py` で、次を確かめている。
- 電碼1〜9199で、変換と逆変換が一致する。
  - 1字目の表が46字なので、表せるのは9199まで。
  - 200の倍数の扱いは [OPEN.md](OPEN.md) を参照。
- 友清氏の一覧にある15組（一＝アアホ、印＝タウホ、哿＝タカス など）の仮名と字が、式と Unihan の表で再現できる。
- `data/groups.csv` が、原文と修正表から再生成したものと同じである。
- 表の電碼が、仮名と字の両方に合っている。
- 第二の写しが126語で、違う語が12語であることと、修正後の綴りが写しにそのまま書かれた5語。

実行方法：

```
python3 -m unittest discover -s tests
```

## 6. 日付
「删」は韻目で15日、「哿」は20日を表す。軍務院が成立したのは1916年5月8日。黄興の返電は5月25日付で、第2電に答えている。さらに、同じ電文が、大正5年（1916年）5月21日に肇慶の太田領事から外務省へ送られている（第3節）。したがって、2通は**1916年5月20日**の発信である。

---

<a id="english"></a>

# Verification (English)

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
  - For the handling of multiples of 200, see [OPEN.md](OPEN.md#english).
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
