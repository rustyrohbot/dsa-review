# 105. Construct Binary Tree from Preorder and Inorder Traversal
#
# Description:
# Given two integer arrays preorder and inorder where preorder is the preorder traversal
# of a binary tree and inorder is the inorder traversal of the same tree, construct and
# return the binary tree.
#
# Constraints:
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
#
# Examples:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

from typing import List, Optional
import unittest

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """
    Constructs the binary tree from preorder and inorder traversal lists.
    """
    # TODO: Implement recursive construction using a hashmap for inorder indices
    pass

class TestBuildTree(unittest.TestCase):
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

        # Helper to compare two binary trees
        def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

        self.test_cases = [
            {
                "preorder": [3, 9, 20, 15, 7],
                "inorder": [9, 3, 15, 20, 7],
                "expected": build_tree([3, 9, 20, None, None, 15, 7]),
                "id": "Example 1"
            },
            {
                "preorder": [-1],
                "inorder": [-1],
                "expected": build_tree([-1]),
                "id": "Single node"
            },
            {
                "preorder": [],
                "inorder": [],
                "expected": None,
                "id": "Empty tree"
            }
        ]

    def test_build_tree(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = buildTree(case["preorder"], case["inorder"])
                self.assertTrue(
                    is_same_tree(result, case["expected"]),
                    f"Tree mismatch for case '{case['id']}'"
                )
                # Ensure the return type is correct
                self.assertTrue(result is None or isinstance(result, TreeNode))

if __name__ == "__main__":
    unittest.main()
