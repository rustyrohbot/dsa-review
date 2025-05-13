# 297. Serialize and Deserialize Binary Tree
#
# Description:
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
# serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be
# serialized to a string and this string can be deserialized to the original tree structure.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000
#
from typing import Optional, List
import unittest

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root: Optional[TreeNode]) -> str:
    """
    Encodes a tree to a single string.
    """
    # TODO: Implement serialization logic
    pass


def deserialize(data: str) -> Optional[TreeNode]:
    """
    Decodes your encoded data to tree.
    """
    # TODO: Implement deserialization logic
    pass

# Helper functions for testing

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


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
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

class TestSerializeDeserialize(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"tree": [],                        "id": "Empty tree"},
            {"tree": [1],                       "id": "Single node"},
            {"tree": [1,2,3,None,None,4,5],     "id": "Complete tree"},
            {"tree": [1,None,2,None,3],         "id": "Right skewed"},
            {"tree": [1,2,None,3],              "id": "Left skewed"},
        ]

    def test_round_trip(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                root = list_to_tree(case["tree"])
                data = serialize(root)
                decoded = deserialize(data)
                result = tree_to_list(decoded)
                self.assertEqual(
                    result,
                    case["tree"],
                    f"Round-trip failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
