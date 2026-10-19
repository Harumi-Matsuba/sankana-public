"""崩れた区間について、置き換え・挿入・削除を合わせて MAXC 回まで認め、読める漢字列の候補を探す。

  python3 src/beam.py data/romaji_raw.txt 48 ナクタ [MAXC=3] [PEN=2.5]

  48     … 区間の最初の組番号
  ナクタ … 区間の直後に来るはずの仮名（目印）
前提: src/lm.py の材料を downloads/ に置いてあること。
48〜52組目は、この探索でも意味の通る候補が出ず、刊本で補った。
"""
import sys
from kana import S1, S2, S3, decode, read_words, tokenize
from lm import bigram_logp, load


def main(path, group, endpat, maxc=3, pen=2.5):
    model = load()
    ctc = model[0]
    k = tokenize(''.join(read_words(path)))
    start = group * 3
    flat = ''.join(x if len(x) == 1 else '?' for x in k)
    end = flat.index(endpat, start)
    seg = k[start:end]
    print('区間', ''.join(seg), len(seg))
    prevc, nextc = decode(k[start - 3:start]), decode(list(endpat[:3]))

    def gen(p, slot, acc, c):
        if slot == 3:
            yield p, acc, c
            return
        S = (S1, S2, S3)[slot]
        if p < len(seg):
            x = seg[p]
            if x in S:
                yield from gen(p + 1, slot + 1, acc + x, c)
            if c < maxc:
                for y in S:
                    if y != x:
                        yield from gen(p + 1, slot + 1, acc + y, c + 1)   # 置き換え
                yield from gen(p + 1, slot, acc, c + 1)                    # 観測の1字を削る
        if c < maxc:
            for y in S:
                yield from gen(p, slot + 1, acc + y, c + 1)                # 1字を補う

    beam, results = [(0.0, 0, 0, prevc, '')], []
    for _ in range(12):
        nb = []
        for sc, pos, cost, pc, txt in beam:
            if pos == len(seg):
                results.append((sc + bigram_logp(model, pc, nextc), cost, txt))
                continue
            for p2, g, c2 in gen(pos, 0, '', cost):
                code = decode(g)
                if code in ctc:
                    nb.append((sc + bigram_logp(model, pc, code) - pen * (c2 - cost),
                               p2, c2, code, txt + ctc[code]))
        nb.sort(reverse=True)
        beam = nb[:4000]
        if not beam:
            break
    seen = set()
    for sc, cost, txt in sorted(results, reverse=True):
        if txt in seen:
            continue
        seen.add(txt)
        print(round(sc, 2), cost, txt)
        if len(seen) >= 15:
            break


if __name__ == '__main__':
    a = sys.argv[1:]
    main(a[0], int(a[1]), a[2], *(int(a[3]),) if len(a) > 3 else (), *(float(a[4]),) if len(a) > 4 else ())
