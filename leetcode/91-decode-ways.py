# 91. Decode Ways
#
# Description:
# A message containing letters from A-Z can be encoded into numbers using the mapping:
# 'A'->"1", 'B'->"2", ..., 'Z'->"26".
# Given a string s containing only digits, return the number of ways to decode it.
# Leading zeros are invalid: "06" cannot be decoded.
#
# Constraints:
# 1 <= len(s) <= 100
# s consists only of digits and may contain leading zeros.
# The answer is guaranteed to fit in a 32-bit integer.

import unittest


def numDecodings(s: str) -> int:
    """
    Returns the number of ways to decode the digit string s into letters A-Z.

    Parameters:
        s (str): The encoded message string.
    Returns:
        int: Number of valid decodings.
    """
    # TODO: Implement dynamic programming solution here
    pass


class TestDecodeWays(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"s": "12",    "expected": 2,  "id": "Basic two ways (1,2 and 12)"},
            {"s": "226",   "expected": 3,  "id": "Three ways (2-2-6, 22-6, 2-26)"},
            {"s": "0",     "expected": 0,  "id": "Single zero invalid"},
            {"s": "10",    "expected": 1,  "id": "Zero with valid prefix"},
            {"s": "100",   "expected": 0,  "id": "Trailing zero invalid"},
            {"s": "27",    "expected": 1,  "id": "Two-digit >26 only singles"},
            {"s": "101",   "expected": 1,  "id": "Zeros only as part of valid '10'"},
            {"s": "11106", "expected": 2,  "id": "Mixed valid and invalid pairs"},
        ]

    def test_num_decodings(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = numDecodings(case["s"])
                # Validate return type
                self.assertIsInstance(result, int, "Result should be an integer")
                # Validate correctness
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed for s='{case['s']}'"
                )


if __name__ == "__main__":
    unittest.main()
