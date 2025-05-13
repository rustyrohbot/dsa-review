# 73. Set Matrix Zeroes
#
# Description:
# Given an m x n matrix, if an element is 0, set its entire row and column to 0's in-place.
#
# Constraints:
# m == len(matrix)
# n == len(matrix[i])
# 1 <= m, n <= 20
# -2^31 <= matrix[i][j] <= 2^31 - 1
#
# Examples:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
#
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

import unittest
from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Modify matrix in-place: if an element is 0, set its entire row and column to 0.
    """
    # TODO: Implement in-place zeroing using constant space or O(m+n) markers
    pass


class TestSetMatrixZeroes(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {
                "input": [[1,1,1],[1,0,1],[1,1,1]],
                "expected": [[1,0,1],[0,0,0],[1,0,1]],
                "id": "Single zero"
            },
            {
                "input": [[0,1,2,0],[3,4,5,2],[1,3,1,5]],
                "expected": [[0,0,0,0],[0,4,5,0],[0,3,1,0]],
                "id": "Multiple zeros"
            },
            {
                "input": [[1,2,3],[4,5,6],[7,8,9]],
                "expected": [[1,2,3],[4,5,6],[7,8,9]],
                "id": "No zeros"
            },
            {
                "input": [[0]],
                "expected": [[0]],
                "id": "1x1 zero"
            },
            {
                "input": [[5]],
                "expected": [[5]],
                "id": "1x1 non-zero"
            },
            {
                "input": [[0,1,2]],
                "expected": [[0,0,0]],
                "id": "1x3 with zero"
            },
            {
                "input": [[1,2,3]],
                "expected": [[1,2,3]],
                "id": "1x3 no zero"
            },
            {
                "input": [[1],[0],[3]],
                "expected": [[0],[0],[0]],
                "id": "3x1 with zero"
            },
            {
                "input": [[1],[2],[3]],
                "expected": [[1],[2],[3]],
                "id": "3x1 no zero"
            }
        ]

    def test_set_zeroes(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                matrix = [row[:] for row in case["input"]]  # deep copy
                setZeroes(matrix)
                self.assertEqual(
                    matrix,
                    case["expected"],
                    f"Case '{case['id']}' failed: got {matrix}, expected {case['expected']}"
                )


if __name__ == "__main__":
    unittest.main()
