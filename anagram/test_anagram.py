import unittest
import anagram


class MyTest(unittest.TestCase):
    def test_anagram(self):
        self.assertEqual(anagram.anagram("cat"), {"cat", "act", "atc", "tca", "tac", "cta"})

if __name__ == '__main__':
    unittest.main()
