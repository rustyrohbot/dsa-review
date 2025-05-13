# 141. Linked List Cycle
#
# Description:
# Given head of a linked list, determine if the linked list has a cycle in it.
# A cycle exists if some node in the list can be reached again by continuously following next pointers.
#
# Constraints:
# The number of nodes in the list is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a zero-based index where tail connects; -1 means no cycle.
#
# Examples:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle connecting tail back to the second node.
#
# Input: head = [1,2], pos = 0
# Output: true
#
# Input: head = [1], pos = -1
# Output: false

from typing import Optional
import unittest

class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


def hasCycle(head: Optional[ListNode]) -> bool:
    """
    Returns True if there is a cycle in the linked list, else False.
    """
    # TODO: Implement Floyd's Tortoise and Hare algorithm
    pass

class TestLinkedListCycle(unittest.TestCase):
    def setUp(self):
        def build_list(values, pos):
            """
            Builds a linked list from `values` and creates a cycle at index `pos` (-1 for no cycle).
            """
            if not values:
                return None
            head = ListNode(values[0])
            current = head
            nodes = [head]
            for val in values[1:]:
                node = ListNode(val)
                current.next = node
                current = node
                nodes.append(node)
            if pos != -1:
                current.next = nodes[pos]
            return head

        self.test_cases = [
            {"values": [3, 2, 0, -4], "pos": 1, "expected": True, "id": "Cycle at pos 1"},
            {"values": [1, 2], "pos": 0, "expected": True, "id": "Cycle at pos 0"},
            {"values": [1], "pos": -1, "expected": False, "id": "Single node no cycle"},
            {"values": [], "pos": -1, "expected": False, "id": "Empty list"},
        ]

    def test_has_cycle(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                head = build_list(case["values"], case["pos"])
                result = hasCycle(head)
                self.assertIsInstance(result, bool, "Result should be a boolean")
                self.assertEqual(result, case["expected"], f"Mismatch for case '{case['id']}'")

if __name__ == "__main__":
    unittest.main()
