# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.
#
# ### Constraints:
# - `0 <= nums.length <= 10^5`
# - `-10^9 <= nums[i] <= 10^9`
# - `nums` is a non-decreasing array.
# - `-10^9 <= target <= 10^9`
#
# ### Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#
# ### Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#
# ### Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

from test.test_suite import run_tests
from typing import *


# 时间：两次二分查找，O(log n)。
#
# 空间：O(1)，仅用常数空间。
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_boundary(nums: list[int], target: int, find_first: bool) -> int:
            """
            辅助函数，使用修改的二分查找找到左边界或右边界。
                find_first: True 表示查找左边界，False 表示查找右边界。
            Returns:
                找到的边界索引，如果未找到则返回 -1。
            """
            low, high = 0, len(nums) - 1
            best_pos = -1  # 记录最佳可能的位置

            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] == target:
                    best_pos = mid  # 找到了一个 target，记录下来
                    if find_first:
                        # 找左边界：尝试继续向左找
                        high = mid - 1
                    else:
                        # 找右边界：尝试继续向右找
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return best_pos

        left_boundary = find_boundary(nums, target, True)

        # 如果连左边界都找不到，说明 target 不存在
        if left_boundary == -1:
            return [-1, -1]

        right_boundary = find_boundary(nums, target, False)

        # 虽然左边界找到了，但右边界的查找是从头开始的，
        # 这里不需要再次判断 right_boundary == -1，因为如果存在，右边界至少是左边界
        # 但为了逻辑完整性，或者如果 find_boundary 实现不同，可能需要判断

        return [left_boundary, right_boundary]


test_cases = [
    {
        "method": "searchRange",
        "nums": [5, 7, 7, 8, 8, 10],
        "target": 8,
        "expected": [3, 4],
        "case_id": 1,
        "description": "Target appears multiple times in the middle of the array"
    },
    {
        "method": "searchRange",
        "nums": [5, 7, 7, 8, 8, 10],
        "target": 6,
        "expected": [-1, -1],
        "case_id": 2,
        "description": "Target not found in the array"
    },
    {
        "method": "searchRange",
        "nums": [],
        "target": 0,
        "expected": [-1, -1],
        "case_id": 3,
        "description": "Empty array edge case"
    },
    {
        "method": "searchRange",
        "nums": [1],
        "target": 1,
        "expected": [0, 0],
        "case_id": 4,
        "description": "Single element array with matching target"
    },
    {
        "method": "searchRange",
        "nums": [1],
        "target": 2,
        "expected": [-1, -1],
        "case_id": 5,
        "description": "Single element array with non-matching target"
    },
    {
        "method": "searchRange",
        "nums": [1, 1, 1, 1, 1],
        "target": 1,
        "expected": [0, 4],
        "case_id": 6,
        "description": "All elements are the target"
    },
    {
        "method": "searchRange",
        "nums": [1, 2, 3, 4, 5],
        "target": 3,
        "expected": [2, 2],
        "case_id": 7,
        "description": "Target appears exactly once"
    },
    {
        "method": "searchRange",
        "nums": [1, 2, 2, 2, 3, 4],
        "target": 2,
        "expected": [1, 3],
        "case_id": 8,
        "description": "Target appears at the beginning of the array"
    },
    {
        "method": "searchRange",
        "nums": [1, 2, 3, 4, 5, 5],
        "target": 5,
        "expected": [4, 5],
        "case_id": 9,
        "description": "Target appears at the end of the array"
    }
]

run_tests()
