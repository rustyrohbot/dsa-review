# Quick Sort

## Description

Quick Sort is a highly efficient, divide-and-conquer sorting algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

## Algorithm

1.  **Choose a pivot:** Select an element from the array to serve as the pivot. There are different pivot selection strategies (e.g., first element, last element, random element, median of three).
2.  **Partitioning:** Rearrange the array so that all elements less than the pivot are placed before it, and all elements greater than the pivot are placed after it. The pivot is now in its final sorted position.
3.  **Recursive calls:** Recursively apply the above steps to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.
4. **Base case**: If the sub-array has 0 or 1 element, it is already sorted, so do nothing.

## Time Complexity

*   **Worst Case:** O(n^2) - This occurs when the pivot is consistently the smallest or largest element, leading to highly unbalanced partitions.
*   **Average Case:** O(n log n) - This is the typical performance for Quick Sort, making it very efficient in most cases.
*   **Best Case:** O(n log n) - Occurs when the pivot consistently divides the array into roughly equal halves.

## Space Complexity

*   **Worst Case:** O(n) - In the worst case, due to recursive calls, the space used on the call stack can be linear.
* **Average Case:** O(log n)- On average, the space used on the call stack is logarithmic due to balanced partitions.