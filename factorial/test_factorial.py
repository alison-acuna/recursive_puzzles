# TDD Factorial

# Test: if fact(n) == n*fact(n-1)
import unittest
import factorial

class TestMethods(unittest.TestCase):
    def test_factorial(self):
        n = 5
        self.assertEqual(factorial.fact(n), n*factorial.fact(n-1))

if __name__ == '__main__':
    unittest.main()
