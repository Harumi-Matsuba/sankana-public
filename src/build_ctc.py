"""Unihan の Unihan_OtherMappings.txt から、電碼→漢字の表 data/ctc_kTaiwanTelegraph.tsv を作り直す。

  1. https://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip を手元に取得して展開する
  2. python3 src/build_ctc.py <展開したフォルダ>/Unihan_OtherMappings.txt

同じ電碼に複数の字がある場合は、ファイルで先に出てくる字を採る。
"""
import sys
from kana import ROOT


def main(src):
    version = ''
    table = {}
    for line in open(src, encoding='utf8'):
        if line.startswith('# Unicode Version'):
            version = line.split('Version')[1].strip()
        if '\tkTaiwanTelegraph\t' not in line:
            continue
        u, _, v = line.rstrip('\n').split('\t')
        for x in v.split():
            table.setdefault(int(x), u)
    out = ROOT / 'data' / 'ctc_kTaiwanTelegraph.tsv'
    with open(out, 'w', encoding='utf8') as f:
        f.write(f'# 電碼（標準中国電碼）→ 漢字。Unicode Unihan データベース（Unicode {version}, '
                'Unihan_OtherMappings.txt）の kTaiwanTelegraph から抽出。\n')
        f.write('# © 2026 Unicode, Inc. 利用条件: https://www.unicode.org/terms_of_use.html'
                ' / ライセンス: https://www.unicode.org/license.txt\n')
        f.write('# 同じ電碼に複数の字がある場合は、ファイルで先に出てくる字を採った。\n')
        f.write('code\tcodepoint\tchar\n')
        for c in sorted(table):
            u = table[c]
            f.write(f'{c:04d}\t{u}\t{chr(int(u[2:], 16))}\n')
    print(len(table), '件 →', out)


if __name__ == '__main__':
    main(sys.argv[1])
