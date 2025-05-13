# 21. Merge Two Sorted Lists
#
# Description:
# Merge two sorted linked lists and return it as a sorted list.
# The list is made by splicing together the nodes of the first two lists.
#
# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
#
# Examples:
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
# Input: l1 = [], l2 = []
# Output: []

import unittest
from typing import Optional, List

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


def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merges two sorted linked lists and returns the head of the merged list.

    Parameters:
        l1 (ListNode): Head of the first sorted list.
        l2 (ListNode): Head of the second sorted list.
    Returns:
        ListNode: Head of the merged sorted list.
    """
    # TODO: Implement the solution here
    pass

class TestMergeTwoSortedLists(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"l1": [1, 2, 4], "l2": [1, 3, 4], "expected": [1, 1, 2, 3, 4, 4], "id": "Example 1"},
            {"l1": [], "l2": [], "expected": [], "id": "Empty lists"},
            {"l1": [], "l2": [0], "expected": [0], "id": "One empty"},
            {"l1": [5], "l2": [1, 2, 3, 4, 6], "expected": [1, 2, 3, 4, 5, 6], "id": "Interleaved"},
            {"l1": [1, 1, 1], "l2": [1, 1], "expected": [1, 1, 1, 1, 1], "id": "Duplicates"},
        ]

    def test_merge_two_lists(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                l1 = build_linked_list(case["l1"])
                l2 = build_linked_list(case["l2"])
                merged = mergeTwoLists(l1, l2)
                result = linked_list_to_list(merged)
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed: got {result}, expected {case['expected']}"
                )

if __name__ == "__main__":
    unittest.main()
