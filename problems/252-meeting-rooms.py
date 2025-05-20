# 252. Meeting Rooms
#
# Description:
# Given an array of meeting time intervals where intervals[i] = [start_i, end_i],
# determine if a person could attend all meetings.
#
# Constraints:
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= start_i < end_i <= 10^6
#
from typing import List
import unittest

def canAttendMeetings(intervals: List[List[int]]) -> bool:
    """
    Determines if a person can attend all meetings without overlap.
    Returns True if no intervals overlap, otherwise False.
    """
    intervals.sort(key=lambda x: x[0]) # sort intervals by the start time

    for i in range(1, len(intervals)): # start iteration at 1 because we want to our first loop to compare index 0 to index 1
        interval1 = intervals[i-1]
        interval2 = intervals[i]

        if interval1[1] > interval2[0]: # return false if interval1's end time is greater than interval2's start time
            return False

    return True



class TestCanAttendMeetings(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"intervals": [[0, 30], [5, 10], [15, 20]], "expected": False, "id": "Overlap exists"},
            {"intervals": [[7, 10], [2, 4]], "expected": True, "id": "No overlap"},
            {"intervals": [], "expected": True, "id": "Empty list"},
            {"intervals": [[5, 10]], "expected": True, "id": "Single meeting"},
            {"intervals": [[1, 2], [2, 3]], "expected": True, "id": "Boundary touching"},
            {"intervals": [[1, 5], [5, 8], [4, 6]], "expected": False, "id": "Partial overlap"},
        ]

    def test_can_attend_meetings(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = canAttendMeetings(case["intervals"])
                self.assertIsInstance(result, bool, "Result should be a boolean")
                self.assertEqual(
                    result,
                    case["expected"],
                    f"canAttendMeetings failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
