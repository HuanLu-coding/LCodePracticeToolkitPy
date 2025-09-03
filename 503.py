# 503. Next Greater Element II
# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
#
# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
#
# ### Constraints:
# - `1 <= nums.length <= 10^4`
# - `-10^9 <= nums[i] <= 10^9`
#
# ### Example 1:
# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number.
# The second 1's next greater number needs to search circularly, which is also 2.
#
# ### Example 2:
# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]
from test.test_suite import run_tests
from typing import *


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        pass


test_cases = [
    {
        "method": "nextGreaterElements",
        "nums": [1, 2, 1],
        "expected": [2, -1, 2],
        "case_id": 1,
        "description": "Basic example with circular search"
    },
    {
        "method": "nextGreaterElements",
        "nums": [1, 2, 3, 4, 3],
        "expected": [2, 3, 4, -1, 4],
        "case_id": 2,
        "description": "Example with both forward and circular lookups"
    },
    {
        "method": "nextGreaterElements",
        "nums": [5, 4, 3, 2, 1],
        "expected": [-1, 5, 5, 5, 5],
        "case_id": 3,
        "description": "Decreasing order array - requires circular search for all but first"
    },
    {
        "method": "nextGreaterElements",
        "nums": [1, 1, 1, 1],
        "expected": [-1, -1, -1, -1],
        "case_id": 4,
        "description": "Edge case: All elements are the same"
    },
    {
        "method": "nextGreaterElements",
        "nums": [1],
        "expected": [-1],
        "case_id": 5,
        "description": "Edge case: Single element array"
    },
    {
        "method": "nextGreaterElements",
        "nums": [100, 1, 11, 1, 120, 111, 123, 1, -1, -100],
        "expected": [120, 11, 120, 120, 123, 123, -1, 100, 100, 100],
        "case_id": 6,
        "description": "Complex case with mix of positive and negative numbers"
    },
    {
        "method": "nextGreaterElements",
        "nums": [-5, -4, -3, -2, -1],
        "expected": [-4, -3, -2, -1, -5],
        "case_id": 7,
        "description": "Edge case: All negative numbers, increasing order"
    }
]

run_tests()
