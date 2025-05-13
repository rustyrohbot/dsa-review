# 1143. Longest Common Subsequence
#
# Description:
# Given two strings text1 and text2, return the length of their longest common subsequence.
# A subsequence of a string is a new string generated from the original string with some characters
# (can be none) deleted without changing the relative order of the remaining characters.
#
# Constraints:
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of lowercase English characters.
#
import unittest

def longestCommonSubsequence(text1: str, text2: str) -> int:
    """
    Returns the length of the longest common subsequence between text1 and text2.
    """
    # TODO: Implement dynamic programming solution (2D DP table)
    pass

class TestLongestCommonSubsequence(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"text1": "abcde", "text2": "ace",     "expected": 3, "id": "Example 1"},
            {"text1": "abc",   "text2": "abc",     "expected": 3, "id": "Identical strings"},
            {"text1": "abc",   "text2": "def",     "expected": 0, "id": "No common"},
            {"text1": "",      "text2": "abc",     "expected": 0, "id": "First empty"},
            {"text1": "abc",   "text2": "",        "expected": 0, "id": "Second empty"},
            {"text1": "bsbininm", "text2": "jmjkbkjkv", "expected": 1, "id": "Single common char"},
        ]

    def test_lcs(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = longestCommonSubsequence(case["text1"], case["text2"])
                self.assertIsInstance(result, int, "Result should be an integer")
                self.assertEqual(
                    result,
                    case["expected"],
                    f"longestCommonSubsequence failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
