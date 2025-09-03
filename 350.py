# 350. Intersection of Two Arrays II

# Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays, and you may return the result in any order.

# ### Constraints:
# - `1 <= nums1.length, nums2.length <= 1000`
# - `0 <= nums1[i], nums2[i] <= 1000`

# ### Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# ### Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

from test.test_suite import run_tests
from typing import *
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        result = []

        for num in nums2:
            # print(count1[1e9]) # Counter 的默认行为是不存在则返回 0，所以 count1[num] > 0 就足够了。
            if count1[num] > 0:
                result.append(num)
                count1[num] -= 1

        return sorted(result)


test_cases = [
    {
        "method": "intersect",
        "nums1": [1, 2, 2, 1],
        "nums2": [2, 2],
        "expected": [2, 2],
        "case_id": 1,
        "description": "Basic intersection with duplicates"
    },
    {
        "method": "intersect",
        "nums1": [4, 9, 5],
        "nums2": [9, 4, 9, 8, 4],
        "expected": [4, 9],  # Or [9, 4], order doesn't matter
        "case_id": 2,
        "description": "Intersection with different frequencies and order"
    },
    {
        "method": "intersect",
        "nums1": [1, 2, 3, 4],
        "nums2": [5, 6, 7, 8],
        "expected": [],
        "case_id": 3,
        "description": "No intersection"
    },
    {
        "method": "intersect",
        "nums1": [],
        "nums2": [1, 2, 3],
        "expected": [],
        "case_id": 4,
        "description": "First array is empty (edge case)"
    },
    {
        "method": "intersect",
        "nums1": [1, 1, 1, 1],
        "nums2": [1, 1],
        "expected": [1, 1],
        "case_id": 5,
        "description": "One array is a subset with fewer duplicates"
    },
    {
        "method": "intersect",
        "nums1": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "nums2": [5, 7, 10],
        "expected": [5, 7, 10],  # Order may vary
        "case_id": 6,
        "description": "Second array is a subset of the first"
    },
    {
        "method": "intersect",
        "nums1": [2, 2],
        "nums2": [1, 2, 2, 1],
        "expected": [2, 2],
        "case_id": 7,
        "description": "Order of input arrays reversed from Example 1"
    },
    {
        "method": "intersect",
        "nums1": [1, 1, 2, 2],
        "nums2": [2],
        "expected": [2],
        "case_id": 8,
        "description": "One array has multiple duplicates, other has only one"
    }
]

run_tests()
