#
# 2248. Intersection of Multiple Arrays
#
# Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
#
# Constraints:
# 	•	1 <= nums.length <= 1000
# 	•	1 <= sum(nums[i].length) <= 1000
# 	•	1 <= nums[i][j] <= 1000
# 	•	All the values of nums[i] are unique. ￼
#
# Example 1:
#
# Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
# Output: [3,4]
# Explanation: The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].
#
# Example 2:
#
# Input: nums = [[1,2,3],[4,5,6]]
# Output: []
# Explanation: There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].
#


from test.test_suite import run_tests
from typing import *

from collections import Counter


class Solution:
    # def intersection(self, nums: List[List[int]]) -> List[int]:
    #     freq = Counter()
    #     for arr in nums:
    #         freq.update(set(arr))  # 使用 set 防止重复统计
    #     n = len(nums)
    #     return sorted([num for num, count in freq.items() if count == n])
    #

    def intersection(self, nums: List[List[int]]) -> List[int]:
        result = set(nums[0])
        for arr in nums[1:]:
            result &= set(arr)
        return sorted(result)


test_cases = [
    {
        "method": "intersection",
        "nums": [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]],
        "expected": [3, 4],
        "case_id": 1,
        "description": "Common elements are 3 and 4"
    },
    {
        "method": "intersection",
        "nums": [[1, 2, 3], [4, 5, 6]],
        "expected": [],
        "case_id": 2,
        "description": "No common elements"
    },
    {
        "method": "intersection",
        "nums": [[1, 2, 3]],
        "expected": [1, 2, 3],
        "case_id": 3,
        "description": "Single array, return sorted elements"
    },
    {
        "method": "intersection",
        "nums": [[1, 2, 3], [2, 3, 4], [3, 4, 5]],
        "expected": [3],
        "case_id": 4,
        "description": "Only 3 is common in all arrays"
    },
    {
        "method": "intersection",
        "nums": [[1, 2], [2, 3], [2, 4]],
        "expected": [2],
        "case_id": 5,
        "description": "2 is the only common element"
    },
    {
        "method": "intersection",
        "nums": [[1], [1], [1]],
        "expected": [1],
        "case_id": 6,
        "description": "All arrays have the same single element"
    }
]

run_tests()
