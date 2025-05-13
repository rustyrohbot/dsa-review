# 269. Alien Dictionary
#
# Description:
# Given a list of words from the alien language dictionary, where the words are sorted lexicographically
# by the rules of this new language, derive the order of characters in the alien alphabet.
# If the order is invalid or cannot be determined, return an empty string.
#
# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of only lowercase English letters.

from typing import List
import unittest

def alienOrder(words: List[str]) -> str:
    """
    Given a sorted list of words in an alien language, returns a string representing
    the characters in lexicographically sorted order according to the alien language rules.
    Returns an empty string if no valid ordering exists.
    """
    # TODO: Implement topological sort on character precedence graph
    pass

class TestAlienDictionary(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {
                "words": ["wrt","wrf","er","ett","rftt"],
                "expected": "wertf",
                "id": "Example 1"
            },
            {
                "words": ["z","x"],
                "expected": "zx",
                "id": "Two letters"
            },
            {
                "words": ["z","x","z"],
                "expected": "",
                "id": "Invalid cycle"
            },
            {
                "words": ["abc","ab"],  # prefix invalid
                "expected": "",
                "id": "Prefix conflict"
            },
            {
                "words": ["a"],
                "expected": "a",
                "id": "Single word"
            },
        ]

    def test_alien_order(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = alienOrder(case["words"])
                self.assertIsInstance(result, str, "Result should be a string")
                self.assertEqual(
                    result,
                    case["expected"],
                    f"alienOrder failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
