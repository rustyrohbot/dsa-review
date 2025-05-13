# 153. Find Minimum in Rotated Sorted Array
#
# Description:
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
# For example, the array nums = [0,1,2,4,5,6,7]
# might become:
# - [4,5,6,7,0,1,2] if it was rotated 4 times.
# - [0,1,2,4,5,6,7] if it was rotated 7 times.
#
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in
# [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
#
# You must write an algorithm that runs in O(log n) time.
#
# Constraints:
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# All the integers of nums are UNIQUE.
# nums is sorted and rotated between 1 and n times.
#
# Examples:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] and it was rotated 3 times.
#
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
#
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The array was not rotated.

from typing import List
import unittest


def findMin(nums: List[int]) -> int:
    """
    Finds the minimum element in a rotated sorted array of unique elements in O(log n) time.
    """
    # TODO: Implement binary search on the rotated array to find the pivot
    pass

class TestFindMinInRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"nums": [3, 4, 5, 1, 2], "expected": 1, "id": "Rotated mid"},
            {"nums": [4, 5, 6, 7, 0, 1, 2], "expected": 0, "id": "Rotated later"},
            {"nums": [11, 13, 15, 17], "expected": 11, "id": "Not rotated"},
            {"nums": [1], "expected": 1, "id": "Single element"},
            {"nums": [2, 1], "expected": 1, "id": "Two elements rotated"},
        ]

    def test_find_min(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = findMin(case["nums"])
                self.assertIsInstance(result, int, "Result should be an integer")
                self.assertEqual(result, case["expected"], f"Mismatch for case '{case['id']}'")

if __name__ == "__main__":
    unittest.main()
