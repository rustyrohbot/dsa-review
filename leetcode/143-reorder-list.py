# 143. Reorder List
#
# Description:
# You are given the head of a singly linked list. The list is: L0→L1→…→Ln-1→Ln.
# Reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
#
# Constraints:
# The number of nodes in the list is in the range [1, 5 * 10^4].
# -1000 <= Node.val <= 1000
#
# Examples:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
#
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

from typing import Optional
import unittest

class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


def reorderList(head: Optional[ListNode]) -> None:
    """
    Reorders the list in-place to the required sequence.
    """
    # TODO: Implement by finding middle, reversing second half, and merging
    pass

class TestReorderList(unittest.TestCase):
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
            {"input": [1,2,3,4], "expected": [1,4,2,3], "id": "Even length"},
            {"input": [1,2,3,4,5], "expected": [1,5,2,4,3], "id": "Odd length"},
            {"input": [], "expected": [], "id": "Empty list"},
            {"input": [1], "expected": [1], "id": "Single node"},
            {"input": [1,2], "expected": [1,2], "id": "Two nodes"},
        ]

    def test_reorder_list(self):
        for case in self.test_cases:
            with self.subTest(case["id"]):
                head = self.build_list(case["input"])
                reorderList(head)
                self.assertEqual(self.to_list(head), case["expected"], f"Mismatch for case '{case['id']}'")

if __name__ == "__main__":
    unittest.main()
