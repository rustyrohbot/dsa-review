# Insertion Sort

## Description

Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, insertion sort provides several advantages:

*   Simple implementation
*   Efficient for (quite) small data sets
*   More efficient in practice than most other simple quadratic (i.e., O(n2)) algorithms such as selection sort or bubble sort
*   Adaptive, i.e., efficient for data sets that are already substantially sorted: the time complexity is O(nk) when each element in the input is no more than k steps away from its sorted position
*   Stable; i.e., does not change the relative order of elements with equal keys
*   In-place; i.e., only requires a constant amount O(1) of additional memory space
*   Online; i.e., can sort a list as it receives it

## Algorithm

Insertion sort iterates, consuming one input element each repetition, and grows a sorted output list. On each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there. It repeats until no input elements remain.

## Time Complexity

*   **Worst-case:** O(n^2) - Occurs when the array is in reverse order.
*   **Average-case:** O(n^2)
*   **Best-case:** O(n) - Occurs when the array is already sorted.

## Space Complexity

*   **Worst-case:** O(1) - Insertion sort is an in-place sorting algorithm, meaning it sorts the array without needing additional space.

## Example Code
```
python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```
## How to Use