# 202. Happy Number
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
# - Starting with any positive integer, replace the number by the sum of the squares of its digits.
# - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# - Those numbers for which this process ends in 1 are happy.
#
# Return true if n is a happy number, and false if not.
#
# ### Constraints:
# - 1 <= n <= 2^31 - 1
#
# ### Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
# ### Example 2:
# Input: n = 2
# Output: false
# Explanation:
# 2^2 = 4
# 4^2 = 16
# 1^2 + 6^2 = 37
# 3^2 + 7^2 = 58
# 5^2 + 8^2 = 89
# 8^2 + 9^2 = 145
# 1^2 + 4^2 + 5^2 = 42
# 4^2 + 2^2 = 20
# 2^2 + 0^2 = 4
# And the process repeats in a cycle.
import math

from test.test_suite import run_tests
from typing import *


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.getNext(n)

        return n == 1

    def getNext(self, n: int) -> int:
        digit_square_sum = 0
        while n:
            (n, rem) = divmod(n, 10)
            digit_square_sum += math.pow(rem,
                                         2)  # 对于各位数字的平方和这种肯定会得到整数结果的计算，直接使用整数乘法 rem * rem 或者幂运算符 rem ** 2 会更符合语义，并且避免了潜在的浮点数精度问题（虽然在这个特定问题中不太可能出现精度问题，因为涉及的数字较小）。
        return digit_square_sum


test_cases = [
    {
        "method": "isHappy",
        "n": 19,
        "expected": True,
        "case_id": 1,
        "description": "Example 1: Happy number that reaches 1"
    },
    {
        "method": "isHappy",
        "n": 2,
        "expected": False,
        "case_id": 2,
        "description": "Example 2: Number that enters a cycle and never reaches 1"
    },
    {
        "method": "isHappy",
        "n": 1,
        "expected": True,
        "case_id": 3,
        "description": "Edge case: n = 1 is already happy"
    },
    {
        "method": "isHappy",
        "n": 7,
        "expected": True,
        "case_id": 4,
        "description": "Another happy number"
    },
    {
        "method": "isHappy",
        "n": 4,
        "expected": False,
        "case_id": 5,
        "description": "Number that quickly enters a cycle"
    },
    {
        "method": "isHappy",
        "n": 2147483647,
        "expected": False,
        "case_id": 6,
        "description": "Edge case: Maximum input value (2^31 - 1)"
    },
    {
        "method": "isHappy",
        "n": 13,
        "expected": True,
        "case_id": 7,
        "description": "Multi-digit number that is happy"
    }
]

run_tests()
