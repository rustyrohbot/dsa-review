# 200. Number of Islands
#
# Description:
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
# return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
#
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
#
# Examples:
# Input:
# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#
# Input:
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

from typing import List
import unittest


def numIslands(grid: List[List[str]]) -> int:
    """
    Returns the number of islands in the given grid.
    """
    # TODO: Implement DFS or BFS flood-fill to count islands
    pass

class TestNumberOfIslands(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {
                "grid": [
                    ["1","1","1","1","0"],
                    ["1","1","0","1","0"],
                    ["1","1","0","0","0"],
                    ["0","0","0","0","0"]
                ],
                "expected": 1,
                "id": "Single island"
            },
            {
                "grid": [
                    ["1","1","0","0","0"],
                    ["1","1","0","0","0"],
                    ["0","0","1","0","0"],
                    ["0","0","0","1","1"]
                ],
                "expected": 3,
                "id": "Multiple islands"
            },
            {"grid": [], "expected": 0, "id": "Empty grid"},
            {"grid": [["1"]], "expected": 1, "id": "Single land"},
            {"grid": [["0"]], "expected": 0, "id": "Single water"},
        ]

    def test_num_islands(self):
        for case in self.test_cases:
            with self.subTest(case["id"]):
                result = numIslands(case["grid"])
                self.assertIsInstance(result, int, "Result should be an integer")
                self.assertEqual(result, case["expected"], f"Mismatch for case '{case['id']}'")

if __name__ == "__main__":
    unittest.main()
