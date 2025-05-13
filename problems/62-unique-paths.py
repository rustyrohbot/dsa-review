# 62. Unique Paths
#
# Description:
# A robot is located at the top-left corner of an m x n grid (rows x columns).
# The robot can only move either down or right at any point in time.
# It is trying to reach the bottom-right corner of the grid.
# How many possible unique paths are there?
#
# Constraints:
# 1 <= m, n <= 100
# The answer is guaranteed to fit in a 32-bit integer for the given constraints.
#
# Examples:
# Input: m = 3, n = 7    Output: 28
# Input: m = 3, n = 2    Output: 3

import unittest


def uniquePaths(m: int, n: int) -> int:
    """
    Returns the number of unique paths from the top-left to bottom-right in an m x n grid,
    where only moves to the right or down are allowed.

    Parameters:
        m (int): Number of rows.
        n (int): Number of columns.
    Returns:
        int: Number of unique paths.
    """
    # TODO: Implement combinatorial or DP solution here
    pass


class TestUniquePaths(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"m": 3,  "n": 7,  "expected": 28,     "id": "Example 1"},
            {"m": 3,  "n": 2,  "expected": 3,      "id": "Example 2"},
            {"m": 1,  "n": 1,  "expected": 1,      "id": "Minimum grid"},
            {"m": 1,  "n": 5,  "expected": 1,      "id": "Single row"},
            {"m": 5,  "n": 1,  "expected": 1,      "id": "Single column"},
            {"m": 3,  "n": 3,  "expected": 6,      "id": "Square grid"},
            {"m": 10, "n": 10, "expected": 48620,  "id": "Larger grid"},
        ]

    def test_unique_paths(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = uniquePaths(case["m"], case["n"])
                # Validate return type
                self.assertIsInstance(result, int, "Result should be an integer")
                # Validate correctness
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed for m={case['m']}, n={case['n']}"
                )


if __name__ == "__main__":
    unittest.main()
