
import quicksort

import unittest

class MyTest(unittest.TestCase):
    def test_quicksort_empty_list(self):
        self.assertEqual(quicksort.quicksort([]), [])
    def test_quicksort_empty_list_1_item(self):
        self.assertEqual(quicksort.quicksort([1]),[1])
    def test_quicksort_2_item(self):
        self.assertEqual(quicksort.quicksort([2,1]),[1,2])

if __name__ == '__main__':
    unittest.main()
