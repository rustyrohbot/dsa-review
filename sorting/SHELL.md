# Shell Sort

## Description

Shell Sort is an optimization of Insertion Sort that allows the exchange of items that are far apart. The idea is to arrange the list so that, starting anywhere, considering every nth item gives a sorted list. This is called an h-sorted list.  The process starts with a large gap and then the gap is reduced.

## Algorithm

1.  **Choose a gap sequence:** Start with a large gap, typically half the size of the array.
2.  **Perform Insertion Sort with the gap:** For each sub-array formed by the gap, perform Insertion Sort.
3.  **Reduce the gap:** Divide the gap by 2 (or use a different decreasing sequence) and repeat step 2.
4.  **Continue until gap is 1:** When the gap is 1, it's equivalent to a regular Insertion Sort, but the list is already nearly sorted, making it more efficient.

## Time Complexity

*   **Worst Case:** O(n^2) - The worst-case time complexity depends on the gap sequence. With a poorly chosen sequence, it can degrade to O(n^2).
*   **Average Case:** O(n log n) to O(n^(3/2)) - The average time complexity is hard to define precisely and varies based on the gap sequence used. Common gap sequences result in O(n log n) or O(n^(3/2)) on average.
*   **Best Case:** O(n log n) - If the array is nearly sorted, Shell Sort can perform in O(n log n) time.

## Space Complexity

*   **Worst Case:** O(1) - Shell Sort is an in-place sorting algorithm, so it only requires a constant amount of extra space.
