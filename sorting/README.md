# Sorting Algorithms

This directory contains Python implementations of various sorting algorithms. These algorithms are fundamental to computer science and are used in a wide range of applications. The directory includes the following sorting algorithms:

*   Bubble Sort
*   Bucket Sort
*   Heap Sort
*   Insertion Sort
*   Merge Sort
*   Quick Sort
*   Selection Sort
*   Shell Sort

## Algorithm Descriptions

### Bubble Sort

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

### Bucket Sort

Bucket Sort, or bin sort, is a sorting algorithm that works by distributing the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sort algorithm.

### Heap Sort

Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure. It divides its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region by extracting the largest element and moving that to the sorted region.

### Insertion Sort

Insertion Sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

### Merge Sort

Merge Sort is a divide-and-conquer algorithm that was invented by John von Neumann in 1945. Conceptually, a merge sort works as follows:
Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

### Quick Sort

Quick Sort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

### Selection Sort

Selection Sort is an in-place comparison sorting algorithm. It has an O(n2) time complexity, which makes it inefficient on large lists, and generally performs worse than the similar insertion sort.

### Shell Sort

Shell Sort is mainly a variation of Insertion Sort. In insertion sort, we move elements only one position ahead. When an element has to be moved far ahead, many movements are involved. The idea of ShellSort is to allow exchange of far items. In shell sort, we make the array h-sorted for a large value of h. We keep reducing the value of h until it becomes 1. An array is said to be h-sorted if all sublists of every h’th element is sorted.

## Navigating the Directory

Each sorting algorithm has its own implementation file (e.g., `BubbleSort.py`) containing the Python code for that algorithm. Additionally, each algorithm has a corresponding markdown file (e.g., `BUBBLE.md`) that provides a detailed description and explanation of how the algorithm works.

## Running the Tests

The tests for all sorting algorithms are located in the `TestSorting.py` file. To run the tests, ensure you are in the project's `sorting` directory in your terminal.

To run all tests, use the following command:
```
bash
python3 TestSorting.py
```
This will execute all the tests defined in the `TestSorting.py` file.

**Running Individual Tests:**

You can run tests for a specific algorithm by appending the lowercase name of the algorithm to the command. For example, to run the test for Bubble Sort, you can run:
```bash
python3 TestSorting.py bubble
```
Similarly, to run the test for Quick Sort, you can run:
```bash
python3 TestSorting.py quick
```