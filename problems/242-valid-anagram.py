# 242. Valid Anagram
#
# Description:
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
#
# Constraints:
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
# Examples:
# Input: s = "anagram", t = "nagaram"    Output: True
# Input: s = "rat", t = "car"             Output: False

import unittest


def isAnagram(s: str, t: str) -> bool:
    """
    Returns True if t is an anagram of s, False otherwise.
    """
    # TODO: Implement the solution here
    pass


class TestValidAnagram(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"s": "anagram", "t": "nagaram", "expected": True,  "id": "Example 1"},
            {"s": "rat",     "t": "car",     "expected": False, "id": "Example 2"},
            {"s": "",        "t": "",        "expected": True,  "id": "Both empty"},
            {"s": "a",       "t": "ab",      "expected": False, "id": "Different lengths"},
            {"s": "ab",      "t": "ba",      "expected": True,  "id": "Two letters swapped"},
            {"s": "aacc",    "t": "ccac",    "expected": False, "id": "Counts mismatch"},
        ]

    def test_is_anagram(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = isAnagram(case["s"], case["t"])
                # Validate return type
                self.assertIsInstance(result, bool, "Result should be a boolean")
                # Validate correctness
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed for s='{case['s']}', t='{case['t']}'"
                )


if __name__ == "__main__":
    unittest.main()
