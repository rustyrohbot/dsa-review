# Heap Sort

## Description

Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure. It divides its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region by extracting the largest element and moving that to the sorted region. The efficiency of Heap Sort is derived from its ability to find the largest (or smallest) element in O(1) time and rearrange the heap in O(log n) time.

## Algorithm

1.  **Build a Max Heap:** Transform the input array into a max heap, a tree-based structure where the value of each parent node is greater than or equal to the values of its children.
2.  **Swap Root with Last Element:** Swap the root (maximum element) of the heap with the last element of the heap.
3.  **Heapify:** Reduce the heap size by one and "heapify" the new root to maintain the max heap property. Heapify involves comparing the root with its children and swapping it with the larger child if necessary. This process is done recursively until the max heap property is restored.
4.  **Repeat:** Repeat steps 2 and 3 until the heap size is 1, at which point the entire array is sorted.

## Time Complexity

*   **Worst Case:** O(n log n) - This occurs when the array is in reverse sorted order or any other case, as the build heap and heapify operations dominate the time complexity.
*   **Average Case:** O(n log n) - Heap Sort consistently has a time complexity of O(n log n) regardless of the input data.
*   **Best Case:** O(n log n) - Even if the array is already sorted, the algorithm will still go through the process of building the heap and extracting elements.

## Space Complexity

*   **Worst Case:** O(1) - Heap Sort is an in-place algorithm, meaning it sorts the array within the existing memory space. It only requires a constant amount of additional memory for temporary variables during swapping, so the space used does not depend on the input size.