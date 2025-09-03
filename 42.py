# 42.py
from test.test_suite import run_tests

# 42. Trapping Rain Water

# Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

# ### Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rainwater (blue section) are being trapped.

# ### Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

# ### Constraints:
# - `n == height.length`
# - `1 <= n <= 2 * 10^4`
# - `0 <= height[i] <= 10^5`

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        pass


test_cases = [
    {
        "method": "trap",
        "height": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        "expected": 6,
        "case_id": 1,
        "description": "Sample input where multiple elevations trap water"
    },
    {
        "method": "trap",
        "height": [4, 2, 0, 3, 2, 5],
        "expected": 9,
        "case_id": 2,
        "description": "Sample input with higher elevation on both ends"
    },
    {
        "method": "trap",
        "height": [],
        "expected": 0,
        "case_id": 3,
        "description": "Empty array (no bars to trap water)"
    },
    {
        "method": "trap",
        "height": [5],
        "expected": 0,
        "case_id": 4,
        "description": "Single element (no water trapped)"
    },
    {
        "method": "trap",
        "height": [3, 0, 3],
        "expected": 3,
        "case_id": 5,
        "description": "Valley between two high bars"
    },
    {
        "method": "trap",
        "height": [2, 0, 1],
        "expected": 1,
        "case_id": 6,
        "description": "Left side higher than right, traps one unit"
    },
    {
        "method": "trap",
        "height": [2, 2, 2, 2],
        "expected": 0,
        "case_id": 7,
        "description": "All elements same height (no trapping)"
    }
]

run_tests()
