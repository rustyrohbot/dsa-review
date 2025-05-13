# 98. Validate Binary Search Tree
#
# Description:
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as:
# - The left subtree of a node contains only nodes with keys < node.val.
# - The right subtree of a node contains only nodes with keys > node.val.
# - Both left and right subtrees must also be binary search trees.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
#
# Examples:
# Input: root = [2,1,3]
# Output: True
#
# Input: root = [5,1,4,null,null,3,6]
# Output: False
# Explanation: The root's right child 4 has a left child 3 which is not >5.

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


def isValidBST(root: Optional[TreeNode]) -> bool:
    """
    Returns True if the binary tree is a valid BST, False otherwise.
    """
    # TODO: Implement DFS with bounds checking here
    pass

class TestValidateBST(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"vals": [2, 1, 3],               "expected": True,  "id": "Simple valid BST"},
            {"vals": [5, 1, 4, None, None, 3, 6], "expected": False, "id": "Invalid due to subtree"},
            {"vals": [2, 2, 2],               "expected": False, "id": "All equal values invalid"},
            {"vals": [10,5,15,None,None,6,20],   "expected": False, "id": "Right subtree invalid"},
            {"vals": [1],                     "expected": True,  "id": "Single node"},
            {"vals": [],                      "expected": True,  "id": "Empty tree"},
        ]

    def test_is_valid_bst(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                root = build_tree(case["vals"])
                result = isValidBST(root)
                self.assertIsInstance(result, bool, "Result should be a boolean")
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed for vals={case['vals']}"
                )

if __name__ == "__main__":
    unittest.main()