# 48. Rotate Image
#
# Description:
# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise), in-place.
#
# Constraints:
# matrix is n x n where 1 <= n <= 20 (or larger depending on environment)
# -10^9 <= matrix[i][j] <= 10^9
#
# Examples:
# Input:  matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
#
# Input:  matrix = [[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]
# Output: [[15,13, 2, 5],[14, 3, 4, 1],[12, 6, 8, 9],[16, 7,10,11]]

import unittest
from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Rotates the matrix in-place by 90 degrees clockwise.
    """
    # TODO: Implement in-place rotation here
    pass


class TestRotateImage(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {
                "input": [[1,2,3],[4,5,6],[7,8,9]],
                "expected": [[7,4,1],[8,5,2],[9,6,3]],
                "id": "3x3 matrix"
            },
            {
                "input": [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
                "expected": [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]],
                "id": "4x4 matrix"
            },
            {
                "input": [[1]],
                "expected": [[1]],
                "id": "1x1 matrix"
            },
            {
                "input": [[1,2],[3,4]],
                "expected": [[3,1],[4,2]],
                "id": "2x2 matrix"
            },
        ]

    def test_rotate(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                matrix = [row[:] for row in case["input"]]  # deep copy
                rotate(matrix)
                self.assertEqual(
                    matrix,
                    case["expected"],
                    f"Failed on case '{case['id']}': expected {case['expected']}, got {matrix}"
                )


if __name__ == "__main__":
    unittest.main()