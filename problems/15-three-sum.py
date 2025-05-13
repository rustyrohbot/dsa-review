# 15. 3Sum
#
# Description:
# Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
# such that i, j, and k are distinct and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
# Constraints:
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
# Examples:
# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
#
from typing import List
import unittest

def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Finds all unique triplets in the list which sum to zero.
    Returns a list of triplets.
    """
    # TODO: Implement the solution here
    pass

class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"nums": [-1, 0, 1, 2, -1, -4], "expected": [[-1, -1, 2], [-1, 0, 1]], "id": "Example 1"},
            {"nums": [], "expected": [], "id": "Empty array"},
            {"nums": [0], "expected": [], "id": "Single element"},
            {"nums": [0, 0, 0], "expected": [[0, 0, 0]], "id": "All zeros"},
            {"nums": [-2, 0, 1, 1, 2], "expected": [[-2, 0, 2], [-2, 1, 1]], "id": "Multiple results"},
            {"nums": [-4, -1, -1, 0, 1, 2], "expected": [[-1, -1, 2], [-1, 0, 1]], "id": "Duplicates handled"},
        ]

    def test_three_sum_cases(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = threeSum(case["nums"])
                # Check result type
                self.assertIsInstance(result, list, "Result should be a list of triplets")
                # Check each triplet is a list of three ints
                for triplet in result:
                    self.assertIsInstance(triplet, list, "Each triplet should be a list")
                    self.assertEqual(len(triplet), 3, "Each triplet must have exactly three elements")

                # Normalize for comparison: sort each inner list and compare as multisets
                normalized = [sorted(triplet) for triplet in result]
                expected_norm = [sorted(triplet) for triplet in case["expected"]]
                self.assertCountEqual(
                    normalized,
                    expected_norm,
                    f"Triplets for case '{case['id']}' do not match expected"
                )

if __name__ == "__main__":
    unittest.main()
