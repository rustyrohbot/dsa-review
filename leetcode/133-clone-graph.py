# 133. Clone Graph
#
# Description:
# Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
# Each node in the graph contains a val (int) and a list (neighbors) of its neighbors.
#
# Constraints:
# The number of nodes is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no repeated edges and no self-loops.
# The graph is connected and simple.
#
# Examples:
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
#
# Input: adjList = []
# Output: []
#
# Input: adjList = [[2],[1]]
# Output: [[2],[1]]

from typing import List, Optional
import unittest

class Node:
    def __init__(self, val: int = 0, neighbors: List['Node'] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: 'Node') -> 'Node':
    """
    Clones an undirected graph given a reference node.
    """
    # TODO: Implement with DFS/BFS and hashmap to map original to cloned nodes
    pass

class TestCloneGraph(unittest.TestCase):
    def setUp(self):
        # Helper to build graph from adjacency list
        def build_graph(adjList: List[List[int]]) -> Optional[Node]:
            if not adjList:
                return None
            nodes = {i+1: Node(i+1) for i in range(len(adjList))}
            for i, neighbors in enumerate(adjList, start=1):
                nodes[i].neighbors = [nodes[n] for n in neighbors]
            return nodes[1]

        # Helper to compare two graphs
        def is_same_graph(node1: 'Node', node2: 'Node', visited=None) -> bool:
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            visited = visited or set()
            if node1.val in visited:
                return True
            if node1.val != node2.val or len(node1.neighbors) != len(node2.neighbors):
                return False
            visited.add(node1.val)
            for n1, n2 in zip(node1.neighbors, node2.neighbors):
                if not is_same_graph(n1, n2, visited):
                    return False
            return True

        self.test_cases = [
            {"adj": [[2,4],[1,3],[2,4],[1,3]], "id": "Example 1"},
            {"adj": [], "id": "Empty graph"},
            {"adj": [[2],[1]], "id": "Two nodes"},
            {"adj": [[2,3],[1,3],[1,2]], "id": "Triangle"},
        ]
        self.build_graph = build_graph
        self.is_same_graph = is_same_graph

    def test_clone_graph(self):
        for case in self.test_cases:
            with self.subTest(case["id"]):
                original = self.build_graph(case["adj"])
                cloned = cloneGraph(original)
                self.assertTrue(self.is_same_graph(original, cloned), f"Mismatch for case '{case['id']}'")
                # Ensure cloned nodes are different objects
                if original:
                    self.assertIsNot(original, cloned)

if __name__ == "__main__":
    unittest.main()
