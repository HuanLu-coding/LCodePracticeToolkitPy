# 496. Next Greater Element I
# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
#
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
#
# For each 0-indexed integer i in nums1, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
#
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
#
# ### Constraints:
# - 1 <= nums1.length <= nums2.length <= 1000
# - 0 <= nums1[i], nums2[i] <= 10^4
# - All integers in nums1 and nums2 are unique.
# - All the integers of nums1 also appear in nums2.
#
# ### Example 1:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation:
# For number 4 in nums1, you cannot find the next greater element, so output -1.
# For number 1 in nums1, the next greater element is 3.
# For number 2 in nums1, you cannot find the next greater element, so output -1.
#
# ### Example 2:
# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation:
# For number 2 in nums1, the next greater element is 3.
# For number 4 in nums1, you cannot find the next greater element, so output -1.

from test.test_suite import run_tests
from typing import *


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # print([nums2.index(n1) for n1 in nums1])
        print('nextGreaterElement()')
        results = []
        for n1 in nums1:
            n1_idx_nums2 = nums2.index(n1)
            print(list(range(n1_idx_nums2 + 1, len(nums2))))
            for j in range(n1_idx_nums2, len(nums2)):
                if nums2[j] > n1:
                    results.append(nums2[j])
                    break
                elif j == len(nums2) - 1:
                    results.append(-1)
                else:
                    continue
        return results


test_cases = [
    {
        "method": "nextGreaterElement",
        "nums1": [4, 1, 2],
        "nums2": [1, 3, 4, 2],
        "expected": [-1, 3, -1],
        "case_id": 1,
        "description": "Standard case with mixed results"
    },
    {
        "method": "nextGreaterElement",
        "nums1": [2, 4],
        "nums2": [1, 2, 3, 4],
        "expected": [3, -1],
        "case_id": 2,
        "description": "Standard case with one element having no greater element"
    },
    {
        "method": "nextGreaterElement",
        "nums1": [1, 3, 5, 2, 4],
        "nums2": [6, 5, 4, 3, 2, 1, 7],
        "expected": [7, 7, 7, 7, 7],
        "case_id": 3,
        "description": "All elements have the same next greater element"
    },
    {
        "method": "nextGreaterElement",
        "nums1": [1],
        "nums2": [1],
        "expected": [-1],
        "case_id": 4,
        "description": "Edge case: Single element arrays with no greater element"
    },
    {
        "method": "nextGreaterElement",
        "nums1": [5, 4, 3, 2, 1],
        "nums2": [5, 4, 3, 2, 1],
        "expected": [-1, -1, -1, -1, -1],
        "case_id": 5,
        "description": "Edge case: Descending arrays with no greater elements"
    },
    {
        "method": "nextGreaterElement",
        "nums1": [1, 2, 3, 4, 5],
        "nums2": [1, 2, 3, 4, 5],
        "expected": [2, 3, 4, 5, -1],
        "case_id": 6,
        "description": "Edge case: Ascending arrays"
    },
    {
        "method": "nextGreaterElement",
        "nums1": [10],
        "nums2": [5, 3, 2, 10, 7, 8],
        "expected": [-1],
        "case_id": 7,
        "description": "Last element in nums1 is the largest in nums2"
    }
]

run_tests()
