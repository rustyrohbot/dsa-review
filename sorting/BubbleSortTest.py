import unittest
from BubbleSort import bubble_sort

class TestBubbleSort(unittest.TestCase):

    def test_empty_list(self):
        arr = []
        expected = []
        self.assertEqual(bubble_sort(arr), expected)

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(arr), expected)

    def test_reversed_list(self):
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(arr), expected)

    def test_list_with_duplicates(self):
        arr = [5, 2, 3, 2, 5]
        expected = [2, 2, 3, 5, 5]
        self.assertEqual(bubble_sort(arr), expected)
    
    def test_unsorted_list(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        expected = [1, 1, 2, 3, 4, 5, 6, 9]
        self.assertEqual(bubble_sort(arr), expected)

if __name__ == '__main__':
    unittest.main()