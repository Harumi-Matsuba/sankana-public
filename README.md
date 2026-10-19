# 1916年の三仮名電報（JACAR B03050089100）の解読

日本の外務省が当時写し取った、黄興宛ての暗号電報2通（1916年5月20日と推定）を、変換式から読み通した記録です。
- 資料：外務省記録「特定人ノ発受郵便物取調」第3巻、JACAR B03050089100、コマ0076〜0078（ローマ字の暗号文）、コマ0079〜0081（当時の日本側の作業紙）
- 方式：漢字を中国の標準電碼（4桁）にし、それを仮名3字に置き換え、ローマ字で送る「三仮名コード」
- 変換式：友清理士氏（Cryptiana）が特定したもの

## 現状
全229組を表にしました（`data/groups.csv`）。

| 区分 | 第1電（組0〜107） | 第2電（組108〜228） |
|---|---|---|
| 変換式どおり（原文の綴りのまま読めた） | 57 | 75 |
| 修正読み（語の綴りを直して読んだ） | 46 | 41 |
| 刊本で補う | 5 | 0 |
| 推定 | 0 | 4 |
| 終わりの印（オワリ） | 0 | 1 |

- **第1電**：軍務院の撫軍10名から黄興へ。
  - 平文は1916年の刊本『護國軍紀事』第5期にあり、先行リポジトリが特定済み。**初めての解読ではなく、刊本との照合です。**
  - 最終の表は、刊本の107字のうち102字と一致します（[docs/VERIFICATION.md](docs/VERIFICATION.md)）。
- **第2電**：肇慶にいた6名（林虎・李根源・程子楷・文羣・楊永泰・章士釗と推定）から黄興へ。
  - 刊本は見つかっていません。この表は、変換式から独立に読んだ結果です。
  - 署名は、黄興の返電（JACAR B03050731500）の暗号文から出る宛先「隱印崧詔鬯行」と照らして比定しました。
- 推定に頼る箇所、確度「中」の修正、先行リポジトリの留保は、[docs/OPEN.md](docs/OPEN.md) にまとめました。

## 構成
| パス | 中身 |
|---|---|
| `data/romaji_raw.txt` | ローマ字原文の字どおりの書き起こし（修正なし） |
| `data/corrections.csv` | 修正の一覧（語41件・組9件。元の綴り、修正後、理由、確度、根拠） |
| `data/groups.csv` | 全229組の表（仮名、電碼、字、区分）。`src/build_groups.py` が生成 |
| `data/worksheet.csv` | 当時の日本側の作業紙の書き込みと、この解読の比較（26件） |
| `data/ctc_kTaiwanTelegraph.tsv` | 電碼→漢字の表（Unicode Unihan から抽出） |
| `src/` | 変換器と道具（`kana.py`、`build_groups.py`、`check.py`、`fix.py`、`beam.py`、`lm.py`、`build_ctc.py`） |
| `tests/` | 変換式・返電・表の整合のテスト |
| `docs/` | 解読の記録（DECIPHERMENT）、検証（VERIFICATION）、未解決の点（OPEN） |

## 使い方
Python 3 の標準ライブラリだけで動きます（`fix.py`・`beam.py` を除く）。

```
python3 src/build_groups.py                      # data/groups.csv と outputs/romaji_corrected.txt を作る
python3 src/check.py outputs/romaji_corrected.txt
python3 -m unittest discover -s tests
```

`fix.py`・`beam.py` は、候補を並べるための頻度モデルを使います。材料の取得方法は `src/lm.py` の冒頭に書きました。材料はリポジトリに含めていません。

## 先行研究とクレジット
- **友清理士氏**「Solution of Two Chinese Cipher Telegrams Archived in Japan (1916)」（Cryptiana）
  - 三仮名コードの変換式を特定した（2026年9月23日追記）。
  - この電報と作業紙を特定し、読みの一部を公開した。
  - この解読は、その式の上に成り立っています。
- **saberwatchmanga/sun-circle-cipher-1916**（GitHub）
  - 2026年10月7〜10日の作業記録。第1電の刊本を特定した。
  - 原文と作業紙の層を分けた転写や、第2電の論点と慎重な留保を残している。
  - 私の転写の誤り2か所（39組目・188組目）は、同リポジトリの転写と比べて見つけ、画像で確かめて直しました。
- **D. Bourdeau 氏**（cyphersolver）：この簿冊の電報群の調査。

出典の詳細は [SOURCES.md](SOURCES.md)。

## AI の使用
- この解読の作業の大部分は、Anthropic の AI である Claude（Claude Code）が行いました。
  - 画像からのローマ字の書き起こし
  - 変換器の作成
  - 修正候補の探索
  - 史料との照合
  - 文書の作成
- 公開者は、方針の指示と確認を行いました。
- 作業の一部は、Claude Code の /goal 機能で、目標に達するまで自動で続けさせました。
- AI の読みや判断には、誤りがありえます。修正の根拠と確度は `data/corrections.csv` と `docs/OPEN.md` に書きました。原資料（JACAR の画像）で確かめてください。

## ライセンス
- コード（`src/`、`tests/`）：MIT
- 文書とデータ（`docs/`、`data/` の自作部分、この README）：CC BY 4.0
- `data/ctc_kTaiwanTelegraph.tsv`：Unicode のライセンスに従います。

詳しくは [LICENSE](LICENSE)。
