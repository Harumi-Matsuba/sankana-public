"""ローマ字の転写ファイルを組ごとに読んで一覧にする。規則に合わない組には印をつける。

  python3 src/check.py data/romaji_raw.txt            # 全部
  python3 src/check.py data/romaji_raw.txt 40 60      # 40〜59組目だけ
"""
import sys
from kana import decode, groups_from_words, load_ctc, read_words


def main(path, lo=None, hi=None):
    ctc = load_ctc()
    groups = groups_from_words(read_words(path))
    lo, hi = lo or 0, hi or len(groups)
    text = ''
    for i, g in enumerate(groups):
        c = decode(g) if len(g) == 3 else None
        ch = ctc.get(c, '□') if c else '？'
        text += ch
        if lo <= i < hi:
            print(i, ''.join(g), c or '', ch, '' if c else '<-- 規則外', sep='\t')
    print(text)


if __name__ == '__main__':
    a = sys.argv[1:]
    main(a[0], *(int(x) for x in a[1:3]))
