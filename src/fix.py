"""指定した組について、仮名1字を置き換えた候補を、前後の字とのつながりで順位付けする。

  python3 src/fix.py data/romaji_raw.txt 39,57

前提: src/lm.py の材料を downloads/ に置いてあること。
順位は目安で、読みの決定には、刊本・日本側の書き込み・文脈などの別の根拠を使った。
"""
import sys
from kana import S1, S2, S3, decode, groups_from_words, read_words
from lm import bigram_logp, load


def main(path, targets):
    model = load()
    ctc = model[0]
    groups = groups_from_words(read_words(path))
    codes = [decode(g) if len(g) == 3 else None for g in groups]
    for i in targets:
        g = groups[i]
        prev = codes[i - 1] if i > 0 else None
        nxt = codes[i + 1] if i + 1 < len(codes) else None
        cands = set()
        for pos, S in enumerate((S1, S2, S3)):
            for x in S:
                gg = list(g)
                if pos < len(gg):
                    gg[pos] = x
                c = decode(gg)
                if c in ctc:
                    score = bigram_logp(model, prev, c) + (bigram_logp(model, c, nxt) if nxt else 0)
                    cands.add((score, ''.join(gg), c, ctc[c]))
        cands = sorted(cands, reverse=True)
        show = lambda c: ctc.get(c, '？') if c else '-'
        print(i, ''.join(g), show(codes[i]), '前', show(prev), '次', show(nxt))
        print('   ', ' '.join(f'{gg}{ch}' for _, gg, _, ch in cands[:15]))


if __name__ == '__main__':
    main(sys.argv[1], [int(x) for x in sys.argv[2].split(',')])
