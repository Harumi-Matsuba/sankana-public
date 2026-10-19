# Prior-work check (the full reading of Telegram 2, and the identification of its six senders)

[日本語](PRIOR_CHECK.md)

A checker who did not do the decipherment received the plaintext, the ciphertext and the earlier prior-work notes, and searched for prior work with the aim of refuting the claims below. The search was done on 20 October 2026 (Japan time). Not finding something does not prove that nobody has worked on it.

## Claims checked
- A. Telegram 2 (20 May 1916, six men at Zhaoqing → Huang Xing; JACAR B03050089100, frames 0076–0078, groups 108–228) was read through as a whole.
- B. Its six senders were identified as Lin Hu, Li Genyuan, Cheng Zikai, Wen Qun, Yang Yongtai and Zhang Shizhao.

## Conclusion
| Claim | Category | Details |
|---|---|---|
| A. Full reading of Telegram 2 | As a whole text: **not found**. Character by character: **a large part has already been read** | No print of the full plaintext and no earlier connected reading was found in the places below. But the Japanese analysts' worksheets of 1916 (frames 0079–0081) already carry readings of Telegram 2, and Tomokiyo's transcription of them (item 1 below) lists 83 characters of Telegram 2 (which has 120 characters, not counting the end marker). The table in saberwatchmanga/sun-circle-cipher-1916 (item 2) assigns characters to most groups of Telegram 2 and lists 10 groups as unresolved |
| B. The six senders | **Partly already identified or proposed** | The six addressees of Huang Xing's reply are identified in a footnote of 『近代史資料』 no. 50 as Lin Hu, Li Genyuan, Cheng Zikai, Zeng Qiheng, Zhao Zhengping and Zhang Shizhao (four of them the same as here). A six-name list (including Yang Yongtai) was proposed in saberwatchmanga and later downgraded to a hypothesis (item 2). No earlier work found here derives the addressees from the reply's ciphertext and uses courtesy names and the 1916 staff lists to make the 4th and 5th names Wen Qun and Yang Yongtai, rejecting the footnote's Zeng Qiheng and Zhao Zhengping |

