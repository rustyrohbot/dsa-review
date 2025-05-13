# 124. Binary Tree Maximum Path Sum
#
# Description:
# Given the root of a binary tree, return the maximum path sum of any non-empty path.
# A path is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
# A node can only appear in the sequence at most once. Note that the path does not need to go through the root.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 3 * 10^4].
# -1000 <= Node.val <= 1000
#
# Examples:
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with sum 6.
#
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with sum 42.

from typing import Optional
import unittest

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: Optional[TreeNode]) -> int:
    """
    Returns the maximum path sum for any path in the binary tree.
    """
    # TODO: Implement using a post-order traversal tracking max gain
    pass

class TestBinaryTreeMaxPathSum(unittest.TestCase):
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
            {"root": build_tree([1, 2, 3]), "expected": 6, "id": "Positive values"},
            {"root": build_tree([-10, 9, 20, None, None, 15, 7]), "expected": 42, "id": "Mixed values"},
            {"root": build_tree([5]), "expected": 5, "id": "Single node"},
            {"root": build_tree([-3]), "expected": -3, "id": "All negative"},
        ]

    def test_max_path_sum(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = maxPathSum(case["root"])
                self.assertIsInstance(result, int, "Result should be an integer")
                self.assertEqual(result, case["expected"], f"Mismatch for case '{case['id']}'")

if __name__ == "__main__":
    unittest.main()
