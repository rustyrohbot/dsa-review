# 53. Maximum Subarray
#
# Description:
# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
#
# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
# Examples:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]  Output: 6  # [4,-1,2,1] has the largest sum
# Input: nums = [1]                      Output: 1
# Input: nums = [5,4,-1,7,8]             Output: 23

import unittest
from typing import List


def maxSubArray(nums: List[int]) -> int:
    """
    Returns the sum of the contiguous subarray with the largest sum.

    Parameters:
        nums (List[int]): List of integers.
    Returns:
        int: Maximum subarray sum.
    """
    # TODO: Implement Kadane's algorithm or similar here
    pass


class TestMaximumSubarray(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"nums": [-2,1,-3,4,-1,2,1,-5,4], "expected": 6,  "id": "Example 1"},
            {"nums": [1],                      "expected": 1,  "id": "Single positive"},
            {"nums": [-1],                     "expected": -1, "id": "Single negative"},
            {"nums": [5,4,-1,7,8],             "expected": 23, "id": "All positive except one"},
            {"nums": [-2,-3,-1,-5],            "expected": -1, "id": "All negative"},
            {"nums": [0,0,0],                  "expected": 0,  "id": "All zeros"},
            {"nums": [2,-1,2,3,4,-5],          "expected": 10, "id": "Mixed values"},
        ]

    def test_max_subarray(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = maxSubArray(case["nums"])
                # Validate return type
                self.assertIsInstance(result, int, "Result should be an integer")
                # Validate correctness
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed for nums={case['nums']}"
                )


if __name__ == "__main__":
    unittest.main()
