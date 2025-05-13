# 102. Binary Tree Level Order Traversal
#
# Description:
# Given the root of a binary tree, return the level order traversal of its nodes' values.
# (i.e., from left to right, level by level).
#
# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
#
# Examples:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
#
import unittest
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Builds a binary tree from a level-order list of values (None for missing nodes).
    Returns the root of the tree.
    """
    if not vals:
        return None
    it = iter(vals)
    root = TreeNode(next(it))
    queue = [root]
    for val in it:
        node = queue.pop(0)
        # left child
        if val is not None:
            node.left = TreeNode(val)
            queue.append(node.left)
        # right child
        try:
            val = next(it)
        except StopIteration:
            break
        if val is not None:
            node.right = TreeNode(val)
            queue.append(node.right)
    return root


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Returns the level order traversal of a binary tree's nodes as a list of levels.
    """
    # TODO: Implement the solution here
    pass


class TestBinaryTreeLevelOrderTraversal(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"vals": [3, 9, 20, None, None, 15, 7], "expected": [[3], [9, 20], [15, 7]], "id": "Example 1"},
            {"vals": [], "expected": [], "id": "Empty Tree"},
            {"vals": [1], "expected": [[1]], "id": "Single Node"},
            {"vals": [1, 2, 3, 4, None, None, 5], "expected": [[1], [2, 3], [4, 5]], "id": "Mixed Children"},
            {"vals": [1, None, 2, None, 3], "expected": [[1], [2], [3]], "id": "Right Skewed"},
            {"vals": [1, 2, None, 3, None, None, None], "expected": [[1], [2], [3]], "id": "Left Skewed"},
        ]

    def test_level_order(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                root = build_tree(case["vals"])
                result = levelOrder(root)
                # Validate result type
                self.assertIsInstance(result, list, "Result should be a list of levels")
                # Validate levels and values
                for level in result:
                    self.assertIsInstance(level, list, "Each level should be a list of integers")
                    for v in level:
                        self.assertIsInstance(v, int, "Node values should be integers")
                # Validate correctness
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Level order mismatch for case '{case['id']}'"
                )


if __name__ == "__main__":
    unittest.main()
