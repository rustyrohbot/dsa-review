# 1. Two Sum
#
# Description:
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# You can return the answer in any order.
#
# Constraints:
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.

from typing import List
import unittest


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Finds two numbers in the list that add up to the target.
    Returns their indices.
    """
    indexes = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in indexes:
            return [indexes[diff], i]
        indexes[n] = i


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1], "id": "Example 1"},
            {"nums": [3, 2, 4], "target": 6, "expected": [1, 2], "id": "Example 2"},
            {"nums": [3, 3], "target": 6, "expected": [0, 1], "id": "Example 3"},
            {"nums": [0, 4, 3, 0], "target": 0, "expected": [0, 3], "id": "Zeros"},
            {"nums": [-1, -3, 5, 7], "target": 4, "expected": [0, 2], "id": "Negative numbers"},
            {"nums": [100, 200, 300, 400], "target": 700, "expected": [2, 3], "id": "Larger numbers"},
            {"nums": [5, 75, 25], "target": 100, "expected": [1, 2], "id": "Unsorted input"},
        ]

    def test_two_sum_cases(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                nums_copy = case["nums"].copy()
                result = twoSum(nums_copy, case["target"])
                # Check result format
                self.assertIsInstance(result, list, "Result should be a list of two indices")
                self.assertEqual(len(result), 2, "Should return exactly two indices")
                i, j = result
                # Validate indices
                self.assertNotEqual(i, j, "Indices should be distinct")
                self.assertTrue(0 <= i < len(case["nums"]), f"Index {i} out of bounds")
                self.assertTrue(0 <= j < len(case["nums"]), f"Index {j} out of bounds")
                # Validate correctness
                self.assertEqual(
                    case["nums"][i] + case["nums"][j],
                    case["target"],
                    f"Elements at indices {i} and {j} should sum to {case['target']}"
                )


if __name__ == "__main__":
    unittest.main()
