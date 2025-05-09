# 314. Binary Tree Vertical Order Traversal
#
# Description:
# Given the root of a binary tree, return the vertical order traversal of its
# nodes' values. (i.e., from top to bottom, column by column).
#
# If two nodes are in the same row and column, the order should be from
# left to right.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

from typing import List, Optional, collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    """Helper function to build a tree from a list (level-order)."""
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = collections.deque([root])
    i = 1
    while i < len(nodes):
        current_node = queue.popleft()
        if nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current_node.right = TreeNode(nodes[i])
            queue.append(current_node.right)
        i += 1
    return root

def verticalOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Performs a vertical order traversal of the binary tree.
    """
    # TODO: Implement the solution here
    pass


if __name__ == "__main__":
    test_cases = [
        {
            "input_list": [3, 9, 20, None, None, 15, 7],
            #   3 (0)
            #  / \
            # 9(-1) 20(1)
            #      /  \
            #    15(0) 7(2)
            # Columns:
            # -1: [9]
            #  0: [3, 15] (3 is above 15)
            #  1: [20]
            #  2: [7]
            "expected": [[9], [3, 15], [20], [7]],
            "id": "Example 1",
        },
        {
            "input_list": [3, 9, 8, 4, 0, 1, 7],
            #      3 (0)
            #    /   \
            #   9(-1) 8(1)
            #  / \   / \
            # 4(-2)0(0)1(0)7(2)
            # Columns:
            # -2: [4]
            # -1: [9]
            #  0: [3,0,1] (0 and 1 are at same level, 0 is left of 1 conceptually via parent)
            #  1: [8]
            #  2: [7]
            "expected": [[4], [9], [3, 0, 1], [8], [7]],
            "id": "Example 2 (left-to-right at same level/col)",
        },
        {
            "input_list": [3,9,8,4,0,1,7,None,None,None,2,5],
            #         3 (0)
            #       /   \
            #      9(-1)  8(1)
            #     / \    / \
            #    4(-2)0(0)1(0)7(2)
            #         \  /
            #         2(1)5(-1) (0's right child is 2, 1's left child is 5)
            #
            # Level 0: 3 (col 0)
            # Level 1: 9 (col -1), 8 (col 1)
            # Level 2: 4 (col -2), 0 (col 0), 1 (col 0), 7 (col 2)
            # Level 3: 2 (col 1, child of 0), 5 (col -1, child of 1)
            #
            # Col -2: [4]
            # Col -1: [9, 5] (9 from L1, 5 from L3)
            # Col  0: [3, 0, 1] (3 from L0, 0 from L2, 1 from L2. 0 before 1 due to BFS order of parents)
            # Col  1: [8, 2] (8 from L1, 2 from L3)
            # Col  2: [7]
            "expected": [[4], [9, 5], [3, 0, 1], [8, 2], [7]],
            "id": "Example 3 (more complex, nodes at different levels in same col)",
        },
        {
            "input_list": [],
            "expected": [],
            "id": "Empty tree",
        },
        {
            "input_list": [1],
            "expected": [[1]],
            "id": "Single node",
        },
        {
            "input_list": [1,2,3,4,5,6,7],
            #       1(0)
            #      /   \
            #     2(-1) 3(1)
            #    / \   / \
            #   4(-2)5(0)6(0)7(2)
            # Col -2: [4]
            # Col -1: [2]
            # Col  0: [1,5,6]
            # Col  1: [3]
            # Col  2: [7]
            "expected": [[4],[2],[1,5,6],[3],[7]],
            "id": "Fuller tree"
        },
        {
            "input_list": [0,8,1,None,None,3,2,None,4,5,None,None,7,6],
            #           0 (0)
            #          / \
            #         8(-1)1(1)
            #            / \
            #           3(0)2(2)
            #            \ / \
            #            4(1)5(1)7(3)
            #               /
            #              6(0)
            #
            # L0: 0 (0)
            # L1: 8 (-1), 1 (1)
            # L2: 3 (0), 2 (2)  (children of 1)
            # L3: 4 (1), 5 (1), 7(3) (children of 3 and 2)
            # L4: 6 (0) (child of 5)
            #
            # Col -1: [8]
            # Col  0: [0,3,6]
            # Col  1: [1,4,5] (1, then 4, then 5 due to BFS levels and parent order)
            # Col  2: [2]
            # Col  3: [7]
            "expected": [[8],[0,3,6],[1,4,5],[2],[7]],
            "id": "Tricky ordering within columns"
        }
    ]

    passed_all = True
    for i, case in enumerate(test_cases):
        input_list = case["input_list"]
        root = build_tree(input_list)
        expected_output = case["expected"]
        case_id = case["id"]

        try:
            actual_output = verticalOrder(root)
            # The order of columns matters, and order within columns matters.
            # Direct comparison should work if implementation is correct.
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
            import traceback
            traceback.print_exc()
            passed_all = False
        print("-" * 40)

    if passed_all:
        print("All test cases passed!")
    else:
        print("Some test cases failed.")

