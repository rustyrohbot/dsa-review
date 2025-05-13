# 11. Container With Most Water
#
# Description:
# Given n non-negative integers `height` where each represents a point at coordinate (i, height[i]),
# `n` vertical lines are drawn such that the endpoints of line i are at (i, 0) and (i, height[i]).
# Find two lines that, together with the x-axis, form a container that holds the most water.
# Return the maximum amount of water a container can store.
#
# Constraints:
# 2 <= len(height) <= 10^5
# 0 <= height[i] <= 10^4
#
# Examples:
# Input: height = [1,8,6,2,5,4,8,3,7]  Output: 49
# Input: height = [1,1]              Output: 1

import unittest
from typing import List


def maxArea(height: List[int]) -> int:
    """
    Returns the maximum water that can be contained between two lines in the `height` list.
    """
    # TODO: Implement the two-pointer solution here
    pass


class TestContainerWithMostWater(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"height": [1,8,6,2,5,4,8,3,7], "expected": 49, "id": "Example 1"},
            {"height": [1,1],               "expected": 1,  "id": "Example 2"},
            {"height": [1,2,3,4,5],         "expected": 6,  "id": "Increasing heights"},
            {"height": [5,4,3,2,1],         "expected": 6,  "id": "Decreasing heights"},
            {"height": [5,5,5,5],           "expected": 15, "id": "All equal heights"},
            {"height": [2,3],               "expected": 2,  "id": "Two elements"},
            {"height": [0,0,0],             "expected": 0,  "id": "Zeros"},
        ]

    def test_max_area(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = maxArea(case["height"])
                # Validate return type
                self.assertIsInstance(result, int, "Result should be an integer")
                # Validate correctness
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed for height={case['height']}"
                )


if __name__ == "__main__":
    unittest.main()
