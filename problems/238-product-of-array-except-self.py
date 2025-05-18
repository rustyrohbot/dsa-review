# 238. Product of Array Except Self
#
# Description:
# Given an integer array nums, return an array answer such that answer[i] is the product
# of all the elements of nums except nums[i]. The product of any prefix or suffix of nums
# is guaranteed to fit in a 32-bit integer.
#
# Constraints:
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
# Examples:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
#
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

import unittest
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Returns an array where each element at index i is the product of all numbers in nums
    except nums[i], without using division and in O(n) time.
    """
    output = [1] * (len(nums)) # initialize output array to all 1 of length nums

    # prefixes
    prefix = 1 # starting prefix is 1
    for i in range(len(nums)):
        output[i] = prefix # update output sub i to the prefix
        prefix *= nums[i] # update the prefix to be itself multiplied by nums sub i

    # postfixes
    postfix = 1 # starting postfix is 1
    for i in range(len(nums)-1, -1, -1): # reverse iterate, start at the last index of nums, stop at 0, and decrement each loop by 1
        output[i] *= postfix # set the output sub i equal to itself multiplied by the postfix
        postfix *= nums[i] # update the postfix to be itself multiplied by nums sub i

    return output

class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"nums": [1, 2, 3, 4],             "expected": [24, 12, 8, 6],   "id": "Example 1"},
            {"nums": [-1, 1, 0, -3, 3],        "expected": [0, 0, 9, 0, 0],   "id": "Contains zero and negatives"},
            {"nums": [0, 0],                  "expected": [0, 0],           "id": "Two zeros"},
            {"nums": [1, 0],                  "expected": [0, 1],           "id": "Single zero"},
            {"nums": [5, 1, 5],               "expected": [5, 25, 5],        "id": "Duplicate values"},
            {"nums": [2, 3],                  "expected": [3, 2],           "id": "Two elements"},
        ]

    def test_product_except_self(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = productExceptSelf(case["nums"])
                # Validate return type and length
                self.assertIsInstance(result, list, "Result should be a list of integers")
                self.assertEqual(len(result), len(case["expected"],), "Result list must match expected length")
                # Validate element types
                for x in result:
                    self.assertIsInstance(x, int, "Each product must be an integer")
                # Validate correctness
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed for input {case['nums']}"
                )


if __name__ == "__main__":
    unittest.main()
