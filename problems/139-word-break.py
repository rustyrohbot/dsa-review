# 139. Word Break
#
# Description:
# Given a string s and a dictionary of strings wordDict, return true if s can be
# segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
#
# Constraints:
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
#
# Examples:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
#
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
#
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

from typing import List
import unittest


def wordBreak(s: str, wordDict: List[str]) -> bool:
    """
    Returns True if s can be segmented into one or more words from wordDict, else False.
    """
    # TODO: Implement dynamic programming (DP) or BFS to check segmentation
    pass

class TestWordBreak(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"s": "leetcode", "wordDict": ["leet", "code"], "expected": True, "id": "Basic example 1"},
            {"s": "applepenapple", "wordDict": ["apple", "pen"], "expected": True, "id": "Basic example 2"},
            {"s": "catsandog", "wordDict": ["cats", "dog", "sand", "and", "cat"], "expected": False, "id": "Basic example 3"},
            {"s": "a", "wordDict": ["a"], "expected": True, "id": "Single char true"},
            {"s": "a", "wordDict": ["b"], "expected": False, "id": "Single char false"},
        ]

    def test_word_break(self):
        for case in self.test_cases:
            with self.subTest(case["id"]):
                result = wordBreak(case["s"], case["wordDict"])
                self.assertIsInstance(result, bool, "Result should be a boolean")
                self.assertEqual(result, case["expected"], f"Mismatch for case '{case['id']}'")

if __name__ == "__main__":
    unittest.main()
