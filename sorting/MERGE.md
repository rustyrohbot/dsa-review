# Merge Sort

## Description

Merge Sort is a divide-and-conquer algorithm that sorts a list by recursively dividing it into smaller sublists, sorting each sublist, and then merging the sorted sublists back together. It's a comparison-based sorting algorithm known for its efficiency and stability.

## Algorithm

1.  **Divide:** If the list has more than one element, divide it into two halves.
2.  **Conquer:** Recursively sort each half by applying Merge Sort to it.
3.  **Combine:** Merge the two sorted halves into a single sorted list. This is done by comparing the first elements of each half, taking the smaller one and adding it to the new sorted list, and repeating until one half is empty, then adding the rest of the other list.

## Time Complexity

*   **Worst Case:** O(n log n) - This occurs when the list needs to be fully divided and merged.
*   **Average Case:** O(n log n)
*   **Best Case:** O(n log n) - Merge sort consistently performs with O(n log n) time complexity, regardless of the initial order of elements.

## Space Complexity

*   **Worst Case:** O(n) - Merge sort requires extra space proportional to the number of elements being sorted because it needs temporary arrays for merging.