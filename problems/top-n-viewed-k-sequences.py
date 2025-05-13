# Problem: Top N Viewed K-Sequences
#
# Description:
# Given a list of user sessions, where each session is a list of items
# (e.g., strings representing product IDs or page URLs) viewed in order.
# Also given two integers, K (the desired sequence length) and N (the
# number of top sequences to return).
#
# Task:
# 1. For each user session, extract all contiguous sub-sequences of length K.
# 2. Count the frequency of each unique K-sequence across all sessions.
# 3. Return the N K-sequences that occurred most frequently.
#
# Output Format:
# A list of tuples, where each tuple is (sequence, frequency).
# The list should be sorted by frequency in descending order.
# If frequencies are tied, the order of sequences with the same frequency
# can be arbitrary (though for testing, we might sort them lexicographically).
# If there are fewer than N unique K-sequences, return all of them, sorted.

from typing import List, Tuple, Any, Dict
import collections
import heapq

# Define a type for an item in a sequence (e.g., str, int)
ItemType = Any
Sequence = Tuple[ItemType, ...] # K-sequences will be tuples to be hashable

def get_top_n_k_sequences(
    user_sessions: List[List[ItemType]], k: int, n: int
) -> List[Tuple[Sequence, int]]:
    """
    Finds the top N most frequent K-length sequences from user sessions.
    """
    if not user_sessions or k <= 0 or n <= 0:
        return []

    sequence_counts: Dict[Sequence, int] = collections.Counter()

    for session in user_sessions:
        if len(session) < k:
            continue
        for i in range(len(session) - k + 1):
            # Extract K-sequence and convert to tuple to be hashable
            k_sequence = tuple(session[i : i + k])
            sequence_counts[k_sequence] += 1

    if not sequence_counts:
        return []

    # Use a min-heap to find the top N elements efficiently
    # The heap will store (frequency, sequence) to sort by frequency
    # Python's heapq is a min-heap, so for top N largest, we can:
    # 1. Push all items and then use nlargest.
    # 2. Maintain a heap of size N: if new item > heap_min, pop and push.

    # Option 1: Using heapq.nlargest (simpler to write)
    # We need to sort by frequency (value) then by sequence (key) for deterministic tie-breaking
    # nlargest takes an iterable and a key for comparison.
    # To handle ties by sequence lexicographically for consistent test results:
    # We can store (-frequency, sequence) in a min-heap to simulate a max-heap by frequency,
    # then sort sequences lexicographically for ties.
    # Or, get all items, sort them, then take top N.

    # Let's use a more direct approach for clarity with sorting for ties:
    # Convert Counter items to a list of (sequence, frequency)
    all_sequences_with_counts = list(sequence_counts.items())

    # Sort: Primary key is frequency (descending), secondary key is sequence (ascending for ties)
    # Python's sort is stable, so we can sort multiple times or use a tuple in lambda.
    # Sorting by (-frequency, sequence_tuple)
    all_sequences_with_counts.sort(key=lambda x: (-x[1], x[0]))

    return all_sequences_with_counts[:n]

    # Alternative using heapq for potentially better performance on very large unique sequence counts:
    # min_heap = [] # Stores (frequency, sequence_tuple)
    # for seq, freq in sequence_counts.items():
    #     if len(min_heap) < n:
    #         heapq.heappush(min_heap, (freq, seq))
    #     elif freq > min_heap[0][0]: # If current freq is greater than smallest in heap
    #         heapq.heapreplace(min_heap, (freq, seq))
    #     elif freq == min_heap[0][0]: # Handle ties for Nth element if specific tie-breaking is needed
    #         # If we need to break ties lexicographically (e.g. smaller sequence wins)
    #         if seq < min_heap[0][1]: # Assuming sequences are comparable
    #              heapq.heapreplace(min_heap, (freq, seq))

    # result = sorted([(seq, freq) for freq, seq in min_heap], key=lambda x: (-x[1], x[0]))
    # return result


