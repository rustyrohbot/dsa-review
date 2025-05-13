# 417. Pacific Atlantic Water Flow
#
# Description:
# Given an m x n matrix of non-negative integers representing the height of each cell,
# return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.
# The Pacific ocean touches the left and top edges; the Atlantic ocean touches the right and bottom edges.
#
# Constraints:
# m == len(heightMap)
# n == len(heightMap[i])
# 1 <= m, n <= 200
# 0 <= heightMap[i][j] <= 10^5

from typing import List, Tuple
import unittest


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    """
    Returns list of [r, c] coordinates where water can flow to both oceans.
    """
    # TODO: Implement BFS/DFS from ocean edges or reverse graph traversal
    pass

class TestPacificAtlanticWaterFlow(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {
                "heights": [
                    [1, 2, 2, 3, 5],
                    [3, 2, 3, 4, 4],
                    [2, 4, 5, 3, 1],
                    [6, 7, 1, 4, 5],
                    [5, 1, 1, 2, 4]
                ],
                "expected": [
                    [0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]
                ],
                "id": "Example 1"
            },
            {
                "heights": [],
                "expected": [],
                "id": "Empty matrix"
            },
            {
                "heights": [[5]],
                "expected": [[0, 0]],
                "id": "Single cell"
            },
            {
                "heights": [
                    [2,1],
                    [1,2]
                ],
                "expected": [[0,0],[0,1],[1,0],[1,1]],
                "id": "2x2 all reachable"
            }
        ]

    def normalize(self, positions: List[List[int]]) -> set:
        return set((r, c) for r, c in positions)

    def test_pacific_atlantic(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = pacificAtlantic(case["heights"])
                self.assertIsInstance(result, list, "Result should be a list of coordinates")
                self.assertEqual(
                    self.normalize(result),
                    self.normalize(case["expected"]),
                    f"pacificAtlantic failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
