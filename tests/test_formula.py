"""変換式と、解読表の整合を確かめるテスト。

  python3 -m unittest discover -s tests
"""
import csv
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'src'))

from kana import decode, encode, groups_from_words, load_ctc, tokenize  # noqa: E402
import build_groups  # noqa: E402

# 友清理士氏の一覧（Cryptiana, chinesecrypto_e2.htm）にある、電碼・字・仮名の対応の一部
TOMOKIYO = [
    (1, '一', 'アアホ'), (13, '世', 'アウヘ'), (22, '中', 'アイフ'), (37, '之', 'アキヒ'),
    (57, '事', 'アキノ'), (76, '亦', 'アカヌ'), (86, '人', 'アカニ'), (149, '何', 'アケタ'),
    (338, '兄', 'カクチ'), (341, '先', 'カアタ'), (354, '入', 'カエソ'), (434, '切', 'サエヒ'),
    (603, '印', 'タウホ'), (776, '哿', 'タカス'), (796, '啓', 'タカサ'),
]

# 黄興の返電（JACAR B03050731500）の冒頭8語。ローマ字は友清氏のページによる。
HUANG_REPLY = 'REKUTATA UHOYAKATE SEKANAOKU SAKEKINISE OSUKAKUCHI REUHONIUSU MAKASUSAKU FUREOHIHE'

# 同じ返電の全文（31語）。ローマ字は友清氏のページによる。
HUANG_REPLY_FULL = (
    'REKUTATA UHOYAKATE SEKANAOKU SAKEKINISE OSUKAKUCHI REUHONIUSU MAKASUSAKU FUREOHIHE '
    'YENIKIYEHI TAKASUREU SASHIKIHE WAONIAAHO SAYEHITE UHINAKUTA NEATEMUYE SUHEUHAKA '
    'YESOMIKANU TEASUUKU TSUHAKOSE KEKININAKI TEAKETASHI KONUOHIKE HIMIKANO SHIKUSAHE '
    'UHATAKASA KEKINIKA ATAREUSASU OSO YUA NIRA KISU'
)


class TestFormula(unittest.TestCase):
    def test_round_trip(self):
        for c in range(1, 9200):
            self.assertEqual(decode(encode(c)), c)
        self.assertRaises(ValueError, encode, 9200)

    def test_all_groups_distinct(self):
        self.assertEqual(len({encode(c) for c in range(1, 9200)}), 9199)

    def test_tomokiyo_examples(self):
        ctc = load_ctc()
        for code, ch, kana in TOMOKIYO:
            self.assertEqual(encode(code), kana, code)
            self.assertEqual(ctc[code], ch, code)

    def test_huang_reply_addressees(self):
        # 『近代史資料』総50号 p.123「致肇慶軍務院電」の冒頭「隱、印、崧、詔、鬯、行諸兄鑒」と照合する
        ctc = load_ctc()
        words = HUANG_REPLY.lower().split()
        text = ''.join(ctc[decode(g)] for g in groups_from_words(words) if len(g) == 3)
        self.assertTrue(text.startswith('隱印崧詔鬯行諸兄鑒正寄函'), text)

    def test_huang_reply_full_text(self):
        # 友清氏が記事で示している2つの直し方だけを当てると、全組が読める。
        #  - 「O HI」は「CHI」に直せる（KONUOHIKE → KONUCHIKE）
        #  - このローマ字の YE は、2字目・3字目ではエ（2字目に入るのはア〜オ・カ〜コだけ）
        ctc = load_ctc()
        words = HUANG_REPLY_FULL.lower().replace('konuohike', 'konuchike').split()
        groups = groups_from_words(words)
        self.assertEqual(len(groups[-1]), 3)
        chars = []
        for g in groups:
            g = [g[0]] + [('エ' if x == 'ヱ' else x) for x in g[1:]]
            chars.append(ctc[decode(g)])
        # 『近代史資料』の活字は「護國軍能入湘贛」で、暗号文にある「速」がない
        self.assertEqual(''.join(chars),
                         '隱印崧詔鬯行諸兄鑒正寄函間適接哿電敬悉一切護國軍能速入湘贑'
                         '甚好行嚴何日東渡望速啓行先電示興徑')

    def test_tokenize(self):
        self.assertEqual(tokenize('shichitsufu'), ['シ', 'チ', 'ツ', 'フ'])
        self.assertEqual(tokenize('aEI'), ['ア', 'ヱ', 'ヰ'])


class TestTable(unittest.TestCase):
    def test_groups_csv_is_up_to_date(self):
        rows = [[str(x) for x in r] for r in build_groups.build()]
        with open(ROOT / 'data' / 'groups.csv', encoding='utf8') as f:
            saved = list(csv.reader(f))[1:]
        self.assertEqual(rows, saved)

    def test_codes_match_kana(self):
        ctc = load_ctc()
        with open(ROOT / 'data' / 'groups.csv', encoding='utf8') as f:
            for r in csv.DictReader(f):
                if r['電碼']:
                    self.assertEqual(decode(r['仮名']), int(r['電碼']), r)
                    self.assertEqual(ctc[int(r['電碼'])], r['字'], r)

    def test_group_count_and_signature(self):
        rows = build_groups.build()
        self.assertEqual(len(rows), 229)
        self.assertEqual(''.join(r[3] for r in rows[221:228]), '虎源楷羣泰釗哿')


if __name__ == '__main__':
    unittest.main()
