# 5. Longest Palindromic Substring
#
# Description:
# Given a string s, return the longest palindromic substring in s.
#
# Constraints:
# 1 <= len(s) <= 1000
# s consists of printable ASCII characters.
#
# Examples:
# Input: s = "babad"       Output: "bab" or "aba"
# Input: s = "cbbd"        Output: "bb"

import unittest


def longestPalindrome(s: str) -> str:
    """
    Returns the longest palindromic substring of s.

    Parameters:
        s (str): Input string.
    Returns:
        str: Longest palindromic substring.
    """
    # TODO: Implement the solution here
    pass


class TestLongestPalindromicSubstring(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"s": "babad",               "expected": ["bab", "aba"],       "id": "Example 1"},
            {"s": "cbbd",                "expected": ["bb"],               "id": "Example 2"},
            {"s": "a",                   "expected": ["a"],                "id": "Single char"},
            {"s": "",                    "expected": [""],                 "id": "Empty string"},
            {"s": "aaaa",                "expected": ["aaaa"],            "id": "All same"},
            {"s": "racecar",             "expected": ["racecar"],         "id": "Odd palindrome"},
            {"s": "forgeeksskeegfor",    "expected": ["geeksskeeg"],       "id": "Even palindrome"},
        ]

    def test_longest_palindrome(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = longestPalindrome(case["s"])
                # Validate return type
                self.assertIsInstance(result, str, "Result should be a string")
                # Validate correctness (allow multiple valid answers)
                self.assertIn(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed for input '{case['s']}'. Got '{result}', expected one of {case['expected']}"
                )


if __name__ == "__main__":
    unittest.main()
