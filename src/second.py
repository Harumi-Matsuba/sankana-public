"""2回目の書き起こし（second/ の Codex 3回）と、data/romaji_raw.txt の一致率を出す。

  python3 src/second.py

一致率 = 1 − （語ごとに並べたときの、違う字の数）/（romaji_raw.txt の字数）。
Codex の不確かな字の候補（[a/o]）は外し、最初の読みだけを使う。書き足しの印（^）と点（.）も外す。
多数の読みは、語ごとに3回のうち2回以上が同じ綴りのとき、その綴り。
"""
import collections
import difflib
import re
from pathlib import Path

from kana import read_words

ROOT = Path(__file__).resolve().parent.parent


def norm(w):
    w = re.sub(r'\[[^\]]*\]', '', w)
    return w.replace('^', '').replace('.', '').lower()


def read_codex(path):
    words = []
    with open(path, encoding='utf8') as f:
        for line in f:
            m = re.match(r'S\d R\d+:\s*(.*)', line)
            if m:
                words += [norm(w) for w in m.group(1).split()]
    return words


def diff_letters(a, b):
    ops = difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes()
    return sum(max(i2 - i1, j2 - j1) for t, i1, i2, j1, j2 in ops if t != 'equal')


def compare():
    ours = [w.lower() for w in read_words(ROOT / 'data' / 'romaji_raw.txt')]
    runs = [read_codex(ROOT / 'second' / f'codex_run{r}.txt') for r in (1, 2, 3)]
    total = sum(len(w) for w in ours)
    out = {'words': len(ours), 'letters': total, 'runs': []}
    for run in runs:
        assert len(run) == len(ours)
        d = sum(diff_letters(a, b) for a, b in zip(ours, run))
        same = sum(a == b for a, b in zip(ours, run))
        out['runs'].append({'diff_letters': d, 'letter_agreement': 1 - d / total, 'same_words': same})
    vote = collections.Counter()
    maj_same = maj_diff = 0
    for i, w in enumerate(ours):
        top, n = collections.Counter(r[i] for r in runs).most_common(1)[0]
        vote[n] += 1
        if n >= 2:
            if top == w:
                maj_same += 1
            else:
                maj_diff += 1
    out['vote'] = {'3of3': vote[3], '2of3': vote[2], 'split': vote[1]}
    out['majority_same'] = maj_same
    out['majority_diff'] = maj_diff
    return out


def main():
    r = compare()
    print(f"romaji_raw.txt: {r['words']} 語・{r['letters']} 字")
    for k, x in enumerate(r['runs'], 1):
        print(f"Codex {k} 回目: 違う字 {x['diff_letters']}、字の一致率 {x['letter_agreement']:.1%}、"
              f"綴りが同じ語 {x['same_words']}/{r['words']}")
    v = r['vote']
    print(f"Codex 3回の語ごとの一致: 3回とも {v['3of3']}、2回 {v['2of3']}、ばらばら {v['split']}")
    print(f"多数の読みがある語のうち、romaji_raw.txt と同じ {r['majority_same']}、違う {r['majority_diff']}")


if __name__ == '__main__':
    main()
