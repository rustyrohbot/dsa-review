# 33. Search in Rotated Sorted Array
#
# Description:
# There is an integer array nums sorted in ascending order (with distinct values),
# which is rotated at an unknown pivot index k (0 <= k < nums.length) such that the
# resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]].
# Given the array nums after rotation and an integer target, return the index of target if it is in nums,
# or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.
#
# Constraints:
# 0 <= nums.length <= 10^4
# -10^4 <= nums[i], target <= 10^4
# All values of nums are unique.
#
# Examples:
# Input: nums = [4,5,6,7,0,1,2], target = 0  Output: 4
# Input: nums = [4,5,6,7,0,1,2], target = 3  Output: -1
#
import unittest
from typing import List


def search(nums: List[int], target: int) -> int:
    """
    Searches for target in a rotated sorted array and returns its index or -1 if not found.
    """
    # TODO: Implement O(log n) binary search here
    pass


class TestSearchRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"nums": [4,5,6,7,0,1,2], "target": 0, "expected": 4,  "id": "Example 1"},
            {"nums": [4,5,6,7,0,1,2], "target": 3, "expected": -1, "id": "Example 2"},
            {"nums": [1,2,3,4,5,6,7], "target": 5, "expected": 4,  "id": "No rotation"},
            {"nums": [6,7,1,2,3,4,5], "target": 6, "expected": 0,  "id": "Different pivot"},
            {"nums": [1],             "target": 1, "expected": 0,  "id": "Single element found"},
            {"nums": [1],             "target": 0, "expected": -1, "id": "Single element not found"},
            {"nums": [2,1],           "target": 1, "expected": 1,  "id": "Two element rotation"},
            {"nums": [],              "target": 5, "expected": -1, "id": "Empty array"},
        ]

    def test_search(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = search(case["nums"], case["target"])
                # Validate return type
                self.assertIsInstance(result, int, "Result should be an integer")
                # Validate correctness
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed for nums={case['nums']} target={case['target']}"
                )


if __name__ == "__main__":
    unittest.main()
