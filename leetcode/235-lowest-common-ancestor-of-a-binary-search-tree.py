# 235. Lowest Common Ancestor of a Binary Search Tree
#
# Description:
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
# The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants
# (where we allow a node to be a descendant of itself).
#
# Constraints:
# The number of nodes in the tree is in the range [2, 10^5]
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p and q are different and both values will exist in the BST.
#
from typing import Optional, List
import unittest

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """
    Finds the lowest common ancestor of nodes p and q in a BST.
    """
    # TODO: Implement BST-based traversal to locate LCA
    pass

# Helper to build tree from level-order list

def list_to_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        node = queue.pop(0)
        if nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    return root

# Helper to find a node by value

def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)

class TestLowestCommonAncestorBST(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {   # Example 1
                "nodes": [6,2,8,0,4,7,9,None,None,3,5],
                "p": 2, "q": 8, "expected": 6, "id": "Example 1"
            },
            {   # Example 2
                "nodes": [6,2,8,0,4,7,9,None,None,3,5],
                "p": 2, "q": 4, "expected": 2, "id": "Example 2"
            },
            {   # LCA is one of the nodes
                "nodes": [2,1],
                "p": 2, "q": 1, "expected": 2, "id": "Root and child"
            },
            {   # Larger tree balanced
                "nodes": [20,10,30,5,15,25,35],
                "p": 5, "q": 15, "expected": 10, "id": "Balanced subtree"
            },
        ]

    def test_lowest_common_ancestor(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                root = list_to_tree(case["nodes"])
                p_node = find_node(root, case["p"])
                q_node = find_node(root, case["q"])
                self.assertIsNotNone(p_node, f"Node {case['p']} should exist in tree")
                self.assertIsNotNone(q_node, f"Node {case['q']} should exist in tree")
                lca = lowestCommonAncestor(root, p_node, q_node)
                self.assertIsInstance(lca, TreeNode, "Result should be a TreeNode")
                self.assertEqual(
                    lca.val,
                    case["expected"],
                    f"lowestCommonAncestor failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
