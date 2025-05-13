# 23. Merge k Sorted Lists
#
# Description:
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
#
# Constraints:
# k == len(lists)
# 0 <= k <= 10^4
# 0 <= total number of nodes <= 10^5
# -10^4 <= Node.val <= 10^4
# lists[i] is sorted in ascending order.
#
# Examples:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
#
# Input: lists = []
# Output: []
#
# Input: lists = [[]]
# Output: []

import unittest
from typing import List, Optional

class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


def build_linked_list(vals: List[int]) -> Optional[ListNode]:
    """
    Helper to build a linked list from a list of values.
    """
    head = None
    prev = None
    for v in vals:
        node = ListNode(v)
        if not head:
            head = node
        else:
            prev.next = node
        prev = node
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """
    Helper to convert linked list back to Python list of values.
    """
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
    return vals


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merges k sorted linked lists and returns the head of the merged sorted list.
    """
    # TODO: Implement the solution here
    pass

class TestMergeKSortedLists(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"lists": [[1,4,5], [1,3,4], [2,6]], "expected": [1,1,2,3,4,4,5,6], "id": "Example"},
            {"lists": [],                       "expected": [],                  "id": "Empty input"},
            {"lists": [[]],                     "expected": [],                  "id": "One empty list"},
            {"lists": [[1,2,3]],               "expected": [1,2,3],            "id": "Single list"},
            {"lists": [[2,2,2], [2,2]],        "expected": [2,2,2,2,2],        "id": "Duplicates"},
            {"lists": [[-1,0,1], [1,2,3]],      "expected": [-1,0,1,1,2,3],      "id": "Negative and positive"},
        ]

    def test_merge_k_lists(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                built = [build_linked_list(vals) for vals in case["lists"]]
                merged = mergeKLists(built)
                result = linked_list_to_list(merged)
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed: got {result}, expected {case['expected']}"
                )

if __name__ == "__main__":
    unittest.main()
