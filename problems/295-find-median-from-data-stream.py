# 295. Find Median from Data Stream
#
# Description:
# The MedianFinder class supports adding numbers from a data stream and finding the median of
# all elements added so far.
#
# Constraints:
# -10^5 <= value <= 10^5
# At most 10^5 calls will be made to addNum and findMedian.

import heapq
import unittest

class MedianFinder:
    def __init__(self):
        """Initialize two heaps: a max-heap for the lower half and a min-heap for the upper half."""
        # TODO: Initialize data structures
        pass

    def addNum(self, num: int) -> None:
        """
        Adds a number into the data structure.
        """
        # TODO: Add number to one of the heaps and rebalance
        pass

    def findMedian(self) -> float:
        """
        Returns the median of all elements so far.
        """
        # TODO: Compute median based on heap sizes
        pass

class TestMedianFinder(unittest.TestCase):
    def test_basic_operations(self):
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        self.assertAlmostEqual(mf.findMedian(), 1.5, msg="Median of [1,2] should be 1.5")
        mf.addNum(3)
        self.assertAlmostEqual(mf.findMedian(), 2.0, msg="Median of [1,2,3] should be 2.0")

    def test_even_odd_sequence(self):
        mf = MedianFinder()
        inputs = [5, 15, 1, 3]
        expected_medians = [5.0, 10.0, 5.0, 4.0]
        results = []
        for num in inputs:
            mf.addNum(num)
            results.append(mf.findMedian())
        self.assertEqual(results, expected_medians, f"Expected medians {expected_medians} but got {results}")

    def test_negative_and_duplicates(self):
        mf = MedianFinder()
        for num in [-1, -2, -3, -4, -5]:
            mf.addNum(num)
        # sequence: [-1] -> -1, [-2,-1] -> -1.5, [-3,-2,-1] -> -2, [-4,-3,-2,-1] -> -2.5, [-5,-4,-3,-2,-1] -> -3
        expected = [-1.0, -1.5, -2.0, -2.5, -3.0]
        results = []
        mf = MedianFinder()
        for num in [-1, -2, -3, -4, -5]:
            mf.addNum(num)
            results.append(mf.findMedian())
        self.assertEqual(results, expected, f"Expected medians {expected} but got {results}")

if __name__ == "__main__":
    unittest.main()
