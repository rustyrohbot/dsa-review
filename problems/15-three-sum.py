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
    nums.sort() # list needs to be sorted in nlog(n) time for a 2 pointers solution to work

    ret = []
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]: # continue loop if nums[i] is equal to its previosu value
            continue

        left, right = i+1, len(nums) -1 # initialize both right and left pointers at i+1 and the end of the list
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0: # increment the left pointer if the total is less than zero
                left += 1
            elif total > 0: # decrement the right pointer if the total is greater than zero
                right -= 1
            else: # found a triplet that sums to zero
                ret.append([nums[i], nums[left], nums[right]]) # triplet found, add it to the list
                while left < right and nums[left] == nums[left + 1]: # increment the left pointer to skip duplicates
                    left += 1
                while left < right and nums[right] == nums[right -1]: # decrement the right pointer to skip duplicates
                    right -= 1
                left += 1 # increment left pointer for the next iteration
                right -= 1 # decrement right pointer for the next iteration

    return ret

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
