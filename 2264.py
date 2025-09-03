# https://leetcode.com/problems/largest-3-same-digit-number-in-string/
# 2264. Largest 3-Same-Digit Number in String
import math

# You are given a string `num` representing a large integer. An integer is `good` if it meets the following conditions:
# It is a `substring` of `num` with length `3`.
# It consists of only one unique digit.
#
# Return the `maximum good` integer as a `string` or an empty string `""` if no such integer exists.
#
# Note:
# A `substring` is a contiguous sequence of characters within a string.
# There may be `leading zeroes` in `num` or a good integer.
#
# ### Constraints:
# - `3 <= num.length <= 1000`
# - `num` only consists of digits.
#
# ### Example 1:
# Input: num = "6777133339"
# Output: "777"
# Explanation: There are two distinct good integers: "777" and "333".
# "777" is the largest, so we return "777".
#
# ### Example 2:
# Input: num = "2300019"
# Output: "000"
# Explanation: "000" is the only good integer.
#
# ### Example 3:
# Input: num = "42352338"
# Output: ""
# Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.

from test.test_suite import run_tests
from typing import *


# AI反人类版
# 优点：
# 性能优秀（O(n) 时间，O(1) 空间）。
# 代码极简，展示 Python 高级用法。
# 边界处理可靠。
# 缺点：
# 可读性极差，逻辑晦涩，增加理解负担。
# 面试中可能因过于“炫技”失分。
# 维护和调试困难。
# class Solution:
#     def largestGoodInteger(self, num: str) -> str:
#         return max((num[i - 2:i + 1] for i in range(2, len(num)) if num[i] == num[i - 1] == num[i - 2]), default="")
#
# 简洁滑动窗口版
# 优点：
# 性能最优（O(n) 时间，O(1) 空间）。
# 代码简洁优雅，可读性高。
# 面试友好，易于解释和维护。
# 边界处理完美。
# 缺点：
# 无，接近最优实现。

# class Solution:
#     def largestGoodInteger(self, num: str) -> str:
#         max_digit = ''
#         for i in range(len(num) - 2):
#             if num[i] == num[i+1] == num[i+2]:
#                 max_digit = max(max_digit, num[i])
#         return max_digit * 3 if max_digit else ""


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        length = 3  # length = 3 作为变量多余，硬编码 3 更直观。
        num_good = -math.inf  # 不优雅，增加理解负担： 初始化为 -math.inf（浮点数），但后续与 int(win)（整数）比较，虽然 Python 允许浮点与整数比较
        l = 0
        while l + length <= len(num):  # 不必要的复杂性： 使用 while 循环和手动索引 l，不如 for 循环简洁（for i in range(len(num) - 2)）。
            win = num[l:l + length]

            if len(set(win)) == 1:
                num_good = max(num_good, int(win))  # 使用 int(win) 转换增加了不必要的计算，字符串比较即可（"777" > "333"）

            l += 1
        if num_good == -math.inf: return ''
        return '000' if num_good == 0 else str(num_good)  # 正确处理 "000"，但通过整数转换和特殊返回逻辑增加了复杂性。


# 最终评判
# 您的解决方案在功能上正确，性能达到理论最优（O(n) 时间，O(1) 空间），展示了滑动窗口的算法思维。然而，代码存在以下严重问题：
#
# 冗余复杂性：整数转换、浮点初始化和特殊返回逻辑增加了不必要的计算和理解负担。
# 类型不一致：使用 -math.inf 与整数比较不优雅，可能引发潜在问题。
# 可读性欠佳：变量名、循环结构和冗余变量降低了代码直观性。
# 面试表现：在面试中可能因复杂性和非最优实现被要求优化，影响印象。
# 评分：70/100
#
# 功能正确性：20/20
# 性能：20/20
# 边界处理：15/15
# 可读性：10/20（冗余逻辑和类型问题）
# 面试适用性：5/25（非最优，需优化）

test_cases = [
    {
        "method": "largestGoodInteger",
        "num": "6777133339",
        "expected": "777",
        "case_id": 1,
        "description": "Example 1: Multiple good integers, largest is 777",
    },
    {
        "method": "largestGoodInteger",
        "num": "2300019",
        "expected": "000",
        "case_id": 2,
        "description": "Example 2: Only one good integer, which is 000",
    },
    {
        "method": "largestGoodInteger",
        "num": "42352338",
        "expected": "",
        "case_id": 3,
        "description": "Example 3: No good integers found",
    },
    {
        "method": "largestGoodInteger",
        "num": "111",
        "expected": "111",
        "case_id": 4,
        "description": "Edge case: String is exactly a good integer",
    },
    {
        "method": "largestGoodInteger",
        "num": "999888777000",
        "expected": "999",
        "case_id": 5,
        "description": "Edge case: Multiple good integers in descending order of digit value",
    },
    {
        "method": "largestGoodInteger",
        "num": "1234567890123",
        "expected": "",
        "case_id": 6,
        "description": "Edge case: String with no consecutive same digits",
    },
    {
        "method": "largestGoodInteger",
        "num": "000111222",
        "expected": "222",
        "case_id": 7,
        "description": "Edge case: Multiple good integers in ascending order of digit value, including 000",
    },
    {
        "method": "largestGoodInteger",
        "num": "999999",
        "expected": "999",
        "case_id": 8,
        "description": "Edge case: String consists of only one digit, longer than 3",
    },
]

run_tests()
