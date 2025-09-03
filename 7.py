# 7.py
# 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside
# the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
# ### Constraints:
# - `-2^31 <= x <= 2^31 - 1`
#
# ### Example 1:
# Input: x = 123
# Output: 321
#
# ### Example 2:
# Input: x = -123
# Output: -321
#
# ### Example 3:
# Input: x = 120
# Output: 21
from test.test_suite import run_tests
from typing import *
from collections import deque


# 为什么 `-123 % 10` 在 Python 中会得到 `7` 这个结果，这确实可能与一些人对取模运算的直觉有所不同，尤其是在涉及到负数时。这是因为不同的编程语言和数学定义在处理负数的取模运算时可能存在差异。
#
# 在 Python 中，取模运算符 `%` 的结果的符号与**除数**的符号保持一致。更精确地说，Python 定义 `a % n` 的结果 `r` 满足以下条件：
#
# 1.  `0 <= abs(r) < abs(n)` （结果的绝对值小于除数的绝对值）
# 2.  `r` 的符号与 `n` 的符号相同，除非 `a` 可以被 `n` 整除（此时 `r` 为 0）。
# 3.  `a = q * n + r`，其中 `q` 是整数商。
#
# 让我们用 `-123 % 10` 这个例子来解释：
#
# * `a = -123` (被除数)
# * `n = 10` (除数)
#
# 我们需要找到一个整数商 `q` 和一个余数 `r`，使得：
#
# `-123 = q * 10 + r`
#
# 并且满足 `0 <= abs(r) < abs(10)`，即 `0 <= abs(r) < 10`。由于除数 `n` 是正数，所以 `r` 的符号也应该是正数（或零）。
#
# 让我们尝试不同的 `q` 值：
#
# * 如果 `q = -12`，那么 `-12 * 10 = -120`，此时 `r = -123 - (-120) = -3`。虽然 `abs(-3) < 10`，但 `r` 的符号与 `n` 的符号不一致。
#
# * 如果 `q = -13`，那么 `-13 * 10 = -130`，此时 `r = -123 - (-130) = 7`。这里 `0 <= abs(7) < 10`，并且 `r` 的符号是正数，与 `n` 的符号一致。
#
# 因此，根据 Python 的定义，`-123 % 10` 的结果是 `7`。
#
# **与直觉的差异：**
#
# 有些人可能更倾向于将取模运算的结果理解为“剩余”的部分，无论被除数是正数还是负数，都希望余数尽可能地“小”或者在某种意义上更“自然”。在某些数学定义或其他的编程语言中，负数的取模运算可能会产生负数结果。例如，一些定义可能会让 `-123 % 10` 的结果是 `-3`。
#
# **总结 Python 的行为：**
#
# Python 的取模运算始终保证余数的符号与除数的符号相同（除非余数为零）。这在某些情况下非常有用，例如在循环索引或者需要将数值限制在特定范围内时。

# My solution:
# class Solution:
#     def reverse(self, x: int) -> int:
#         if x == 0: return x
#         sign = 1 if x > 0 else -1
#         x_copy = abs(x)
#         nums = []
#
#         while x_copy:
#             nums.append(x_copy % 10)
#             x_copy = x_copy // 10
#         reversed_x = 0
#         if nums:
#             n = len(nums)
#             for i in range(n):
#                 reversed_x += nums[i] * pow(10, n - i - 1) # 不必去除前导零
#
#         return sign * reversed_x


# # 最优方案:
class Solution:
    def reverse(self, x: int) -> int:
        reversed_x = 0
        sign = 1 if x > 0 else -1
        x = abs(x)  # 这行代码创建了一个新的整数对象，其值是原始 x 的绝对值，并将函数内部的局部变量 x 指向了这个新的对象。这并不会改变函数外部调用者传递进来的 x 所引用的对象。
        while x > 0:
            digit = x % 10
            if reversed_x > (2 ** 31 - 1) // 10 or (reversed_x == (2 ** 31 - 1) // 10 and digit > 7):
                return 0
            reversed_x = reversed_x * 10 + digit
            x //= 10
        return reversed_x * sign


test_cases = [
    {
        "method": "reverse",
        "x": 123,
        "expected": 321,
        "case_id": 1,
        "description": "Positive integer"
    },
    {
        "method": "reverse",
        "x": -123,
        "expected": -321,
        "case_id": 2,
        "description": "Negative integer"
    },
    {
        "method": "reverse",
        "x": 120,
        "expected": 21,
        "case_id": 3,
        "description": "Positive integer with trailing zeros"
    },
    {
        "method": "reverse",
        "x": 0,
        "expected": 0,
        "case_id": 4,
        "description": "Zero (edge case)"
    },
    {
        "method": "reverse",
        "x": 7080,  # 2^31 - 1 (INT_MAX)
        "expected": 807,
        "case_id": 5,
        "description": "Integer that causes overflow when reversed (edge case)"
    },
    {
        "method": "reverse",
        "x": -70800,  # -2^31 (INT_MIN)
        "expected": -807,
        "case_id": 6,
        "description": "Integer that causes overflow when reversed (edge case)"
    },
    {
        "method": "reverse",
        "x": 1534236469,
        "expected": 9646324351,
        "case_id": 7,
        "description": "Integer that causes overflow when reversed"
    },
    {
        "method": "reverse",
        "x": -1563847412,
        "expected": -2147483651,
        "case_id": 8,
        "description": "Negative integer that causes overflow when reversed"
    }
]

run_tests()
