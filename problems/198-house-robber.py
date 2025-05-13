# 198. House Robber
#
# Description:
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed. All houses at this place are arranged in a straight line.
# That means the first and the last house are not adjacent.
# Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police
# if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.
#
# Constraints:
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 400

from typing import List
import unittest


def rob(nums: List[int]) -> int:
    """
    Returns the maximum sum of non-adjacent elements in nums.
    """
    # TODO: Implement DP tracking include/exclude states
    pass

class TestHouseRobber(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"nums": [1, 2, 3, 1], "expected": 4, "id": "Example 1"},
            {"nums": [2, 7, 9, 3, 1], "expected": 12, "id": "Example 2"},
            {"nums": [], "expected": 0, "id": "Empty list"},
            {"nums": [5], "expected": 5, "id": "Single house"},
            {"nums": [2, 1], "expected": 2, "id": "Two houses"},
            {"nums": [2, 7, 9, 3, 1, 1], "expected": 14, "id": "Extended"}
        ]

    def test_rob(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = rob(case["nums"])
                self.assertIsInstance(result, int, "Result should be an integer")
                self.assertEqual(result, case["expected"], f"Mismatch for case '{case['id']}'")

if __name__ == "__main__":
    unittest.main()
