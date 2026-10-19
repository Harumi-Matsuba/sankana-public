# 未解決の点と、先行リポジトリの指摘

**日本語** ｜ [English](#english)

先行リポジトリ saberwatchmanga/sun-circle-cipher-1916 は、この電報について慎重な留保をいくつも書いている（同リポジトリの docs/CHRONOLOGY.md、docs/HYPOTHESES.md）。
この解読は、そのいくつかについて、より踏み込んだ読みを採っている。以下では、留保と、この解読が採る根拠を並べる。どちらかで確定したわけではない。

## 1. 152組目：韶か蘿か
- **先行リポジトリの指摘**：韶（7300、ヱコナ）と蘿（5700、エコナ）は、ローマ字ではどちらも ekona になり、原文からは区別できない。
- **この解読が韶を採る根拠**
  - 文は「協和軍旬內可齊卽由韶入贑」（協和軍は10日以内にそろい、韶から江西へ入る）。韶州は、広東から江西へ北上する道筋にある。
  - 中国語版 Wikipedia「李烈鈞」によると、李烈鈞の軍は広東から北上して江西を目指し、6月19日に韶州で龍濟光の軍と戦っている。
  - 「蘿」は、この文の地名として通らない。
  - 当時の日本側の作業紙（コマ0080）の書き込みは「詔」で、韶と同じ旁の字。韶の裏付けとしては弱い。
- **判断**：韶（推定・強）。原文の文字だけで決めたものではない。

## 2. 署名の3〜5番目：原文はそろって nu で始まる
- **先行リポジトリの指摘**
  - 署名の原文は ekato、minuna、nukuhe、nukufu、nuata、mekano。3〜5番目は、はっきり「nu」で始まる。
  - 返電の宛先が、そのまま第2電の署名者だとは限らない。
- **この解読の読み**
  - ヌクヘ → 楷（ニクヘ）
  - ヌクフ → 羣（ムクフ）
  - ヌアタ → 泰（ヒアタ）

  3つとも1字目だけを替えた読み。根拠は、黄興の返電の宛先（崧・詔・鬯）を暗号文から確かめたことと、字・号との対応（[DECIPHERMENT.md](DECIPHERMENT.md)）。
- **弱い点**
  - 3組がそろって1字目だけ崩れている理由は、説明できていない。
  - 当時の日本側も、ヌクヘの横には「公」、ヌアタの横には「渠?」と書いている（コマ0081）。どちらも、この解読の読みとは違う。

## 3. 5番目の人物：『近代史資料』の注は趙正平
- **先行リポジトリの指摘**：『近代史資料』の返電の宛先の注は、5番目を趙正平としている。これは、楊永泰という比定と食い違う。
- **この解読の見方**
  - 宛先の字は、返電の暗号文から「鬯」と確かめた。
  - 趙正平の字は「厚生」（Wikipedia）で、「鬯」と合わない。1916年の『軍務院考實』第2卷（附録『兩廣都司令部考實』の職員錄）でも、「參謀部 編制兼稽查主任 趙正平 厚生 江蘇太倉」とある（PDF の223ページ）。
  - 楊永泰の字は「鬯卿」（Wikipedia。「暢卿」とも）。同じ職員錄では「財政廳 廳長 楊永泰 暢卿 廣東茂名」とある（PDF の237ページ）。「鬯」と「暢」は同じ音（chàng）で、宛先に同じ音の字を使ったとみる（この点は解釈）。
  - 4番目「詔」についても、同じ注は曾其衡（字は詔文）としている。しかし、衡の仮名はケケナで、原文 nukufu と合わない。
  - 文羣（号は詔雲）は、同じ職員錄に「秘書廳 秘書 文羣 詔雲 江西萍鄉」「外交局 兼代局長 文羣 詔雲」とある（PDF の230・236ページ）。1916年に肇慶の都司令部にいたことが、当時の資料で確かめられる。
- **判断**：鬯＝楊永泰、詔＝文羣を採る。1916年の職員錄でも、趙正平の字は「厚生」なので、注が取り違えている可能性は高い。

## 4. 164組目：電碼6381
- **先行リポジトリの指摘**
  - 6381 は、1915年版・1926年版の電碼書で空欄になっている。
  - 贑（6371）の1桁違いの可能性がある（同リポジトリの仮説 P3）。
- **この解読の読み**
  - 贑（推定）。文は「非俟幹卿協和兵入湘贑」。
  - 黄興の返電にも「護國軍能入湘贛」（『近代史資料』の活字では簡体字の「护国军能入湘赣」）とある。
- **注意**
  - 1桁違いという仕組みの実例として、刊本で確かめられるのは、第1電の 慮1982／憂1992 だけ。
  - 2字目は一の位、3字目は十の位を表す。そのため、2字目か3字目を1字替える修正は、自動的に「1桁違い」に見える。こうした修正を、桁ずれの独立した証拠に数えることはできない。

## 5. そのほかの推定・確度「中」の組
- **211組目「出」**：原文サテフは規則外（2字目のテは使えない）。サキフ＝出と1字違いで、直前の「亦卽出贑」と同じ言い回しになる。
- **確度「中」の修正**：僅・定・齊・恐・發・代・謀・師・舊部などは、原文の綴りが崩れていて、1字の修正と文脈で決めた（`data/corrections.csv` の確度欄）。
  - 「恐」「發」は、作業紙の書き込み（心偏の字、「蘿?」）とも一致しない。
- **第1電の48〜52組目・58組目**：原文の綴りからは読めず、刊本の字（富・有・方・各・復）で補った。置き換え・挿入・削除を合わせて探索しても（`src/beam.py`）、刊本の字にたどり着く修正は見つかっていない。

## 6. 内容の未解決点
- **「潤輔」**（113・114組目）：どちらも変換式どおりに読めるので、字どおりに残した。人物を指すとみられるが、誰かは特定できていない。
  - 有力な候補は、張孝準（字は潤農）。『軍務院考實』第1卷の軍務院職員表に「駐日委員 張孝準 潤農」とある（PDF の250ページ）。電文は「潤○當告公近形」（潤○が、公に最近の様子を伝える）で、日本にいた黄興に、日本駐在の委員が伝えるという筋によく合う。『近代史資料』の注も張孝準（字は潤龍、また閏農）を挙げている。
  - ただし、農の仮名はネウサ（6593）で、原文のネエチ（輔、6534）とは2字目と3字目の2か所が違う。1字の読み違いでは説明できないので、確定はしない（推定・弱）。
- **「虎任第四師長」**：Wikipedia では、林虎の1916年の肩書きは第6軍軍長で、合わない。
  - 『軍務院考實』第1卷の職員錄でも、林虎は「林軍職員表（護國第六軍）」の總司令（PDF の254ページ）。
  - 一方、同じ職員錄の滇軍職員表（護國第二軍。李烈鈞の軍で、第2電の「協和軍」）には「第四師 師長 方聲濤」がある（PDF の253ページ）。第2電の「第四師長」は、同じ軍の中に実際にあった役職だと分かる。
  - この職員錄は、5月20日より後の時点のものかもしれない（本は軍務院の撤廃まで扱い、一覧の日付は書かれていない）。「5月20日には林虎を第四師長とする予定だったが、のちに林虎は第六軍を率い、第四師は方聲濤が率いた」という筋は考えられるが、推定で、確かめられていない。

## 7. 変換式の境界
友清氏の式では、200の倍数の電碼（200、400、…）は、1字目が次の行に進み、「コサ」で終わる組になる。
- この解読の2通にも、黄興の返電にも、「コサ」で終わる組はない。
- そのため、この境界の扱いは、実際の電文では確かめられていない（`src/kana.py` の注記）。

---

<a id="english"></a>

# Open questions and the prior repository's caveats (English)

The prior repository saberwatchmanga/sun-circle-cipher-1916 records many careful caveats about this telegram (its docs/CHRONOLOGY.md and docs/HYPOTHESES.md).
This decipherment takes a firmer reading on several of them. Below, each caveat is set beside the evidence this decipherment relies on. None of them is settled either way.

## 1. Group 152: 韶 or 蘿
- **Prior repository's caveat**: 韶 (7300, ヱコナ) and 蘿 (5700, エコナ) are both "ekona" in romaji and cannot be distinguished from the text.
- **Grounds for reading 韶**
  - The sentence is 「協和軍旬內可齊卽由韶入贑」 (the Xiehe army will be assembled within ten days and enter Jiangxi from Shao). Shaozhou lies on the route north from Guangdong to Jiangxi.
  - According to the Chinese Wikipedia article 「李烈鈞」, Li Liejun's army marched north from Guangdong towards Jiangxi and fought Long Jiguang's army at Shaozhou on 19 June.
  - 蘿 makes no sense as a place name in this sentence.
  - The note on the Japanese worksheet (frame 0080) is 詔, which shares its phonetic component with 韶. This is only weak support for 韶.
- **Judgment**: 韶 (inferred, strong). Not decided from the letters of the text alone.

## 2. Signature slots 3–5: in the text, all three begin with "nu"
- **Prior repository's caveats**
  - The raw signatures are ekato, minuna, nukuhe, nukufu, nuata, mekano. Slots 3–5 clearly begin with "nu".
  - The addressees of a reply are not necessarily the signers of Telegram 2.
- **This decipherment's reading**
  - ヌクヘ → 楷 (ニクヘ)
  - ヌクフ → 羣 (ムクフ)
  - ヌアタ → 泰 (ヒアタ)

  All three change only the 1st kana. The grounds are the addressees of Huang Xing's reply (崧・詔・鬯), confirmed from its cipher text, and their correspondence with courtesy and art names ([DECIPHERMENT.md](DECIPHERMENT.md#english)).
- **Weak points**
  - Why all three groups are corrupted only in the 1st kana is not explained.
  - The Japanese analysts wrote 公 beside ヌクヘ and 渠? beside ヌアタ (frame 0081). Neither matches this decipherment's reading.

## 3. The 5th person: the 『近代史資料』 footnote says Zhao Zhengping
- **Prior repository's caveat**: the footnote to the addressees of the reply in 『近代史資料』 identifies the 5th as Zhao Zhengping 趙正平. This conflicts with the identification as Yang Yongtai.
- **This decipherment's view**
  - The addressee character was confirmed as 鬯 from the cipher text of the reply.
  - Zhao Zhengping's courtesy name is 厚生 (Wikipedia), which does not match 鬯. The 1916 『軍務院考實』 vol. 2 (staff list of the appendix 『兩廣都司令部考實』) also gives 「參謀部 編制兼稽查主任 趙正平 厚生 江蘇太倉」 (PDF p. 223).
  - Yang Yongtai's courtesy name is 鬯卿 (Wikipedia; also 暢卿). The same staff list gives 「財政廳 廳長 楊永泰 暢卿 廣東茂名」 (PDF p. 237). 鬯 and 暢 have the same sound (chàng); I take it that the addressee was written with a homophone (this is an interpretation).
  - For the 4th, 詔, the same footnote gives Zeng Qiheng 曾其衡 (courtesy name 詔文). But the kana for 衡 are ケケナ, which do not match the text nukufu.
  - Wen Qun 文羣 (art name 詔雲) appears in the same staff list as 「秘書廳 秘書 文羣 詔雲 江西萍鄉」 and 「外交局 兼代局長 文羣 詔雲」 (PDF pp. 230, 236). That he was at the Zhaoqing headquarters in 1916 is confirmed by a contemporary source.
- **Judgment**: 鬯 = Yang Yongtai, 詔 = Wen Qun. Since Zhao Zhengping's courtesy name is 厚生 also in the 1916 staff list, the footnote has probably confused the two.

## 4. Group 164: code 6381
- **Prior repository's caveats**
  - 6381 is blank in the 1915 and 1926 codebooks.
  - It may be a one-digit slip for 贑 (6371) (that repository's hypothesis P3).
- **This decipherment's reading**
  - 贑 (inferred). The sentence is 「非俟幹卿協和兵入湘贑」.
  - Huang Xing's reply also has 「護國軍能入湘贛」 (in the 『近代史資料』 print, in simplified characters, 「护国军能入湘赣」).
- **Caution**
  - The only example of a one-digit slip that can be confirmed against the print is 慮 1982 / 憂 1992 in Telegram 1.
  - The 2nd kana encodes the units digit and the 3rd kana the tens digit. Any correction that changes one 2nd or 3rd kana therefore automatically looks like a "one-digit slip". Such corrections cannot be counted as independent evidence of digit slips.

## 5. Other inferred or medium-certainty groups
- **Group 211, 出**: the text サテフ breaks the rules (テ cannot be the 2nd kana). It differs by one kana from サキフ = 出, giving the same phrase as the preceding 「亦卽出贑」.
- **Medium-certainty corrections**: 僅・定・齊・恐・發・代・謀・師・舊部 and others were decided by one-letter corrections and context, because the spelling of the text is corrupted (see the certainty column of `data/corrections.csv`).
  - 恐 and 發 also do not match the worksheet notes (a character with the heart radical; 蘿?).
- **Groups 48–52 and 58 of Telegram 1**: they cannot be read from the spelling of the text and were filled with the printed characters (富・有・方・各・復). Even a search combining substitution, insertion and deletion (`src/beam.py`) found no correction leading to the printed characters.

## 6. Open questions of content
- **潤輔** (groups 113–114): both read by the formula as written, so they are left as they are. They probably refer to a person, who has not been identified.
  - A strong candidate is Zhang Xiaozhun 張孝準 (courtesy name 潤農). The Military Affairs Council staff table in 『軍務院考實』 vol. 1 lists 「駐日委員 張孝準 潤農」 (PDF p. 250). The text is 「潤○當告公近形」 ("潤○ will tell you of the recent situation"), which fits a delegate resident in Japan reporting to Huang Xing in Japan. The 『近代史資料』 footnote also mentions Zhang Xiaozhun (courtesy name 潤龍, also 閏農).
  - However, the kana for 農 are ネウサ (6593), which differ from the text ネエチ (輔, 6534) in both the 2nd and 3rd kana. A single misreading cannot explain this, so it is not adopted (inferred, weak).
- **虎任第四師長**: according to Wikipedia, Lin Hu's title in 1916 was commander of the 6th Army, which does not match.
  - In the staff lists of 『軍務院考實』 vol. 1, Lin Hu is also commander-in-chief in the 「林軍職員表（護國第六軍）」 (PDF p. 254).
  - On the other hand, the 滇軍職員表 in the same lists (the 2nd National Protection Army, Li Liejun's army, i.e. the 協和軍 of Telegram 2) has 「第四師 師長 方聲濤」 (PDF p. 253). So the "4th Division commander" of Telegram 2 was a post that actually existed in that army.
  - These staff lists may reflect a time after 20 May (the book covers events up to the abolition of the Council, and the lists are undated). One possible account is that on 20 May Lin Hu was planned to become commander of the 4th Division, but later he led the 6th Army and Fang Shengtao led the 4th Division. This is an inference and has not been confirmed.

## 7. The boundary of the formula
In Tomokiyo's formula, codes that are multiples of 200 (200, 400, …) advance the 1st kana to the next entry and give groups ending in コサ.
- Neither of the two telegrams nor Huang Xing's reply contains a group ending in コサ.
- So the handling of this boundary cannot be checked against actual telegrams (see the note in `src/kana.py`).
