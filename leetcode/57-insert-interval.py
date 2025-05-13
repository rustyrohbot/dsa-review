# 57. Insert Interval
#
# Description:
# You are given an array of non-overlapping intervals "intervals" where intervals[i] = [start_i, end_i]
# sorted in ascending order by start_i, and a new interval "newInterval" = [start, end].
# Insert "newInterval" into "intervals" such that the intervals remain non-overlapping and sorted.
# Merge overlapping intervals if necessary.
#
# Constraints:
# 0 <= len(intervals) <= 10^4
# intervals[i].length == 2
# 0 <= start_i <= end_i <= 10^5
# newInterval.length == 2
# 0 <= start <= end <= 10^5
#
# Examples:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]

import unittest
from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    Inserts a new interval into a list of sorted, non-overlapping intervals, merging if necessary.

    Parameters:
        intervals (List[List[int]]): Sorted list of non-overlapping intervals.
        newInterval (List[int]): Interval to insert.
    Returns:
        List[List[int]]: Updated list of merged intervals.
    """
    # TODO: Implement the insertion and merging logic here
    pass


class TestInsertInterval(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"intervals": [[1, 3], [6, 9]], "newInterval": [2, 5],
             "expected": [[1, 5], [6, 9]], "id": "Overlap merge"},
            {"intervals": [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], "newInterval": [4, 8],
             "expected": [[1, 2], [3, 10], [12, 16]], "id": "Multiple overlap"},
            {"intervals": [], "newInterval": [5, 7],
             "expected": [[5, 7]], "id": "Empty intervals"},
            {"intervals": [[1, 5]], "newInterval": [2, 3],
             "expected": [[1, 5]], "id": "Contained new interval"},
            {"intervals": [[1, 5]], "newInterval": [6, 8],
             "expected": [[1, 5], [6, 8]], "id": "Append no overlap"},
            {"intervals": [[3, 5]], "newInterval": [1, 2],
             "expected": [[1, 2], [3, 5]], "id": "Prepend no overlap"},
        ]

    def test_insert_interval(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = insert(case["intervals"], case["newInterval"])
                # Validate return type
                self.assertIsInstance(result, list, "Result should be a list of intervals")
                # Validate interval structure
                for interval in result:
                    self.assertIsInstance(interval, list, "Each interval should be a list of two ints")
                    self.assertEqual(len(interval), 2)
                    self.assertIsInstance(interval[0], int)
                    self.assertIsInstance(interval[1], int)
                # Compare as sorted lists
                self.assertEqual(
                    sorted(result),
                    sorted(case["expected"]),
                    f"Case '{case['id']}' failed: got {result}, expected {case['expected']}"
                )


if __name__ == "__main__":
    unittest.main()
