# 212. Word Search II
#
# Description:
# Given an m x n board of characters and a list of strings `words`, return all words on the board.
# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once in a word.
#
# Constraints:
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.

from typing import List
import unittest


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    """
    Returns all words from the list that can be formed on the board.
    """
    # TODO: Implement using trie + DFS/backtracking for efficiency
    pass

class TestWordSearchII(unittest.TestCase):
    def setUp(self):
        self.board = [
            ['o','a','a','n'],
            ['e','t','a','e'],
            ['i','h','k','r'],
            ['i','f','l','v']
        ]
        self.words = ["oath","pea","eat","rain"]

    def assertUnorderedEqual(self, list1, list2):
        self.assertEqual(sorted(list1), sorted(list2), f"Expected {list2}, got {list1}")

    def test_example(self):
        result = findWords(self.board, self.words)
        self.assertUnorderedEqual(result, ["oath","eat"] )

    def test_empty_words(self):
        self.assertEqual(findWords(self.board, []), [])

    def test_single_letter_board(self):
        board = [['a']]
        self.assertUnorderedEqual(findWords(board, ['a','b']), ['a'])

    def test_no_matches(self):
        self.assertEqual(findWords(self.board, ['xyz']), [])

if __name__ == "__main__":
    unittest.main()