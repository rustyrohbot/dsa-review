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

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Performs a level order traversal of the binary tree.
    """
    pass

if __name__ == "__main__":
    test_cases_102 = [
        {
            "input_list": [3, 9, 20, None, None, 15, 7],
            "expected": [[3], [9, 20], [15, 7]],
            "id": "LC Example 1",
        },
        {
            "input_list": [1],
            "expected": [[1]],
            "id": "Single node",
        },
        {
            "input_list": [],
            "expected": [],
            "id": "Empty tree",
        },
        {
            "input_list": [1, 2, 3, 4, None, None, 5],
            #    1
            #   / \
            #  2   3
            # /     \
            # 4       5
            "expected": [[1], [2, 3], [4, 5]],
            "id": "Incomplete tree",
        },
        {
            "input_list": [None], # Test case for build_tree_level_order
            "expected": [],
            "id": "Tree with None root"
        }
    ]
    passed_all = True
    print("--- Testing LeetCode #102: Level Order Traversal ---")
    for i, case in enumerate(test_cases_102):
        input_list = case["input_list"]
        root = build_tree_level_order(input_list)
        expected_output = case["expected"]
        case_id = case["id"]
        try:
            actual_output = levelOrder(root)
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
        print("All #102 test cases passed!\n")
    else:
        print("Some #102 test cases failed.\n")
