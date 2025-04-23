import unittest
from SelectionSort import selection_sort

class TestSelectionSort(unittest.TestCase):
    def test_empty_list(self):
        arr = []
        selection_sort(arr)
        self.assertEqual(arr, [])

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        selection_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reversed_list(self):
        arr = [5, 4, 3, 2, 1]
        selection_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_list_with_duplicates(self):
        arr = [5, 2, 8, 2, 5, 1]
        selection_sort(arr)
        self.assertEqual(arr, [1, 2, 2, 5, 5, 8])

    def test_general_list(self):
      arr = [5,3,6,1,9,0,2]
      selection_sort(arr)
      self.assertEqual(arr,[0,1,2,3,5,6,9])

if __name__ == '__main__':
    unittest.main()