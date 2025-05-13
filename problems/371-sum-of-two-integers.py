# 371. Sum of Two Integers
#
# Description:
# Calculate the sum of two integers a and b without using the '+' or '-' operators.
#
# Constraints:
# -2^31 <= a, b <= 2^31 - 1
# The result should fit within a 32-bit signed integer (assume overflow behavior as in 32-bit two's complement).

import unittest

def getSum(a: int, b: int) -> int:
    """
    Returns the sum of a and b without using '+' or '-' operators, handling 32-bit overflow.
    """
    # TODO: Implement using bitwise operations and masking for 32-bit overflow
    pass

class TestSumOfTwoIntegers(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(getSum(1, 2), 3)
        self.assertEqual(getSum(-2, 3), 1)
        self.assertEqual(getSum(-3, -1), -4)

    def test_zero_and_negative(self):
        self.assertEqual(getSum(0, 0), 0)
        self.assertEqual(getSum(0, 5), 5)
        self.assertEqual(getSum(5, 0), 5)
        self.assertEqual(getSum(-5, 5), 0)

    def test_large_values(self):
        # 32-bit overflow examples
        self.assertEqual(getSum(2147483647, 1), -2147483648)
        self.assertEqual(getSum(-2147483648, -1), 2147483647)
        # arbitrary large
        self.assertEqual(getSum(123456, 654321), 777777)

if __name__ == "__main__":
    unittest.main()
