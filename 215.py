# 215. Kth Largest Element in an Array
# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# ### Constraints:
# - `1 <= k <= nums.length <= 10^4`
# - `-10^4 <= nums[i] <= 10^4`
#
# ### Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
#
# ### Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
from test.test_suite import run_tests
from typing import *
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


test_cases = [
    {
        "method": "findKthLargest",
        "nums": [3, 2, 1, 5, 6, 4],
        "k": 2,
        "expected": 5,
        "case_id": 1,
        "description": "Standard case with unique elements"
    },
    {
        "method": "findKthLargest",
        "nums": [3, 2, 3, 1, 2, 4, 5, 5, 6],
        "k": 4,
        "expected": 4,
        "case_id": 2,
        "description": "Array with duplicate elements"
    },
    {
        "method": "findKthLargest",
        "nums": [1],
        "k": 1,
        "expected": 1,
        "case_id": 3,
        "description": "Edge case: array with single element"
    },
    {
        "method": "findKthLargest",
        "nums": [10, 10, 10, 10, 10],
        "k": 3,
        "expected": 10,
        "case_id": 4,
        "description": "Edge case: array with all identical elements"
    },
    {
        "method": "findKthLargest",
        "nums": [-1, -2, -3, -4, -5],
        "k": 2,
        "expected": -2,
        "case_id": 5,
        "description": "Array with all negative elements"
    },
    {
        "method": "findKthLargest",
        "nums": [5, 4, 3, 2, 1],
        "k": 1,
        "expected": 5,
        "case_id": 6,
        "description": "Edge case: finding the largest element (k=1)"
    },
    {
        "method": "findKthLargest",
        "nums": [1, 2, 3, 4, 5],
        "k": 5,
        "expected": 1,
        "case_id": 7,
        "description": "Edge case: finding the smallest element (k=length)"
    },
    {
        "method": "findKthLargest",
        "nums": [10000, -10000, 0],
        "k": 2,
        "expected": 0,
        "case_id": 8,
        "description": "Array with extreme values within constraints"
    }
]

run_tests()
