# 15. 3Sum
#
# Description:
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
# Constraints:
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Finds all unique triplets in the array which give the sum of zero.
    """
    # TODO: Implement the solution here
    pass


def compare_list_of_lists(list1: List[List[int]], list2: List[List[int]]) -> bool:
    """
    Compares two lists of lists, where the order of inner lists and
    the order of elements within inner lists do not matter.
    """
    if len(list1) != len(list2):
        return False

    set1 = set(tuple(sorted(sublist)) for sublist in list1)
    set2 = set(tuple(sorted(sublist)) for sublist in list2)

    return set1 == set2


if __name__ == "__main__":
    test_cases = [
        {
            "input": [-1, 0, 1, 2, -1, -4],
            "expected": [[-1, -1, 2], [-1, 0, 1]],
            "id": "Example 1",
        },
        {
            "input": [0, 1, 1],
            "expected": [],
            "id": "Example 2 (No solution)",
        },
        {
            "input": [0, 0, 0],
            "expected": [[0, 0, 0]],
            "id": "Example 3 (All zeros)",
        },
        {
            "input": [0, 0, 0, 0],
            "expected": [[0, 0, 0]],
            "id": "Multiple zeros",
        },
        {
            "input": [-2, 0, 1, 1, 2],
            "expected": [[-2, 0, 2], [-2, 1, 1]],
            "id": "Duplicates in input, distinct triplets",
        },
        {
            "input": [1, 2, -2, -1],
            "expected": [], # No triplet sums to 0
            "id": "No zero sum",
        },
        {
            "input": [-1,0,1],
            "expected": [[-1,0,1]],
            "id": "Single triplet exact match"
        },
        {
            "input": [3,0,-2,-1,1,2],
            # Possible:
            # 3, -2, -1
            # 0, -2, 2
            # 0, -1, 1
            # -2, -1, 3 (same as first)
            "expected": [[-2,-1,3],[-2,0,2],[-1,0,1]],
            "id": "Mixed numbers"
        },
        {
            "input": [1, -1, -1, 0],
            "expected": [[-1, 0, 1]],
            "id": "Another simple case"
        }
    ]

    passed_all = True
    for i, case in enumerate(test_cases):
        nums_input = case["input"]
        expected_output = case["expected"]
        case_id = case["id"]

        try:
            actual_output = threeSum(list(nums_input)) # Pass a copy

            if actual_output is None: # Solution should return a list
                print(f"Test Case {i + 1} ({case_id}): FAILED")
                print(f"  Input:    {nums_input}")
                print(f"  Expected: {expected_output}")
                print(f"  Actual:   None (Function should return a list)")
                passed_all = False
                print("-" * 40)
                continue

            # Validate structure of actual_output before comparison
            valid_structure = True
            if not isinstance(actual_output, list):
                valid_structure = False
            else:
                for triplet in actual_output:
                    if not (isinstance(triplet, list) and len(triplet) == 3 and \
                            all(isinstance(num, int) for num in triplet)):
                        valid_structure = False
                        break
                    # Optional: Check if sum is 0 for each triplet (good for debugging user's code)
                    if sum(triplet) != 0:
                        print(f"Test Case {i + 1} ({case_id}): WARNING - Triplet {triplet} in actual output does not sum to 0.")


            if not valid_structure:
                print(f"Test Case {i + 1} ({case_id}): FAILED (Invalid output structure)")
                print(f"  Input:    {nums_input}")
                print(f"  Expected format: List of lists, e.g., [[a,b,c], [d,e,f]]")
                print(f"  Actual:   {actual_output}")
                passed_all = False
            elif compare_list_of_lists(actual_output, expected_output):
                print(f"Test Case {i + 1} ({case_id}): PASSED")
            else:
                print(f"Test Case {i + 1} ({case_id}): FAILED")
                print(f"  Input:    {nums_input}")
                # To help debug, show sorted versions for easier comparison by eye
                processed_expected = sorted([tuple(sorted(t)) for t in expected_output])
                processed_actual = sorted([tuple(sorted(t)) for t in actual_output])
                print(f"  Expected (processed): {processed_expected}")
                print(f"  Actual (processed):   {processed_actual}")
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

