import unittest
from BucketSort import bucket_sort

class TestBucketSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(bucket_sort([]), [])

    def test_sorted_list(self):
        self.assertEqual(bucket_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(bucket_sort([5, 2, 8, 1, 9, 4]), [1, 2, 4, 5, 8, 9])

    def test_negative_numbers(self):
        self.assertEqual(bucket_sort([-5, -2, -8, -1, -9, -4]), [-9, -8, -5, -4, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(bucket_sort([-5, 2, -8, 1, 9, -4]), [-8, -5, -4, 1, 2, 9])

    def test_duplicate_numbers(self):
        self.assertEqual(bucket_sort([5, 2, 8, 1, 9, 4, 2, 1]), [1, 1, 2, 2, 4, 5, 8, 9])

    def test_large_numbers(self):
        self.assertEqual(bucket_sort([500, 200, 800, 100, 900, 400]), [100, 200, 400, 500, 800, 900])

if __name__ == '__main__':
    unittest.main()