# 261. Graph Valid Tree
#
# Description:
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to check whether these edges make up a valid tree.
#
# Constraints:
# 1 <= n <= 2000
# 0 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= u_i, v_i < n
# No duplicate edges, undirected.

from typing import List
import unittest


def validTree(n: int, edges: List[List[int]]) -> bool:
    """
    Determines whether the undirected graph with n nodes and given edges forms a valid tree.
    A valid tree is an acyclic, fully connected graph with exactly n - 1 edges.
    Returns True if valid, else False.
    """
    # TODO: Implement using union-find or DFS/BFS connectivity+cycle check
    pass

class TestGraphValidTree(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"n": 5, "edges": [[0,1],[0,2],[0,3],[1,4]], "expected": True,  "id": "Basic valid tree"},
            {"n": 5, "edges": [[0,1],[1,2],[2,3],[1,3],[1,4]], "expected": False, "id": "Contains cycle"},
            {"n": 4, "edges": [[0,1],[2,3]],                   "expected": False, "id": "Disconnected graph"},
            {"n": 1, "edges": [],                              "expected": True,  "id": "Single node"},
            {"n": 2, "edges": [[1,0]],                         "expected": True,  "id": "Two nodes one edge"},
        ]

    def test_valid_tree(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = validTree(case["n"], case["edges"])
                self.assertIsInstance(result, bool, "Result should be a boolean")
                self.assertEqual(
                    result,
                    case["expected"],
                    f"validTree failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
