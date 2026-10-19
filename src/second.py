"""2回目の書き起こし（second/ の Codex）と、data/romaji_raw.txt の一致率を出す。

  python3 src/second.py

- 1〜3回目（codex_run1〜3）：照合の記録。この比較を見て romaji_raw.txt の5語を直したので、独立の2回目とは呼ばない。
- 4回目（codex_run4）：直した後に、新しい文脈で、答えを見せずに読ませたもの。これを独立の2回目とする。

一致率 = 1 − （語ごとに並べたときの、違う字の数）/（romaji_raw.txt の字数）。
Codex の不確かな字の候補（[a/o]）は外し、最初の読みだけを使う。書き足しの印（^）と点（.）も外す。
多数の読みは、語ごとに3回のうち2回以上が同じ綴りのとき、その綴り。
"""
import collections
import difflib
import re
import sys
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
    run4 = read_codex(ROOT / 'second' / 'codex_run4.txt')
    assert len(run4) == len(ours)
    d = sum(diff_letters(a, b) for a, b in zip(ours, run4))
    out['independent'] = {'diff_letters': d, 'letter_agreement': 1 - d / total,
                          'same_words': sum(a == b for a, b in zip(ours, run4))}
    return out


# 照合（1〜3回目）を見て直した5語。語番号（0から）→（照合した時点の綴り、直した後の綴り）
FIXED = {46: ('huuchitaka', 'hiuchitaka'), 58: ('nikochitak', 'rikochitak'), 63: ('echiuashit', 'echinashit'),
         96: ('takaonomie', 'takaononie'), 116: ('esatefumika', 'esatefmika')}


def crosscheck_rows():
    """照合した時点の1回目と Codex 1〜3回目の多数の読みが違った語と、その扱い。"""
    ours = [w.lower() for w in read_words(ROOT / 'data' / 'romaji_raw.txt')]
    old = list(ours)
    for i, (before, after) in FIXED.items():
        assert ours[i] == after
        old[i] = before
    runs = [read_codex(ROOT / 'second' / f'codex_run{r}.txt') for r in (1, 2, 3)]
    rows = []
    for i, w in enumerate(old):
        top, n = collections.Counter(r[i] for r in runs).most_common(1)[0]
        if n < 2 or top == w:
            continue
        if i in FIXED:
            d = '直した：画像で確かめて、1回目の読み違いと判断 / corrected: confirmed on the image as a misreading in the first pass'
        elif i == 121:
            d = ('直さない：画像で a の上に小さな o の書き足しを確かめ、字どおりの転写は残し、corrections.csv の修正の根拠に加えた'
                 ' / not changed: the small o written above the a was confirmed on the image; kept in the literal transcription and added to the grounds of the correction in corrections.csv')
        else:
            d = ('直さない：Codex の読みを当てると解読が崩れる（内訳は VERIFICATION.md 第2節）。画像で確かめた記録はない'
                 ' / not changed: the Codex reading breaks the decoding (breakdown in VERIFICATION §2); no record of an image check')
        rows.append((i, w, top, ours[i], d))
    return rows


def main():
    r = compare()
    print(f"romaji_raw.txt: {r['words']} 語・{r['letters']} 字")
    x = r['independent']
    print(f"独立の2回目（Codex 4回目）: 違う字 {x['diff_letters']}、字の一致率 {x['letter_agreement']:.1%}、"
          f"綴りが同じ語 {x['same_words']}/{r['words']}")
    print('照合の記録（Codex 1〜3回目。これを見て5語を直した）:')
    for k, x in enumerate(r['runs'], 1):
        print(f"Codex {k} 回目: 違う字 {x['diff_letters']}、字の一致率 {x['letter_agreement']:.1%}、"
              f"綴りが同じ語 {x['same_words']}/{r['words']}")
    v = r['vote']
    print(f"Codex 3回の語ごとの一致: 3回とも {v['3of3']}、2回 {v['2of3']}、ばらばら {v['split']}")
    print(f"多数の読みがある語のうち、romaji_raw.txt と同じ {r['majority_same']}、違う {r['majority_diff']}")


if __name__ == '__main__':
    if '--crosscheck' in sys.argv:
        print('# EN: Words where the majority of Codex runs 1-3 differed from the first transcription at the time of the check (python3 src/second.py --crosscheck). word number (from 0), first transcription at the time, Codex majority, current data/romaji_raw.txt, decision')
        print('# 照合した時点の1回目と、Codex 1〜3回目の多数の読みが違った語。語番号（0から）、照合した時点の1回目、Codex の多数、今の data/romaji_raw.txt、扱い')
        print('word\tfirst_at_check\tcodex_majority\tcurrent\tdecision')
        for r in crosscheck_rows():
            print('\t'.join(map(str, r)))
    else:
        main()
