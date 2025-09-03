# 53. Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
#
# A subarray is a contiguous part of an array.
#
# ### Constraints:
# - 1 <= nums.length <= 10^5
# - -10^4 <= nums[i] <= 10^4
#
# ### Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
# ### Example 2:
# Input: nums = [1]
# Output: 1
#
# ### Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The entire array [5,4,-1,7,8] has the largest sum = 23.
import math

from test.test_suite import run_tests
from typing import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
            卡丹算法 (动态规划):
            一次遍历，动态地更新“以当前元素结尾的最大和”和“全局最大和”。
            这是面试中最期望的答案。
            """
        # 初始化全局最大和 和 当前最大和 为数组的第一个元素。
        # 这是关键，保证了单元素数组和全负数数组的正确性。
        global_max = nums[0]
        current_max = nums[0]

        # 从第二个元素开始遍历
        for i in range(1, len(nums)):
            num = nums[i]
            # 核心决策：对于当前元素 num，
            # 是将它自己作为一个新的开始 (num)，
            # 还是将它加入到之前的子数组中 (current_max + num)？
            # 我们选择能让“以当前元素结尾的和”更大的那个选项。
            current_max = max(num, current_max + num)

            global_max = max(current_max, global_max)

        return global_max


test_cases = [
    {
        "method": "maxSubArray",
        "nums": [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        "expected": 6,
        "case_id": 1,
        "description": "Array with mixed positive and negative numbers"
    },
    {
        "method": "maxSubArray",
        "nums": [1],
        "expected": 1,
        "case_id": 2,
        "description": "Array with a single element"
    },
    {
        "method": "maxSubArray",
        "nums": [5, 4, -1, 7, 8],
        "expected": 23,
        "case_id": 3,
        "description": "Array where the entire array is the maximum subarray"
    },
    {
        "method": "maxSubArray",
        "nums": [-1],
        "expected": -1,
        "case_id": 4,
        "description": "Edge case: Array with a single negative element"
    },
    {
        "method": "maxSubArray",
        "nums": [-2, -1, -3, -4, -1, -2, -1, -5, -4],
        "expected": -1,
        "case_id": 5,
        "description": "Edge case: Array with all negative elements"
    },
    {
        "method": "maxSubArray",
        "nums": [0, 0, 0, 0],
        "expected": 0,
        "case_id": 6,
        "description": "Edge case: Array with all zeros"
    },
    {
        "method": "maxSubArray",
        "nums": [-1, -2, -3, 0, -1, -2],
        "expected": 0,
        "case_id": 7,
        "description": "Array with negative numbers and a zero"
    },
    {
        "method": "maxSubArray",
        "nums": [-2, 1, -3, 4, -1, 2, 1, -5, 4, -10, 100],
        "expected": 100,
        "case_id": 8,
        "description": "Array with a large value at the end"
    },
    {
        "method": "maxSubArray",
        "nums": [-1, -2],
        "expected": -1,
        "case_id": 9,
        "description": "Array with a large value at the end"
    }
]

run_tests()
