# 152. Maximum Product Subarray
#
# Description:
# Given an integer array nums, find a contiguous non-empty subarray within the array that
# has the largest product, and return the product.
#
# Constraints:
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# Examples:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

from typing import List
import unittest


def maxProduct(nums: List[int]) -> int:
    """
    Returns the maximum product of a contiguous subarray within nums.
    """
    # TODO: Implement tracking both max and min products at each position
    pass

class TestMaximumProductSubarray(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"nums": [2, 3, -2, 4], "expected": 6, "id": "Example 1"},
            {"nums": [-2, 0, -1], "expected": 0, "id": "Example 2"},
            {"nums": [-2], "expected": -2, "id": "Single negative"},
            {"nums": [0, 2], "expected": 2, "id": "Zero then positive"},
            {"nums": [-2, -3, -4], "expected": 12, "id": "All negatives even count"},
            {"nums": [2, -5, -2, -4, 3], "expected": 24, "id": "Mixed large middle"},
        ]

    def test_max_product(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = maxProduct(case["nums"])
                self.assertIsInstance(result, int, "Result should be an integer")
                self.assertEqual(result, case["expected"], f"Mismatch for case '{case['id']}'")

if __name__ == "__main__":
    unittest.main()
