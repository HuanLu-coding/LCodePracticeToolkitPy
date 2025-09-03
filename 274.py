# 274. H-Index

# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
#
# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
#
# ### Constraints:
# - `n == citations.length`
# - `1 <= n <= 5000`
# - `0 <= citations[i] <= 1000`
#
# ### Example 1:
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and they received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
#
# ### Example 2:
# Input: citations = [1,3,1]
# Output: 1
#
from test.test_suite import run_tests
from typing import List

# Note: The constraint 1 <= n <= 5000 means an empty list [] is not a valid input according to the problem statement.
# If an empty list were possible, the h-index would logically be 0.
# 要求计算研究人员的 H 指数。给定一个整数数组 citations，其中 citations[i] 表示某篇论文的引用次数。H 指数定义为：一个研究人员的 H 指数是最大的 h，使得该研究人员至少有 h 篇论文的引用次数大于或等于 h。
#
# 核心要求：
#
# 找到最大的 h，满足至少有 h 篇论文的引用次数 ≥ h。
# 输入数组无序，需处理引用次数的分布。
# 返回整数 h。
# 方法 1：排序
# 将引用次数数组排序（降序），遍历检查第 h 篇论文的引用次数是否 ≥ h。H 指数为最后一个满足条件的 h。
#
#
# 输出：3（有 3 篇论文引用次数 ≥ 3） 关键解释！
#
# Beats 100%
# class Solution:
#     def hIndex(self, citations: list[int]) -> int:
#         citations.sort(reverse=True)  # 降序排序
#         h = 0
#         for i, citation in enumerate(citations):
#             if citation >= i + 1:
#                 h = i + 1
#             else:
#                 break
#         return h


# 执行演示
# 测试用例：citations = [3, 0, 6, 1, 5]
# 步骤：
# 排序：citations = [6, 5, 3, 1, 0]
# h = 0
# 遍历：
# i=0: citation=6, 6 ≥ 1, h=1
# i=1: citation=5, 5 ≥ 2, h=2
# i=2: citation=3, 3 ≥ 3, h=3
# i=3: citation=1, 1 < 4, 跳出
# 返回：h = 3
# 输出：3（有 3 篇论文引用次数 ≥ 3）

# 方法 2：计数排序（桶排序）
# 使用计数数组统计引用次数的频率，累积计算满足条件的论文数量，找到最大 h。由于引用次数可能很大，需限制桶大小。
# 核心思想是：
#
# 统计频次: 我们不关心具体的论文引用数是多少，而是关心有多少篇论文的引用数 至少 是某个值 h。我们可以统计每个引用次数（或某个范围的引用次数）出现了多少次。
# 利用 H 指数的性质: H 指数 h 不会超过论文的总数 n。因为根据定义，你需要有 h 篇论文，每篇至少有 h 次引用。如果 h > n，你不可能有 h 篇论文。因此，任何大于 n 的引用次数，对于计算 H 指数来说，其效果和 n 次引用是等价的（它们都能满足 h <= n 的条件）。
# 计数数组/桶: 我们可以创建一个大小为 n + 1 的数组（或哈希表）counts，其中 counts[i] 用来记录引用次数恰好为 i 的论文有多少篇。特别地，对于引用次数大于或等于 n 的论文，我们都计入 counts[n] 中。
# Runtime 4ms, Beats 16.31%
# class Solution:
#     def hIndex(self, citations: list[int]) -> int:
#         n = len(citations)
#         counts = [0] * (n + 1)  # 桶：引用次数 0 到 n
#         # 如果 h > n，你不可能有 h 篇论文。因此，任何大于 n 的引用次数，对于计算 H 指数来说，其效果和 n 次引用是等价的（它们都能满足 h <= n 的条件）。
#         for c in citations:
#             if c >= n:
#                 counts[n] += 1
#             else:
#                 counts[c] += 1
#
#         total_papers = 0
#         for h in range(n, -1, -1):  # 从 n 遍历到 0
#             total_papers += counts[h]
#             if total_papers >= h:
#                 return h
#
#         return 0

# Beats 100%
# import collections
# from typing import List
#
#
# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         n = len(citations)
#         if n == 0:
#             return 0
#
#         # 1. 使用 Counter 统计精确频次 O(n)
#         raw_counts = collections.Counter(citations)
#
#         # 2. 转换到大小为 n+1 的计数数组 O(k)，k 为不同引用值的数量 (k <= n)
#         counts_array = [0] * (n + 1)
#         for citation_value, paper_count in raw_counts.items():
#             if citation_value >= n:
#                 # 引用次数 >= n 的，都归入 counts_array[n]
#                 counts_array[n] += paper_count
#             else:
#                 counts_array[citation_value] += paper_count
#
#         # 3. 从 n 向下遍历，计算累积数量并查找 H 指数 O(n)
#         total_papers = 0
#         for h in range(n, -1, -1):  # 从 h = n 遍历到 h = 0
#             total_papers += counts_array[h]  # 累加引用次数恰好为 h 的论文数
#             # 此刻 total_papers 代表引用次数 >= h 的论文总数
#             if total_papers >= h:
#                 # 找到第一个满足条件的 h，即为 H 指数
#                 return h
#
#         # 按理说对于非空输入总能找到 h (至少是 0)，加个默认返回值以防万一
#         return 0


test_cases = [
    {
        "method": "hIndex",
        "citations": [3, 0, 6, 1, 5],
        "expected": 3,
        "case_id": 1,
        "description": "Example 1 from LeetCode"
    },
    {
        "method": "hIndex",
        "citations": [1, 3, 1],
        "expected": 1,
        "case_id": 2,
        "description": "Example 2 from LeetCode"
    },
    {
        "method": "hIndex",
        "citations": [0],
        "expected": 0,
        "case_id": 3,
        "description": "Edge Case: Single paper with 0 citations"
    },
    {
        "method": "hIndex",
        "citations": [100],
        "expected": 1,
        "case_id": 4,
        "description": "Edge Case: Single paper with many citations"
    },
    {
        "method": "hIndex",
        "citations": [0, 0, 0, 0],
        "expected": 0,
        "case_id": 5,
        "description": "Edge Case: All papers have 0 citations"
    },
    {
        "method": "hIndex",
        "citations": [1, 1, 1, 1, 1],
        "expected": 1,
        "case_id": 6,
        "description": "Multiple papers, all with 1 citation"
    },
    {
        "method": "hIndex",
        "citations": [5, 5, 5, 5, 5],
        "expected": 5,
        "case_id": 7,
        "description": "All papers have citations equal to the number of papers"
    },
    {
        "method": "hIndex",
        "citations": [10, 8, 5, 4, 3],
        "expected": 4,
        "case_id": 8,
        "description": "Sorted descending order example"
    },
    {
        "method": "hIndex",
        "citations": [11, 15],
        "expected": 2,
        "case_id": 9,
        "description": "Two papers with high citations"
    }

]

run_tests()
