# 227. Basic Calculator II
#
# Description:
# Implement a basic calculator to evaluate a simple expression string.
# The expression string contains only non-negative integers, '+', '-', '*', '/', and spaces.
# Integer division should truncate toward zero and discard the fractional part.
#
# Constraints:
# 1 <= len(s) <= 3 * 10^5
# s consists of digits and the operators '+', '-', '*', '/', and spaces.
# The expression is always valid.
#
# Examples:
# Input: s = "3+2*2"       Output: 7
# Input: s = " 3/2 "       Output: 1
# Input: s = " 3+5 / 2 "   Output: 5
# Input: s = "14-3/2"      Output: 13

import unittest


def calculate(s: str) -> int:
    """
    Evaluates the arithmetic expression in s, supporting +, -, *, / and spaces.
    Integer division truncates toward zero.
    """
    # TODO: Implement the solution here
    pass


class TestBasicCalculatorII(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"s": "3+2*2",           "expected": 7,              "id": "Simple multiplication and addition"},
            {"s": " 3/2 ",           "expected": 1,              "id": "Simple division"},
            {"s": " 3+5 / 2 ",       "expected": 5,              "id": "Addition and division"},
            {"s": "14-3/2",          "expected": 13,             "id": "Subtraction and division"},
            {"s": "42",              "expected": 42,             "id": "Single number"},
            {"s": "0-2147483647",    "expected": -2147483647,    "id": "Large negative result"},
            {"s": " 42* 3 + 5 / 2 ", "expected": 42*3 + 5//2,     "id": "Complex expression"},
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
