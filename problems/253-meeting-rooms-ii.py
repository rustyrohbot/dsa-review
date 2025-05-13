# 253. Meeting Rooms II
#
# Description:
# Given an array of meeting time intervals intervals where intervals[i] = [start_i, end_i],
# return the minimum number of conference rooms required to hold all the meetings.
#
# Constraints:
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= start_i < end_i <= 10^6
#
from typing import List
import unittest

def minMeetingRooms(intervals: List[List[int]]) -> int:
    """
    Returns the minimum number of conference rooms required so that all meetings
    can take place without overlaps.
    """
    # TODO: Implement using a min-heap or two-pointer technique
    pass

class TestMeetingRoomsII(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"intervals": [[0, 30], [5, 10], [15, 20]], "expected": 2, "id": "Example overlap"},
            {"intervals": [], "expected": 0, "id": "No meetings"},
            {"intervals": [[7, 10]], "expected": 1, "id": "Single meeting"},
            {"intervals": [[1, 5], [6, 10]], "expected": 1, "id": "No overlap"},
            {"intervals": [[1, 5], [2, 6], [3, 7]], "expected": 3, "id": "All overlap"},
            {"intervals": [[1, 5], [2, 3], [3, 6]], "expected": 2, "id": "Partial overlap"},
            {"intervals": [[2, 15], [36, 45], [9, 29], [16, 23]], "expected": 2, "id": "Unsorted intervals"},
        ]

    def test_min_meeting_rooms(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = minMeetingRooms(case["intervals"])
                self.assertIsInstance(result, int, "Result should be an integer")
                self.assertEqual(
                    result,
                    case["expected"],
                    f"minMeetingRooms failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
