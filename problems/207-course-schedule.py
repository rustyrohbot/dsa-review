# 207. Course Schedule
#
# Description:
# There are numCourses courses you have to take, labeled from 0 to numCourses-1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi]
# indicates that you must take course bi first if you want to take course ai.
# Return true if you can finish all courses. Otherwise, return false.
#
# Constraints:
# 1 <= numCourses <= 10^5
# 0 <= prerequisites.length <= 10^5
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
#
# Examples:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should have finished course 1. This is impossible.

from typing import List
import unittest


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Determines if you can finish all courses given the prerequisites.
    """
    # TODO: Implement cycle detection using DFS or Kahn's topological sort
    pass

class TestCourseSchedule(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"numCourses": 2, "prerequisites": [[1, 0]], "expected": True, "id": "Simple chain"},
            {"numCourses": 2, "prerequisites": [[1, 0], [0, 1]], "expected": False, "id": "Cycle detection"},
            {"numCourses": 3, "prerequisites": [[1, 0], [2, 1]], "expected": True, "id": "Longer chain"},
            {"numCourses": 4, "prerequisites": [], "expected": True, "id": "No prerequisites"},
            {"numCourses": 5, "prerequisites": [[1,0],[2,0],[3,1],[3,2],[4,3]], "expected": True, "id": "Complex DAG"},
            {"numCourses": 3, "prerequisites": [[1,0],[2,0],[0,2]], "expected": False, "id": "Cycle with root"},
        ]

    def test_can_finish(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = canFinish(case["numCourses"], case["prerequisites"])
                self.assertIsInstance(result, bool, "Result should be a boolean")
                self.assertEqual(result, case["expected"], f"Mismatch for case '{case['id']}'")

if __name__ == "__main__":
    unittest.main()
