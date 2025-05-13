# 56. Merge Intervals
#
# Description:
# Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
# Constraints:
# 0 <= len(intervals) <= 10^4
# intervals[i].length == 2
# 0 <= start_i <= end_i <= 10^5
#
# Examples:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]

import unittest
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merges overlapping intervals and returns a list of the merged intervals.

    Parameters:
        intervals (List[List[int]]): List of [start, end] intervals.
    Returns:
        List[List[int]]: List of merged, non-overlapping intervals sorted by start.
    """
    # TODO: Implement the sort-and-scan merge solution here
    pass


class TestMergeIntervals(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"intervals": [[1,3],[2,6],[8,10],[15,18]], "expected": [[1,6],[8,10],[15,18]], "id": "Example 1"},
            {"intervals": [[1,4],[4,5]],              "expected": [[1,5]],             "id": "Example 2"},
            {"intervals": [],                          "expected": [],                  "id": "Empty input"},
            {"intervals": [[5,7]],                     "expected": [[5,7]],             "id": "Single interval"},
            {"intervals": [[1,10],[2,3],[4,8]],        "expected": [[1,10]],            "id": "Nested intervals"},
            {"intervals": [[2,3],[1,4],[6,8]],         "expected": [[1,4],[6,8]],      "id": "Unordered input"},
        ]

    def test_merge(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = merge(case["intervals"])
                # Validate return type
                self.assertIsInstance(result, list, "Result should be a list of intervals")
                for interval in result:
                    self.assertIsInstance(interval, list, "Each interval should be a list of two integers")
                    self.assertEqual(len(interval), 2, "Each interval must have exactly two elements")
                    self.assertIsInstance(interval[0], int)
                    self.assertIsInstance(interval[1], int)
                # Compare sorted results by start
                self.assertEqual(
                    sorted(result),
                    sorted(case["expected"]),
                    f"Case '{case['id']}' failed: got {result}, expected {case['expected']}"
                )


if __name__ == "__main__":
    unittest.main()
