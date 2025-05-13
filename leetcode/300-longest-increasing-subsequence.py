# 300. Longest Increasing Subsequence
#
# Description:
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
#
# Constraints:
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
#
from typing import List
import unittest

def lengthOfLIS(nums: List[int]) -> int:
    """
    Computes the length of the longest strictly increasing subsequence in nums.
    """
    # TODO: Implement dynamic programming or patience sorting solution
    pass

class TestLongestIncreasingSubsequence(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"nums": [10,9,2,5,3,7,101,18], "expected": 4,  "id": "Example 1"},
            {"nums": [0,1,0,3,2,3],           "expected": 4,  "id": "Example 2"},
            {"nums": [7,7,7,7,7,7,7],         "expected": 1,  "id": "All same"},
            {"nums": [1,3,6,7,9,4,10,5,6],    "expected": 6,  "id": "Mixed sequence"},
            {"nums": [-1, -2, -3],            "expected": 1,  "id": "Decreasing negatives"},
            {"nums": [1],                     "expected": 1,  "id": "Single element"},
        ]

    def test_length_of_lis(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = lengthOfLIS(case["nums"])
                self.assertIsInstance(result, int, "Result should be an integer")
                self.assertEqual(
                    result,
                    case["expected"],
                    f"lengthOfLIS failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
