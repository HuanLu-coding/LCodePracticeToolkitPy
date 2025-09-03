# 455.py
from test.test_suite import run_tests
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1  # 孩子满足了
            j += 1  # 饼干被用了，无论是否满足
        return i


test_cases = []

run_tests()
