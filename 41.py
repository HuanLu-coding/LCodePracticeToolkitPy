# 41. First Missing Positive
# Given an unsorted integer array nums, return the smallest missing positive integer.
#
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
#
# ### Constraints:
# - `1 <= nums.length <= 10^5`
# - `-2^31 <= nums[i] <= 2^31 - 1`
#
# ### Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
#
# ### Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
#
# ### Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
from test.test_suite import run_tests
from typing import *
from collections import Counter


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set(nums)

        for i in range(1, n + 2):
            if i not in seen:
                return i


# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         cnt = Counter(nums)
#         print(cnt)
#         # print('1 in cnt: ', 1 in cnt)
#         max_num = max(nums)
#         print('max_num: ', max_num)
#         min_num = min(nums)
#         print('min_num: ', min_num)
#         missing = min_num
#         start = min_num
#         if min_num <= 0:
#             start = 1
#
#         while start in cnt:
#             start += 1
#         else:
#             missing = start
#         if missing > 1 and 1 not in cnt:
#             missing = 1
#         print('missing: ', missing)
#         return missing


test_cases = [
    {
        "method": "firstMissingPositive",
        "nums": [1, 2, 0],
        "expected": 3,
        "case_id": 1,
        "description": "Sequential positive numbers with zero"
    },
    {
        "method": "firstMissingPositive",
        "nums": [3, 4, -1, 1],
        "expected": 2,
        "case_id": 2,
        "description": "Mix of positive and negative numbers with gap"
    },
    {
        "method": "firstMissingPositive",
        "nums": [7, 8, 9, 11, 12],
        "expected": 1,
        "case_id": 3,
        "description": "All positive numbers starting above 1"
    },
    {
        "method": "firstMissingPositive",
        "nums": [1],
        "expected": 2,
        "case_id": 4,
        "description": "Edge case: Single element array with 1"
    },
    {
        "method": "firstMissingPositive",
        "nums": [2],
        "expected": 1,
        "case_id": 5,
        "description": "Edge case: Single element array without 1"
    },
    {
        "method": "firstMissingPositive",
        "nums": [-5, -4, -3, -2, -1],
        "expected": 1,
        "case_id": 6,
        "description": "Edge case: All negative numbers"
    },
    {
        "method": "firstMissingPositive",
        "nums": [1, 1, 1, 1, 1],
        "expected": 2,
        "case_id": 7,
        "description": "Edge case: Repeated positive numbers"
    },
    {
        "method": "firstMissingPositive",
        "nums": [1, 2, 3, 4, 5],
        "expected": 6,
        "case_id": 8,
        "description": "Complete sequence from 1 to n"
    },
    {
        "method": "firstMissingPositive",
        "nums": [2147483647],
        "expected": 1,
        "case_id": 9,
        "description": "Edge case: Maximum 32-bit integer"
    }
]

run_tests()
