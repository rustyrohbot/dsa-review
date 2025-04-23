# Selection Sort

## Algorithm Description

Selection Sort is a simple comparison-based sorting algorithm. It works by repeatedly finding the minimum element from the unsorted part of the array and putting it at the beginning. The algorithm divides the array into two parts: a sorted subarray, which is built up from left to right at the beginning of the array, and the remaining unsorted subarray.

**Here's how it works:**

1.  Find the minimum element in the unsorted array.
2.  Swap it with the first element of the unsorted part.
3.  Move the boundary of the sorted subarray one element to the right.
4.  Repeat steps 1-3 until the entire array is sorted.

## Time Complexity

*   **Worst-case:** O(n^2) - Occurs when the array is in reverse order.
*   **Average-case:** O(n^2) - The algorithm performs the same number of comparisons in most cases.
*   **Best-case:** O(n^2) - Even if the array is sorted, the algorithm still needs to iterate and compare.

## Space Complexity

*   **Worst-case:** O(1) - Selection Sort sorts the array in-place, meaning it only requires a constant amount of extra space.