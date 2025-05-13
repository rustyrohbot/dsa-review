# 104. Maximum Depth of Binary Tree
#
# Description:
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 10^4].
# -100 <= Node.val <= 100
#
# Examples:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#
# Input: root = [1,null,2]
# Output: 2
from typing import Optional
import unittest

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    """
    Returns the maximum depth of the binary tree rooted at `root`.
    """
    # TODO: Implement depth-first or breadth-first traversal to compute depth
    pass

class TestMaxDepth(unittest.TestCase):
    def setUp(self):
        # Helper to build a tree from a level-order list representation
        def build_tree(nodes):
            if not nodes:
                return None
            vals = list(nodes)
            val = vals.pop(0)
            root = TreeNode(val) if val is not None else None
            queue = [root]
            while queue and vals:
                node = queue.pop(0)
                if node:
                    left_val = vals.pop(0) if vals else None
                    right_val = vals.pop(0) if vals else None
                    node.left = TreeNode(left_val) if left_val is not None else None
                    node.right = TreeNode(right_val) if right_val is not None else None
                    queue.append(node.left)
                    queue.append(node.right)
            return root

        self.test_cases = [
            {"root": None, "expected": 0, "id": "Empty tree"},
            {"root": build_tree([1]), "expected": 1, "id": "Single node"},
            {"root": build_tree([3, 9, 20, None, None, 15, 7]), "expected": 3, "id": "Example 1"},
            {"root": build_tree([1, None, 2]), "expected": 2, "id": "Example 2"},
            {"root": build_tree([1, 2, 3, 4, None, None, 5]), "expected": 3, "id": "Unbalanced tree"},
        ]

    def test_max_depth(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = maxDepth(case["root"])
                self.assertIsInstance(result, int, "Result should be an integer")
                self.assertEqual(result, case["expected"], f"Mismatch for case '{case['id']}'")

if __name__ == "__main__":
    unittest.main()
