# 167. Two Sum II - Input Array Is Sorted
#
# Description:
# Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target.
# The function should return the indices of the two numbers (index1 < index2) as a 1-indexed list [index1, index2].
# You may assume exactly one solution exists and you may not reuse the same element twice.
#
# Constraints:
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
#
# Examples:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
#
import unittest
from typing import List


def twoSumSorted(nums: List[int], target: int) -> List[int]:
    """
    Finds two numbers in the sorted list that add up to target and returns their 1-based indices.
    """
    left, right = 0, len(nums) -1 # initialize two pointers

    while left < right:
        sum = nums[left] + nums[right]
        if sum == target: # if left plus right is the target, return the pair
            return [left+1, right+1]
        elif sum > target: # the list is sorted, so decrement right if the sum is larger than the target
            right -= 1
        else: # sum is less than target so increment left
            left += 1

class TestTwoSumSorted(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"numbers": [2, 7, 11, 15], "target": 9,    "expected": [1, 2], "id": "Example 1"},
            {"numbers": [2, 3, 4],   "target": 6,    "expected": [1, 3], "id": "Simple case"},
            {"numbers": [-1, 0],     "target": -1,   "expected": [1, 2], "id": "Two elements negative"},
            {"numbers": [1,2,3,4,4,9],"target": 8,    "expected": [4, 5], "id": "Duplicate values"},
            {"numbers": [0, 0, 3, 4], "target": 0,    "expected": [1, 2], "id": "Zeros"},
            {"numbers": [-3,-1,0,2,4,5],"target": 1,  "expected": [2, 4], "id": "Mixed negatives"},
        ]

    def test_two_sum_sorted(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = twoSumSorted(case["numbers"], case["target"])
                # Validate return type and length
                self.assertIsInstance(result, list, "Result should be a list of two indices")
                self.assertEqual(len(result), 2, "Result should contain exactly two indices")
                i, j = result
                # Validate indices are integers
                self.assertIsInstance(i, int)
                self.assertIsInstance(j, int)
                # Validate 1-based indexing and ordering
                self.assertLess(i, j, "Index1 should be less than Index2")
                self.assertTrue(1 <= i <= len(case["numbers"]))
                self.assertTrue(1 <= j <= len(case["numbers"]))
                # Validate correctness of the sum
                self.assertEqual(
                    case["numbers"][i-1] + case["numbers"][j-1],
                    case["target"],
                    f"Elements at indices {i-1} and {j-1} should sum to {case['target']}"
                )


if __name__ == "__main__":
    unittest.main()
