import unittest
from QuickSort import quick_sort

class TestQuickSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(quick_sort([]), [])

    def test_sorted_list(self):
        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        
    def test_unsorted_list(self):
        self.assertEqual(quick_sort([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])

    def test_list_with_duplicates(self):
        self.assertEqual(quick_sort([3, 1, 4, 1, 5, 3]), [1, 1, 3, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()