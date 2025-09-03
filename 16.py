# 16. 3Sum Closest
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.
#
# ### Constraints:
# - `3 <= nums.length <= 1000`
# - `-1000 <= nums[i] <= 1000`
# - `-10^4 <= target <= 10^4`
#
# ### Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
# ### Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
import math

from test.test_suite import run_tests
from typing import *


# 总体而言，这是一个相当不错的解法，达到了这道题的最优复杂度。
# 主要改进点在于添加剪枝操作来跳过重复元素, if i < n - 2判断是多余的，因为for循环已经确保了i的范围
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        min_diff = math.inf
        result_sum = 0
        nums.sort()
        # print('nums: ', nums, ' target: ', target)

        for i in range(n):
            if i < n - 2:
                # print('第1个数: ', nums[i])
                l, r = i + 1, n - 1
                while l < r:
                    # print('第2个数: ', nums[l], ', 第3个数: ', nums[r])
                    summary = nums[i] + nums[l] + nums[r]
                    diff = abs(summary - target)
                    if diff < min_diff:
                        min_diff = diff
                        # print('min_diff: ', min_diff)
                        result_sum = summary
                        # print('result_sum: ', result_sum)

                    if summary > target:
                        r -= 1
                    elif summary < target:
                        l += 1
                    else:
                        break

        return result_sum


# import math
#
#
# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         n = len(nums)
#         closest_sum = float('inf')
#
#         for i in range(n - 2):
#             # 跳过重复元素
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#
#             left, right = i + 1, n - 1
#             while left < right:
#                 current_sum = nums[i] + nums[left] + nums[right]
#
#                 # 找到精确匹配，直接返回
#                 if current_sum == target:
#                     return target
#
#                 # 更新最接近的和
#                 if abs(current_sum - target) < abs(closest_sum - target):
#                     closest_sum = current_sum
#
#                 # 调整指针
#                 if current_sum < target:
#                     left += 1
#                     # 跳过重复元素
#                     while left < right and nums[left] == nums[left - 1]:
#                         left += 1
#                 else:
#                     right -= 1
#                     # 跳过重复元素
#                     while left < right and nums[right] == nums[right + 1]:
#                         right -= 1
#
#         return closest_sum

test_cases = [
    {
        "method": "threeSumClosest",
        "nums": [-1, 2, 1, -4],
        "target": 1,
        "expected": 2,
        "case_id": 1,
        "description": "Standard case with mixed positive and negative numbers"
    },
    {
        "method": "threeSumClosest",
        "nums": [0, 0, 0],
        "target": 1,
        "expected": 0,
        "case_id": 2,
        "description": "All zeros array"
    },
    {
        "method": "threeSumClosest",
        "nums": [1, 1, 1, 1],
        "target": 0,
        "expected": 3,
        "case_id": 3,
        "description": "All positive identical numbers"
    },
    {
        "method": "threeSumClosest",
        "nums": [0, 1, 2],
        "target": 3,
        "expected": 3,
        "case_id": 4,
        "description": "Edge case: All negative numbers with negative target"
    },
    {
        "method": "threeSumClosest",
        "nums": [-1000, 1000, 1000],
        "target": 100,
        "expected": 1000,
        "case_id": 5,
        "description": "Edge case: Constraint boundary values"
    },
    {
        "method": "threeSumClosest",
        "nums": [1, 2, 5, 10, 11],
        "target": 12,
        "expected": 13,
        "case_id": 6,
        "description": "Multiple possible combinations, closest is 1+2+10=13"
    }
]

run_tests()
