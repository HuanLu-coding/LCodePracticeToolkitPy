# 349. Intersection of Two Arrays

# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique, and you can return the result in any order.
#
# ### Constraints:
# - `1 <= nums1.length, nums2.length <= 1000`
# - `0 <= nums1[i], nums2[i] <= 1000`
#
# ### Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
#
# ### Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4] # or [4,9]

from test.test_suite import run_tests
from typing import *


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        result = set()
        for num in nums2:
            if num in seen:
                result.add(num)
        return sorted(list(result))


# Test cases definition
test_cases = [
    {
        "method": "intersection",
        "nums1": [1, 2, 2, 1],
        "nums2": [2, 2],
        "expected": [2],
        "case_id": 1,
        "description": "Example 1: Basic intersection with duplicates"
    },
    {
        "method": "intersection",
        "nums1": [4, 9, 5],
        "nums2": [9, 4, 9, 8, 4],
        "expected": [4, 9],  # Output order may vary, test should handle e.g. by sorting
        "case_id": 2,
        "description": "Example 2: Intersection with duplicates in second array"
    },
    {
        "method": "intersection",
        "nums1": [1, 2, 3],
        "nums2": [4, 5, 6],
        "expected": [],
        "case_id": 3,
        "description": "Edge Case: No common elements"
    },
    {
        "method": "intersection",
        "nums1": [1, 2, 3],
        "nums2": [],
        "expected": [],
        "case_id": 4,
        "description": "Edge Case: One empty array"
    },
    {
        "method": "intersection",
        "nums1": [],
        "nums2": [],
        "expected": [],
        "case_id": 5,
        "description": "Edge Case: Both arrays empty"
    },
    {
        "method": "intersection",
        "nums1": [5, 6, 7, 5],
        "nums2": [7, 6, 5, 7, 6],
        "expected": [5, 6, 7],  # Output order may vary
        "case_id": 6,
        "description": "All elements intersect with duplicates in both"
    },
    {
        "method": "intersection",
        "nums1": [0, 1000, 500],
        "nums2": [1000, 0, 0],
        "expected": [0, 1000],  # Output order may vary
        "case_id": 7,
        "description": "Intersection with boundary values (0 and 1000)"
    },
    {
        "method": "intersection",
        "nums1": [1, 1, 1, 1],
        "nums2": [1, 1],
        "expected": [1],
        "case_id": 8,
        "description": "Edge Case: Intersection where inputs contain only duplicates"
    }
]

run_tests()
