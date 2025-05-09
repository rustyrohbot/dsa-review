# 238. Product of Array Except Self
#
# Description:
# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a
# 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the
# division operation.
#
# Constraints:
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
# Follow up: Can you solve the problem in O(1) extra space complexity?
# (The output array does not count as extra space for space complexity analysis.)

from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Calculates the product of all elements of nums except nums[i] for each i.
    """
    # TODO: Implement the solution here
    pass


if __name__ == "__main__":
    test_cases = [
        {
            "input": [1, 2, 3, 4],
            "expected": [24, 12, 8, 6], # [2*3*4, 1*3*4, 1*2*4, 1*2*3]
            "id": "Example 1",
        },
        {
            "input": [-1, 1, 0, -3, 3],
            # For 0: -1 * 1 * -3 * 3 = 9
            # For others: 0
            "expected": [0, 0, 9, 0, 0],
            "id": "Example 2 (with zero)",
        },
        {
            "input": [1, 2, 0, 4, 0],
            # Two zeros, so all products will be 0
            "expected": [0, 0, 0, 0, 0],
            "id": "Multiple zeros",
        },
        {
            "input": [1, -1, 2, -2],
            # [-1*2*-2, 1*2*-2, 1*-1*-2, 1*-1*2]
            # [4, -4, 2, -2]
            "expected": [4, -4, 2, -2],
            "id": "With negative numbers",
        },
        {
            "input": [0, 0],
            "expected": [0, 0],
            "id": "Two zeros only",
        },
        {
            "input": [5, 2],
            "expected": [2, 5],
            "id": "Length 2",
        },
        {
            "input": [1, 1, 1, 1],
            "expected": [1, 1, 1, 1],
            "id": "All ones",
        },
        {
            "input": [10, 3, 5, 6, 2],
            # [3*5*6*2, 10*5*6*2, 10*3*6*2, 10*3*5*2, 10*3*5*6]
            # [180, 600, 360, 300, 900]
            "expected": [180, 600, 360, 300, 900],
            "id": "Slightly larger numbers",
        },
        {
            "input": [0, 4, 0],
            "expected": [0,0,0],
            "id": "Zero at ends, one in middle"
        }
    ]

    passed_all = True
    for i, case in enumerate(test_cases):
        nums_input = case["input"]
        expected_output = case["expected"]
        case_id = case["id"]

        try:
            actual_output = productExceptSelf(list(nums_input)) # Pass a copy

            if actual_output == expected_output:
                print(f"Test Case {i + 1} ({case_id}): PASSED")
            else:
                print(f"Test Case {i + 1} ({case_id}): FAILED")
                print(f"  Input:    {nums_input}")
                print(f"  Expected: {expected_output}")
                print(f"  Actual:   {actual_output}")
                passed_all = False
        except Exception as e:
            print(f"Test Case {i + 1} ({case_id}): ERROR")
            print(f"  Input:    {nums_input}")
            print(f"  Exception: {e}")
            import traceback
            traceback.print_exc()
            passed_all = False
        print("-" * 40)

    if passed_all:
        print("All test cases passed!")
    else:
        print("Some test cases failed.")

