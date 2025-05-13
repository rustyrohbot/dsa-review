# 206. Reverse Linked List
#
# Description:
# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
# Constraints:
# The number of nodes in the list is in the range [0, 5000].
# -5000 <= Node.val <= 5000

from typing import Optional
import unittest

class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverses a singly linked list and returns the new head.
    """
    # TODO: Implement iterative or recursive reversal
    pass

class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        def build_list(vals):
            head = ListNode(vals[0]) if vals else None
            curr = head
            for v in vals[1:]:
                curr.next = ListNode(v)
                curr = curr.next
            return head

        def to_list(head):
            vals = []
            curr = head
            while curr:
                vals.append(curr.val)
                curr = curr.next
            return vals

        self.build_list = build_list
        self.to_list = to_list
        self.test_cases = [
            {"input": [],       "expected": [],       "id": "Empty list"},
            {"input": [1],      "expected": [1],      "id": "Single node"},
            {"input": [1,2,3,4,5], "expected": [5,4,3,2,1], "id": "Multiple nodes"},
            {"input": [1,2],    "expected": [2,1],    "id": "Two nodes"},
        ]

    def test_reverse_list(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                head = self.build_list(case["input"])
                reversed_head = reverseList(head)
                self.assertEqual(self.to_list(reversed_head), case["expected"], f"Mismatch for case '{case['id']}'")
                # Check that for non-empty, the original head now ends at None
                if case["input"]:
                    # original head value is last of reversed list
                    self.assertIsNone(head.next if len(case["input"]) == 1 else None)

if __name__ == "__main__":
    unittest.main()
