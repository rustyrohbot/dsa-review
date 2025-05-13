# 211. Design Add and Search Words Data Structure
#
# Description:
# Design a data structure that supports adding new words and finding if a string matches any previously added string.
# Implement the WordDictionary class:
#   - WordDictionary() Initializes the object.
#   - void addWord(word) Adds word to the data structure, it can be matched later.
#   - bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
#     word may contain dots '.' where dots can be matched with any letter.
#
# Constraints:
# 1 <= word.length <= 25
# addWord and search are called at most 5 * 10^4 times in total.
# word consists of lowercase English letters or '.'.

import unittest

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # TODO: Initialize root node
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        # TODO: Insert word into trie
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        # TODO: Search with support for '.' wildcard using DFS
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            ch = word[i]
            if ch == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            if ch not in node.children:
                return False
            return dfs(node.children[ch], i + 1)
        return dfs(self.root, 0)

class TestWordDictionary(unittest.TestCase):
    def setUp(self):
        self.dic = WordDictionary()
        # Add some words
        for w in ["bad", "dad", "mad"]:
            self.dic.addWord(w)

    def test_search_exact(self):
        self.assertTrue(self.dic.search("bad"))
        self.assertTrue(self.dic.search("dad"))
        self.assertFalse(self.dic.search("pad"))

    def test_search_with_wildcard(self):
        self.assertTrue(self.dic.search(".ad"))
        self.assertTrue(self.dic.search("b.."))
        self.assertFalse(self.dic.search("..z"))

    def test_mixed_operations(self):
        self.dic.addWord("a")
        self.assertTrue(self.dic.search("."))
        self.assertFalse(self.dic.search("b"))

if __name__ == "__main__":
    unittest.main()
