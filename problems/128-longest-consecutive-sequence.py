# 128. Longest Consecutive Sequence
#
# Description:
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
#
# Constraints:
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
# Examples:
# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive sequence is [1, 2, 3, 4].
#
# Input: nums = []
# Output: 0

from typing import List
import unittest

def longestConsecutive(nums: List[int]) -> int:
    """
    Returns the length of the longest consecutive elements sequence in nums.
    """
    # TODO: Implement using a hash set for O(n) scanning
    pass

class TestLongestConsecutiveSequence(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"nums": [100, 4, 200, 1, 3, 2], "expected": 4, "id": "Basic example"},
            {"nums": [], "expected": 0, "id": "Empty list"},
            {"nums": [1], "expected": 1, "id": "Single element"},
            {"nums": [0, -1, -2, -3], "expected": 4, "id": "Negative sequence"},
            {"nums": [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], "expected": 7, "id": "Mixed order with duplicates"},
        ]

    def test_longest_consecutive(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = longestConsecutive(case["nums"])
                self.assertIsInstance(result, int, "Result should be an integer")
                self.assertEqual(result, case["expected"], f"Mismatch for case '{case['id']}'")

if __name__ == "__main__":
    unittest.main()