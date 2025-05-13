# 213. House Robber II
#
# Description:
# You are a professional robber planning to rob houses along a street arranged in a circle.
# That means the first and the last house are adjacent.
# Each house has a certain amount of money stashed.
# Determine the maximum amount of money you can rob tonight without alerting the police,
# ensuring you do not rob two adjacent houses (including the circle adjacency).
#
# Constraints:
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 400
#
# Examples:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: Rob house 2 (money = 3), cannot rob houses 1 or 3.
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob houses 1 and 3 (1 + 3 = 4).
#
# Input: nums = []
# Output: 0

from typing import List
import unittest


def rob(nums: List[int]) -> int:
    """
    Returns the maximum amount of money you can rob from a circular street of houses.
    """
    # TODO: Implement by taking max of two linear robber runs: nums[1:] and nums[:-1]
    pass

class TestHouseRobberII(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"nums": [2, 3, 2], "expected": 3, "id": "Example 1"},
            {"nums": [1, 2, 3, 1], "expected": 4, "id": "Example 2"},
            {"nums": [], "expected": 0, "id": "Empty list"},
            {"nums": [5], "expected": 5, "id": "Single house"},
            {"nums": [2, 7, 9, 3, 1], "expected": 11, "id": "Longer circle"},
            {"nums": [1,1,1,1], "expected": 2, "id": "All equal"},
        ]

    def test_rob_circular(self):
        for case in self.test_cases:
            with self.subTest(case["id"]):
                result = rob(case["nums"])
                self.assertIsInstance(result, int, "Result should be an integer")
                self.assertEqual(result, case["expected"], f"Mismatch for case '{case['id']}'")

if __name__ == "__main__":
    unittest.main()
