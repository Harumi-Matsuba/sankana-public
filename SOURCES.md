# 出典

## 一次資料（リポジトリには含めていない）
- **JACAR（アジア歴史資料センター）B03050089100**
  - 外務省記録 1.6.1.4-2-1-2「各国内政関係雑纂／支那ノ部／革命党関係（亡命者ヲ含ム）／特定人ノ発受郵便物取調」第3巻（外務省外交史料館）
  - コマ0076〜0078：ローマ字の暗号文
  - コマ0079〜0081：日本側の作業紙
  - https://www.jacar.archives.go.jp/das/meta/B03050089100
- **JACAR B03050731500**：黄興の返電（1916年5月25日）
  - https://www.jacar.archives.go.jp/das/meta/B03050731500

画像・PDF は再配布していません。コマ番号で参照してください。

## 刊本
- **『護國軍紀事』第5期（1916年）「軍政府歡迎黃克強電」**
  - Wikimedia Commons（先行リポジトリの記載による）：https://commons.wikimedia.org/wiki/File:SSID-11382807_護國軍紀事_第5期.pdf
  - 照合には、先行リポジトリ（下記）の手作業の翻字を使った。本文はこのリポジトリに含めていない。
- **『近代史資料』総50号 p.123「致肇慶軍務院電」**（黄興の返電の活字）
  - 注の宛先比定（曾其衡・趙正平）は、[docs/OPEN.md](docs/OPEN.md) で検討した。

## 先行研究
- 友清理士「Solution of Two Chinese Cipher Telegrams Archived in Japan (1916)」Cryptiana
  - https://cryptiana.web.fc2.com/code/chinesecrypto_e2.htm（2026年9月18日初出、9月23日更新）
  - 三仮名コードの変換式。テストで使った15組の対応と、黄興の返電のローマ字（全文31語）と、その直し方（O HI → CHI）は、このページによる。
- saberwatchmanga/sun-circle-cipher-1916
  - https://github.com/saberwatchmanga/sun-circle-cipher-1916（2026年10月10日の版を参照）
  - 第1電の刊本の特定と翻字。先行リポジトリの指摘は docs/OPEN.md に挙げた。このリポジトリには、同リポジトリのファイルを含めていない。
- D. Bourdeau, cyphersolver（黄興の返電の、当時の日本側の写しの翻字は https://dbourdeau.github.io/cyphersolver/huangxing.html による）
  - https://github.com/dbourdeau/cyphersolver
  - https://dbourdeau.github.io/cyphersolver/sunintercepts.html

## データ
- **Unicode Unihan データベース**（Unicode 18.0.0）
  - kTaiwanTelegraph（電碼→漢字）
  - kSimplifiedVariant（`src/lm.py` のみ）
  - https://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip
  - © Unicode, Inc. 利用条件 https://www.unicode.org/terms_of_use.html、ライセンス https://www.unicode.org/license.txt
- **jieba の辞書 dict.txt**（`src/lm.py` のみ。リポジトリには含めない）
  - https://raw.githubusercontent.com/fxsjy/jieba/master/jieba/dict.txt

## 人物の字・号、史実
- 林虎、李根源、程子楷、文羣、楊永泰、章士釗、趙正平の字・号：Wikipedia の各項目による。6人の字・号と、趙正平の字（厚生）は、下の『軍務院考實』の職員錄でも確かめた。
- **『軍務院考實』第1卷（1916年）**
  - Wikimedia Commons：https://commons.wikimedia.org/wiki/File:NLC416-02jh005230-14942_軍務院考實_第1卷.pdf（パブリックドメイン、261ページ）
  - 第五編「職員錄」（PDF の247〜261ページ）を使った。軍務院職員表（張孝準＝駐日委員・字は潤農、李根源、章士釗）、滇軍職員表（第四師師長 方聲濤）、林軍職員表（總司令 林虎・字は隱青）、程旅職員表（程子楷・字は崧生）。
  - 本文はこのリポジトリに含めていない。
- **『軍務院考實』第2卷（1916年。附録『兩廣都司令部考實』を含む）**
  - Wikimedia Commons：https://commons.wikimedia.org/wiki/File:NLC416-02jh005230-14943_軍務院考實_第2卷.pdf（パブリックドメイン、261ページ）
  - 『兩廣都司令部考實』第六編「職員錄」（PDF の220〜251ページ）を使った。參謀部（趙正平・字は厚生）、秘書廳（文羣・号は詔雲）、外交局（文羣）、財政廳（楊永泰・字は暢卿）。
  - 本文はこのリポジトリに含めていない。
- 李烈鈞の軍の動き（1916年6月19日の韶州での戦闘）：中国語版 Wikipedia「李烈鈞」による。
- 陸榮廷の字が幹卿であること：梁啓超『從軍日記』などによる。
