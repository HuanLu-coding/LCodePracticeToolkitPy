# 1399. Count Largest Group

# Given an integer n, each number from 1 to n is grouped according to the sum of its digits.
# Return the number of groups that have the largest size.
#
# ### Constraints:
# - 1 <= n <= 10^4
#
# ### Example 1:
# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, grouped according to the sum of digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
# There are 4 groups with the largest size.
#
# ### Example 2:
# Input: n = 2
# Output: 2
# Explanation: There are 2 groups [1], [2] of size 1.

from test.test_suite import run_tests
from typing import *


class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashed = {}
        largest_size = 0
        for i in range(1, n + 1):
            sum_i = self.getSum(i)
            if sum_i not in hashed:
                hashed[sum_i] = [i]
            else:
                hashed[sum_i].append(i)
            largest_size = max(largest_size, len(hashed[sum_i]))
        result = 0
        for grp in hashed.values():
            if len(grp) == largest_size:
                result += 1
        return result

    def getSum(self, n: int) -> int:
        result = 0
        while n:
            result += n % 10
            n = n // 10
        return result


test_cases = [
    {
        "method": "countLargestGroup",
        "n": 13,
        "expected": 4,
        "case_id": 1,
        "description": "Standard case with multiple groups of the largest size"
    },
    {
        "method": "countLargestGroup",
        "n": 2,
        "expected": 2,
        "case_id": 2,
        "description": "Smallest non-trivial input with two groups of size 1"
    },
    {
        "method": "countLargestGroup",
        "n": 1,
        "expected": 1,
        "case_id": 3,
        "description": "Edge case with only one number"
    },
    {
        "method": "countLargestGroup",
        "n": 24,
        "expected": 5,
        "case_id": 4,
        "description": "Multiple groups with the largest size"
    },
    {
        "method": "countLargestGroup",
        "n": 9999,
        "expected": 1,
        "case_id": 5,
        "description": "Large input to test performance and correctness"
    },
    {
        "method": "countLargestGroup",
        "n": 10000,
        "expected": 1,
        "case_id": 6,
        "description": "Maximum allowed input value"
    }
]

run_tests()
