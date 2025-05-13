# 647. Palindromic Substrings
#
# Description:
# Given a string s, return the number of palindromic substrings in it.
# A substring is a contiguous sequence of characters within the string.
# A string is palindromic if it reads the same backward as forward.
#
# Constraints:
# 1 <= s.length <= 1000
# s consists of lowercase English letters.

import unittest

def countSubstrings(s: str) -> int:
    """
    Returns the total number of palindromic substrings in s.
    """
    # TODO: Implement expand-around-center or DP solution
    pass

class TestPalindromicSubstrings(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"s": "abc",    "expected": 3,  "id": "No repeats"},   # "a","b","c"
            {"s": "aaa",    "expected": 6,  "id": "All same"},     # "a","a","a","aa","aa","aaa"
            {"s": "aba",    "expected": 4,  "id": "Simple palindrome"}, # "a","b","a","aba"
            {"s": "ababa",  "expected": 9,  "id": "Nested pals"},
            {"s": "a",      "expected": 1,  "id": "Single char"},
            {"s": "abcb",   "expected": 5,  "id": "Partial pals"}   # "a","b","c","b","bcb"
        ]

    def test_count_substrings(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = countSubstrings(case["s"])
                self.assertIsInstance(result, int, "Result should be an integer")
                self.assertEqual(
                    result,
                    case["expected"],
                    f"countSubstrings failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
