# 13. Roman to Integer

# 罗马数字由七种符号表示：I（1）、V（5）、X（10）、L（50）、C（100）、D（500）、M（1000）。
#
# 通常情况下，罗马数字从左到右按数值从大到小排列。但在以下六种情况下，使用减法规则：
# - I 可放在 V（5）和 X（10）前，表示 4 和 9；
# - X 可放在 L（50）和 C（100）前，表示 40 和 90；
# - C 可放在 D（500）和 M（1000）前，表示 400 和 900。
#
# 给定一个表示罗马数字的字符串 s，返回其对应的整数值。
#
# ### 约束条件：
# - 1 <= s.length <= 15
# - s 仅包含字符 'I'、'V'、'X'、'L'、'C'、'D'、'M'
# - 保证 s 是一个有效的罗马数字，且其表示的整数在 [1, 3999] 范围内
#
# ### 示例 1：
# 输入：s = "III"
# 输出：3
#
# ### 示例 2：
# 输入：s = "IV"
# 输出：4
#
# ### 示例 3：
# 输入：s = "IX"
# 输出：9
#
# ### 示例 4：
# 输入：s = "LVIII"
# 输出：58
# 解释：L = 50, V = 5, III = 3
#
# ### 示例 5：
# 输入：s = "MCMXCIV"
# 输出：1994
# 解释：M = 1000, CM = 900, XC = 90, IV = 4

from test.test_suite import run_tests
from typing import *


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        for i in range(len(s)):
            value = roman[s[i]]
            if i + 1 < len(s) and value < roman[s[i + 1]]:
                total -= value
            else:
                total += value
        return total


test_cases = [
    {
        "method": "romanToInt",
        "s": "III",
        "expected": 3,
        "case_id": 1,
        "description": "基本情况：连续相同字符"
    },
    {
        "method": "romanToInt",
        "s": "IV",
        "expected": 4,
        "case_id": 2,
        "description": "减法规则：I 在 V 前"
    },
    {
        "method": "romanToInt",
        "s": "IX",
        "expected": 9,
        "case_id": 3,
        "description": "减法规则：I 在 X 前"
    },
    {
        "method": "romanToInt",
        "s": "LVIII",
        "expected": 58,
        "case_id": 4,
        "description": "混合加法：L + V + III"
    },
    {
        "method": "romanToInt",
        "s": "MCMXCIV",
        "expected": 1994,
        "case_id": 5,
        "description": "复杂组合：包含多个减法规则"
    },
    {
        "method": "romanToInt",
        "s": "MMMCMXCIX",
        "expected": 3999,
        "case_id": 6,
        "description": "边界情况：最大有效值"
    },
    {
        "method": "romanToInt",
        "s": "I",
        "expected": 1,
        "case_id": 7,
        "description": "边界情况：最小有效值"
    }
]

run_tests()
