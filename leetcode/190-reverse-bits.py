# 190. Reverse Bits
#
# Description:
# Reverse bits of a given 32 bits unsigned integer and return the result.
#
# Constraints:
# The input is a 32-bit unsigned integer.
#
# Examples:
# Input: n = 0b00000010100101000001111010011100 (43261596)
# Output: 0b00111001011110000010100101000000 (964176192)
#
# Input: n = 0b11111111111111111111111111111101 (4294967293)
# Output: 0b10111111111111111111111111111111 (3221225471)

import unittest

def reverseBits(n: int) -> int:
    """
    Reverses the bits of a 32-bit unsigned integer.
    """
    # TODO: Implement bitwise reversal by iterating through all 32 bits
    pass

class TestReverseBits(unittest.TestCase):
    def test_examples(self):
        # Example 1
        self.assertIsInstance(reverseBits(43261596), int)
        self.assertEqual(reverseBits(43261596), 964176192)
        # Example 2
        self.assertEqual(reverseBits(4294967293), 3221225471)

    def test_edge_zero(self):
        # All bits zero stays zero
        self.assertEqual(reverseBits(0), 0)

    def test_edge_power_of_two(self):
        # Single 1-bit moves to opposite end
        self.assertEqual(reverseBits(1), 1 << 31)
        self.assertEqual(reverseBits(1 << 31), 1)

    def test_edge_all_ones(self):
        # All bits one stays all ones
        self.assertEqual(reverseBits(0xFFFFFFFF), 0xFFFFFFFF)

if __name__ == "__main__":
    unittest.main()
