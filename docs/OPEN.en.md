# Open questions and the prior repository's caveats

[日本語](OPEN.md) ｜ **English**

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

  All three change only the 1st kana. The grounds are the addressees of Huang Xing's reply (崧・詔・鬯), confirmed from its cipher text, and their correspondence with courtesy and art names ([DECIPHERMENT.md](DECIPHERMENT.en.md)).
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
