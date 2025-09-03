# 69.py
from test.test_suite import run_tests


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # 直接处理 x=0 或 x=1

        low, high = 0, x // 2  # 数学依据：√x ≤ x // 2 对所有 x ≥ 2 成立
        while low <= high:
            mid = low + (high - low) // 2
            square = mid * mid
            if square <= x < (mid + 1) * (mid + 1):
                return mid
            elif square < x:
                low = mid + 1
            else:
                high = mid - 1


# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x < 2:
#             return x
#
#         low, high = 1, x
#         while low <= high:
#             mid = (low + high) // 2
#             if mid * mid == x:
#                 return mid
#             elif mid * mid < x:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return high


test_cases = [
    {
        "method": "mySqrt",
        "x": 4,
        "expected": 2,
        "case_id": 1,
        "description": "Perfect square case with x=4"
    },
    {
        "method": "mySqrt",
        "x": 8,
        "expected": 2,
        "case_id": 2,
        "description": "Non-perfect square case with x=8, rounding down"
    }, {
        "method": "mySqrt",
        "x": 0,
        "expected": 0,
        "case_id": 3,
        "description": "Edge case with the smallest non-negative number"
    }, {
        "method": "mySqrt",
        "x": 1,
        "expected": 1,
        "case_id": 4,
        "description": "Edge case with x=1"
    }, {
        "method": "mySqrt",
        "x": 2147395599,
        "expected": 46339,
        "case_id": 5,
        "description": "Edge case with the largest valid input whose sqrt does not overflow"
    }, {
        "method": "mySqrt",
        "x": 2 ** 31 - 1,
        "expected": 46340,
        "case_id": 6,
        "description": "Edge case with the maximum constraint value"
    }
]
run_tests()
