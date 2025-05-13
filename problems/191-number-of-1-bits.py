# 191. Number of 1 Bits
#
# Description:
# Write a function that takes the binary representation of a 32-bit unsigned integer
# and returns the number of '1' bits it has (the Hamming weight).
#
# Constraints:
# The input is a 32-bit unsigned integer.

import unittest


def hammingWeight(n: int) -> int:
    """
    Returns the number of '1' bits in the 32-bit unsigned integer n.
    """
    # TODO: Implement bit count (e.g., Brian Kernighan's algorithm)
    pass

class TestNumberOf1Bits(unittest.TestCase):
    def test_examples(self):
        # Example 1
        self.assertEqual(hammingWeight(0b00000000000000000000000000001011), 3)
        # Example 2
        self.assertEqual(hammingWeight(0b00000000000000000000000010000000), 1)
        # Example 3
        self.assertEqual(hammingWeight(0b11111111111111111111111111111101), 31)

    def test_edge_cases(self):
        # All zeros
        self.assertEqual(hammingWeight(0), 0)
        # All ones
        self.assertEqual(hammingWeight(0xFFFFFFFF), 32)

if __name__ == "__main__":
    unittest.main()