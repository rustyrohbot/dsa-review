from typing import List, Optional, collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_level_order(
    input_list: List[Optional[int]],
) -> Optional[TreeNode]:
    """
    Builds a binary tree from a list representation (level order with None
    for missing children).
    This function is provided to help with testing.
    """
    if not input_list or input_list[0] is None:
        return None

    root = TreeNode(input_list[0])
    queue = collections.deque([root])
    i = 1
    while queue and i < len(input_list):
        current_node = queue.popleft()

        # Left child
        if i < len(input_list):
            left_val = input_list[i]
            if left_val is not None:
                current_node.left = TreeNode(left_val)
                queue.append(current_node.left)
            i += 1

        # Right child
        if i < len(input_list):
            right_val = input_list[i]
            if right_val is not None:
                current_node.right = TreeNode(right_val)
                queue.append(current_node.right)
            i += 1
    return root

# 662. Maximum Width of Binary Tree
#
# Description:
# Given the root of a binary tree, return the maximum width of the given tree.
# The maximum width of a tree is the maximum width among all levels.
# The width of one level is defined as the length between the end-nodes
# (the leftmost and rightmost non-null nodes), where the null nodes between
# the end-nodes that would be present in a complete binary tree extending down
# to that level are also counted into the length calculation.
# It is guaranteed that the answer will in the range of 32-bit signed integer.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 3000].
# -100 <= Node.val <= 100

def widthOfBinaryTree(root: Optional[TreeNode]) -> int:
    """
    Calculates the maximum width of the binary tree.
    """
    # TODO: Implement the solution here
    pass

if __name__ == "__main__":
    test_cases_662 = [
        {
            "input_list": [1, 3, 2, 5, 3, None, 9],
            # Level 0: 1 (idx 0) -> width 1
            # Level 1: 3 (idx 0), 2 (idx 1) -> width 1-0+1 = 2
            # Level 2: 5 (idx 0), 3 (idx 1), 9 (idx 3) -> width 3-0+1 = 4
            "expected": 4,
            "id": "LC Example 1",
        },
        {
            "input_list": [1, 3, None, 5, 3],
            # Level 0: 1 (idx 0) -> width 1
            # Level 1: 3 (idx 0) -> width 1
            # Level 2: 5 (idx 0), 3 (idx 1) -> width 1-0+1 = 2
            "expected": 2,
            "id": "LC Example 2",
        },
        {
            "input_list": [1, 3, 2, 5],
            # Level 0: 1 (idx 0) -> width 1
            # Level 1: 3 (idx 0), 2 (idx 1) -> width 2
            # Level 2: 5 (idx 0) -> width 1
            "expected": 2,
            "id": "LC Example 3",
        },
        {
            "input_list": [],
            "expected": 0,
            "id": "Empty tree",
        },
        {
            "input_list": [1],
            "expected": 1,
            "id": "Single node",
        },
        {
            "input_list": [1, 2, 3, 4, None, None, 7, 8],
            # L0: 1 (0) -> w 1
            # L1: 2 (0), 3 (1) -> w 2
            # L2: 4 (0), 7 (3) -> w 4 (indices 0,1,2,3)
            # L3: 8 (0) -> w 1
            "expected": 4,
            "id": "Wider at lower level",
        },
        {
            "input_list": [None], # Test case for build_tree_level_order
            "expected": 0, # Expected width for an empty tree
            "id": "Tree with None root"
        }
    ]
    passed_all = True
    print("--- Testing LeetCode #662: Maximum Width of Binary Tree ---")
    for i, case in enumerate(test_cases_662):
        input_list = case["input_list"]
        root_node = build_tree_level_order(input_list) # Renamed to avoid conflict
        expected_output = case["expected"]
        case_id = case["id"]
        try:
            # If the tree is empty (root_node is None), widthOfBinaryTree
            # should handle it.
            # The problem statement implies 0 nodes means width 0.
            if not root_node and not input_list: # Specifically for truly empty list
                 actual_output = 0
            elif not root_node and input_list == [None]: # For [None] input
                 actual_output = 0
            else:
                actual_output = widthOfBinaryTree(root_node)

            if actual_output == expected_output:
                print(f"Test Case {i + 1} ({case_id}): PASSED")
            else:
                print(f"Test Case {i + 1} ({case_id}): FAILED")
                print(f"  Input List: {input_list}")
                print(f"  Expected:   {expected_output}")
                print(f"  Actual:     {actual_output}")
                passed_all = False
        except Exception as e:
            print(f"Test Case {i + 1} ({case_id}): ERROR")
            print(f"  Input List: {input_list}")
            print(f"  Exception: {e}")
            passed_all = False
        print("-" * 30)
    if passed_all:
        print("All #662 test cases passed!\n")
    else:
        print("Some #662 test cases failed.\n")
