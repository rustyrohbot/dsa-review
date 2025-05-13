# 314. Binary Tree Vertical Order Traversal
#
# Description:
# Given the root of a binary tree, return the vertical order traversal of its nodes' values.
# Columns are ordered from leftmost to rightmost. Within each column, nodes are ordered from top to bottom.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 1000].
# -1000 <= Node.val <= 1000
#
# Examples:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
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


def verticalOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Returns the vertical order traversal of the binary tree.
    """
    # TODO: Implement the solution here
    pass


class TestBinaryTreeVerticalOrderTraversal(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"vals": [3, 9, 20, None, None, 15, 7], "expected": [[9], [3, 15], [20], [7]], "id": "Example"},
            {"vals": [], "expected": [], "id": "Empty Tree"},
            {"vals": [1], "expected": [[1]], "id": "Single Node"},
            {"vals": [1, 2, 3, 4, 5, 6, 7], "expected": [[4], [2], [1, 5, 6], [3], [7]], "id": "Full Tree"},
            {"vals": [1, 2, None, 3], "expected": [[3], [2], [1]], "id": "Left Skewed"},
            {"vals": [1, None, 2, None, 3], "expected": [[1], [2], [3]], "id": "Right Skewed"},
        ]

    def test_vertical_order(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                root = build_tree(case["vals"])
                result = verticalOrder(root)
                # Validate type
                self.assertIsInstance(result, list, "Result should be a list of lists")
                # Validate structure
                for col in result:
                    self.assertIsInstance(col, list, "Each column should be a list of integers")
                    for v in col:
                        self.assertIsInstance(v, int, "Node values should be integers")
                # Validate correctness
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed for vals={case['vals']}"
                )

if __name__ == "__main__":
    unittest.main()
