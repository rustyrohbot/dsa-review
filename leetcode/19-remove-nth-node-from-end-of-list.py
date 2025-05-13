# 19. Remove Nth Node From End of List
#
# Description:
# Given the head of a linked list, remove the n-th node from the end of the list and
# return its head.
#
# Constraints:
# The number of nodes in the list is in the range [1, 30].
# 0 <= Node.val <= 100
# 1 <= n <= size of the list
#
# Examples:
# Input: head = [1,2,3,4,5], n = 2    Output: [1,2,3,5]
# Input: head = [1], n = 1            Output: []
# Input: head = [1,2], n = 1          Output: [1]
# Input: head = [1,2], n = 2          Output: [2]

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


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Removes the n-th node from end of list and returns the head.
    """
    # TODO: Implement the two-pointer solution here
    pass

class TestRemoveNthNodeFromEnd(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"vals": [1,2,3,4,5], "n": 2, "expected": [1,2,3,5], "id": "Remove middle"},
            {"vals": [1],         "n": 1, "expected": [],        "id": "Single node"},
            {"vals": [1,2],       "n": 1, "expected": [1],       "id": "Remove tail"},
            {"vals": [1,2],       "n": 2, "expected": [2],       "id": "Remove head"},
            {"vals": [1,2,3],     "n": 3, "expected": [2,3],     "id": "Remove first of three"},
            {"vals": [1,2,3],     "n": 1, "expected": [1,2],     "id": "Remove last of three"},
        ]

    def test_remove_nth(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                head = build_linked_list(case["vals"])
                modified = removeNthFromEnd(head, case["n"])
                result = linked_list_to_list(modified)
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed: got {result}, expected {case['expected']}"
                )

if __name__ == "__main__":
    unittest.main()
