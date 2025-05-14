# 20. Valid Parentheses
#
# Description:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets are closed by the same type of brackets.
# 2. Open brackets are closed in the correct order.
#
# Constraints:
# 1 <= len(s) <= 10^4
# s consists only of '(', ')', '{', '}', '[' and ']'.
#
# Examples:
# Input: s = "()"         Output: True
# Input: s = "()[]{}"     Output: True
# Input: s = "(]"         Output: False

import unittest


def isValid(s: str) -> bool:
    """
    Returns True if the parentheses string is valid according to matching rules.
    Parameters:
        s (str): The string containing bracket characters.
    Returns:
        bool: True if valid, False otherwise.
    """

    matching = { '}': '{', ']': '[', ')': '('}
    stack = []

    for c in s:
        if c in matching:
            if stack and stack[-1] == matching[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return len(stack) == 0


class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"s": "()",        "expected": True,  "id": "Simple pair"},
            {"s": "()[]{}",    "expected": True,  "id": "Mixed types"},
            {"s": "(]",        "expected": False, "id": "Mismatched"},
            {"s": "([)]",      "expected": False, "id": "Cross order"},
            {"s": "{[]}",      "expected": True,  "id": "Nested"},
            {"s": "",          "expected": True,  "id": "Empty string"},
            {"s": "((([])))",  "expected": True,  "id": "Deep nesting"},
            {"s": "]",         "expected": False, "id": "Single closing"},
        ]

    def test_is_valid(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = isValid(case["s"])
                # Validate return type
                self.assertIsInstance(result, bool, "Result should be a boolean")
                # Validate correctness
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed for input '{case['s']}'"
                )


if __name__ == "__main__":
    unittest.main()