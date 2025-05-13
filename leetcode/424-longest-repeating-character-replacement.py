# 424. Longest Repeating Character Replacement
#
# Description:
# Given a string s and an integer k, you can choose any character of the string and change it to any other uppercase English character.
# You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
#
# Constraints:
# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length

import unittest

def characterReplacement(s: str, k: int) -> int:
    """
    Returns the length of the longest substring containing the same letter after at most k replacements.
    """
    # TODO: Implement sliding window with character count tracking
    pass

class TestCharacterReplacement(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"s": "ABAB",     "k": 2, "expected": 4, "id": "Example 1"},
            {"s": "AABABBA",  "k": 1, "expected": 4, "id": "Example 2"},
            {"s": "AAAA",     "k": 2, "expected": 4, "id": "All same"},
            {"s": "ABCDE",    "k": 1, "expected": 2, "id": "No repeats"},
            {"s": "AABBB",    "k": 2, "expected": 5, "id": "Extend B"},
            {"s": "",         "k": 0, "expected": 0, "id": "Empty string"},
        ]

    def test_character_replacement(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = characterReplacement(case["s"], case["k"])
                self.assertIsInstance(result, int, "Result should be an integer")
                self.assertEqual(
                    result,
                    case["expected"],
                    f"characterReplacement failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
