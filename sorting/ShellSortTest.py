import unittest
from ShellSort import shell_sort

class TestShellSort(unittest.TestCase):
    def test_empty_list(self):
        arr = []
        shell_sort(arr)
        self.assertEqual(arr, [])

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        shell_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reversed_list(self):
        arr = [5, 4, 3, 2, 1]
        shell_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_list_with_duplicates(self):
        arr = [5, 2, 8, 2, 5]
        shell_sort(arr)
        self.assertEqual(arr, [2, 2, 5, 5, 8])

    def test_general_list(self):
        arr = [5,1,4,2,8]
        shell_sort(arr)
        self.assertEqual(arr, [1,2,4,5,8])

if __name__ == '__main__':
    unittest.main()