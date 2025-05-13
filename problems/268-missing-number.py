# 268. Missing Number
#
# Description:
# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
#
# Constraints:
# n == nums.length
# 1 <= n <= 10^4
# 0 <= nums[i] <= n
# All the numbers of nums are unique.

from typing import List
import unittest

def missingNumber(nums: List[int]) -> int:
    """
    Finds the missing number in the array of distinct numbers from 0 to n.
    Uses constant extra space and linear time.
    """
    # TODO: Implement using XOR or arithmetic sum formula
    pass

class TestMissingNumber(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"nums": [3, 0, 1],                     "expected": 2, "id": "Example 1"},
            {"nums": [0, 1],                        "expected": 2, "id": "Small n"},
            {"nums": [9,6,4,2,3,5,7,0,1],           "expected": 8, "id": "Unsorted large"},
            {"nums": [0],                          "expected": 1, "id": "Single zero"},
            {"nums": [1],                          "expected": 0, "id": "Single non-zero"},
        ]

    def test_missing_number(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = missingNumber(case["nums"])
                self.assertIsInstance(result, int, "Result should be an integer")
                self.assertEqual(
                    result,
                    case["expected"],
                    f"missingNumber failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
