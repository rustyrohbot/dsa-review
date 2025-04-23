import unittest
from InsertionSort import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def test_empty_list(self):
        arr = []
        insertion_sort(arr)
        self.assertEqual(arr, [])

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reversed_list(self):
        arr = [5, 4, 3, 2, 1]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_list_with_duplicates(self):
        arr = [5, 2, 8, 2, 5, 1]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 2, 5, 5, 8])

    def test_negative_numbers(self):
      arr = [-1, -5, -3, -2]
      insertion_sort(arr)
      self.assertEqual(arr, [-5, -3, -2, -1])

if __name__ == '__main__':
    unittest.main()