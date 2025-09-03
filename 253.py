# 253.py
from test.test_suite import run_tests

from typing import List


class Solution:
    # 时间线扫描（Line Sweep）
    # 思路: 将问题转化为时间轴上的增减事件：
    #
    # 对每个会议，在开始时间处标记 +1（房间需求增加），在结束时间处标记 -1（房间需求减少）。
    # 按时间顺序扫描所有事件，累计房间数，记录最大值。
    # def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    #     if not intervals:
    #         return 0
    #         # 创建时间点的事件列表
    #     events = []
    #     for start, end in intervals:
    #         events.append((start, 1))
    #         events.append((end, -1))
    #     # print('events: ', events)
    #     # 按时间开始排序
    #     events.sort()
    #     # print('sorted events: ', events)
    #     rooms = max_rooms = 0
    #     for time, delta in events:
    #         rooms += delta
    #         max_rooms = max(max_rooms, rooms)
    #     return max_rooms
    # 时间线扫描法非常通用，适合处理区间问题。
    # 虽然有趣，但在面试中可能显得过于学术化，除非面试官明确要求这种思路。
    #
    # 排序 + 双指针（Chronological Ordering）
    # 正确性证明: 在任何时刻，我们需要的会议室数量等于已经开始但尚未结束的会议数量。
    # 思路: 将开始时间和结束时间分开处理，利用双指针计算同一时刻的最大重叠数：
    #
    # 提取所有开始时间和结束时间，分别排序。
    # 用两个指针分别遍历开始时间和结束时间：
    #       如果当前开始时间小于当前结束时间，说明一个新会议开始，房间数加 1。
    #       如果当前开始时间大于等于当前结束时间，说明一个会议结束，房间数减 1。
    # 记录过程中的最大房间数。

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:   return 0

        starts = sorted(x[0] for x in intervals)
        ends = sorted(x[1] for x in intervals)
        # 为什么分开排序开始和结束时间？
        # 这是关键, 我们需要单独知道每个会议的开始和结束时间的顺序
        # 如果只排序整个区间，我们将失去跟踪单个事件（开始/结束）的能力
        print('starts: ', starts)
        print('ends: ', ends)
        rooms = max_rooms = 0

        s, e = 0, 0

        # 处理所有会议开始事件
        while s < len(intervals):
            if starts[s] < ends[e]:
                # 一个边界情况：`<`：在时间相等时会选择处理结束事件（else情况），因为如果一个会议结束的同时另一个会议开始，我们应该先处理结束事件。因为我们可以在同一个时间点释放和重用同一个会议室
                rooms += 1
                s += 1
            else:
                # 释放一个会议室
                rooms -= 1
                e += 1
            max_rooms = max(max_rooms, rooms)

        return max_rooms

    # 时间复杂度：
    # 排序开始时间和结束时间：O(n log n)。
    # 双指针遍历：O(n)。
    # 总时间复杂度：O(n log n)。
    # 空间复杂度：O(n)，用于存储开始时间和结束时间的数组。
    # 评价: 这种方法空间复杂度与堆方法相当，但避免了堆操作的额外开销。它本质上是对时间轴上的“事件”进行计数，逻辑清晰。然而，分离开始和结束时间需要额外的内存，且代码稍显冗长。如果输入数据量很大，内存分配可能成为瓶颈。
    # 正确性证明：
    #
    # 假设在任意时刻t，我们已经正确计算了需要的会议室数量
    # 在下一个事件发生时（无论是开始还是结束），我们通过增加或减少会议室数量来更新状态
    # 由于我们按照时间顺序处理事件，所以rooms变量始终代表当前所需的会议室数量
    # max_rooms记录了历史上任何时刻所需的最大会议室数量，这就是我们的答案
    #
    #
    #
    # 严格的数学证明
    # 设A(t)表示时刻t已经开始的会议数量，B(t)表示时刻t已经结束的会议数量。
    # 则时刻t需要的会议室数量R(t) = A(t) - B(t)。
    # 我们的目标是求max{R(t)}，即所有时刻中需要的最大会议室数量。
    # 在算法中：
    #
    # rooms变量就是当前的R(t)
    # 当我们处理一个开始事件时，A(t)增加1，所以rooms += 1
    # 当我们处理一个结束事件时，B(t)增加1，所以rooms -= 1
    # max_rooms记录了max{R(t)}的当前最大值
    #
    # 由于我们按照时间顺序处理所有事件，所以算法正确计算了max{R(t)}。


test_cases = [
    {
        "method": "minMeetingRooms",
        "intervals": [[0, 30], [5, 10], [15, 20]],
        "expected": 2,
        "case_id": 1,
        "description": "Overlapping meetings requiring two rooms"
    }, {
        "method": "minMeetingRooms",
        "intervals": [[7, 10], [2, 4]],
        "expected": 1,
        "case_id": 2,
        "description": "Non-overlapping meetings requiring only one room"
    }, {
        "method": "minMeetingRooms",
        "intervals": [[1, 5], [8, 9], [8, 9]],
        "expected": 2,
        "case_id": 3,
        "description": "Overlapping meetings starting at the same time"
    }, {
        "method": "minMeetingRooms",
        "intervals": [[1, 2], [2, 3], [3, 4]],
        "expected": 1,
        "case_id": 4,
        "description": "Back-to-back meetings requiring only one room"
    }, {
        "method": "minMeetingRooms",
        "intervals": [[0, 1000000], [1, 2], [2, 3], [3, 4]],
        "expected": 2,
        "case_id": 5,
        "description": "One large meeting overlapping with several smaller meetings"
    }, {
        "method": "minMeetingRooms",
        "intervals": [[5, 10], [10, 15], [15, 20], [20, 25]],
        "expected": 1,
        "case_id": 6,
        "description": "Meetings ending when the next one starts, requiring only one room"
    }, {
        "method": "minMeetingRooms",
        "intervals": [[1, 10], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],
        "expected": 2,
        "case_id": 7,
        "description": "One long meeting overlapping with several smaller sequential meetings"
    }
]

run_tests()
