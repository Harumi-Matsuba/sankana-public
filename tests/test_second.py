"""2回目の書き起こし（second/）との一致率が、docs/METHOD.md の数字と合うことを確かめる。"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))

import second  # noqa: E402


class TestSecond(unittest.TestCase):
    def test_numbers_in_method(self):
        r = second.compare()
        self.assertEqual((r['words'], r['letters']), (126, 1265))
        self.assertEqual([x['diff_letters'] for x in r['runs']], [76, 72, 74])
        self.assertEqual(r['vote'], {'3of3': 60, '2of3': 55, 'split': 11})
        self.assertEqual((r['majority_same'], r['majority_diff']), (78, 37))


if __name__ == '__main__':
    unittest.main()
