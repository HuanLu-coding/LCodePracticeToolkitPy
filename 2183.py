# 2183. Count Array Pairs Divisible by K

# Given a **0-indexed** integer array `nums` of length `n` and an integer `k`, return *the number of pairs* `(i, j)` such that:
# - `0 <= i < j <= n - 1` and
# - `nums[i] * nums[j]` is divisible by `k`.
#
# ### Constraints:
# - `1 <= nums.length <= 10^5`
# - `1 <= nums[i] <= 10^9`
# - `1 <= k <= 10^9`
#
# ### Example 1:
# ```
# Input: nums = [1,2,3,4], k = 5
# Output: 0
# Explanation: There are no pairs (i, j) that satisfy the conditions since no product of nums[i] * nums[j] is divisible by 5.
# ```
#
# ### Example 2:
# ```
# Input: nums = [1,2,3,4,5], k = 2
# Output: 7
# Explanation: The pairs (i, j) with nums[i] * nums[j] divisible by 2 are:
# (0, 1) -> 1 * 2 = 2
# (0, 3) -> 1 * 4 = 4
# (0, 4) -> 1 * 5 = 5
# (1, 3) -> 2 * 4 = 8
# (1, 4) -> 2 * 5 = 10
# (2, 3) -> 3 * 4 = 12
# (3, 4) -> 4 * 5 = 20
# There are 7 pairs satisfying the conditions.
# ```
#
# ### Example 3:
# ```
# Input: nums = [5,10,15,20], k = 5
# Output: 6
# Explanation: The pairs (i, j) with nums[i] * nums[j] divisible by 5 are:
# (0, 1) -> 5 * 10 = 50
# (0, 2) -> 5 * 15 = 75
# (0, 3) -> 5 * 20 = 100
# (1, 2) -> 10 * 15 = 150
# (1, 3) -> 10 * 20 = 200
# (2, 3) -> 15 * 20 = 300
# All 6 pairs satisfy the conditions.
# ```

from test.test_suite import run_tests
from typing import *
import math
from math import gcd
from collections import defaultdict


# class Solution:
#     def countPairs(self, nums: List[int], k: int) -> int:
#         # 预处理k的所有因数
#         def get_factors(x):
#             factors = set()
#             for i in range(1, int(math.isqrt(x)) + 1):
#                 if x % i == 0:
#                     factors.add(i)
#                     factors.add(x // i)
#             return sorted(factors)
#
#         D = get_factors(k)
#         # 预处理每个因数对应的有效因数列表
#         valid_pairs = defaultdict(list)
#         for d_i in D:
#             for d_j in D:
#                 if (d_i * d_j) % k == 0:
#                     valid_pairs[d_i].append(d_j)
#
#         freq = defaultdict(int)
#         res = 0
#         for num in nums:
#             g = gcd(num, k)
#             # 累加有效因数对应的频率总和
#             res += sum(freq[d_j] for d_j in valid_pairs[g])
#             freq[g] += 1
#         return res

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        res = 0
        for num in nums:
            g = gcd(num, k)
            complement = k // g
            res += freq[complement]
            # Update all divisors of g
            for d in range(1, int(g ** 0.5) + 1):
                if g % d == 0:
                    freq[d] += 1
                    if g // d != d:
                        freq[g // d] += 1
        return res


test_cases = [
    {
        "method": "countPairs",
        "nums": [1, 2, 3, 4],
        "k": 5,
        "expected": 0,
        "case_id": 1,
        "description": "No pairs divisible by k"
    },
    {
        "method": "countPairs",
        "nums": [1, 2, 3, 4, 5],
        "k": 2,
        "expected": 7,
        "case_id": 2,
        "description": "Multiple pairs divisible by k"
    },
    {
        "method": "countPairs",
        "nums": [5, 10, 15, 20],
        "k": 5,
        "expected": 6,
        "case_id": 3,
        "description": "All numbers divisible by k"
    },
    {
        "method": "countPairs",
        "nums": [1],
        "k": 1,
        "expected": 0,
        "case_id": 4,
        "description": "Single element array (minimum length)"
    },
    {
        "method": "countPairs",
        "nums": [1000000000, 1000000000],
        "k": 1000000000,
        "expected": 1,
        "case_id": 5,
        "description": "Maximum value edge case"
    },
    {
        "method": "countPairs",
        "nums": [1, 1, 1, 1],
        "k": 1,
        "expected": 6,
        "case_id": 6,
        "description": "All identical elements divisible by k"
    }
]

run_tests()
