# 84. Largest Rectangle in Histogram

# Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
#
# ### Constraints:
# - `1 <= heights.length <= 10^5`
# - `0 <= heights[i] <= 10^4`
#
# ### Example 1:
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The largest rectangle is shown in the shaded area, which has an area = 10 units.
#
# ### Example 2:
# Input: heights = [2,4]
# Output: 4

from test.test_suite import run_tests
from typing import *


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pass


test_cases = [
    {
        "method": "largestRectangleArea",
        "heights": [2, 1, 5, 6, 2, 3],
        "expected": 10,
        "case_id": 1,
        "description": "Standard case with mixed heights"
    },
    {
        "method": "largestRectangleArea",
        "heights": [2, 4],
        "expected": 4,
        "case_id": 2,
        "description": "Two bars with increasing height"
    },
    {
        "method": "largestRectangleArea",
        "heights": [2, 1, 2],
        "expected": 3,
        "case_id": 3,
        "description": "Valley in the middle"
    },
    {
        "method": "largestRectangleArea",
        "heights": [1, 1, 1, 1],
        "expected": 4,
        "case_id": 4,
        "description": "All bars of equal height"
    },
    {
        "method": "largestRectangleArea",
        "heights": [0, 0, 0],
        "expected": 0,
        "case_id": 5,
        "description": "All bars of zero height (edge case)"
    },
    {
        "method": "largestRectangleArea",
        "heights": [10000] * 100000,
        "expected": 1000000000,
        "case_id": 6,
        "description": "Maximum input size with maximum heights (edge case)"
    }
]

run_tests()