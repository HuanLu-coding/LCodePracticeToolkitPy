# 1046. Last Stone Weight
# We have a collection of stones, each stone has a positive integer weight.
#
# Each turn, we choose the two heaviest stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:
#
# - If x == y, both stones are totally destroyed;
# - If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
#
# At the end, there is at most 1 stone left. Return the weight of this stone (or 0 if there are no stones left).
#
# ### Constraints:
# - 1 <= stones.length <= 30
# - 1 <= stones[i] <= 1000
#
# ### Example 1:
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

from test.test_suite import run_tests
from typing import *
from collections import deque
import bisect
import heapq


# 暴力法，每次放回delta后，二分查找插入
# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         stones.sort()
#
#         while len(stones) > 1:
#             y = stones.pop()  # 最大石头
#             x = stones.pop()  # 次大石头
#
#             if x != y:
#                 bisect.insort(stones, y - x)
#
#         return stones[0] if stones else 0

# O(N log N)
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)  # 堆化是返回 None 的原地操作

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if first > second:
                heapq.heappush(stones, -(first - second))

        return -stones[0] if stones else 0


# ┌────────────┐         ┌────────────┐
# │ 最小堆操作  │         │  最大堆操作  │
# ├────────────┤         ├────────────┤
# │  原始数据   │  取反   │  取反数据    │
# │    [3,1,2] │  ====>  │  [-3,-1,-2] │
# └────────────┘         └────────────┘
#        │                      │
#        │                      │ heapify
#        │                      ▼
#        │               ┌────────────┐
#        │               │ 堆化后数据  │
#        │               │ [-3,-1,-2] │
#        │               └────────────┘
#        │                      │
#        │                      │ heappop
#        │                      ▼
#        │               ┌────────────┐
#        │               │  取出最小值  │
#        │               │    -3      │
#        │               └────────────┘
#        │                      │
#        │                      │ 取反
#        ▼                      ▼
# ┌────────────┐         ┌────────────┐
# │  实际操作   │         │  实际结果   │
# │  最小值     │         │   最大值    │
# │    1       │         │     3      │
# └────────────┘         └────────────┘
test_cases = [
    {
        "method": "lastStoneWeight",
        "stones": [2, 7, 4, 1, 8, 1],
        "expected": 1,
        "case_id": 1,
        "description": "Example from problem statement"
    },
    {
        "method": "lastStoneWeight",
        "stones": [1],
        "expected": 1,
        "case_id": 2,
        "description": "Edge case: single stone"
    },
    {
        "method": "lastStoneWeight",
        "stones": [2, 2],
        "expected": 0,
        "case_id": 3,
        "description": "Edge case: two equal stones that destroy each other"
    },
    {
        "method": "lastStoneWeight",
        "stones": [3, 7, 2],
        "expected": 2,
        "case_id": 4,
        "description": "Small example with 3 stones"
    },
    {
        "method": "lastStoneWeight",
        "stones": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        "expected": 0,
        "case_id": 5,
        "description": "Edge case: multiple equal stones"
    },
    {
        "method": "lastStoneWeight",
        "stones": [1, 1, 1, 1, 1, 1, 1, 1, 2],
        "expected": 0,
        "case_id": 6,
        "description": "Multiple 1s with a single 2"
    },
    {
        "method": "lastStoneWeight",
        "stones": [1000, 1000, 1, 1, 1, 1],
        "expected": 0,
        "case_id": 7,
        "description": "Edge case: maximum allowed stone weights"
    }
]

run_tests()
