# 322. Coin Change
#
# Description:
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.
#
# Constraints:
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4

from typing import List
import unittest


def coinChange(coins: List[int], amount: int) -> int:
    """
    Returns the minimum number of coins needed to make up the given amount, or -1 if not possible.
    """
    # TODO: Implement using dynamic programming (bottom-up or top-down)
    pass

class TestCoinChange(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"coins": [1, 2, 5], "amount": 11, "expected": 3,  "id": "Example 1"},
            {"coins": [2],       "amount": 3,  "expected": -1, "id": "No combination"},
            {"coins": [1],       "amount": 0,  "expected": 0,  "id": "Zero amount"},
            {"coins": [1],       "amount": 1,  "expected": 1,  "id": "Single coin"},
            {"coins": [1],       "amount": 2,  "expected": 2,  "id": "Multiple same coin"},
            {"coins": [2, 5, 10, 1], "amount": 27, "expected": 4, "id": "Complex mix"},
        ]

    def test_coin_change(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = coinChange(case["coins"], case["amount"])
                self.assertIsInstance(result, int, "Result should be an integer")
                self.assertEqual(
                    result,
                    case["expected"],
                    f"coinChange failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
