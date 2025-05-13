# 49. Group Anagrams
#
# Description:
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
#
# Constraints:
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
#
# Examples:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
#
# Input: strs = []
# Output: []
#
# Input: strs = [""]
# Output: [[""]]

import unittest
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups a list of strings into anagrams.

    Parameters:
        strs (List[str]): List of lowercase strings.
    Returns:
        List[List[str]]: A list of groups of anagrams.
    """
    # TODO: Implement the grouping logic here
    pass


class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"strs": ["eat","tea","tan","ate","nat","bat"], "expected": [["eat","tea","ate"],["tan","nat"],["bat"]], "id": "Example 1"},
            {"strs": [],                                        "expected": [],                                           "id": "Empty input"},
            {"strs": [""],                                      "expected": [[""]],                                       "id": "Single empty string"},
            {"strs": ["a"],                                     "expected": [["a"]],                                     "id": "Single string"},
            {"strs": ["a","b","ab","ba"],                "expected": [["a"],["b"],["ab","ba"]],           "id": "Mixed groups"},
        ]

    def test_group_anagrams(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = groupAnagrams(case["strs"])
                # Validate type
                self.assertIsInstance(result, list, "Result should be a list of lists of strings")
                for group in result:
                    self.assertIsInstance(group, list, "Each group should be a list of strings")
                    for s in group:
                        self.assertIsInstance(s, str, "Anagram elements should be strings")
                # Normalize for comparison: sort each group and compare as multisets
                normalized_result = [sorted(group) for group in result]
                normalized_expected = [sorted(group) for group in case["expected"]]
                self.assertCountEqual(
                    normalized_result,
                    normalized_expected,
                    f"Case '{case['id']}' failed: got {result}, expected {case['expected']}"
                )


if __name__ == "__main__":
    unittest.main()