import unittest
from HeapSort import heap_sort

class TestHeapSort(unittest.TestCase):

    def test_empty_list(self):
        arr = []
        heap_sort(arr)
        self.assertEqual(arr, [])

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        heap_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        arr = [5, 4, 3, 2, 1]
        heap_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        heap_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 4, 5, 6, 9])
    
    def test_duplicate_elements(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 1]
        heap_sort(arr)
        self.assertEqual(arr, [1, 1, 1, 2, 3, 4, 5, 6, 9])

if __name__ == '__main__':
    unittest.main()