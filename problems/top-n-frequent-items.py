# Problem: Top N Frequent Items
#
# Description:
# Given a collection of items (e.g., a list of lists, where each inner
# list contains items like product IDs, words, etc.), and an integer N.
#
# Task:
# 1. Count the frequency of each unique item across the entire collection.
# 2. Return the N items that occurred most frequently.
#
# Output Format:
# A list of tuples, where each tuple is (item, frequency).
# The list should be sorted by frequency in descending order.
# If frequencies are tied, items with the same frequency should be sorted
# by the item itself (e.g., lexicographically for strings, numerically for
# numbers) in ascending order.
# If there are fewer than N unique items, return all of them, sorted.

from typing import List, Tuple, Any, Dict
import collections
import heapq # For alternative Top N implementation

# Define a type for an item (e.g., str, int)
ItemType = Any

def get_top_n_items(
    data_collection: List[List[ItemType]], n: int
) -> List[Tuple[ItemType, int]]:
    """
    Finds the top N most frequent items from a collection (list of lists).
    """
    if not data_collection or n <= 0:
        return []

    item_counts: Dict[ItemType, int] = collections.Counter()

    for sub_list in data_collection:
        for item in sub_list:
            item_counts[item] += 1

    # If the input is expected to be a flat list:
    # def get_top_n_items_flat(items_list: List[ItemType], n: int):
    #     if not items_list or n <= 0: return []
    #     item_counts = collections.Counter(items_list)

    if not item_counts:
        return []

    # Convert Counter items to a list of (item, frequency)
    all_items_with_counts = list(item_counts.items())

    # Sort:
    # Primary key: frequency (descending, so use -x[1])
    # Secondary key: item (ascending, so use x[0])
    all_items_with_counts.sort(key=lambda x: (-x[1], x[0]))

    return all_items_with_counts[:n]

    # Alternative using heapq.nlargest (often very convenient):
    # return heapq.nlargest(n, item_counts.items(), key=lambda x: (x[1], x[0]))
    # Note: For nlargest, to get descending frequency then ascending item for ties,
    # the key needs careful thought. The above lambda for nlargest would sort by
    # freq ascending, then item ascending.
    # To match the sort:
    # sorted_items = sorted(item_counts.items(), key=lambda x: (-x[1], x[0]))
    # return sorted_items[:n]
    #
    # Or, if using a min-heap manually for top N largest:
    # min_heap = [] # Stores (frequency, item)
    # for item, freq in item_counts.items():
    #     # For tie-breaking with item, if we push (-freq, item) to a min-heap,
    #     # it becomes a max-heap on freq, and min-heap on item for ties.
    #     # Or push (freq, "inverted_item_for_sorting") if item is not directly comparable in reverse.
    #     # Simpler to sort after getting all items as done above.
    #     pass


if __name__ == "__main__":
    test_cases = [
        {
            "id": "Simple case",
            "data_collection": [
                ["apple", "banana", "apple"],
                ["orange", "banana"],
                ["apple", "orange", "orange", "grape"],
            ],
            "n": 2,
            # Frequencies:
            # "apple": 3
            # "banana": 2
            # "orange": 3
            # "grape": 1
            # Sorted by (-freq, item):
            # ("apple", 3)
            # ("orange", 3)
            # ("banana", 2)
            # ("grape", 1)
            "expected": [("apple", 3), ("orange", 3)], # or [("orange",3),("apple",3)]
                                                      # With sort key (-x[1], x[0]):
                                                      # apple comes before orange
        },
        {
            "id": "N larger than unique items",
            "data_collection": [["a", "b"], ["a"]],
            "n": 5,
            # "a": 2
            # "b": 1
            "expected": [("a", 2), ("b", 1)],
        },
        {
            "id": "Empty collection",
            "data_collection": [],
            "n": 3,
            "expected": [],
        },
        {
            "id": "Empty sublists",
            "data_collection": [[], [], []],
            "n": 2,
            "expected": [],
        },
        {
            "id": "All items unique, N smaller",
            "data_collection": [["x"], ["y"], ["z"]],
            "n": 2,
            # "x":1, "y":1, "z":1
            # Sorted: ("x",1), ("y",1), ("z",1)
            "expected": [("x", 1), ("y", 1)],
        },
        {
            "id": "Integer items",
            "data_collection": [[1, 2, 2], [3, 1, 2], [4]],
            "n": 3,
            # 1: 2
            # 2: 3
            # 3: 1
            # 4: 1
            # Sorted: (2,3), (1,2), (3,1) or (4,1)
            # (2,3), (1,2), (3,1) (since 3 < 4)
            "expected": [(2, 3), (1, 2), (3, 1)],
        },
        {
            "id": "Single sublist",
            "data_collection": [["cat", "dog", "cat", "mouse", "cat", "dog"]],
            "n": 2,
            # "cat": 3
            # "dog": 2
            # "mouse": 1
            "expected": [("cat", 3), ("dog", 2)],
        },
         {
            "id": "N=1",
            "data_collection": [
                ["apple", "banana", "apple"],
                ["orange", "banana"],
                ["apple", "orange", "orange", "grape"],
            ],
            "n": 1,
            "expected": [("apple", 3)], # apple before orange due to tie-breaking
        },
    ]

    passed_all = True
    print("--- Testing Top N Frequent Items ---")
    for i, case in enumerate(test_cases):
        collection = case["data_collection"]
        n_val = case["n"]
        expected = case["expected"]
        case_id = case["id"]

        try:
            actual = get_top_n_items(collection, n_val)

            if actual == expected:
                print(f"Test Case {i + 1} ({case_id}): PASSED")
            else:
                print(f"Test Case {i + 1} ({case_id}): FAILED")
                print(f"  Input collection: {collection}, n={n_val}")
                print(f"  Expected:         {expected}")
                print(f"  Actual:           {actual}")
                passed_all = False
        except Exception as e:
            print(f"Test Case {i + 1} ({case_id}): ERROR")
            print(f"  Input collection: {collection}, n={n_val}")
            print(f"  Exception: {e}")
            import traceback
            traceback.print_exc()
            passed_all = False
        print("-" * 40)

    if passed_all:
        print("All Top N Frequent Items test cases passed!")
    else:
        print("Some Top N Frequent Items test cases failed.")

