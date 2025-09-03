# 509.py
from test.test_suite import run_tests


class Solution:
    def fib(self, n: int) -> int:
        if n < 2: return n
        memo = [None] * (n + 1)
        memo[0] = 0
        memo[1] = 1
        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[n]

    # 空间优化（仅使用两个变量）空间复杂度降低到 O(1)。
    # def fib(self, n: int) -> int:
    #     if n < 2:
    #         return n
    #     a, b = 0, 1
    #     for _ in range(2, n + 1):
    #         a, b = b, a + b
    #     return b


test_cases = [
    {
        "method": "fib",
        "n": 0,
        "expected": 0,
        "case_id": 1,
        "description": "Edge case: the first Fibonacci number, F(0)"
    },
    {
        "method": "fib",
        "n": 1,
        "expected": 1,
        "case_id": 2,
        "description": "Edge case: the second Fibonacci number, F(1)"
    },
    {
        "method": "fib",
        "n": 2,
        "expected": 1,
        "case_id": 3,
        "description": "Standard case: F(2) = F(1) + F(0) = 1"
    },
    {
        "method": "fib",
        "n": 3,
        "expected": 2,
        "case_id": 4,
        "description": "Standard case: F(3) = F(2) + F(1) = 1 + 1 = 2"
    },
    {
        "method": "fib",
        "n": 4,
        "expected": 3,
        "case_id": 5,
        "description": "Standard case: F(4) = F(3) + F(2) = 2 + 1 = 3"
    },
    {
        "method": "fib",
        "n": 10,
        "expected": 55,
        "case_id": 6,
        "description": "Standard case: F(10) = 55"
    },
    {
        "method": "fib",
        "n": 30,
        "expected": 832040,
        "case_id": 7,
        "description": "Edge case: maximum constraint value F(30)"
    }
]

run_tests()
