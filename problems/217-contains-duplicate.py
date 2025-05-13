# 217. Contains Duplicate
#
# Description:
# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.
#
# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
from typing import List
import unittest

def containsDuplicate(nums: List[int]) -> bool:
    """
    Determines if any duplicates exist in the list.
    Returns True if a duplicate is found, otherwise False.
    """
    # TODO: Implement the solution here
    pass

class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"nums": [1, 2, 3, 1], "expected": True, "id": "Example 1"},
            {"nums": [1, 2, 3, 4], "expected": False, "id": "No duplicates"},
            {"nums": [1, 1, 1, 3, 3, 4, 3, 2, 4, 2], "expected": True, "id": "Multiple duplicates"},
            {"nums": [], "expected": False, "id": "Empty array"},
            {"nums": [5], "expected": False, "id": "Single element"},
            {"nums": [-1, -1], "expected": True, "id": "Negative duplicates"},
        ]

    def test_contains_duplicate_cases(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = containsDuplicate(case["nums"])
                self.assertIsInstance(result, bool, "Result should be a boolean")
                self.assertEqual(
                    result,
                    case["expected"],
                    f"containsDuplicate failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
