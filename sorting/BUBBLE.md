# Bubble Sort

## Description

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. The algorithm, which is a comparison sort, is named for the way smaller or larger elements "bubble" to the top of the list.

## Algorithm

1.  Start at the beginning of the list.
2.  Compare the first two elements. If the first element is greater than the second, swap them.
3.  Move to the next pair of elements (the second and third) and repeat step 2.
4.  Continue this process, moving through the entire list. After one pass, the largest element will be at its correct position (the end of the list).
5.  Repeat steps 1-4, but this time stop at the second to last element, since the last element is already sorted.
6.  Continue this process, each time reducing the section of the list you are checking by one, until you reach the beginning of the list.

## Time Complexity

*   **Worst Case:** O(n^2) - This occurs when the list is in reverse order.
*   **Average Case:** O(n^2)
*   **Best Case:** O(n) - This occurs when the list is already sorted.

## Space Complexity

*   **Worst Case:** O(1) - Bubble sort is an in-place sorting algorithm, meaning it sorts the list within the existing memory space, without requiring extra memory proportional to the input size.
