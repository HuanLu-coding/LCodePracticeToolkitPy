# 169. Majority Element
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
#
# ### Constraints:
# - n == nums.length
# - 1 <= n <= 5 * 10^4
# - -10^9 <= nums[i] <= 10^9
#
# ### Example 1:
# Input: nums = [3,2,3]
# Output: 3
#
# ### Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
# Can you solve the problem in linear time and in O(1) space?
from pprint import pprint

from test.test_suite import run_tests
from typing import *

import collections


class Solution:
    # Boyer-Moore 投票算法
    # def majorityElement(self, nums: List[int]) -> int:
    #     elected = nums[0]
    #     cnt = 1
    #     for i, n in enumerate(nums):
    #         if n == elected:
    #             cnt += 1
    #         else:
    #             cnt -= 1
    #             if cnt == 0:
    #                 elected = n
    #                 cnt = 1
    #     return elected
    #
    # Boyer-Moore 投票算法
    # def majorityElement(self, nums: list[int]) -> int:
    #     candidate = None
    #     count = 0
    #
    #     for num in nums:
    #         if count == 0:
    #             candidate = num
    #             count = 1
    #         elif num == candidate:
    #             count += 1
    #         else:
    #             count -= 1
    #
    #     return candidate

    def majorityElement(self, nums: list[int]) -> int:
        counts = collections.Counter(nums)
        # 或者手动实现：
        # counts = {}
        # for num in nums:
        #     counts[num] = counts.get(num, 0) + 1
        # pprint(counts)
        majority_count = len(nums) // 2
        for num, count in counts.items():
            if count > majority_count:
                return num


test_cases = [
    {
        "method": "majorityElement",
        "nums": [3, 2, 3],
        "expected": 3,
        "case_id": 1,
        "description": "Basic case with majority element appearing exactly n/2 + 1 times"
    },
    {
        "method": "majorityElement",
        "nums": [2, 2, 1, 1, 1, 2, 2],
        "expected": 2,
        "case_id": 2,
        "description": "Majority element appearing more than n/2 times"
    },
    {
        "method": "majorityElement",
        "nums": [1],
        "expected": 1,
        "case_id": 3,
        "description": "Edge case: Array with single element"
    },
    {
        "method": "majorityElement",
        "nums": [1, 1, 1, 1, 1, 1, 2, 2, 2],
        "expected": 1,
        "case_id": 4,
        "description": "Majority element at beginning of array"
    },
    {
        "method": "majorityElement",
        "nums": [0, 100, 1, 100, 2, 100, 3, 100, 4, 100, 5, 100, 6, 100, 7, 100, 8, 100, 9, 100, 10, 100, 11, 100, 12,
                 100, 13, 100, 14, 100, 15, 100, 16, 100, 17, 100, 18, 100, 19, 100, 20, 100, 21, 100, 22, 100, 23, 100,
                 24, 100, 25, 100, 26, 100, 27, 100, 28, 100, 29, 100, 30, 100, 31, 100, 32, 100, 33, 100, 34, 100, 35,
                 100, 36, 100, 37, 100, 38, 100, 39, 100, 40, 100, 41, 100, 42, 100, 43, 100, 44, 100, 45, 100, 46, 100,
                 47, 100, 48, 100, 49, 100, 50, 100, 51, 100, 52, 100, 53, 100, 54, 100, 55, 100, 56, 100, 57, 100, 58,
                 100, 59, 100, 60, 100, 61, 100, 62, 100, 63, 100, 64, 100, 65, 100, 66, 100, 67, 100, 68, 100, 69, 100,
                 70, 100, 71, 100, 72, 100, 73, 100, 74, 100, 75, 100, 76, 100, 77, 100, 78, 100, 79, 100, 80, 100, 81,
                 100, 82, 100, 83, 100, 84, 100, 85, 100, 86, 100, 87, 100, 88, 100, 89, 100, 90, 100, 91, 100, 92, 100,
                 93, 100, 94, 100, 95, 100, 96, 100, 97, 100, 98, 100, 99, 100, 100]
        ,
        "expected": 100,
        "case_id": 5,
        "description": "Array with negative numbers"
    },
    {
        "method": "majorityElement",
        "nums": [1, 2, 1, 2, 1, 2, 1],
        "expected": 1,
        "case_id": 6,
        "description": "Alternating elements with one being majority"
    },
    {
        "method": "majorityElement",
        "nums": ([100] * 101) + list(range(100)),
        "expected": 100,
        "case_id": 7,
        "description": "Edge case: Maximum constraint value"
    }
]

run_tests()
