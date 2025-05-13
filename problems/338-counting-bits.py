# 338. Counting Bits
#
# Description:
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
# ans[i] is the number of 1's in the binary representation of i.
#
# Constraints:
# 0 <= n <= 10^5
#
from typing import List
import unittest


def countBits(n: int) -> List[int]:
    """
    Returns a list where the i-th element is the count of 1s in the binary representation of i,
    for all 0 <= i <= n.
    """
    # TODO: Implement dynamic programming or bit manipulation solution
    pass

class TestCountingBits(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"n": 2,  "expected": [0, 1, 1],               "id": "Small n"},
            {"n": 5,  "expected": [0, 1, 1, 2, 1, 2],      "id": "Example 1"},
            {"n": 0,  "expected": [0],                    "id": "Zero case"},
            {"n": 1,  "expected": [0, 1],                  "id": "One bit"},
            {"n": 10, "expected": [0,1,1,2,1,2,2,3,1,2,2], "id": "Larger n"},
        ]

    def test_count_bits(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = countBits(case["n"])
                self.assertIsInstance(result, list, "Result should be a list of integers")
                self.assertEqual(
                    result,
                    case["expected"],
                    f"countBits failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
