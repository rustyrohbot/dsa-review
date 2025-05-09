# 1. Two Sum
#
# Description:
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# You can return the answer in any order.
#
# Constraints:
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Finds two numbers in the list that add up to the target.
    Returns their indices.
    """
    # TODO: Implement the solution here
    pass


if __name__ == "__main__":
    test_cases = [
        {
            "input": {"nums": [2, 7, 11, 15], "target": 9},
            "expected": [0, 1],
            "id": "Example 1",
        },
        {
            "input": {"nums": [3, 2, 4], "target": 6},
            "expected": [1, 2],
            "id": "Example 2",
        },
        {
            "input": {"nums": [3, 3], "target": 6},
            "expected": [0, 1],
            "id": "Example 3",
        },
        {
            "input": {"nums": [0, 4, 3, 0], "target": 0},
            "expected": [0, 3],
            "id": "Zeros",
        },
        {
            "input": {"nums": [-1, -3, 5, 7], "target": 4},
            "expected": [0, 2],
            "id": "Negative numbers",
        },
        {
            "input": {"nums": [1, 2, 3, 4, 5], "target": 10},
            "expected": None,  # Or handle as per problem if no solution (though problem states one exists)
            # For this problem, it's guaranteed one solution exists.
            # If we were to test for no solution, we'd adjust.
            # Let's assume the problem setter guarantees a solution.
            # For a case where we might expect a specific pair:
            # "expected": [?, ?] # if we knew the specific pair for a target of 10
            # For now, let's stick to cases with guaranteed solutions as per problem statement.
            "id": "No solution (if allowed, but problem guarantees one)",
        }, # Removing this test case as problem guarantees a solution
        {
            "input": {"nums": [100, 200, 300, 400], "target": 700},
            "expected": [2, 3],
            "id": "Larger numbers",
        },
        {
            "input": {"nums": [5, 75, 25], "target": 100},
            "expected": [1, 2],
            "id": "Unsorted input",
        },
    ]

    passed_all = True
    for i, case in enumerate(test_cases):
        nums_input = case["input"]["nums"]
        target_input = case["input"]["target"]
        expected_output = case["expected"]
        case_id = case["id"]

        # For "Two Sum", the order of indices in the output doesn't matter.
        # So, we sort both the actual and expected output before comparison.
        # However, the problem statement says "You can return the answer in any order."
        # A robust test would check if the elements at the returned indices sum to the target.
        # And that the indices are different.

        try:
            actual_output = twoSum(list(nums_input), target_input) # Pass a copy of nums

            if actual_output is None and expected_output is None:
                 print(f"Test Case {i + 1} ({case_id}): PASSED (No solution expected and none found)")
            elif actual_output is None:
                print(f"Test Case {i + 1} ({case_id}): FAILED")
                print(f"  Input:    nums={nums_input}, target={target_input}")
                print(f"  Expected: {expected_output}")
                print(f"  Actual:   {actual_output}")
                passed_all = False
            elif len(actual_output) == 2 and \
                 actual_output[0] != actual_output[1] and \
                 0 <= actual_output[0] < len(nums_input) and \
                 0 <= actual_output[1] < len(nums_input) and \
                 nums_input[actual_output[0]] + nums_input[actual_output[1]] == target_input:
                # To make comparison easier if expected is sorted, we can sort actual_output
                # Or, check if set(actual_output) == set(expected_output)
                # For this problem, since there's exactly one solution,
                # we can check if the numbers at the indices sum to target.
                # And that the indices are valid and distinct.
                # The `expected` array is just one valid pair.
                # A more flexible check:
                val1 = nums_input[actual_output[0]]
                val2 = nums_input[actual_output[1]]
                if val1 + val2 == target_input:
                     print(f"Test Case {i + 1} ({case_id}): PASSED")
                else:
                    print(f"Test Case {i + 1} ({case_id}): FAILED (Incorrect sum)")
                    print(f"  Input:    nums={nums_input}, target={target_input}")
                    print(f"  Indices:  {actual_output} -> values {val1}, {val2} -> sum {val1+val2}")
                    print(f"  Expected sum: {target_input}")
                    passed_all = False

            else:
                print(f"Test Case {i + 1} ({case_id}): FAILED (Invalid output format or indices)")
                print(f"  Input:    nums={nums_input}, target={target_input}")
                print(f"  Expected format: list of 2 distinct valid indices")
                print(f"  Actual:   {actual_output}")
                passed_all = False

        except Exception as e:
            print(f"Test Case {i + 1} ({case_id}): ERROR")
            print(f"  Input:    nums={nums_input}, target={target_input}")
            print(f"  Exception: {e}")
            passed_all = False
        print("-" * 40)

    if passed_all:
        print("All test cases passed!")
    else:
        print("Some test cases failed.")
