# 100. Same Tree
#
# Description:
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same values.
#
# Constraints:
# The number of nodes in both trees is in the range [0, 100].
# -10^4 <= Node.val <= 10^4
#
# Examples:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

from typing import Optional
import unittest

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Compares two binary trees and returns True if they are structurally identical and node values are equal.
    """
    if not p and not q:
        return True
    if not p and q:
        return False
    if p and not q:
        return False
    if p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False

class TestSameTree(unittest.TestCase):
    def setUp(self):
        # Helper to build a tree from a level-order list representation
        def build_tree(nodes):
            if not nodes:
                return None
            vals = list(nodes)  # Copy to avoid modifying original
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
            {"p": None, "q": None, "expected": True, "id": "Both empty"},
            {"p": build_tree([1, 2, 3]), "q": build_tree([1, 2, 3]), "expected": True, "id": "Identical trees"},
            {"p": build_tree([1, 2]), "q": build_tree([1, None, 2]), "expected": False, "id": "Different structure"},
            {"p": build_tree([1, 2, 1]), "q": build_tree([1, 1, 2]), "expected": False, "id": "Different values"},
            {"p": TreeNode(1), "q": TreeNode(1), "expected": True, "id": "Single node equal"},
            {"p": TreeNode(1), "q": TreeNode(2), "expected": False, "id": "Single node not equal"},
        ]

    def test_is_same_tree(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = isSameTree(case["p"], case["q"])
                self.assertIsInstance(result, bool, "Result should be a boolean")
                self.assertEqual(result, case["expected"], f"Mismatch for case '{case['id']}'")

if __name__ == "__main__":
    unittest.main()
