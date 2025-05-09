# 224. Basic Calculator
#
# Description:
# Given a string s representing a valid expression, implement a basic
# calculator to evaluate it, and return the result of the evaluation.
#
# Note: You are not allowed to use any built-in function which evaluates
# strings as mathematical expressions, such as eval().
#
# Constraints:
# 1 <= s.length <= 3 * 10^5
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operator (e.g., "+1" and "+(2 + 3)" is invalid).
# '-' can be used as a unary operator (e.g., "-1" and "-(2 + 3)" is valid).
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.


def calculate_basic_i(s: str) -> int: # Renamed to avoid conflict if you have both
    """
    Evaluates a string expression with +, -, (, ), and non-negative integers.
    """
    # TODO: Implement the solution here
    pass


if __name__ == "__main__":
    test_cases = [
        {
            "input": "1 + 1",
            "expected": 2,
            "id": "Example 1",
        },
        {
            "input": " 2-1 + 2 ",
            "expected": 3,
            "id": "Example 2",
        },
        {
            "input": "(1+(4+5+2)-3)+(6+8)",
            # (1 + 11 - 3) + 14
            # (12 - 3) + 14
            # 9 + 14 = 23
            "expected": 23,
            "id": "Example 3 (with parentheses)",
        },
        {
            "input": "0",
            "expected": 0,
            "id": "Single zero",
        },
        {
            "input": "42",
            "expected": 42,
            "id": "Single number",
        },
        {
            "input": "(5)",
            "expected": 5,
            "id": "Number in parentheses",
        },
        {
            "input": " ( 3 ) ",
            "expected": 3,
            "id": "Number in parentheses with spaces",
        },
        {
            "input": "1-(     -2)", # 1 - (-2) = 1 + 2 = 3
            "expected": 3,
            "id": "Subtraction of negative in parens (unary minus inside)",
        },
        {
            "input": "- (3 + (4 - 5))", # -(3 + (-1)) = -(3-1) = -2
            "expected": -2,
            "id": "Unary minus outside complex parentheses",
        },
        {
            "input": "2147483647", # Max int
            "expected": 2147483647,
            "id": "Max integer",
        },
        {
            "input": "-2+3", # This case might be tricky based on "'+' is not used as a unary operator"
                           # but '-' can be. If s starts with '-', it's unary.
                           # The problem implies "1 + -2" is invalid, but "-2 + 1" is fine.
            "expected": 1,
            "id": "Starts with unary minus",
        },
        {
            "input": "1-12+(1-3)", # 1-12 + (-2) = -11 - 2 = -13
            "expected": -13,
            "id": "Mixed operations",
        },
        {
            "input": "(7)-(0)+(4)", # 7 - 0 + 4 = 11
            "expected": 11,
            "id": "Parentheses around numbers",
        },
        {
            "input": " (1-(4+5-2)) + (6+8) - ((1+2)-3) ",
            # (1 - (11-2)) + 14 - (3-3)
            # (1 - 9) + 14 - 0
            # -8 + 14 = 6
            "expected": 6,
            "id": "Complex nested with spaces",
        },
        {
            "input": "-( -1 + ( -2 - 3) + 5)", # -( -1 + (-5) + 5) = -(-1 -5 + 5) = -(-1) = 1
            "expected": 1,
            "id": "Multiple unary minuses nested"
        }
    ]

    passed_all = True
    for i, case in enumerate(test_cases):
        s_input = case["input"]
        expected_output = case["expected"]
        case_id = case["id"]

        try:
            # Using the renamed function here
            actual_output = calculate_basic_i(s_input)
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

