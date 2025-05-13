# 39. Combination Sum
#
# Description:
# Given an array of distinct integers "candidates" and a target integer "target",
# return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may use the same number from candidates an unlimited number of times.
# The combinations may be returned in any order.
#
# Constraints:
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.\# 1 <= target <= 500
#
# Examples:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[7],[2,2,3]]
#
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

import unittest
from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Returns all unique combinations in candidates where the numbers sum to target.

    Parameters:
        candidates (List[int]): Distinct positive integers.
        target (int): Target sum.
    Returns:
        List[List[int]]: List of unique combinations.
    """
    # TODO: Implement backtracking solution here
    pass


class TestCombinationSum(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"candidates": [2, 3, 6, 7], "target": 7,  "expected": [[7], [2, 2, 3]],           "id": "Example 1"},
            {"candidates": [2, 3, 5],    "target": 8,  "expected": [[2, 2, 2, 2], [2, 3, 3], [3, 5]], "id": "Example 2"},
            {"candidates": [2],          "target": 1,  "expected": [],                            "id": "No combination"},
            {"candidates": [1],          "target": 1,  "expected": [[1]],                         "id": "Single candidate equals target"},
            {"candidates": [1],          "target": 2,  "expected": [[1, 1]],                     "id": "Repeated uses"},
            {"candidates": [8, 7, 4, 3], "target": 11, "expected": [[3, 4, 4], [3, 8], [4, 7]],     "id": "Unordered candidates"},
        ]

    def test_combination_sum(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = combinationSum(case["candidates"], case["target"])
                # Validate return type
                self.assertIsInstance(result, list, "Result should be a list of combinations")
                # Each combination should be list of ints
                for combo in result:
                    self.assertIsInstance(combo, list, "Each combination should be a list of integers")
                    for num in combo:
                        self.assertIsInstance(num, int, "Combination elements should be integers")
                # Normalize for comparison: sort each combination
                normalized_result = [sorted(combo) for combo in result]
                normalized_expected = [sorted(combo) for combo in case["expected"]]
                # Compare as multisets of combinations
                self.assertCountEqual(
                    normalized_result,
                    normalized_expected,
                    f"Case '{case['id']}' failed: got {result}, expected {case['expected']}"
                )


if __name__ == "__main__":
    unittest.main()
