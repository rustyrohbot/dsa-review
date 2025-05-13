# 70. Climbing Stairs
#
# Description:
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Constraints:
# 1 <= n <= 45
#
# Examples:
# Input: n = 2    Output: 2  # (1+1, 2)
# Input: n = 3    Output: 3  # (1+1+1, 1+2, 2+1)

import unittest


def climbStairs(n: int) -> int:
    """
    Returns the number of distinct ways to climb to the top of an n-step staircase,
    where at each move you can climb either 1 or 2 steps.

    Parameters:
        n (int): Total number of steps.
    Returns:
        int: Number of distinct ways to reach the top.
    """
    # TODO: Implement the dynamic programming or Fibonacci solution here
    pass


class TestClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"n": 1,  "expected": 1,    "id": "One step"},
            {"n": 2,  "expected": 2,    "id": "Two steps"},
            {"n": 3,  "expected": 3,    "id": "Three steps"},
            {"n": 4,  "expected": 5,    "id": "Four steps"},
            {"n": 5,  "expected": 8,    "id": "Five steps"},
            {"n": 10, "expected": 89,   "id": "Ten steps"},
            {"n": 45, "expected": 1836311903, "id": "Max constraint"},
        ]

    def test_climb_stairs(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                result = climbStairs(case["n"])
                # Validate return type
                self.assertIsInstance(result, int, "Result should be an integer")
                # Validate correctness
                self.assertEqual(
                    result,
                    case["expected"],
                    f"Case '{case['id']}' failed for n={case['n']}"
                )


if __name__ == "__main__":
    unittest.main()
