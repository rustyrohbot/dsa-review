# 55. Jump Game
#
# Description:
# Given an array of non-negative integers nums, you are initially positioned at the first index.
# Each element represents your maximum jump length at that position.
# Determine if you are able to reach the last index.
#
# Constraints:
# 1 <= len(nums) <= 10^4
# 0 <= nums[i] <= 10^5
#
# Examples:
# Input: nums = [2,3,1,1,4]   Output: True
# Input: nums = [3,2,1,0,4]   Output: False

import unittest
from typing import List


def canJump(nums: List[int]) -> bool:
    """
    Determines if the last index can be reached from the start.

    Parameters:
        nums (List[int]): List of maximum jump lengths.
    Returns:
        bool: True if reachable, False otherwise.
    """
    # TODO: Implement the greedy solution here
    pass


class TestJumpGame(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"nums": [2, 3, 1, 1, 4],       "expected": True,  "id": "Example 1"},
            {"nums": [3, 2, 1, 0, 4],       "expected": False, "id": "Example 2"},
            {"nums": [0],                  "expected": True,  "id": "Single element"},
            {"nums": [0, 2, 3],            "expected": False, "id": "Zero at start"},
            {"nums": [5, 4, 0, 0, 0, 0],    "expected": True,  "id": "Large initial jump"},
            {"nums": [1, 1, 1, 0],          "expected": True,  "id": "Just enough jumps"},
            {"nums": [2, 0, 0],             "expected": True,  "id": "Zeros after first"},
            {"nums": [1, 0, 1],             "expected": False, "id": "Stuck in middle"},
        ]

    def test_can_jump(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = canJump(case["nums"])
                self.assertIsInstance(result, bool, "Result should be a boolean")
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed for nums={case['nums']}"
                )


if __name__ == "__main__":
    unittest.main()
