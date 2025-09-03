# 88. Merge Sorted Array

# You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively. Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.
#
# The merged array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.
#
# ### Constraints:
# - `nums1.length == m + n`
# - `nums2.length == n`
# - `0 <= m, n <= 200`
# - `1 <= m + n <= 200`
# - `-10^9 <= nums1[i], nums2[j] <= 10^9`
# - `nums1` and `nums2` are sorted in non-decreasing order.
#
# ### Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays to be merged are [1,2,3] and [2,5,6].
# The result is [1,2,2,3,5,6].
# Note that the output array is nums1 and is colored in purple.
#
# ### Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays to be merged are [1] and [].
# The result is [1].
# Note that the output array is nums1 and is colored in purple.
#
# ### Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays to be merged are [] and [1].
# The result is [1].
# Note that the output array is nums1 and is colored in purple. The initial nums1 array is empty and contains 0.

from test.test_suite import run_tests
from typing import *

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1  # nums1 的有效元素末尾
        j = n - 1  # nums2 的末尾
        k = m + n - 1  # nums1 的总末尾

        # 当 nums1 和 nums2 都有元素时
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # 处理 nums2 剩余元素
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        return nums1


test_cases = [
    {
        "method": "merge",
        "nums1": [1, 2, 3, 0, 0, 0],
        "m": 3,
        "nums2": [2, 5, 6],
        "n": 3,
        "expected": [1, 2, 2, 3, 5, 6],
        "case_id": 1,
        "description": "Example 1: Standard merge case"
    },
    {
        "method": "merge",
        "nums1": [1],
        "m": 1,
        "nums2": [],
        "n": 0,
        "expected": [1],
        "case_id": 2,
        "description": "Edge Case: nums2 is empty"
    },
    {
        "method": "merge",
        "nums1": [0],
        "m": 0,
        "nums2": [1],
        "n": 1,
        "expected": [1],
        "case_id": 3,
        "description": "Edge Case: nums1 is initially empty"
    },
    {
        "method": "merge",
        "nums1": [2, 0],
        "m": 1,
        "nums2": [1],
        "n": 1,
        "expected": [1, 2],
        "case_id": 4,
        "description": "Edge Case: Smallest possible non-trivial merge"
    },
    {
        "method": "merge",
        "nums1": [4, 5, 6, 0, 0, 0],
        "m": 3,
        "nums2": [1, 2, 3],
        "n": 3,
        "expected": [1, 2, 3, 4, 5, 6],
        "case_id": 5,
        "description": "Edge Case: All elements in nums2 are smaller than nums1"
    },
    {
        "method": "merge",
        "nums1": [1, 2, 2, 0, 0],
        "m": 3,
        "nums2": [1, 2],
        "n": 2,
        "expected": [1, 1, 2, 2, 2],
        "case_id": 6,
        "description": "Edge Case: Arrays contain duplicates"
    }
]

run_tests()
