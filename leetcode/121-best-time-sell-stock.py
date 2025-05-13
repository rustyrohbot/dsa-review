# 121. Best Time to Buy and Sell Stock
#
# Description:
# You are given an array prices where prices[i] is the price of a given stock on the i-th day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
# Constraints:
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4
#
# Examples:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

from typing import List
import unittest


def maxProfit(prices: List[int]) -> int:
    """
    Computes the maximum profit from a single buy-sell transaction.
    """
    # TODO: Implement one-pass scan tracking min price and max profit
    pass

class TestBestTimeToBuySellStock(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"prices": [7, 1, 5, 3, 6, 4], "expected": 5, "id": "Example 1"},
            {"prices": [7, 6, 4, 3, 1], "expected": 0, "id": "Example 2"},
            {"prices": [1], "expected": 0, "id": "Single day"},
            {"prices": [2, 4, 1], "expected": 2, "id": "Profit later"},
            {"prices": [3, 2, 6, 5, 0, 3], "expected": 4, "id": "Peak after valley"},
        ]

    def test_max_profit(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = maxProfit(case["prices"])
                self.assertIsInstance(result, int, "Result should be an integer")
                self.assertEqual(result, case["expected"], f"Mismatch for case '{case['id']}'")

if __name__ == "__main__":
    unittest.main()
