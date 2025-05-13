# 347. Top K Frequent Elements
#
# Description:
# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.
#
# Constraints:
# 1 <= nums.length <= 10^5
# k is in the range [1, the number of unique elements in the array]
# It is guaranteed that the answer is unique.

from typing import List
import unittest


def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    Returns a list of the k most frequent elements in nums.
    """
    # TODO: Implement using a heap or bucket sort approach
    pass

class TestTopKFrequent(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"nums": [1,1,1,2,2,3],       "k": 2, "expected": [1,2],    "id": "Example 1"},
            {"nums": [1],                 "k": 1, "expected": [1],      "id": "Single element"},
            {"nums": [4,1,-1,2,-1,2,3],   "k": 2, "expected": [-1,2],  "id": "With negatives"},
            {"nums": [1,2,3,4,5],         "k": 3, "expected": [1,2,3], "id": "All unique"},
            {"nums": [5,5,4,4,4,3,3,3,3], "k": 1, "expected": [3],      "id": "Single top frequency"},
        ]

    def test_top_k_frequent(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = topKFrequent(case["nums"], case["k"])
                self.assertIsInstance(result, list, "Result should be a list")
                self.assertCountEqual(
                    result,
                    case["expected"],
                    f"topKFrequent failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
