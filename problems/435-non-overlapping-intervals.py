# 435. Non-overlapping Intervals
#
# Description:
# Given an array of intervals where intervals[i] = [start_i, end_i],
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
#
# Constraints:
# 0 <= intervals.length <= 10^5
# intervals[i].length == 2
# -10^6 <= start_i < end_i <= 10^6
#
from typing import List
import unittest


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    """
    Returns the minimum number of intervals to remove to eliminate all overlapping intervals.
    """
    # TODO: Implement greedy algorithm by sorting by end times
    pass

class TestNonOverlappingIntervals(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"intervals": [[1,2],[2,3],[3,4],[1,3]], "expected": 1, "id": "Example 1"},
            {"intervals": [[1,2],[1,2],[1,2]],       "expected": 2, "id": "All identical"},
            {"intervals": [[1,2],[2,3]],             "expected": 0, "id": "No overlap"},
            {"intervals": [],                         "expected": 0, "id": "Empty"},
            {"intervals": [[0,5]],                   "expected": 0, "id": "Single interval"},
            {"intervals": [[2,3],[1,2],[1,3]],       "expected": 1, "id": "Unsorted list"},
        ]

    def test_erase_overlap_intervals(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = eraseOverlapIntervals(case["intervals"])
                self.assertIsInstance(result, int, "Result should be an integer")
                self.assertEqual(
                    result,
                    case["expected"],
                    f"eraseOverlapIntervals failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
# 435. Non-overlapping Intervals
#
# Description:
# Given an array of intervals where intervals[i] = [start_i, end_i],
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
#
# Constraints:
# 0 <= intervals.length <= 10^5
# intervals[i].length == 2
# -10^6 <= start_i < end_i <= 10^6
#
from typing import List
import unittest


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    """
    Returns the minimum number of intervals to remove to eliminate all overlapping intervals.
    """
    # TODO: Implement greedy algorithm by sorting by end times
    pass

class TestNonOverlappingIntervals(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"intervals": [[1,2],[2,3],[3,4],[1,3]], "expected": 1, "id": "Example 1"},
            {"intervals": [[1,2],[1,2],[1,2]],       "expected": 2, "id": "All identical"},
            {"intervals": [[1,2],[2,3]],             "expected": 0, "id": "No overlap"},
            {"intervals": [],                         "expected": 0, "id": "Empty"},
            {"intervals": [[0,5]],                   "expected": 0, "id": "Single interval"},
            {"intervals": [[2,3],[1,2],[1,3]],       "expected": 1, "id": "Unsorted list"},
        ]

    def test_erase_overlap_intervals(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = eraseOverlapIntervals(case["intervals"])
                self.assertIsInstance(result, int, "Result should be an integer")
                self.assertEqual(
                    result,
                    case["expected"],
                    f"eraseOverlapIntervals failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
