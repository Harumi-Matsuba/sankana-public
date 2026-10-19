"""三仮名コード（1916年）の変換式と、ローマ字原文の分解。

変換式は友清理士氏（Cryptiana, chinesecrypto_e2.htm, 2026-09-23 追記）が特定したもの。
電碼 c から仮名3字を作る（1字目の表が46字なので、表せるのは 1〜9199）:
  1字目 = S1[c // 200]
  2字目 = S2[(c - 1) % 10]
  3字目 = S3[((c - 1) // 10) % 20]
ここではその逆（仮名3字→電碼）も実装する。

注意：この式では、200の倍数の電碼（200, 400, …）は1字目が次の行に進み、2・3字目が「コサ」になる
（例：200→カコサ）。逆に「アコサ」はどの電碼にもならない。友清氏の Excel の式（INT(A1/200)）のとおりに
実装したが、今回の2通の電報と黄興の返電には「コサ」で終わる組がなく、実際の電文での確認はできていない。
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

S1 = "アカサタナハマヤラワイキシチニヒミリヰウクスツヌフムユルエケセテネヘメレヱオコソトノホモヨロ"
S2 = "アイウエオカキクケコ"
S3 = "ホヘフヒハノネヌニナトテツチタソセスシサ"

VOWELS = {'a': 'ア', 'i': 'イ', 'u': 'ウ', 'e': 'エ', 'o': 'オ',
          'E': 'ヱ', 'I': 'ヰ'}          # 大文字 E/I はヱ/ヰ（ローマ字では区別できないため、修正で明示する）
SPECIAL = [('shi', 'シ'), ('chi', 'チ'), ('tsu', 'ツ'), ('fu', 'フ'),
           ('si', 'シ'), ('ti', 'チ'), ('tu', 'ツ'), ('hu', 'フ'),
           ('wi', 'ヰ'), ('we', 'ヱ'), ('ye', 'ヱ')]
ROWS = {'k': 'カキクケコ', 's': 'サシスセソ', 't': 'タチツテト', 'n': 'ナニヌネノ',
        'h': 'ハヒフヘホ', 'm': 'マミムメモ', 'y': 'ヤ?ユ?ヨ', 'r': 'ラリルレロ',
        'w': 'ワヰ?ヱヲ'}


def encode(code):
    """電碼 → 仮名3字"""
    if not 1 <= code < 200 * len(S1):
        raise ValueError(code)
    return S1[code // 200] + S2[(code - 1) % 10] + S3[((code - 1) // 10) % 20]


def decode(group):
    """仮名3字 → 電碼。規則に合わない組は None。"""
    if len(group) != 3:
        return None
    try:
        a, u, t = S1.index(group[0]), S2.index(group[1]), S3.index(group[2])
    except ValueError:
        return None
    if u == 9 and t == 19:          # 2・3字目が「コサ」：200の倍数（上の注意を参照）
        return 200 * a if a > 0 else None
    return 200 * a + 10 * t + u + 1


def tokenize_spans(s):
    """ローマ字の文字列を仮名に分ける。(仮名, 始まりの位置, 文字数) の列を返す。
    読めない文字は [x] として1つの仮名と数える。"""
    out, i = [], 0
    while i < len(s):
        for sp, k in SPECIAL:
            if s.startswith(sp, i):
                out.append((k, i, len(sp)))
                break
        else:
            c = s[i]
            if c in VOWELS:
                out.append((VOWELS[c], i, 1))
            elif c in ROWS and i + 1 < len(s) and s[i + 1] in 'aiueo':
                k = ROWS[c]['aiueo'.index(s[i + 1])]
                out.append((k if k != '?' else '[' + s[i:i + 2] + ']', i, 2))
            elif c == 'n':
                out.append(('ン', i, 1))
            else:
                out.append(('[' + c + ']', i, 1))
        i += out[-1][2]
    return out


def tokenize(s):
    return [k for k, _, _ in tokenize_spans(s)]


def read_words(path):
    """転写ファイル（# で始まる行は注記）から語の列を読む。"""
    with open(path, encoding='utf8') as f:
        return [w for line in f if not line.startswith('#') for w in line.split()]


def groups_from_words(words):
    k = tokenize(''.join(words))
    return [k[i:i + 3] for i in range(0, len(k), 3)]


def load_ctc(path=ROOT / 'data' / 'ctc_kTaiwanTelegraph.tsv'):
    """電碼 → 漢字の表（Unihan kTaiwanTelegraph から抽出したもの）"""
    table = {}
    with open(path, encoding='utf8') as f:
        for line in f:
            if line.startswith('#') or line.startswith('code'):
                continue
            code, _cp, ch = line.rstrip('\n').split('\t')
            table[int(code)] = ch
    return table
