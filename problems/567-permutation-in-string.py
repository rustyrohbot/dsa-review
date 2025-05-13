# 567. Permutation in String
#
# Description:
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.
#
# Constraints:
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.
#
# Examples:
# Input: s1 = "ab", s2 = "eidbaooo"    Output: True
# Input: s1 = "ab", s2 = "eidboaoo"    Output: False

import unittest


def checkInclusion(s1: str, s2: str) -> bool:
    """
    Returns True if s2 contains any permutation of s1 as a substring.
    """
    # TODO: Implement the solution here
    pass


class TestPermutationInString(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"s1": "ab",    "s2": "eidbaooo",   "expected": True,  "id": "Example 1"},
            {"s1": "ab",    "s2": "eidboaoo",   "expected": False, "id": "Example 2"},
            {"s1": "a",     "s2": "ab",         "expected": True,  "id": "Single char true"},
            {"s1": "a",     "s2": "bc",         "expected": False, "id": "Single char false"},
            {"s1": "abc",   "s2": "bbbca",      "expected": True,  "id": "Permutation at end"},
            {"s1": "abcd",  "s2": "abc",        "expected": False, "id": "s2 shorter than s1"},
            {"s1": "aa",    "s2": "aaaaa",      "expected": True,  "id": "Repeated chars"},
        ]

    def test_check_inclusion(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = checkInclusion(case["s1"], case["s2"])
                # Validate return type
                self.assertIsInstance(result, bool, "Result should be a boolean")
                # Validate correctness
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed for s1='{case['s1']}', s2='{case['s2']}'"
                )


if __name__ == "__main__":
    unittest.main()
