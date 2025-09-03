# 259. 3Sum Smaller
# Given an array of n integers nums and an integer target, find the number of triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
#
# ### Constraints:
# - `n == nums.length`
# - `0 <= n <= 3500`
# - `-100 <= nums[i] <= 100`
# - `-100 <= target <= 100`
#
# ### Example 1:
# Input: nums = [-2,0,1,3], target = 2
# Output: 2
# Explanation: Because there are two triplets which sums are less than 2:
# [-2,0,1]
# [-2,0,3]
#
# ### Example 2:
# Input: nums = [], target = 0
# Output: 0
#
# ### Example 3:
# Input: nums = [0], target = 0
# Output: 0

from test.test_suite import run_tests
from typing import *

from typing import List

from typing import List


#
#
# class Solution:
#     def threeSumSmaller(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         count = 0
#         n = len(nums)
#         for i in range(n - 2):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue  # 跳过重复的 nums[i]
#             left, right = i + 1, n - 1
#             while left < right:
#                 current_sum = nums[i] + nums[left] + nums[right]
#                 if current_sum < target:
#                     count += right - left
#                     # right - left 表示的是 以 nums[left] 作为第二个数时，第三个数 nums[k] 的可选数量（即 k 从 left+1 到 right）。
#                     # 例如： 如果 right - left = 2，则 k 可以是 left+1 和 left+2（共 2 个）。
#                     # 每找到一个满足的 nums[right]，就相当于找到了 right - left 个新的三元组。
#                     left += 1
#                     while left < right and nums[left] == nums[left - 1]:
#                         left += 1  # 跳过重复的 nums[left]
#                 else:
#                     right -= 1
#         return count

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans, n = 0, len(nums)
        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s >= target:
                    k -= 1
                else:
                    ans += k - j
                    j += 1
        return ans


test_cases = [
    {
        "method": "threeSumSmaller",
        "nums": [-2, 0, 1, 3],
        "target": 2,
        "expected": 2,
        "case_id": 1,
        "description": "Basic case with negative and positive integers"
    },
    {
        "method": "threeSumSmaller",
        "nums": [],
        "target": 0,
        "expected": 0,
        "case_id": 2,
        "description": "Empty array edge case"
    },
    {
        "method": "threeSumSmaller",
        "nums": [0],
        "target": 0,
        "expected": 0,
        "case_id": 3,
        "description": "Single element array edge case"
    },
    {
        "method": "threeSumSmaller",
        "nums": [1, 2],
        "target": 5,
        "expected": 0,
        "case_id": 4,
        "description": "Two elements array edge case (not enough for a triplet)"
    },
    {
        "method": "threeSumSmaller",
        "nums": [-1, 0, 1, 2, -1, -4],
        "target": 0,
        "expected": 9,
        "case_id": 5,
        "description": "Multiple possible triplets with duplicates"
    },
    {
        "method": "threeSumSmaller",
        "nums": [3, 1, 0, -2],
        "target": 4,
        "expected": 3,
        "case_id": 6,
        "description": "Unsorted array with all triplets satisfying the condition"
    },
    {
        "method": "threeSumSmaller",
        "nums": [5, 1, 3, 4, 7],
        "target": 12,
        "expected": 4,
        "case_id": 7,
        "description": "Larger numbers with multiple valid triplets"
    },
    {
        "method": "threeSumSmaller",
        "nums": [-5, -4, -3, -2, -1],
        "target": -8,
        "expected": 6,
        "case_id": 8,
        "description": "All negative numbers"
    }
]

run_tests()
