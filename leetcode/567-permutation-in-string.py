# 567. Permutation in String
#
# Description:
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.
#
# Constraints:
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.


def checkInclusion(s1: str, s2: str) -> bool:
    """
    Determines if s2 contains a permutation of s1 as a substring.
    s1 is the pattern, s2 is the text to search within.
    """
    # TODO: Implement the solution here
    pass


if __name__ == "__main__":
    test_cases = [
        {
            "input": {"s1": "ab", "s2": "eidbaooo"},
            "expected": True,
            "id": "Example 1 (ba is in s2)",
        },
        {
            "input": {"s1": "ab", "s2": "eidboaoo"},
            "expected": False,
            "id": "Example 2 (no permutation of ab in s2)",
        },
        {
            "input": {"s1": "a", "s2": "b"},
            "expected": False,
            "id": "Single char, no match",
        },
        {
            "input": {"s1": "a", "s2": "a"},
            "expected": True,
            "id": "Single char, match",
        },
        {
            "input": {"s1": "abc", "s2": "bbbca"},
            "expected": True,
            "id": "Permutation at end (bca)",
        },
        {
            "input": {"s1": "adc", "s2": "dcda"},
            "expected": True,
            "id": "Permutation 'dca' or 'acd' (cda is in s2)",
        },
        {
            "input": {"s1": "hello", "s2": "ooolleoooleh"},
            "expected": True,
            "id": "Longer strings, permutation 'lloeh' or 'olelh'",
        },
        {
            "input": {"s1": "aabb", "s2": "bbbaaacccbbaa"},
            "expected": True,
            "id": "Pattern with duplicates, found",
        },
        {
            "input": {"s1": "aabbc", "s2": "abbacab"},
            "expected": True, # "abbac" is a permutation of "aabbc"
            "id": "Pattern with duplicates, complex find",
        },
        {
            "input": {"s1": "aabb", "s2": "ab"},
            "expected": False,
            "id": "s1 longer than s2",
        },
        {
            "input": {"s1": "trinitrophenylmethylnitramine", "s2": "dinitrophenylhydrazinetrinitrophenylmethylnitramine"},
            "expected": True,
            "id": "Very long strings, s1 is substring of s2",
        },
        {
            "input": {"s1": "abacaba", "s2": "zzzaaacabbb"}, # "aacab" is not a perm of "abacaba"
            "expected": False,
            "id": "No permutation found",
        },
         {
            "input": {"s1": "x", "s2": "abcdefghijklmnopqrstuvwxyz"},
            "expected": True,
            "id": "Single char pattern in long string",
        },
        {
            "input": {"s1": "q", "s2": "abcdefghijklmnoprstuvwxyz"}, # missing q
            "expected": False,
            "id": "Single char pattern not in long string",
        }
    ]

    passed_all = True
    for i, case in enumerate(test_cases):
        s1_input = case["input"]["s1"]
        s2_input = case["input"]["s2"]
        expected_output = case["expected"]
        case_id = case["id"]

        try:
            actual_output = checkInclusion(s1_input, s2_input)
            if actual_output == expected_output:
                print(f"Test Case {i + 1} ({case_id}): PASSED")
            else:
                print(f"Test Case {i + 1} ({case_id}): FAILED")
                print(f"  Input s1: '{s1_input}'")
                print(f"  Input s2: '{s2_input}'")
                print(f"  Expected: {expected_output}")
                print(f"  Actual:   {actual_output}")
                passed_all = False
        except Exception as e:
            print(f"Test Case {i + 1} ({case_id}): ERROR")
            print(f"  Input s1: '{s1_input}'")
            print(f"  Input s2: '{s2_input}'")
            print(f"  Exception: {e}")
            passed_all = False
        print("-" * 40)

    if passed_all:
        print("All test cases passed!")
    else:
        print("Some test cases failed.")

