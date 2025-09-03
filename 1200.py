# 1200. Minimum Absolute Difference
# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
#
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows:
# - a, b are from arr
# - a < b
# - b - a equals to the minimum absolute difference of any two elements in arr
#
# ### Constraints:
# - 2 <= arr.length <= 10^5
# - -10^6 <= arr[i] <= 10^6
#
# ### Example 1:
# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
#
# ### Example 2:
# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]
# Explanation: The minimum absolute difference is 2. List all pairs with difference equal to 2 in ascending order.
#
# ### Example 3:
# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]
# Explanation: The minimum absolute difference is 4. List all pairs with difference equal to 4 in ascending order.

from test.test_suite import run_tests
from typing import *
import math


# >>> math.inf == float('inf')
# True
# 单次遍历法
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = math.inf
        result = []

        for i in range(1, len(arr)):
            curr_diff = arr[i] - arr[i - 1]

            # 发现更小的差值，清空结果并更新最小差值
            if curr_diff < min_diff:
                min_diff = curr_diff
                result = [[arr[i - 1], arr[i]]]
            # 相同的最小差值，添加到结果中
            elif curr_diff == min_diff:
                result.append([arr[i - 1], arr[i]])

        return result


test_cases = [
    {
        "method": "minimumAbsDifference",
        "arr": [4, 2, 1, 3],
        "expected": [[1, 2], [2, 3], [3, 4]],
        "case_id": 1,
        "description": "Array with consecutive integers in random order"
    },
    {
        "method": "minimumAbsDifference",
        "arr": [1, 3, 6, 10, 15],
        "expected": [[1, 3]],
        "case_id": 2,
        "description": "Array with increasing elements and single minimum diff pair"
    },
    {
        "method": "minimumAbsDifference",
        "arr": [3, 8, -10, 23, 19, -4, -14, 27],
        "expected": [[-14, -10], [19, 23], [23, 27]],
        "case_id": 3,
        "description": "Array with positive and negative integers"
    },
    {
        "method": "minimumAbsDifference",
        "arr": [-100000, 100000],
        "expected": [[-100000, 100000]],
        "case_id": 4,
        "description": "Edge case: array with only two elements (extreme values)"
    },
    {
        "method": "minimumAbsDifference",
        "arr": [1000000, -1000000],
        "expected": [[-1000000, 1000000]],
        "case_id": 5,
        "description": "Edge case: array with minimum and maximum possible values"
    },
    {
        "method": "minimumAbsDifference",
        "arr": [1, 1000000],
        "expected": [[1, 1000000]],
        "case_id": 6,
        "description": "Array with large difference between elements"
    }
]

run_tests()
