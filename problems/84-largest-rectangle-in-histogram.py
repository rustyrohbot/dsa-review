# 84. Largest Rectangle in Histogram
#
# Description:
# Given an array heights representing the histogram's bar heights where the width of each bar is 1,
# return the area of the largest rectangle in the histogram.
#
# Constraints:
# 1 <= len(heights) <= 10^5
# 0 <= heights[i] <= 10^4
#
# Examples:
# Input: heights = [2,1,5,6,2,3]
# Output: 10  # The largest rectangle has area 10 (bars at indices 2 and 3 of heights 5 and 6)
#
import unittest
from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    """
    Calculates the area of the largest rectangle in the histogram.

    Parameters:
        heights (List[int]): List of non-negative integers representing bar heights.

    Returns:
        int: Maximum rectangular area under the histogram.
    """
    # TODO: Implement the solution here
    pass


class TestLargestRectangleHistogram(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"heights": [2, 1, 5, 6, 2, 3], "expected": 10, "id": "Example"},
            {"heights": [], "expected": 0, "id": "Empty"},
            {"heights": [1], "expected": 1, "id": "Single bar"},
            {"heights": [2, 2, 2], "expected": 6, "id": "Flat bars"},
            {"heights": [5, 4, 3, 2, 1], "expected": 9, "id": "Descending"},
            {"heights": [1, 2, 3, 4, 5], "expected": 9, "id": "Ascending"},
            {"heights": [0,1,0,2,1,0,1,3,2,1,2,1], "expected": 6, "id": "Complex"},
        ]

    def test_largest_rectangle_area(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = largestRectangleArea(case["heights"])
                # Validate return type
                self.assertIsInstance(result, int, "Result should be an integer")
                # Validate correctness
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed for heights {case['heights']}"
                )


if __name__ == "__main__":
    unittest.main()
