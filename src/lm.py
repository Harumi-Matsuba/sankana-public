"""候補の順位付けに使う、漢字1字・2字の頻度モデル。

材料（どちらも手元に取得して、downloads/ に置く。リポジトリには含めない）:
  downloads/Unihan_Variants.txt … Unihan.zip（https://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip）の中のファイル
  downloads/dict.txt            … jieba の辞書（https://raw.githubusercontent.com/fxsjy/jieba/master/jieba/dict.txt）

jieba の辞書は現代の簡体字の語の頻度なので、繁体字は Unihan の kSimplifiedVariant で簡体字に寄せてから引く。
1916年の文語とは違うので、点数は候補を並べるための目安にとどめ、読みの根拠にはしない。
初回に outputs/lm.pkl を作り、2回目からはそれを読む。
"""
import collections
import math
import pickle

from kana import ROOT, load_ctc

DL = ROOT / 'downloads'
CACHE = ROOT / 'outputs' / 'lm.pkl'
FLOOR = -8.0


def _build():
    ctc = load_ctc()
    simp = {}
    for line in open(DL / 'Unihan_Variants.txt', encoding='utf8'):
        if '\tkSimplifiedVariant\t' in line:
            u, _, v = line.rstrip('\n').split('\t')
            simp[chr(int(u[2:], 16))] = chr(int(v.split()[0][2:], 16))
    uni, bi = collections.Counter(), collections.Counter()
    for line in open(DL / 'dict.txt', encoding='utf8'):
        p = line.split()
        if len(p) < 2:
            continue
        w, f = p[0], int(p[1])
        if not all('一' <= ch <= '鿿' for ch in w):
            continue
        for ch in w:
            uni[ch] += f
        for a, b in zip(w, w[1:]):
            bi[a + b] += f
    n = sum(uni.values())
    lu = {ch: math.log10(c / n) for ch, c in uni.items()}
    code2s = {k: simp.get(ch, ch) for k, ch in ctc.items()}
    obj = (ctc, code2s, lu, dict(bi), dict(uni))
    CACHE.parent.mkdir(exist_ok=True)
    pickle.dump(obj, open(CACHE, 'wb'))
    return obj


def load():
    if CACHE.exists():
        return pickle.load(open(CACHE, 'rb'))
    return _build()


def bigram_logp(model, a, b):
    """電碼 a の次に電碼 b が来るときの log10 確率（2字と1字の頻度を 0.7:0.3 で混ぜる）"""
    _ctc, code2s, lu, bi, uni = model
    sa, sb = code2s.get(a), code2s.get(b)
    if sb is None:
        return FLOOR - 4
    pu = 10 ** lu.get(sb, FLOOR)
    if sa and sa in uni:
        return math.log10(0.7 * bi.get(sa + sb, 0) / uni[sa] + 0.3 * pu)
    return math.log10(pu)
