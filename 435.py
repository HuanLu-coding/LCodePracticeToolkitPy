# 435.py
from test.test_suite import run_tests

# 方法一：贪心算法
# 贪心算法的核心是“局部最优解推导全局最优解”。这里按区间结束时间排序，选择结束最早的区间，逻辑是尽量为后续区间留出更多空间。这种策略直观且高效，但前提是问题性质支持贪心选择（即局部最优能保证全局最优）。对于无重叠区间问题，这种贪心策略是正确的，因为：
#
#     如果两个区间重叠，移除结束时间较晚的那个总是更优（它与更多后续区间可能冲突）。
#     排序后，线性扫描即可完成选择，算法简洁。
# 步骤
# 	1.	排序：将所有区间按结束时间从小到大排序。
# 	2.	初始化：设定变量 count = 0（记录需要移除的区间数）和 pre_end 为排序后第一个区间的结束时间。
# 	3.	遍历：从第二个区间开始，若当前区间的起点小于 pre_end，说明与前一个区间重叠，此时将 count 加 1（移除当前区间）；否则更新 pre_end 为当前区间的结束时间。
# 	4.	返回：最终 count 的值即为需要移除的区间数。
#

# 这里有一个重要的见解：对于LeetCode #435这个问题，按区间结束时间排序后的贪心算法总是能得到最优解。这是因为：
#
# 当我们按区间结束时间排序后，如果不选择第一个区间（结束时间最早的区间），那么任何替代方案都不会比选择它更优。
# 对于剩余区间，我们总是应该贪心地选择下一个不重叠且结束时间最早的区间。
#
# 所以，算法中隐含了"保留第一个区间"的逻辑并不是武断的假设，而是基于贪心策略的最优选择。
#       时间复杂度优秀：O(n log n)由排序主导，遍历仅O(n)，总体清晰且高效。
#       空间复杂度低：只需O(1)额外空间（不计排序所需空间）。
#
#   参考时间更新策略：关键点在prev_end = min(prev_end, intervals[i][1])这一行。当发现重叠时：
#
# 如果当前区间结束时间更早，则更新参考时间为当前区间的结束时间
# 否则保持原参考时间不变
#
#
#
# 这体现了贪心的核心思想：在处理重叠时，总是尽量保留结束时间更早的区间，无论它是已保留的还是当前遍历到的。
#     证明： 为何“按结束时间排序+选择最早结束”能保证最优解。虽然这是经典结论，反证法说明，若不选最早结束的区间，总能构造更优解。
#     明确边界：空数组返回0，单区间返回0。

# 伪代码：
# sort(intervals by end time)
# count = 0
# pre_end = intervals[0].end
# for i = 1 to n-1:
#     if intervals[i].start < pre_end:
#         count += 1
#     else:
#         pre_end = intervals[i].end
# return count


from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:  return 0

        # 按区间结束时间排序
        intervals.sort(key=lambda x: x[1])

        count = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:  # 重叠
                count += 1  # 移除当前区间
                prev_end = min(prev_end, intervals[i][1])
            else:  # 不重叠
                prev_end = intervals[i][1]  # 更新结束时间

        return count


test_cases = [
    {
        "method": "eraseOverlapIntervals",
        "intervals": [[1, 2], [2, 3], [3, 4], [1, 3]],
        "expected": 1,
        "case_id": 1,
        "description": "Standard case where removing one interval makes others non-overlapping"
    }, {
        "method": "eraseOverlapIntervals",
        "intervals": [[1, 2], [1, 2], [1, 2]],
        "expected": 2,
        "case_id": 2,
        "description": "All intervals are the same, must remove all but one"
    }, {
        "method": "eraseOverlapIntervals",
        "intervals": [[1, 2], [2, 3]],
        "expected": 0,
        "case_id": 3,
        "description": "Already non-overlapping, no need to remove any interval"
    }, {
        "method": "eraseOverlapIntervals",
        "intervals": [[-50, -49], [1, 2], [2, 3], [3, 4], [5, 6], [7, 8], [9, 10]],
        "expected": 0,
        "case_id": 4,
        "description": "All intervals are non-overlapping, no need to remove any interval"
    }, {
        "method": "eraseOverlapIntervals",
        "intervals": [[1, 10], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],
        "expected": 1,
        "case_id": 5,
        "description": "One large interval overlapping all others, removing it solves the problem"
    }, {
        "method": "eraseOverlapIntervals",
        "intervals": [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]],
        "expected": 4,
        "case_id": 6,
        "description": "Multiple intervals overlapping each other, needs optimal removal"
    }
]
run_tests()
