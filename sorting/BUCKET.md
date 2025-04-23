# Bucket Sort

## Description

Bucket Sort is a sorting algorithm that works by distributing the elements of an array into a number of buckets. Each bucket is then sorted individually, typically using another sorting algorithm or recursively using Bucket Sort again. It is most effective when input data is uniformly distributed across a range.

## Algorithm

1.  **Scatter:** Set up an array of initially empty "buckets."
2.  **Distribute:** Go over the original array, putting each object in its bucket.
3.  **Sort Each Bucket:** Sort each non-empty bucket individually.
4.  **Gather:** Visit the buckets in order and put all elements back into the original array.

## Time Complexity

*   **Worst Case:** O(n^2) - This occurs when elements are not uniformly distributed and most elements fall into the same bucket.
*   **Average Case:** O(n+k) - This occurs when elements are uniformly distributed. Here, n is the number of elements, and k is the number of buckets.
*   **Best Case:** O(n+k) - This occurs when elements are uniformly distributed.

## Space Complexity

*   **Worst Case:** O(n+k) - This is the space needed to store the buckets and the elements, where n is the number of elements, and k is the number of buckets.




