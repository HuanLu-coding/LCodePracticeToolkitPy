# 697. Degree of an Array

# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
#
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
#
# ### Constraints:
# - nums.length will be between 1 and 50,000.
# - nums[i] will be an integer between 0 and 49,999.
#
# ### Example 1:
# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
#
# ### Example 2:
# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation:
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

from test.test_suite import run_tests
from typing import List  # 加上类型提示


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # 使用一个字典存储每个数字的信息: { 'first': 第一次出现索引, 'count': 频率, 'last': 最后一次出现索引 }
        num_info = {}

        # 第一次遍历：记录首次出现、频率和最后一次出现的位置
        for idx, num in enumerate(nums):
            if num not in num_info:  # 使用 not in 稍微明确一些
                num_info[num] = {
                    'first': idx,
                    'count': 1,
                    'last': idx  # 第一次出现时，最后一次出现位置就是当前位置
                }
            else:
                # 如果已经存在，更新频率和最后一次出现的位置
                num_info[num]['count'] += 1
                num_info[num]['last'] = idx

                # 找到数组的度（最大频率）
        degree = 0
        # num_info 非空因为根据约束 len >= 1
        degree = max(info['count'] for info in num_info.values())

        # 初始化最短子数组长度为数组总长度
        min_length = len(nums)

        # 遍历 num_info 字典，找到所有度为 degree 的数字
        for num, info in num_info.items():
            if info['count'] == degree:
                # 计算包含该数字的子数组长度（从第一次到最后一次出现）
                current_length = info['last'] - info['first'] + 1
                # 更新最短长度
                min_length = min(min_length, current_length)

        return min_length


test_cases = [
    {
        "method": "findShortestSubArray",
        "nums": [1, 2, 2, 3, 1],
        "expected": 2,
        "case_id": 1,
        "description": "Multiple elements have same max frequency"
    },
    {
        "method": "findShortestSubArray",
        "nums": [1, 2, 2, 3, 1, 4, 2],
        "expected": 6,
        "case_id": 2,
        "description": "Element with max frequency spans large portion of array"
    },
    {
        "method": "findShortestSubArray",
        "nums": [1, 1, 2, 2, 2, 1],
        "expected": 3,
        "case_id": 3,
        "description": "Multiple elements have same max frequency, but different spans"
    },
    {
        "method": "findShortestSubArray",
        "nums": [1, 2, 3, 4, 5],
        "expected": 1,
        "case_id": 4,
        "description": "Edge case: All elements appear only once"
    },
    {
        "method": "findShortestSubArray",
        "nums": [1],
        "expected": 1,
        "case_id": 5,
        "description": "Edge case: Single element array"
    },
    {
        "method": "findShortestSubArray",
        "nums": [2, 2, 2, 2, 2],
        "expected": 5,
        "case_id": 6,
        "description": "Edge case: All elements are the same"
    },
    {
        "method": "findShortestSubArray",
        "nums": [1, 2, 3, 1, 2, 3, 2],
        "expected": 6,
        "case_id": 7,
        "description": "Element with highest frequency occurs in middle of array"
    }
]

run_tests()
