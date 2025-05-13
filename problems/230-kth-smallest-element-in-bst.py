# 230. Kth Smallest Element in a BST
#
# Description:
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^4]
# 0 <= Node.val <= 10^4
# 1 <= k <= number of nodes in the tree
#
from typing import Optional, List
import unittest

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    """
    Returns the kth smallest element in the BST.
    """
    # TODO: Implement in-order traversal to find the kth smallest element
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

class TestKthSmallest(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"root": [3,1,4,None,2],    "k": 1, "expected": 1, "id": "Example 1"},
            {"root": [5,3,6,2,4,None,None,1], "k": 3, "expected": 3, "id": "Example 2"},
            {"root": [1],              "k": 1, "expected": 1, "id": "Single node"},
            {"root": [2,1,3],          "k": 2, "expected": 2, "id": "Middle element"},
            {"root": [5,3,7,2,4,6,8],   "k": 5, "expected": 6, "id": "Balanced tree"},
        ]

    def test_kth_smallest(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                root = list_to_tree(case["root"])
                result = kthSmallest(root, case["k"])
                self.assertIsInstance(result, int, "Result should be an integer")
                self.assertEqual(
                    result,
                    case["expected"],
                    f"kthSmallest failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
