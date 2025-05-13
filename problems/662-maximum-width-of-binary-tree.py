# 662. Maximum Width of Binary Tree
#
# Description:
# Given the root of a binary tree, return the maximum width of the given tree.
# The maximum width of a tree is the maximum width among all levels.
# The width of one level is defined as the length between the end-nodes
# (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes
# are also counted into the length calculation.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 3000].
# -100 <= Node.val <= 100
#
# Examples:
# Input: root = [1,3,2,5,3,null,9]   Output: 4
# Input: root = [1,3,null,5,3]       Output: 2

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
        if val is not None:
            node.left = TreeNode(val)
            queue.append(node.left)
        try:
            val = next(it)
        except StopIteration:
            break
        if val is not None:
            node.right = TreeNode(val)
            queue.append(node.right)
    return root


def widthOfBinaryTree(root: Optional[TreeNode]) -> int:
    """
    Returns the maximum width of the binary tree.
    """
    # TODO: Implement the solution here
    pass


class TestMaximumWidthBinaryTree(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"vals": [1, 3, 2, 5, 3, None, 9],        "expected": 4,  "id": "Example 1"},
            {"vals": [1, 3, None, 5, 3],                "expected": 2,  "id": "Example 2"},
            {"vals": [],                                "expected": 0,  "id": "Empty Tree"},
            {"vals": [1],                                "expected": 1,  "id": "Single Node"},
            {"vals": [1, 2, 3, 4, 5, 6, 7],             "expected": 4,  "id": "Full Tree"},
            {"vals": [1, 2, None, 4, None, None, 7],    "expected": 2,  "id": "Sparse Tree"},
        ]

    def test_width_of_binary_tree(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                root = build_tree(case["vals"])
                result = widthOfBinaryTree(root)
                # Validate return type
                self.assertIsInstance(result, int, "Result should be an integer")
                # Validate correctness
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed for vals={case['vals']}"
                )


if __name__ == "__main__":
    unittest.main()
