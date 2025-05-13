# 208. Implement Trie (Prefix Tree)
#
# Description:
# Implement a trie with insert, search, and startsWith methods.
# A trie is a tree-like data structure that stores a dynamic set of strings, where keys are usually strings.
#
# Constraints:
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist of lowercase English letters.

from typing import Dict
import unittest

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end: bool = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # TODO: Initialize root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # TODO: Traverse or create nodes for each character, mark end
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie, else False.
        """
        # TODO: Traverse and check is_end
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that starts with the given prefix.
        """
        # TODO: Traverse and return True if traversal succeeds
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert_and_search(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"), "Inserted word should be found.")
        self.assertFalse(self.trie.search("app"), "Non-complete prefix shouldn't be found as word.")
        self.assertTrue(self.trie.startsWith("app"), "Prefix should be recognized.")
        self.trie.insert("app")
        self.assertTrue(self.trie.search("app"), "After inserting prefix, search should succeed.")

    def test_empty_trie(self):
        self.assertFalse(self.trie.search("a"), "Search in empty trie should return False.")
        self.assertTrue(self.trie.startsWith(""), "Empty prefix should always return True.")

    def test_multiple_words(self):
        words = ["test", "trie", "tree", "algorithm"]
        for w in words:
            self.trie.insert(w)
        for w in words:
            self.assertTrue(self.trie.search(w), f"Word '{w}' should be found.")
        self.assertFalse(self.trie.search("tri"), "Non-inserted word shouldn't be found.")
        self.assertTrue(self.trie.startsWith("tri"), "Inserted words share prefix 'tri'.")
        self.assertFalse(self.trie.startsWith("algoz"), "Non-existent prefix shouldn't be found.")

if __name__ == "__main__":
    unittest.main()
