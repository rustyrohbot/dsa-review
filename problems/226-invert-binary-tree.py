# 226. Invert Binary Tree
#
# Description:
# Given the root of a binary tree, invert the tree, and return its root.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 100]
# -100 <= Node.val <= 100
#
from typing import Optional, List
import unittest

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Inverts a binary tree by swapping left and right children at every node.
    Returns the root of the inverted tree.
    """
    # TODO: Implement the inversion logic
    pass

# Helper functions for tests

def list_to_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Builds a binary tree from a level-order list, using None for missing nodes.
    """
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


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Converts a binary tree to a level-order list, using None for missing nodes.
    """
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Trim trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

class TestInvertBinaryTree(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {
                "root": [4,2,7,1,3,6,9],
                "expected": [4,7,2,9,6,3,1],
                "id": "Example 1"
            },
            {
                "root": [],
                "expected": [],
                "id": "Empty tree"
            },
            {
                "root": [1,2],
                "expected": [1,None,2],
                "id": "Left child only"
            },
            {
                "root": [1,None,2],
                "expected": [1,2],
                "id": "Right child only"
            },
        ]

    def test_invert_tree(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                root = list_to_tree(case["root"])
                inverted = invertTree(root)
                result = tree_to_list(inverted)
                self.assertEqual(
                    result,
                    case["expected"],
                    f"invertTree failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
