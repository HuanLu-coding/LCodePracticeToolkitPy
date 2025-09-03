# 392.py
from test.test_suite import run_tests

# 392. Is Subsequence

# Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).
#
# Constraints:
# - 0 <= s.length <= 100
# - 0 <= t.length <= 10^4
# - `s` and `t` consist only of lowercase English letters.
#
# **Follow up:** If there are lots of incoming `s`, say s1, s2, ..., sk where k >= 10^9, and you want to check one by one to see if `t` has its subsequence. In this scenario, how would you change your code?

# ## 问题评估
#
# ### 1. 问题陈述分析
# LeetCode #392 “Is Subsequence” 的 follow-up 要求处理大量传入的字符串 `s`（如 `s1, s2, ..., sk`，其中 `k >= 10^9`），逐一检查它们是否是固定字符串 `t` 的子序列。子序列是从原字符串中删除一些字符（或不删除）而不改变其余字符相对顺序所形成的新字符串。
#
# - **输入**：
#   - 固定字符串 `t`，由小写英文字母组成。
#   - 大量查询字符串 `s`，逐一传入。
# - **输出**：布尔值，`True` 表示 `s` 是 `t` 的子序列，`False` 则不是。
# - **限制**：
#   - `0 <= len(s) <= 100`
#   - `0 <= len(t) <= 10^4`
#   - `s` 和 `t` 仅由小写英文字母组成。
#
# ### 2. 边缘情况和约束
# - **边缘情况**：
#   - `s` 为空字符串：应返回 `True`（空字符串是任何字符串的子序列）。
#   - `t` 为空字符串：仅当 `s` 也为空时返回 `True`。
#   - `s` 长度大于 `t`：直接返回 `False`。
#   - `s` 中的字符在 `t` 中未按顺序出现：返回 `False`。
# - **约束**：由于 `s` 查询次数极多（`k >= 10^9`），需要优化查询效率，单次查询应尽量接近 O(len(s))。
#
# ### 3. 思维和优化过程
# - **直觉**：基本双指针法每次查询需遍历 `t`，时间复杂度 O(len(t))，对大量查询效率低下。
# - **优化思路**：预处理 `t`，记录每个字符的出现位置，利用二分查找快速定位字符匹配位置。
# - **分析**：通过哈希表存储 `t` 中字符的位置列表，查询时按顺序检查 `s` 的字符是否能在 `t` 中找到递增的位置。
#
# ### 4. 解决方案提议
# - **解法**：预处理 `t` 建立字符位置映射，使用二分查找优化查询。
# - **数据结构**：哈希表（字典）存储字符到位置列表的映射。
# - **算法**：二分查找定位满足顺序的下一个字符位置。
#
# ## 解决方案
#
# ### 实现
#
# ```python
# from typing import List
# from bisect import bisect_left
#
# class Solution:
#     def __init__(self, t: str):
#         self.t = t
#         self.index_map = {char: [] for char in 'abcdefghijklmnopqrstuvwxyz'}
#         for i, char in enumerate(t):
#             self.index_map[char].append(i)
#
#     def isSubsequence(self, s: str) -> bool:
#         if len(s) == 0:
#             return True
#         pos = -1
#         for char in s:
#             if char not in self.index_map:
#                 return False
#             indices = self.index_map[char]
#             idx = bisect_left(indices, pos + 1)
#             if idx == len(indices):
#                 return False
#             pos = indices[idx]
#         return True
# ```

import bisect
from collections import defaultdict


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 预处理：记录每个字符的出现位置
        char_indices = defaultdict(list)
        for idx, char in enumerate(t):
            char_indices[char].append(idx)

        current_pos = -1
        for char in s:
            if char not in char_indices:
                return False
            indices = char_indices[char]
            # 二分查找第一个大于 current_pos 的位置
            i = bisect.bisect_right(indices, current_pos)
            if i == len(indices):
                return False
            current_pos = indices[i]
        return True


#
# ### Big O 分析
# - **预处理时间**：O(len(t))，遍历 `t` 构建 `index_map`。
# - **预处理空间**：O(len(t))，存储字符位置列表。
# - **查询时间**：O(len(s) * log(len(t)))，每次二分查找 O(log(len(t)))。
# - **查询空间**：O(1)，仅使用少量变量。
#
# ### 优缺点
# - **优点**：
#   - 预处理后查询效率高，适合大量 `s` 查询场景。
#   - 对固定 `t` 只需一次预处理，摊销成本低。
# - **缺点**：
#   - 预处理需要额外空间 O(len(t))。
#   - 单次查询复杂度高于双指针法，不适合单次查询场景。
#
# ## 解决方案比较
# - **双指针法**（原解法）：
#   - 时间复杂度：O(len(t))
#   - 空间复杂度：O(1)
#   - 面试适用性：高，简单易懂
#   - 适合场景：单次查询
# - **预处理 + 二分查找**（本解法）：
#   - 预处理时间：O(len(t))
#   - 查询时间：O(len(s) * log(len(t)))
#   - 空间复杂度：O(len(t))
#   - 面试适用性：中等，需解释预处理和二分查找
#   - 适合场景：大量查询
#
# ### 比较结果
# | 标准           | 双指针法          | 预处理 + 二分查找             |
# |----------------|-------------------|-------------------------------|
# | **面试适用性** | 高，简单直观     | 中等，需更多解释             |
# | **时间复杂度** | O(len(t))         | 查询 O(len(s) * log(len(t))) |
# | **空间复杂度** | O(1)              | O(len(t))                    |
# | **代码可读性** | 高，逻辑清晰     | 中等，涉及复杂数据结构       |
# | **边缘处理**   | 优秀             | 优秀，依赖数据结构鲁棒性     |
#
# - **最优选择**：对于 follow-up 大量查询场景，**预处理 + 二分查找** 是最优解，因其查询效率高且预处理成本可摊销。
#
# ## 总结
# 针对 follow-up 场景，推荐使用预处理 `t` 并结合二分查找的方案。初始化时构建字符位置映射，查询时快速定位字符，满足高效处理大量 `s` 的需求。
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s): return False

        ps, pt = 0, 0
        while ps < len(s) and pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
            pt += 1

        return ps == len(s)


test_cases = [
    {
        "method": "isSubsequence",
        "s": "abc",
        "t": "ahbgdc",
        "expected": True,
        "case_id": 1
    },
    {
        "method": "isSubsequence",
        "s": "axc",
        "t": "ahbgdc",
        "expected": False,
        "case_id": 2
    },
    {
        "method": "isSubsequence",
        "s": "",
        "t": "ahbgdc",
        "expected": True,
        "case_id": 3
    },
    {
        "method": "isSubsequence",
        "s": "acb",
        "t": "ahbgdc",
        "expected": False,
        "case_id": 4
    },
    {
        "method": "isSubsequence",
        "s": "abcde",
        "t": "abcde",
        "expected": True,
        "case_id": 5
    }
]

run_tests()
