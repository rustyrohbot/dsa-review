# 3. Longest Substring Without Repeating Characters
#
# Description:
# Given a string s, find the length of the longest substring without repeating characters.
#
# Constraints:
# 0 <= len(s) <= 5 * 10^4
# s consists of English letters, digits, symbols, and spaces.
#
# Examples:
# Input: s = "abcabcbb"  Output: 3
# Input: s = "bbbbb"     Output: 1
# Input: s = "pwwkew"    Output: 3
# Input: s = ""          Output: 0
# Input: s = " "         Output: 1
# Input: s = "au"        Output: 2
# Input: s = "dvdf"      Output: 3

import unittest


def lengthOfLongestSubstring(s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.
    """
    chars = set() # keeps track of characters in the substring
    result = 0 # length of longest substring
    start = 0 # start of substring

    for end in range(len(s)): # use loop iterator to track end of the substring
        while s[end] in chars: # duplicate found
            chars.remove(s[start]) # remove characters from the front of the window
            start += 1 # increment start of the window
        chars.add(s[end]) # add current character to the set
        result = max(result, end - start + 1) # result is the max of its current value or the difference between the end and begining index of the window plus one
    return result


class TestLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"s": "abcabcbb", "expected": 3, "id": "Simple repetition"},
            {"s": "bbbbb",    "expected": 1, "id": "All same"},
            {"s": "pwwkew",   "expected": 3, "id": "Mixed"},
            {"s": "",         "expected": 0, "id": "Empty string"},
            {"s": " ",        "expected": 1, "id": "Single space"},
            {"s": "au",       "expected": 2, "id": "Two unique"},
            {"s": "dvdf",     "expected": 3, "id": "Overlap case"},
        ]

    def test_length_of_longest_substring(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = lengthOfLongestSubstring(case["s"])
                # Validate return type
                self.assertIsInstance(result, int, "Result should be an integer")
                # Validate correctness
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed for input '{case['s']}'"
                )


if __name__ == "__main__":
    unittest.main()
