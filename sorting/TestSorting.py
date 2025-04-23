import unittest
import sys

from BubbleSort import bubble_sort
from BucketSort import bucket_sort
from HeapSort import heap_sort
from InsertionSort import insertion_sort
from MergeSort import merge_sort
from QuickSort import quick_sort
from SelectionSort import selection_sort
from ShellSort import shell_sort

class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            ([], []),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]),
            ([5, 2, 3, 2, 5], [2, 2, 3, 5, 5]),
            ([-5, -2, -8, -1, -9, -4], [-9, -8, -5, -4, -2, -1]),
            ([5, 3, 6, 1, 9, 0, 2], [0, 1, 2, 3, 5, 6, 9]),
            ([1], [1]),  # single-element list
            ([2, 2, 2, 2, 2], [2, 2, 2, 2, 2]),  # all elements equal
            ([float('inf'), 1, -1, float('-inf')], [float('-inf'), -1, 1, float('inf')]),  # including infinities
            ([0, -0.0, 0.0, -0, +0], [0, 0, 0, 0, 0]),  # testing zero variants
            ([1000000, -1000000, 0], [-1000000, 0, 1000000]),  # wide range
        ]

    def check_algorithm(self, sort_func, in_place=False):
        for original, expected in self.test_cases:
            data = original[:]
            if in_place:
                sort_func(data)
                self.assertEqual(data, expected)
            else:
                result = sort_func(data)
                self.assertEqual(result, expected)

    def test_bubble_sort(self):
        self.check_algorithm(bubble_sort)

    def test_bucket_sort(self):
        self.check_algorithm(bucket_sort)

    def test_heap_sort(self):
        self.check_algorithm(heap_sort, in_place=True)

    def test_insertion_sort(self):
        self.check_algorithm(insertion_sort, in_place=True)

    def test_merge_sort(self):
        self.check_algorithm(merge_sort)

    def test_quick_sort(self):
        self.check_algorithm(quick_sort)

    def test_selection_sort(self):
        self.check_algorithm(selection_sort, in_place=True)

    def test_shell_sort(self):
        self.check_algorithm(shell_sort, in_place=True)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv.pop()  # Remove extra arg so unittest doesn't misinterpret
        test_name = f"test_{arg}_sort"
        suite = unittest.TestSuite()
        suite.addTest(TestSortingAlgorithms(test_name))
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        unittest.main(verbosity=2)