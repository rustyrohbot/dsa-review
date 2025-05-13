# 323. Number of Connected Components in an Undirected Graph
#
# Description:
# You have n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes).
# Return the number of connected components in the graph.
#
# Constraints:
# 1 <= n <= 10^4
# 0 <= edges.length <= 2 * 10^4
# edges[i].length == 2
# 0 <= u_i, v_i < n
# No duplicate edges.

from typing import List
import unittest


def countComponents(n: int, edges: List[List[int]]) -> int:
    """
    Returns the number of connected components in an undirected graph given n nodes and edges.
    """
    # TODO: Implement using union-find or DFS/BFS
    pass

class TestConnectedComponents(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"n": 5, "edges": [[0,1],[1,2],[3,4]],          "expected": 2, "id": "Two components"},
            {"n": 5, "edges": [],                           "expected": 5, "id": "No edges"},
            {"n": 4, "edges": [[0,1],[1,2],[2,3]],          "expected": 1, "id": "Fully connected chain"},
            {"n": 4, "edges": [[0,1],[2,3],[1,2]],          "expected": 1, "id": "Cycle forms one component"},
            {"n": 1, "edges": [],                           "expected": 1, "id": "Single node"},
            {"n": 3, "edges": [[0,1]],                      "expected": 2, "id": "One isolated node"},
        ]

    def test_count_components(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = countComponents(case["n"], case["edges"])
                self.assertIsInstance(result, int, "Result should be an integer")
                self.assertEqual(
                    result,
                    case["expected"],
                    f"countComponents failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
