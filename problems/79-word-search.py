# 79. Word Search
#
# Description:
# Given an m x n board of characters and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells
# are horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Constraints:
# m == len(board)
# n == len(board[i])
# 1 <= m, n <= 200
# 1 <= len(word) <= 10^3
# board[i][j] and word consist of uppercase and/or lowercase English letters.
#
# Examples:
# Input:
# board = [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ], word = "ABCCED"
# Output: True
#
# Input:
# board = [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ], word = "SEE"
# Output: True
#
# Input:
# board = [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ], word = "ABCB"
# Output: False

import unittest
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    """
    Returns True if the word exists in the board by sequentially adjacent (horizontal/vertical)
    cells without revisiting any cell.
    """
    # TODO: Implement backtracking solution here
    pass


class TestWordSearch(unittest.TestCase):
    def setUp(self):
        self.example_board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ]
        self.test_cases = [
            {"board": self.example_board, "word": "ABCCED", "expected": True,  "id": "Example 1"},
            {"board": self.example_board, "word": "SEE",    "expected": True,  "id": "Example 2"},
            {"board": self.example_board, "word": "ABCB",   "expected": False, "id": "Example 3"},
            {"board": [['A']],              "word": "A",      "expected": True,  "id": "Single cell match"},
            {"board": [['A']],              "word": "B",      "expected": False, "id": "Single cell no match"},
            {"board": [['C','A','A'], ['A','A','A'], ['B','C','D']], "word": "AAB", "expected": True, "id": "Path with turn"},
            {"board": [['a','b'], ['c','d']],           "word": "abcd",   "expected": False, "id": "Cannot reuse cells"},
        ]

    def test_exist(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                board_copy = [row[:] for row in case["board"]]
                result = exist(board_copy, case["word"])
                self.assertIsInstance(result, bool, "Result should be a boolean")
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed for word '{case['word']}'"
                )


if __name__ == "__main__":
    unittest.main()