### What can be called new (from this check)
- Telegram 2: it cannot be called "read for the first time". Many of its characters were read by the 1916 worksheets, and Tomokiyo and saberwatchmanga published them in 2026. What is new is (1) readings for groups that earlier work left unresolved or blank, or where the character given by the formula does not fit the sentence; (2) joining them into a text that reads as a whole; and (3) finding and comparing the second copy of the same ciphertext (JACAR B03050731100), which none of the places below mentions.
- The senders: it cannot be called "the six identified for the first time". Four of them are in the printed footnote as the reply's addressees, and a six-name list exists as a hypothesis in saberwatchmanga. What is new is the check from the reply's ciphertext and the 1916 staff lists, and the grounds for making the 4th and 5th names Wen Qun and Yang Yongtai.
- The README sentence saying the prior repository "left many groups of Telegram 2 blank" would be better written so that the numbers above can be seen (10 unresolved groups, plus groups where only the formula's character is given and it does not fit the sentence). It would also be better to say, under the relation to prior work, that the 1916 worksheets carry 83 characters of Telegram 2.

## Where the numbers come from
- 83 characters (from the record): the 87 pairs transcribed by Tomokiyo from worksheet pages 3–5, minus the 4 that end Telegram 1 (光・公・望・哿). They include the worksheet's own slips (齎/齋, 葛 for 萬, 俣 for 俟).
- 10 unresolved groups (from the record): rows with status UNRESOLVED among the 114 rows of Telegram 2 in saberwatchmanga's data/whole_source_alignment.tsv (version of 10 October 2026): nashi, maseso, notaekona, tesu, tathe, caose, watuno, kutena, yunikeiso, satef.
- Group-by-group comparison (calculated): aligning the 121 groups of Telegram 2 here with those 114 rows by their code numbers paired 96 groups automatically (the other 25 did not pair and were not compared). Of the 96, 70 have the same character as the worksheet or pencil reading in that table, and 84 the same as some column of it (including characters given by the formula).

## Places checked (20 October 2026)
| Place | Version or date | Result |
|---|---|---|
| 1. S. Tomokiyo, "Solution of Two Chinese Cipher Telegrams Archived in Japan (1916)", https://cryptiana.web.fc2.com/code/chinesecrypto_e2.htm | Last-Modified 19 Oct 2026 13:45 GMT | Transcription of the worksheet readings (pp. 1–5) and the formula. 83 characters of Telegram 2. No full reading. The addition of 19 October 2026 describes this repository's (Harumi-Matsuba's) work and is not prior work |
| Same site, unsolved.htm and ai.htm | 13 Oct 2026, 19 Oct 2026 | The three-kana code is mentioned only as identified by Bourdeau with the formula by Tomokiyo. No reading of Telegram 2 |
| 2. saberwatchmanga/sun-circle-cipher-1916, https://github.com/saberwatchmanga/sun-circle-cipher-1916 | 4907616 (10 Oct 2026) | Identification of the print of Telegram 1. Telegram 2 as a table of characters per group ("a dated research snapshot, not a continuous verified plaintext"), 10 groups unresolved. docs/CHRONOLOGY.md: an AI review proposed a six-name list (including Yang Yongtai), later withdrawn. data/hypotheses/: signature characters 虎・源・釗・羣 (P1), 楷 and 泰 unresolved (P2). docs/ROUND4.md: the five files of the same series for 15 May–15 June 1916 were screened; no other telegram in the same key and no second copy was found |
| 3. D. Bourdeau, cyphersolver, https://github.com/dbourdeau/cyphersolver | origin/main 0258b8ab (18 Oct 2026) | sunintercepts.html: "The kana stream of B03050089100 fr. 0076–0078 … is not decoded here either". huangxing.html quotes the Japanese note on the reply, 「林虎・李根源等ノ字ナラン」. Of all issues and PRs from 17 October 2026 on, only #48 deals with Telegram 2, and it is this repository's own report |
| 4. B. Dudout, wenmi, https://github.com/bdudout/wenmi | b5439a7 (19 Oct 2026) | Mentions the three-kana reply only as something different. No reading of Telegram 2 |
| 5. limin112 (GitHub) | repository list, 20 Oct 2026 | Only sun-dai-1917-cipher (a different telegram of 1917) is related |
| 6. 『近代史資料』 no. 50 (public PDF, SHA256 5d6cdee4…a819) | — | Text recognition of every page searched for words of Telegram 2 (虛名, 舊部, 面達, 近情, 協和, etc.). Telegram 2 is not there. Footnote 1 to 「致肇慶軍務院電」 on p. 123 (PDF p. 125) identifies the reply's addressees as Lin Hu (隱青), Li Genyuan (印泉), Cheng Zikai (嵩山), Zeng Qiheng (詔文), Zhao Zhengping (鬯卿) and Zhang Shizhao (行嚴) (checked on the image) |
| 7. Six printed volumes of 1916 (Wikimedia Commons): 『軍務院考實』 vols. 1 and 2 (NLC416-02jh005230-14942, -14943), 『護國軍紀事』 no. 4 (SSID-11382682) and no. 5 (SSID-11382807), and 『護國軍紀事』 NLC416-07jh010500-21155 and NLC416-07jh010501-21164 (issue numbers not checked) | 1,394 pages in all | Vertical traditional-Chinese text recognition (tesseract chi_tra_vert), then a count per page of how many of Telegram 2's character pairs (117 kinds) appear. As a positive control, Telegram 1's pairs (107 kinds) were counted too: the page with the print of Telegram 1 (no. 5, PDF p. 26) scored 21, the highest, so the method does pick up a printed telegram. Telegram 2's highest score was 12 (『軍務院考實』 vol. 1, PDF p. 175: a different telegram, Li Genyuan to Tang Jiyao, with similar content about the council not yet being organised), and its 95th percentile was 5. No page carrying Telegram 2 was found |
| 8. Web search (English and Chinese: phrases of Telegram 2, the six names with "to Huang Xing", Huang Xing's chronicle) | — | Nothing relevant |
| 9. JACAR B03050731100 (the second copy) | — | Not mentioned in items 2 or 3 (string search of the ledger and the repository) |
| 10. GitHub repository search | — | Only item 2 and this repository are related |

## Not checked, or could not be checked
- Not checked: 『黃興集』, 『黃興年譜長編』, Li Genyuan's 『雪生年錄』, 『章士釗全集』, source collections on the National Protection War in Yunnan and Guangdong, other issues of 『護國軍紀事』 (nos. 1–3 and 6, SSID-12587438, the CADAL copies), newspapers of the time (e.g. 申報), and Chinese and Taiwanese article databases.
- Could not be checked: Google Books search (the API stopped with 429). GitHub code search did not return even this repository, so it is not exhaustive.
- Limits of the text recognition: the type is small and vertical, and recognition of the body text is poor (even on Telegram 1's print page only 21 of 107 character pairs were picked up). A print with slightly different wording, or a partial quotation, may be missed.

## Note (found during the check)
- 『軍務院考實』 vol. 1, part 4 「各省文電」, p. 14 (PDF p. 119), in 「岑撫軍副長組織聯合軍請唐撫軍長指揮進行電」, has 「兩廣護國軍新編第六軍總司令兼陸軍第四師師長林虎」 (checked on the image): Lin Hu as commander of the 6th Army *and* commander of the 4th Division. The same telegram names 程子楷 as commander of the 1st Mixed Brigade. This agrees with Telegram 2's 「虎任第四師長」 and is material for revisiting the point in [OPEN.en.md](OPEN.en.md) that the title "commander of the 4th Division" does not match later records.
