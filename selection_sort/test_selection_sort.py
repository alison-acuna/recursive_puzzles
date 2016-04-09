import unittest
import selection_sort



class MyTest(unittest.TestCase):
    def test_selection_sort_empty_list(self):
        self.assertEqual(selection_sort.selection_sort([]), [])
    def test_selection_sort_1_item(self):
        self.assertEqual(selection_sort.selection_sort([1]),[1])
    def test_selection_sort_2_item(self):
        self.assertEqual(selection_sort.selection_sort([2,1]),[1,2])
    def test_selection_sort_4_item(self):
        self.assertEqual(selection_sort.selection_sort([2,1,3,1]),[1,1,2,3])


if __name__ == '__main__':
    unittest.main()
