# 54. Spiral Matrix
#
# Description:
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
#
# Examples:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

import unittest
from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    """
    Returns the elements of the matrix in spiral order.

    Parameters:
        matrix (List[List[int]]): 2D list of integers.
    Returns:
        List[int]: Elements in spiral traversal order.
    """
    # TODO: Implement the spiral traversal here
    pass


class TestSpiralMatrix(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"matrix": [[1,2,3],[4,5,6],[7,8,9]],
             "expected": [1,2,3,6,9,8,7,4,5],
             "id": "3x3 matrix"},
            {"matrix": [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
             "expected": [1,2,3,4,8,12,11,10,9,5,6,7],
             "id": "3x4 matrix"},
            {"matrix": [[1]],
             "expected": [1],
             "id": "1x1 matrix"},
            {"matrix": [[1,2,3,4]],
             "expected": [1,2,3,4],
             "id": "1x4 row"},
            {"matrix": [[1],[2],[3],[4]],
             "expected": [1,2,3,4],
             "id": "4x1 column"},
            {"matrix": [[1,2],[3,4]],
             "expected": [1,2,4,3],
             "id": "2x2 matrix"},
        ]

    def test_spiral_order(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                # make a deep copy to ensure in-place modifications are handled
                matrix = [row[:] for row in case["matrix"]]
                result = spiralOrder(matrix)
                # Validate return type
                self.assertIsInstance(result, list, "Result should be a list of integers")
                # Validate correctness
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed: got {result}, expected {case['expected']}"
                )


if __name__ == "__main__":
    unittest.main()
