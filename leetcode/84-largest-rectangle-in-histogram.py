# 84. Largest Rectangle in Histogram
#
# Description:
# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle
# in the histogram.
#
# Constraints:
# 1 <= heights.length <= 10^5
# 0 <= heights[i] <= 10^4


from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    """
    Calculates the area of the largest rectangle in the histogram.
    """
    # TODO: Implement the solution here
    pass


if __name__ == "__main__":
    test_cases = [
        {
            "input": [2, 1, 5, 6, 2, 3],
            "expected": 10,  # Achieved by height 5, width 2 (5*2) or height 2, width 5 (2*?)
            # For [2,1,5,6,2,3]:
            # h=2, w=1 -> 2
            # h=1, w=6 -> 6 (1*6)
            # h=5, w=1 -> 5
            # h=6, w=1 -> 6
            # h=2, w=1 -> 2
            # h=3, w=1 -> 3
            #
            # With 5: can extend to 6. Area = 5 * 2 = 10
            # With 6: cannot extend. Area = 6 * 1 = 6
            # With 1: can extend across all. Area = 1 * 6 = 6
            # With 2 (first): can extend to 1. Area = 1 * 6 = 6. Or 2*1=2
            # With 2 (second): can extend to 3. Area = 2 * 2 = 4.
            # The rectangle of height 5 can span indices 2 and 3 (5,6). Min height is 5, width is 2. Area 10.
            # The rectangle of height 6 is just index 3. Min height is 6, width is 1. Area 6.
            # The rectangle of height 2 (at index 0) can span index 0. Area 2.
            # The rectangle of height 1 (at index 1) can span indices 0-5. Area 1*6=6.
            # The rectangle of height 2 (at index 4) can span indices 4-5 (heights 2,3). Min height 2, width 2. Area 4.
            # Or can span indices 0-4 (heights 2,1,5,6,2). Min height 1, width 5. Area 5.
            # The largest is indeed 10 (using bars 5 and 6, the effective height is 5, width is 2).
            "id": "Example 1",
        },
        {
            "input": [2, 4],
            "expected": 4, # max(2*2, 4*1) = max(4,4) = 4
            "id": "Example 2",
        },
        {
            "input": [1],
            "expected": 1,
            "id": "Single bar",
        },
        {
            "input": [0, 0, 0],
            "expected": 0,
            "id": "All zeros",
        },
        {
            "input": [1, 2, 3, 4, 5],
            # h=1, w=5 -> 5
            # h=2, w=2 -> 4 (from index 1, [2,3,4,5] -> min height 2, width 4 -> 8)
            # h=3, w=3 -> 9 (from index 2, [3,4,5] -> min height 3, width 3 -> 9)
            # h=4, w=2 -> 8
            # h=5, w=1 -> 5
            # Max is 9.
            "expected": 9,
            "id": "Increasing heights",
        },
        {
            "input": [5, 4, 3, 2, 1],
            # h=5, w=1 -> 5
            # h=4, w=2 -> 8
            # h=3, w=3 -> 9
            # h=2, w=4 -> 8
            # h=1, w=5 -> 5
            # Max is 9.
            "expected": 9,
            "id": "Decreasing heights",
        },
        {
            "input": [2, 1, 2],
            # h=2 (idx 0), w=1 -> 2
            # h=1 (idx 1), w=3 -> 3
            # h=2 (idx 2), w=1 -> 2
            # Max is 3.
            "expected": 3,
            "id": "Valley shape",
        },
        {
            "input": [4, 2, 0, 3, 2, 5],
            # h=4, w=1 -> 4
            # h=2, w=2 -> 4 (4,2)
            # h=0 -> 0
            # h=3, w=1 -> 3
            # h=2, w=2 -> 4 (3,2) or w=3 (0,3,2) -> min 0. (3,2,5) -> min 2, w=3 -> 6
            # h=5, w=1 -> 5
            # Consider bar 3: can go left to 0 (width 1). Can go right to 2,5 (width 3, height 2).
            # For height 2 (index 1): can go left to 4 (width 2, height 2). Area 4.
            # For height 3 (index 3): can go right to 2,5 (width 3, height 2). Area 6.
            # For height 2 (index 4): can go left to 3 (width 2, height 2). Area 4. Can go left to 0,3 (width 3, height 2). Area 6.
            # For height 5 (index 5): width 1, height 5. Area 5.
            # The rectangle with height 2 starting at index 3 and ending at index 5 (heights [3,2,5]) has min height 2 and width 3. Area = 6.
            "expected": 6,
            "id": "Complex case with zero",
        },
        {
            "input": [1,1,1,1,1],
            "expected": 5,
            "id": "All same height"
        },
        {
            "input": [6, 2, 5, 4, 5, 1, 6],
            # For bar 4 (index 3):
            #   Can extend left to 5,2,6. Min height 4. Width 3 (indices 2,3,4). Area 4*3 = 12.
            # For bar 1 (index 5):
            #   Can extend across whole array. Width 7. Height 1. Area 7.
            # For bar 2 (index 1):
            #   Can extend left to 6. Width 2. Height 2. Area 4.
            #   Can extend right to 5,4,5,1,6. Min height 1. Width 6. Area 6.
            # The rectangle formed by heights [2,5,4,5] (indices 1-4) has min height 2, width 4. Area 8.
            # The rectangle formed by heights [5,4,5] (indices 2-4) has min height 4, width 3. Area 12.
            "expected": 12,
            "id": "LeetCode discussion example"
        }
    ]

    passed_all = True
    for i, case in enumerate(test_cases):
        heights_input = case["input"]
        expected_output = case["expected"]
        case_id = case["id"]

        try:
            actual_output = largestRectangleArea(list(heights_input)) # Pass a copy

            if actual_output == expected_output:
                print(f"Test Case {i + 1} ({case_id}): PASSED")
            else:
                print(f"Test Case {i + 1} ({case_id}): FAILED")
                print(f"  Input:    {heights_input}")
                print(f"  Expected: {expected_output}")
                print(f"  Actual:   {actual_output}")
                passed_all = False
        except Exception as e:
            print(f"Test Case {i + 1} ({case_id}): ERROR")
            print(f"  Input:    {heights_input}")
            print(f"  Exception: {e}")
            import traceback
            traceback.print_exc()
            passed_all = False
        print("-" * 40)

    if passed_all:
        print("All test cases passed!")
    else:
        print("Some test cases failed.")

