# 167. Two Sum II - Input Array Is Sorted
#
# Description:
# Given a 1-indexed array of integers numbers that is already sorted in
# non-decreasing order, find two numbers such that they add up to a specific
# target number. Let these two numbers be numbers[index1] and numbers[index2]
# where 1 <= index1 < index2 <= numbers.length.
#
# Return the indices of the two numbers, index1 and index2, added by one as an
# integer array [index1, index2] of length 2.
#
# The tests are generated such that there is exactly one solution. You may not
# use the same element twice.
#
# Your solution must use only constant extra space.
#
# Constraints:
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.

from typing import List


def twoSumII(numbers: List[int], target: int) -> List[int]:
    """
    Finds two numbers in the sorted list that add up to the target.
    Returns their 1-based indices.
    """
    # TODO: Implement the solution here
    pass


if __name__ == "__main__":
    test_cases = [
        {
            "input": {"numbers": [2, 7, 11, 15], "target": 9},
            "expected": [1, 2],
            "id": "Example 1",
        },
        {
            "input": {"numbers": [2, 3, 4], "target": 6},
            "expected": [1, 3],
            "id": "Example 2",
        },
        {
            "input": {"numbers": [-1, 0], "target": -1},
            "expected": [1, 2],
            "id": "Example 3",
        },
        {
            "input": {"numbers": [5, 25, 75], "target": 100},
            "expected": [2, 3],
            "id": "Simple case",
        },
        {
            "input": {"numbers": [0, 0, 3, 4], "target": 0},
            "expected": [1, 2],
            "id": "Zeros at beginning",
        },
        {
            "input": {"numbers": [-3, -1, 0, 2, 5], "target": -1},
            "expected": [1, 3], # -3 + 2 = -1 (indices 1, 4) OR -1 + 0 = -1 (indices 2,3)
                                # Problem states exactly one solution.
                                # Let's recheck example: [-1, 0], target -1 -> [1,2]
                                # For [-3, -1, 0, 2, 5], target -1:
                                # -3 + 2 = -1 (indices 1, 4)
                                # -1 + 0 = -1 (indices 2, 3)
                                # The problem statement says "exactly one solution".
                                # This implies my test case might be flawed if it has multiple.
                                # Let's assume the LeetCode test generator ensures this.
                                # If target is -1, and numbers are [-3, -1, 0, 2, 5]
                                # -3 + x = -1 => x = 2 (index 4) -> [1,4]
                                # -1 + x = -1 => x = 0 (index 3) -> [2,3]
                                # This test case seems to have two solutions.
                                # Let's pick one that is unambiguous or trust LC's generator.
                                # For now, I'll assume one of these is the "intended" one by LC.
                                # Let's use a target that has a clear single solution.
            "id": "Negative numbers",
        },
        {
            "input": {"numbers": [-5, -3, -1, 0, 2, 4], "target": -1}, # -5+4, -3+2, -1+0
            "expected": [3,6], # -1 + 2 = 1. No. -1 + 0 = -1. Indices 3, 4
                               # -3 + 2 = -1. Indices 2, 5
                               # -5 + 4 = -1. Indices 1, 6
                               # This is tricky for test case generation if not careful.
                               # Let's use a simpler one.
            "id": "Negative numbers v2",
        },
        {
            "input": {"numbers": [1,2,3,4,4,9,56,90], "target": 8},
            "expected": [4,5], # numbers[3] + numbers[4] (0-indexed) -> 4+4=8
                               # 1-indexed: 4, 5
            "id": "Duplicates in array, target uses them",
        },
         {
            "input": {"numbers": [-10, -5, 0, 5, 10], "target": 0},
            "expected": [1, 5], # -10 + 10 = 0
            "id": "Symmetric negatives and positives",
        },
        {
            "input": {"numbers": [1,2,7,11,15], "target": 9},
            "expected": [2,3], # 2+7 = 9 (0-indexed: 1,2 -> 1-indexed: 2,3)
            "id": "Standard case",
        }
    ]
    # Clean up ambiguous test cases
    test_cases = [tc for tc in test_cases if tc["id"] not in ["Negative numbers", "Negative numbers v2"]]
    test_cases.append(
        {
            "input": {"numbers": [-3, 0, 1, 2, 5], "target": -1},
            "expected": [1, 4], # -3 + 2 = -1
            "id": "Negative numbers unambiguous",
        }
    )


    passed_all = True
    for i, case in enumerate(test_cases):
        numbers_input = case["input"]["numbers"]
        target_input = case["input"]["target"]
        expected_output = case["expected"] # Expected is 1-based
        case_id = case["id"]

        try:
            actual_output = twoSumII(list(numbers_input), target_input) # Pass a copy

            if actual_output is None and expected_output is None:
                 print(f"Test Case {i + 1} ({case_id}): PASSED (No solution expected and none found)")
            elif actual_output is None:
                print(f"Test Case {i + 1} ({case_id}): FAILED")
                print(f"  Input:    numbers={numbers_input}, target={target_input}")
                print(f"  Expected: {expected_output} (1-based)")
                print(f"  Actual:   {actual_output}")
                passed_all = False
            elif len(actual_output) == 2 and \
                 1 <= actual_output[0] < actual_output[1] <= len(numbers_input) and \
                 numbers_input[actual_output[0]-1] + numbers_input[actual_output[1]-1] == target_input:
                # Output is 1-based, so access numbers_input with index-1
                # Check if actual_output matches expected_output (both should be sorted as per problem)
                if sorted(actual_output) == sorted(expected_output):
                    print(f"Test Case {i + 1} ({case_id}): PASSED")
                else:
                    # This branch might occur if my expected_output is one of multiple valid ones,
                    # but the problem guarantees only one. So, if the sum is correct and indices are valid,
                    # it should be fine. The primary check is the sum and valid 1-based indices.
                    print(f"Test Case {i + 1} ({case_id}): FAILED (Output mismatch, but sum might be correct)")
                    print(f"  Input:    numbers={numbers_input}, target={target_input}")
                    print(f"  Expected: {expected_output} (1-based)")
                    print(f"  Actual:   {actual_output} (1-based)")
                    print(f"  Values at actual indices: {numbers_input[actual_output[0]-1]}, {numbers_input[actual_output[1]-1]}")
                    passed_all = False

            else:
                print(f"Test Case {i + 1} ({case_id}): FAILED (Invalid output format or indices)")
                print(f"  Input:    numbers={numbers_input}, target={target_input}")
                print(f"  Expected: List of 2 1-based indices [idx1, idx2] where idx1 < idx2.")
                print(f"  Actual:   {actual_output}")
                if actual_output and len(actual_output) == 2:
                    if not (1 <= actual_output[0] < len(numbers_input) +1):
                        print(f"    Actual index1 ({actual_output[0]}) out of 1-based bounds.")
                    if not (1 <= actual_output[1] < len(numbers_input) +1):
                        print(f"    Actual index2 ({actual_output[1]}) out of 1-based bounds.")
                    if actual_output[0] >= actual_output[1]:
                        print(f"    Actual index1 ({actual_output[0]}) not less than index2 ({actual_output[1]}).")
                    if 1 <= actual_output[0] < actual_output[1] <= len(numbers_input):
                         val1 = numbers_input[actual_output[0]-1]
                         val2 = numbers_input[actual_output[1]-1]
                         if val1 + val2 != target_input:
                            print(f"    Sum of values at actual indices ({val1} + {val2} = {val1+val2}) does not match target ({target_input}).")

                passed_all = False

        except Exception as e:
            print(f"Test Case {i + 1} ({case_id}): ERROR")
            print(f"  Input:    numbers={numbers_input}, target={target_input}")
            print(f"  Exception: {e}")
            passed_all = False
        print("-" * 40)

    if passed_all:
        print("All test cases passed!")
    else:
        print("Some test cases failed.")

