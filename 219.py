# 219. Contains Duplicate II
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
#
# ### Constraints:
# - 1 <= nums.length <= 10^5
# - -10^9 <= nums[i] <= 10^9
# - 0 <= k <= 10^5
#
# ### Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true
#
# ### Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true
#
# ### Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
from test.test_suite import run_tests
from typing import *


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashed = {}
        for idx, num in enumerate(nums):
            # 检查数字是否已在哈希表中 并且 距离是否 <= k
            # 注意：如果 num 不在 hashed 中，num in hashed 为 False，整个条件短路，不会出错
            if num in hashed and idx - hashed[num] <= k:
                return True
            # 无论上面条件是否成立，都更新或设置该数字的最新索引
            hashed[num] = idx

        return False


test_cases = [
    {
        "method": "containsNearbyDuplicate",
        "nums": [1, 2, 3, 1],
        "k": 3,
        "expected": True,
        "case_id": 1,
        "description": "Basic case with duplicate elements within distance k"
    },
    {
        "method": "containsNearbyDuplicate",
        "nums": [1, 0, 1, 1],
        "k": 1,
        "expected": True,
        "case_id": 2,
        "description": "Array with consecutive duplicates"
    },
    {
        "method": "containsNearbyDuplicate",
        "nums": [1, 2, 3, 1, 2, 3],
        "k": 2,
        "expected": False,
        "case_id": 3,
        "description": "Duplicate elements with distance greater than k"
    },
    {
        "method": "containsNearbyDuplicate",
        "nums": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "k": 5,
        "expected": False,
        "case_id": 4,
        "description": "Array with no duplicates"
    },
    {
        "method": "containsNearbyDuplicate",
        "nums": [1, 1],
        "k": 0,
        "expected": False,
        "case_id": 5,
        "description": "Edge case: k=0 meaning only identical adjacent elements count"
    },
    {
        "method": "containsNearbyDuplicate",
        "nums": [1, 1],
        "k": 1,
        "expected": True,
        "case_id": 6,
        "description": "Edge case: k=1 with adjacent duplicates"
    },
    {
        "method": "containsNearbyDuplicate",
        "nums": [99, 99],
        "k": 2,
        "expected": True,
        "case_id": 7,
        "description": "Edge case: k=2 with only two elements that are duplicates"
    },
    {
        "method": "containsNearbyDuplicate",
        "nums": [-1, -1],
        "k": 1,
        "expected": True,
        "case_id": 8,
        "description": "Array with negative duplicate values"
    },
    {
        "method": "containsNearbyDuplicate",
        "nums": [1],
        "k": 1,
        "expected": False,
        "case_id": 9,
        "description": "Edge case: Single element array"
    },
    {
        "method": "containsNearbyDuplicate",
        "nums": [1, 2, 1, 2, 1],
        "k": 3,
        "expected": True,
        "case_id": 10,
        "description": "Array with multiple duplicates at various distances"
    }
]
run_tests()