if __name__ == "__main__":
    test_cases = [
        {
            "id": "Simple case",
            "user_sessions": [
                ["a", "b", "c", "d"],
                ["a", "b", "e"],
                ["a", "b", "c", "e"],
                ["x", "y", "z"],
            ],
            "k": 3,
            "n": 2,
            # Frequencies:
            # ("a","b","c"): 2
            # ("b","c","d"): 1
            # ("a","b","e"): 1
            # ("b","c","e"): 1
            # ("x","y","z"): 1
            # Top 2: (("a","b","c"), 2), then one of the 1-count sequences.
            # For deterministic output, let's assume tie-breaking by sequence lexicographically.
            # ("a","b","e") comes before ("b","c","d")
            "expected": [(("a", "b", "c"), 2), (("a", "b", "e"), 1)],
        },
        {
            "id": "Session shorter than K",
            "user_sessions": [["a", "b"], ["c", "d", "e", "f"]],
            "k": 3,
            "n": 1,
            # ("c","d","e"): 1
            # ("d","e","f"): 1
            "expected": [(("c", "d", "e"), 1)], # or (("d","e","f"),1) depending on tie-break
        },
        {
            "id": "N larger than unique sequences",
            "user_sessions": [["x", "y", "z"]],
            "k": 3,
            "n": 5,
            "expected": [(("x", "y", "z"), 1)],
        },
        {
            "id": "Empty sessions",
            "user_sessions": [],
            "k": 3,
            "n": 2,
            "expected": [],
        },
        {
            "id": "k=1",
            "user_sessions": [["a","b","a"],["b","c"]],
            "k": 1,
            "n": 2,
            # ("a",): 2
            # ("b",): 2
            # ("c",): 1
            "expected": [(("a",), 2), (("b",), 2)], # or (("b",),2), (("a",),2)
        },
        {
            "id": "All same sequence",
            "user_sessions": [["s1","s2","s3"], ["s1","s2","s3"], ["s1","s2","s3"]],
            "k": 3,
            "n": 1,
            "expected": [(("s1", "s2", "s3"), 3)],
        },
        {
            "id": "No sequences of length K",
            "user_sessions": [["a","b"], ["c"]],
            "k": 3,
            "n": 1,
            "expected": [],
        },
        {
            "id": "Complex tie-breaking scenario",
            "user_sessions": [
                ["a", "b", "c"], ["a", "b", "d"], ["a", "b", "e"],
                ["x", "y", "a"], ["x", "y", "b"]
            ],
            "k": 3,
            "n": 3,
            # ("a","b","c"): 1
            # ("a","b","d"): 1
            # ("a","b","e"): 1
            # ("x","y","a"): 1
            # ("x","y","b"): 1
            # All have freq 1. Top 3 by lexicographical:
            "expected": [
                (("a", "b", "c"), 1),
                (("a", "b", "d"), 1),
                (("a", "b", "e"), 1),
            ],
        },
    ]

    passed_all = True
    print("--- Testing Top N Viewed K-Sequences ---")
    for i, case in enumerate(test_cases):
        sessions = case["user_sessions"]
        k_val = case["k"]
        n_val = case["n"]
        expected = case["expected"]
        case_id = case["id"]

        try:
            actual = get_top_n_k_sequences(sessions, k_val, n_val)

            # For comparison, ensure actual is also sorted like expected if not using heap's specific order
            # The provided solution sorts by (-freq, sequence), so it should be deterministic.

            if actual == expected:
                print(f"Test Case {i + 1} ({case_id}): PASSED")
            else:
                print(f"Test Case {i + 1} ({case_id}): FAILED")
                print(f"  Input sessions: {sessions}, k={k_val}, n={n_val}")
                print(f"  Expected:       {expected}")
                print(f"  Actual:         {actual}")
                passed_all = False
        except Exception as e:
            print(f"Test Case {i + 1} ({case_id}): ERROR")
            print(f"  Input sessions: {sessions}, k={k_val}, n={n_val}")
            print(f"  Exception: {e}")
            import traceback
            traceback.print_exc()
            passed_all = False
        print("-" * 40)

    if passed_all:
        print("All Top N K-Sequences test cases passed!")
    else:
        print("Some Top N K-Sequences test cases failed.")

