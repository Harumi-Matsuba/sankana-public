"""ローマ字原文（data/romaji_raw.txt）に修正（data/corrections.csv）を当て、
組ごとの表 data/groups.csv を作る。

  python3 src/build_groups.py

あわせて、修正後の転写 outputs/romaji_corrected.txt も書き出す（check.py などに渡せる）。

区分:
  変換式どおり … 原文の綴りのまま変換式で読めた組
  修正読み     … 語の綴りを直して読んだ組（corrections.csv の「語」の行）
  刊本で補う   … 原文が崩れていて、刊本の字で補った組
  推定         … 原文が崩れていて、文脈・返電から推定した組
  終わりの印   … 最後の組（オワリ）
"""
import csv
from kana import ROOT, decode, load_ctc, read_words, tokenize_spans



DATA = ROOT / 'data'


def load_corrections(path=DATA / 'corrections.csv'):
    words, groups = {}, {}
    with open(path, encoding='utf8') as f:
        for r in csv.DictReader(f):
            n = int(r['語番号または組番号'])
            if r['段階'] == '語':
                words[n] = (r['元の綴り'], r['修正後'])
            else:
                groups[n] = (r['修正後'], r['理由'].split('。')[0])
    return words, groups


def corrected_words():
    """原文の語の列に、corrections.csv の「語」の修正を当てたもの"""
    raw = read_words(DATA / 'romaji_raw.txt')
    wfix, _ = load_corrections()
    words = list(raw)
    for i, (old, new) in wfix.items():
        assert raw[i] == old, (i, raw[i], old)   # 修正表と原文がずれていないか
        words[i] = new
    return words


def build():
    wfix, gfix = load_corrections()
    words = corrected_words()
    # 仮名は語をまたいで続くことがある（例：語末の s と次の語頭の hi で shi）。
    # そこで、つないだ文字列を分解し、各仮名が始まる文字の位置から語番号を引く。
    owner_ch = [i for i, w in enumerate(words) for _ in w]
    spans = tokenize_spans(''.join(words))
    kana = [k for k, _, _ in spans]
    owner = [owner_ch[p] for _, p, _ in spans]
    ctc = load_ctc()
    rows = []
    for g in range(0, (len(kana) + 2) // 3):
        ks = kana[3 * g:3 * g + 3]
        ws = sorted(set(owner[3 * g:3 * g + 3]))
        c = decode(ks) if len(ks) == 3 else None
        ch = ctc.get(c, '') if c else ''
        kind = '修正読み' if any(w in wfix for w in ws) else '変換式どおり'
        if g in gfix:
            ch, kind = gfix[g]
            c = None
        if g == (len(kana) + 2) // 3 - 1 and ''.join(ks) == 'オワリ':
            ch, kind = '', '終わりの印'
        if not ch and kind != '終わりの印':
            kind = '読めない'
        rows.append([g, ''.join(ks), c or '', ch, kind, ' '.join(str(w) for w in ws)])
    return rows


if __name__ == '__main__':
    rows = build()
    with open(DATA / 'groups.csv', 'w', newline='', encoding='utf8') as f:
        w = csv.writer(f)
        w.writerow(['組', '仮名', '電碼', '字', '区分', '語番号'])
        w.writerows(rows)
    out = ROOT / 'outputs'
    out.mkdir(exist_ok=True)
    words = corrected_words()
    with open(out / 'romaji_corrected.txt', 'w', encoding='utf8') as f:
        f.write('# data/romaji_raw.txt に data/corrections.csv の語の修正を当てたもの（src/build_groups.py が生成）\n')
        for i in range(0, len(words), 3):
            f.write(' '.join(words[i:i + 3]) + '\n')
    from collections import Counter
    print(len(rows), '組', dict(Counter(r[4] for r in rows)))
