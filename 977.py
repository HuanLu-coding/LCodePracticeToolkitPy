# 977. Squares of a Sorted Array

# Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#
# ### Constraints:
# - `1 <= nums.length <= 10^4`
# - `-10^4 <= nums[i] <= 10^4`
# - `nums` is sorted in non-decreasing order.
#
# ### Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
#
# ### Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

from test.test_suite import run_tests
from typing import *
from collections import deque


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = [num * num for num in nums]
        a, b = 0, len(squared) - 1
        results = deque()
        while a <= b:
            if squared[a] >= squared[b]:
                results.appendleft(squared[a])
                a += 1
            else:
                results.appendleft(squared[b])
                b -= 1
        return list(results)


test_cases = [
    {
        "method": "sortedSquares",
        "nums": [-4, -1, 0, 3, 10],
        "expected": [0, 1, 9, 16, 100],
        "case_id": 1,
        "description": "Example 1: Mixed negative, zero, positive numbers"
    },
    {
        "method": "sortedSquares",
        "nums": [-7, -3, 2, 3, 11],
        "expected": [4, 9, 9, 49, 121],
        "case_id": 2,
        "description": "Example 2: Mixed negative, positive numbers"
    },
    {
        "method": "sortedSquares",
        "nums": [0],
        "expected": [0],
        "case_id": 3,
        "description": "Edge Case: Single element - zero"
    },
    {
        "method": "sortedSquares",
        "nums": [-5],
        "expected": [25],
        "case_id": 4,
        "description": "Edge Case: Single element - negative"
    },
    {
        "method": "sortedSquares",
        "nums": [1, 2, 3, 4, 5],
        "expected": [1, 4, 9, 16, 25],
        "case_id": 5,
        "description": "Edge Case: All non-negative numbers"
    },
    {
        "method": "sortedSquares",
        "nums": [-5, -4, -3, -2, -1],
        "expected": [1, 4, 9, 16, 25],
        "case_id": 6,
        "description": "Edge Case: All non-positive numbers"
    }
]

run_tests()
