# 76.py
from test.test_suite import run_tests

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

            # 目标字符频率
        t_count = Counter(t)

        # 窗口状态
        window = Counter()
        need = len(t_count)  # 需要匹配的字符种类数
        have = 0  # 当前匹配的字符种类数
        left = 0
        answer = (float('inf'), 0, 0)  # (长度, 起点, 终点)

        # 滑动窗口
        for right, char in enumerate(s):
            window[char] += 1
            if char in t_count and window[char] == t_count[char]:
                have += 1

            # 当窗口有效时收缩
            while have == need:
                if right - left + 1 < answer[0]:
                    answer = (right - left + 1, left, right + 1)
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        # 返回结果
        return s[answer[1]:answer[2]] if answer[0] != float('inf') else ""


# 时间复杂度：O(n)
#
# 两个指针分别最多移动 n 次
# 哈希表操作是常数时间
# 总体：O(n)
#
# 空间复杂度：O(k)，其中 k 是字符集大小

# 关键点：
# 滑动窗口框架：
# 扩展：右指针通过enumerate移动，不断加入新字符，直到满足条件。
# 匹配：have在窗口字符频率达到目标时增加。
# 收缩：左指针当have == need时，满足条件，尝试缩小窗口，寻找最优解。
# 更新：用ans一次性记录最小窗口。

# 边界处理：
# 开头检查空字符串和长度不足的情况。
# 结尾用float('inf')判断是否找到有效窗口。

test_cases = [
    {
        "method": "minWindow",
        "s": "ADOBECODEBANC",
        "t": "ABC",
        "expected": "BANC",
        "case_id": 1,
        "description": "Typical case with a mix of uppercase letters and multiple occurrences of required characters."
    }, {
        "method": "minWindow",
        "s": "a",
        "t": "a",
        "expected": "a",
        "case_id": 2,
        "description": "Minimal case where both strings are the same and of length 1."
    }, {
        "method": "minWindow",
        "s": "a",
        "t": "aa",
        "expected": "",
        "case_id": 3,
        "description": "Edge case where `t` has more occurrences of 'a' than `s` has."
    }, {
        "method": "minWindow",
        "s": "abc",
        "t": "d",
        "expected": "",
        "case_id": 4,
        "description": "Edge case where `t` contains a character not present in `s`."
    }, {
        "method": "minWindow",
        "s": "abcdebdde",
        "t": "bde",
        "expected": "deb",
        "case_id": 5,
        "description": "Case where the answer is at the end of the string."
    }, {
        "method": "minWindow",
        "s": "abaccccbca",
        "t": "abc",
        "expected": "bac",
        "case_id": 6,
        "description": "Case with repeating characters where a different permutation of `t` may be needed."
    }
]

run_tests()
