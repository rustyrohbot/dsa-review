# 224. Basic Calculator
#
# Description:
# Implement a basic calculator to evaluate a simple expression string.
# The string may contain digits, '+', '-', '(', ')', and spaces.
#
# Constraints:
# 1 <= len(s) <= 3 * 10^5
# s consists of digits, '+', '-', '(', ')', and ' '.
# The expression is always valid.
#
# Examples:
# Input: s = "1 + 1"               Output: 2
# Input: s = " 2-1 + 2 "           Output: 3
# Input: s = "(1+(4+5+2)-3)+(6+8)" Output: 23

import unittest


def calculate(s: str) -> int:
    """
    Evaluates the arithmetic expression in s, supporting +, -, parentheses, and spaces.
    """
    # TODO: Implement the solution here
    pass


class TestBasicCalculator(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"s": "1 + 1",                         "expected": 2,             "id": "Simple addition"},
            {"s": " 2-1 + 2 ",                     "expected": 3,             "id": "Addition and subtraction"},
            {"s": "(1+(4+5+2)-3)+(6+8)",           "expected": 23,            "id": "Parentheses example"},
            {"s": "   3 + (2 - (8 + 1)) ",         "expected": -4,            "id": "Nested parentheses"},
            {"s": "10- (2 + 3 - (4-5))",           "expected": 4,             "id": "Complex nested"},
            {"s": "2147483647",                    "expected": 2147483647,    "id": "Large number"},
            {"s": "-2+ 1",                         "expected": -1,            "id": "Leading minus"},
        ]

    def test_calculate(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = calculate(case["s"])
                # Validate return type
                self.assertIsInstance(result, int, "Result should be an integer")
                # Validate correctness
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed for input '{case['s']}'"
                )


if __name__ == "__main__":
    unittest.main()
