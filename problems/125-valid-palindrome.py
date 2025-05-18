# 125. Valid Palindrome
#
# Description:
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Constraints:
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
#
# Examples:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

import unittest
import string

def is_palindrome(s: str) -> bool:
    """
    Returns True if s is a palindrome ignoring non-alphanumeric chars and case, else False.
    """
    punctuation = [' ', '.', ',', ':', '!', '?']
    left, right = 0, len(s) -1 # initialize two points
    while left < right:
        if s[left] in punctuation: # increment left pointer if the character is a punctation or a space
            left += 1
            continue
        if s[right] in punctuation: # decrement right pointer if the chater is punctuation or a space
            right -= 1
            continue

        if s[left].lower() != s[right].lower(): # returns false if the right and left values don't match
            return False
        left += 1
        right -= 1
    return True # while loop exists without returning false so return true

class TestValidPalindrome(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"s": "", "expected": True, "id": "Empty string"},
            {"s": "A man, a plan, a canal: Panama", "expected": True, "id": "Mixed case and punctuation"},
            {"s": "race a car", "expected": False, "id": "Not palindrome"},
            {"s": ".,", "expected": True, "id": "Only punctuation"},
            {"s": "0P", "expected": False, "id": "Alphanumeric mixed"},
            {"s": "a", "expected": True, "id": "Single character"},
        ]

    def test_is_palindrome(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = is_palindrome(case["s"])
                self.assertIsInstance(result, bool, "Result should be a boolean")
                self.assertEqual(result, case["expected"], f"Mismatch for case '{case['id']}'")

if __name__ == "__main__":
    unittest.main()