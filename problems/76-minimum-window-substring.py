# 76. Minimum Window Substring
#
# Description:
# Given two strings s and t of lengths m and n respectively, return the minimum window substring
# of s such that every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".
#
# Constraints:
# m == len(s)
# n == len(t)
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
#
# Examples:
# Input: s = "ADOBECODEBANC", t = "ABC"  Output: "BANC"
# Input: s = "a", t = "a"              Output: "a"
# Input: s = "a", t = "aa"             Output: ""

import unittest


def minWindow(s: str, t: str) -> str:
    """
    Returns the smallest substring of s that contains all characters of t.
    If no such substring exists, returns an empty string.
    """
    # TODO: Implement the sliding window solution here
    pass


class TestMinimumWindowSubstring(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"s": "ADOBECODEBANC", "t": "ABC", "expected": "BANC", "id": "Example 1"},
            {"s": "a",             "t": "a",   "expected": "a",    "id": "Single match"},
            {"s": "a",             "t": "aa",  "expected": "",     "id": "No possible window"},
            {"s": "ab",            "t": "b",   "expected": "b",    "id": "Two chars"},
            {"s": "aa",            "t": "aa",  "expected": "aa",   "id": "Exact match"},
        ]

    def test_min_window(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = minWindow(case["s"], case["t"])
                # Validate return type
                self.assertIsInstance(result, str, "Result should be a string")
                # Validate correctness
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed for s='{case['s']}', t='{case['t']}'"
                )


if __name__ == "__main__":
    unittest.main()
