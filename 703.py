# 703. Kth Largest Element in a Stream
# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Implement KthLargest class:
# - KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# - int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
#
# ### Constraints:
# - `1 <= k <= 10^4`
# - `0 <= nums.length <= 10^4`
# - `-10^4 <= nums[i] <= 10^4`
# - `-10^4 <= val <= 10^4`
# - At most `10^4` calls will be made to add.
# - It is guaranteed that there will be at least k elements in the array when you search for the kth element.
#
# ### Example 1:
# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]
#
# Explanation
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8

from test.test_suite import run_tests
from typing import *


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        pass

    def add(self, val: int) -> int:
        pass


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

test_cases = [
    {
        "method": ["KthLargest", "add", "add", "add", "add", "add"],
        "params": [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
        "expected": [None, 4, 5, 5, 8, 8],
        "case_id": 1,
        "description": "Standard example from problem statement"
    },
    {
        "method": ["KthLargest", "add", "add", "add", "add", "add", "add"],
        "params": [[1, []], [3], [1], [5], [2], [4], [10]],
        "expected": [None, 3, 3, 5, 5, 5, 10],
        "case_id": 2,
        "description": "Edge case: k=1 with initially empty stream"
    },
    {
        "method": ["KthLargest", "add", "add", "add", "add"],
        "params": [[2, [0]], [1], [1], [1], [1]],
        "expected": [None, 0, 1, 1, 1],
        "case_id": 3,
        "description": "Edge case: Multiple identical elements added to stream"
    },
    {
        "method": ["KthLargest", "add", "add", "add", "add", "add"],
        "params": [[3, [-10, -5, -2, 0, 5, 8, 10]], [-7], [15], [-8], [20], [-4]],
        "expected": [None, 5, 8, 8, 10, 10],
        "case_id": 4,
        "description": "Mixed positive and negative numbers"
    },
    {
        "method": ["KthLargest", "add", "add", "add", "add"],
        "params": [[5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [11], [12], [13], [14]],
        "expected": [None, 7, 8, 9, 10],
        "case_id": 5,
        "description": "Edge case: Already sorted array with k in middle"
    },
    {
        "method": ["KthLargest", "add", "add", "add", "add", "add"],
        "params": [[10, [10000, -10000, 5000, -5000, 2000, -2000, 1000]], [8000], [-8000], [9000], [-9000], [10000]],
        "expected": [None, -5000, -2000, -2000, -2000, 1000],
        "case_id": 6,
        "description": "Edge case: Large values near constraints bounds"
    }
]

run_tests()
