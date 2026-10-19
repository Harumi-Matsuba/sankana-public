"""2回目の書き起こし（second/）との一致率が、docs/METHOD.md の数字と合うことを確かめる。"""
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'src'))

import second  # noqa: E402


class TestSecond(unittest.TestCase):
    def test_numbers_in_method(self):
        r = second.compare()
        self.assertEqual((r['words'], r['letters']), (126, 1265))
        self.assertEqual([x['diff_letters'] for x in r['runs']], [76, 72, 74])
        self.assertEqual(r['vote'], {'3of3': 60, '2of3': 55, 'split': 11})
        self.assertEqual((r['majority_same'], r['majority_diff']), (78, 37))
        self.assertEqual((r['independent']['diff_letters'], r['independent']['same_words']), (68, 76))


    def test_crosscheck_list(self):
        rows = second.crosscheck_rows()
        self.assertEqual(len(rows), 42)
        self.assertEqual(sum(r[4].startswith('直した') for r in rows), 5)
        out = subprocess.run([sys.executable, str(ROOT / 'src' / 'second.py'), '--crosscheck'],
                             capture_output=True, text=True, check=True).stdout
        self.assertEqual(out, (ROOT / 'second' / 'crosscheck_decisions.tsv').read_text(encoding='utf8'))


if __name__ == '__main__':
    unittest.main()
