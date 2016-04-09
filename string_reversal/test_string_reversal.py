# test string reversal

import string_reversal

import unittest


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(string_reversal.str_reverse("string"), "gnirts")

if __name__ == '__main__':
    unittest.main()
