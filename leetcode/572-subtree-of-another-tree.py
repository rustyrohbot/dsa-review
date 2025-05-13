# 572. Subtree of Another Tree
#
# Description:
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root
# with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree "root" is a tree that consists of a node in root and all of that node's descendants.
# The tree "root" could also be considered as a subtree of itself.
#
# Constraints:
# The number of nodes in the root tree is in the range [1, 2000]
# The number of nodes in the subRoot tree is in the range [1, 1000]
# -10^4 <= root.val, subRoot.val <= 10^4

from typing import Optional, List
import unittest

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    """
    Returns True if subRoot is a subtree of root, otherwise False.
    """
    # TODO: Implement tree traversal and subtree comparison
    pass

# Helper functions for testing

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
    while result and result[-1] is None:
        result.pop()
    return result

class TestSubtreeOfAnotherTree(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {
                "root": [3,4,5,1,2],
                "subRoot": [4,1,2],
                "expected": True,
                "id": "Example 1"
            },
            {
                "root": [3,4,5,1,2,None,None,None,None,0],
                "subRoot": [4,1,2],
                "expected": False,
                "id": "Example 2"
            },
            {
                "root": [1,1],
                "subRoot": [1],
                "expected": True,
                "id": "Single match"
            },
            {
                "root": [],
                "subRoot": [],
                "expected": True,
                "id": "Both empty"
            },
            {
                "root": [1],
                "subRoot": [2],
                "expected": False,
                "id": "No match"
            }
        ]

    def test_is_subtree(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                root = list_to_tree(case["root"])
                subRoot = list_to_tree(case["subRoot"])
                result = isSubtree(root, subRoot)
                self.assertIsInstance(result, bool, "Result should be a boolean")
                self.assertEqual(
                    result,
                    case["expected"],
                    f"isSubtree failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
