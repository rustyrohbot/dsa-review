# 242. Valid Anagram
#
# Description:
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters
# exactly once.
#
# Constraints:
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
# Follow up: What if the inputs contain Unicode characters? How would you
# adapt your solution? (For this template, we'll stick to lowercase English letters)


def isAnagram(s: str, t: str) -> bool:
    """
    Determines if string t is an anagram of string s.
    """
    # TODO: Implement the solution here
    pass


if __name__ == "__main__":
    test_cases = [
        {
            "input": {"s": "anagram", "t": "nagaram"},
            "expected": True,
            "id": "Example 1",
        },
        {
            "input": {"s": "rat", "t": "car"},
            "expected": False,
            "id": "Example 2",
        },
        {
            "input": {"s": "listen", "t": "silent"},
            "expected": True,
            "id": "Simple anagram",
        },
        {
            "input": {"s": "hello", "t": "world"},
            "expected": False,
            "id": "Different words",
        },
        {
            "input": {"s": "aabb", "t": "bbaa"},
            "expected": True,
            "id": "Repeated characters",
        },
        {
            "input": {"s": "aabbc", "t": "aabbd"},
            "expected": False,
            "id": "Different characters",
        },
        {
            "input": {"s": "a", "t": "ab"},
            "expected": False,
            "id": "Different lengths (t longer)",
        },
        {
            "input": {"s": "ab", "t": "a"},
            "expected": False,
            "id": "Different lengths (s longer)",
        },
        {
            "input": {"s": "", "t": ""}, # Problem constraint s.length >= 1
            "expected": True,            # but if allowed, empty strings are anagrams
            "id": "Empty strings (if allowed by constraints)",
        },
         {
            "input": {"s": "a", "t": "a"},
            "expected": True,
            "id": "Single character match",
        },
        {
            "input": {"s": "z", "t": "y"},
            "expected": False,
            "id": "Single character mismatch",
        },
        {
            "input": {"s": "qwerty", "t": "ytrewq"},
            "expected": True,
            "id": "Longer anagram",
        },
        {
            "input": {"s": "qwertyuiop", "t": "poiuytrewq"},
            "expected": True,
            "id": "Very long anagram",
        },
        {
            "input": {"s": "badcredit", "t": "debitcard"},
            "expected": True,
            "id": "Phrase like anagram",
        }
    ]
    # Adjusting for constraints: 1 <= s.length, t.length
    test_cases = [tc for tc in test_cases if tc["id"] != "Empty strings (if allowed by constraints)"]
    # If the problem setter guarantees s and t consist of lowercase English letters,
    # we don't need to test for other character types unless doing the follow-up.

    passed_all = True
    for i, case in enumerate(test_cases):
        s_input = case["input"]["s"]
        t_input = case["input"]["t"]
        expected_output = case["expected"]
        case_id = case["id"]

        try:
            actual_output = isAnagram(s_input, t_input)
            if actual_output == expected_output:
                print(f"Test Case {i + 1} ({case_id}): PASSED")
            else:
                print(f"Test Case {i + 1} ({case_id}): FAILED")
                print(f"  Input s:  '{s_input}'")
                print(f"  Input t:  '{t_input}'")
                print(f"  Expected: {expected_output}")
                print(f"  Actual:   {actual_output}")
                passed_all = False
        except Exception as e:
            print(f"Test Case {i + 1} ({case_id}): ERROR")
            print(f"  Input s:  '{s_input}'")
            print(f"  Input t:  '{t_input}'")
            print(f"  Exception: {e}")
            passed_all = False
        print("-" * 40)

    if passed_all:
        print("All test cases passed!")
    else:
        print("Some test cases failed.")
