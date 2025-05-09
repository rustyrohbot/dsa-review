# 227. Basic Calculator II
#
# Description:
# Given a string s which represents an expression, evaluate this expression
# and return its value.
#
# The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid. All intermediate
# results will be in the range of [-2^31, 2^31 - 1].
#
# Note: You are not allowed to use any built-in function which evaluates
# strings as mathematical expressions, such as eval().
#
# Constraints:
# 1 <= s.length <= 3 * 10^5
# s consists of integers and operators ('+', '-', '*', '/') separated by
#   one or more spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range
#   [0, 2^31 - 1].
# The answer is guaranteed to fit in a 32-bit integer.


def calculate(s: str) -> int:
    """
    Evaluates a string expression with +, -, *, / operators.
    """
    # TODO: Implement the solution here
    pass


if __name__ == "__main__":
    test_cases = [
        {
            "input": "3+2*2",
            "expected": 7, # 3 + (2*2) = 3 + 4 = 7
            "id": "Example 1 (Multiply then Add)",
        },
        {
            "input": " 3/2 ",
            "expected": 1, # Integer division truncates
            "id": "Example 2 (Division)",
        },
        {
            "input": " 3+5 / 2 ",
            "expected": 5, # 3 + (5/2) = 3 + 2 = 5
            "id": "Example 3 (Add then Divide)",
        },
        {
            "input": "42",
            "expected": 42,
            "id": "Single number",
        },
        {
            "input": "1*2-3/4+5*6-7*8+9/10",
            # 1*2 = 2
            # 3/4 = 0
            # 5*6 = 30
            # 7*8 = 56
            # 9/10 = 0
            # Expression: 2 - 0 + 30 - 56 + 0
            #           : 2 + 30 - 56
            #           : 32 - 56 = -24
            "expected": -24,
            "id": "Complex expression",
        },
        {
            "input": "1+1+1",
            "expected": 3,
            "id": "Multiple additions",
        },
        {
            "input": "10 - 2 * 3", # 10 - 6
            "expected": 4,
            "id": "Subtraction after multiplication",
        },
        {
            "input": "0-2147483647", # Max int
            "expected": -2147483647,
            "id": "Subtraction leading to negative",
        },
        {
            "input": "1*2*3*4*5",
            "expected": 120,
            "id": "Multiple multiplications",
        },
        {
            "input": "100/10/2", # (100/10)/2 = 10/2 = 5
            "expected": 5,
            "id": "Multiple divisions",
        },
        {
            "input": "1 + 1", # With spaces
            "expected": 2,
            "id": "Spaces around operator",
        },
        {
            "input": "   1   + 2  ",
            "expected": 3,
            "id": "More spaces",
        },
        {
            "input": "14 / 3 * 2", # (14/3)*2 = 4*2 = 8
            "expected": 8,
            "id": "Division then multiplication"
        }
    ]

    passed_all = True
    for i, case in enumerate(test_cases):
        s_input = case["input"]
        expected_output = case["expected"]
        case_id = case["id"]

        try:
            actual_output = calculate(s_input)
            if actual_output == expected_output:
                print(f"Test Case {i + 1} ({case_id}): PASSED")
            else:
                print(f"Test Case {i + 1} ({case_id}): FAILED")
                print(f"  Input:    '{s_input}'")
                print(f"  Expected: {expected_output}")
                print(f"  Actual:   {actual_output}")
                passed_all = False
        except Exception as e:
            print(f"Test Case {i + 1} ({case_id}): ERROR")
            print(f"  Input:    '{s_input}'")
            print(f"  Exception: {e}")
            import traceback
            traceback.print_exc()
            passed_all = False
        print("-" * 40)

    if passed_all:
        print("All test cases passed!")
    else:
        print("Some test cases failed.")

