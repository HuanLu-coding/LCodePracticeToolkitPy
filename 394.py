# 394. Decode String
# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
#
# ### Constraints:
# - `1 <= s.length <= 30`
# - `s` consists of lowercase English letters, digits, and square brackets '[]'.
# - `s` is guaranteed to be a valid input.
# - All the integers in `s` are in the range [1, 300].
#
# ### Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
#
# ### Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
#
# ### Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
from test.test_suite import run_tests
from typing import *
from collections import deque


#
# - **关键点**：
#   - 双栈法和单栈法

# #### 问题背景与分析
# LeetCode 394 号问题“解码字符串”要求解码一个包含数字、字母和方括号的字符串，规则为 `k[encoded_string]` 表示 `encoded_string` 重复 `k` 次，可能存在嵌套，如 `"3[a2[c]]"` 解码为 `"accaccacc"`。
# 首先理解问题
# - 简单情况如 `"abc"` 直接返回，复杂情况如 `"3[a2[c]]"` 需要先解内层 `"2[c]"` 为 `"cc"`，再处理外层。
# - 思考过程：从左到右扫描，遇到数字记录重复次数，字母累积到字符串，`[` 开始新层需保存状态，`]` 结束层时重复并合并。
# - 自然想到用栈保存状态：一个数字栈，一个字符串栈，模拟嵌套处理。

# - **第一步：理解示例**
#   - `"3[a]2[bc]"` → `"aaabcbc"`，说明需要处理多个编码块并拼接。
#   - `"3[a2[c]]"` → `"accaccacc"`，说明存在嵌套，先解内层 `"2[c]"` 为 `"cc"`，再处理 `"a" + "cc"` 为 `"acc"`，最后重复 3 次。
# - **第二步：考虑处理方式**
#   - 从左到右扫描字符串，遇到字母直接累积，遇到数字需记录重复次数。
#   - 遇到 `[` 时，开始一个新层，需要保存当前状态（如数字和字符串），因为内层可能还有嵌套。
#   - 遇到 `]` 时，结束当前层，将当前字符串按之前记录的数字重复，并与上一层合并。
# - **第三步：数据结构选择**
#   - 嵌套结构提示需要保存多层状态，人类可能想到栈，因为栈适合处理括号匹配或嵌套问题（如表达式求值）。
#   - 可以用两个栈：一个存储数字（`num_stack`），一个存储字符串（`str_stack`），模拟状态保存和恢复。
# - **第四步：模拟过程**
#   - 以 `"3[a2[b]]"` 为例：
#     - 初始 `num_stack=[]`, `str_stack=[]`, `current_str=""`, `current_num=0`。
#     - `'3'`：`current_num=3`。
#     - `'['`：压入 `num_stack=[3]`, `str_stack=[""]`，重置 `current_num=0`, `current_str=""`。
#     - `'a'`：`current_str="a"`。
#     - `'2'`：`current_num=2`。
#     - `'['`：压入 `num_stack=[3,2]`, `str_stack=["","a"]`，重置 `current_num=0`, `current_str=""`。
#     - `'b'`：`current_str="b"`。
#     - `']'`：弹出 `num_stack` 得 2，`str_stack` 得 "a"，`current_str="a" + "b"*2 = "abb"`。
#     - 再遇 `']'`：弹出 `num_stack` 得 3，`str_stack` 得 ""，`current_str="" + "abb"*3 = "abbabbabb"`。
#   - 最终返回 `"abbabbabb"`，正确。
# ### 关键引用
# - [In-Depth Explanation LeetCode 394](https://algo.monster/liteproblems/394)
# - [LeetCode 394 Problem](https://leetcode.com/problems/decode-string/)

# class Solution:
#     def decodeString(self, s: str) -> str:
#         num_stack = []
#         str_stack = []
#         current_str = ""
#         current_num = 0
#
#         for char in s:
#             if char.isdigit():
#                 current_num = current_num * 10 + int(char)
#             elif char == '[':
#                 num_stack.append(current_num)
#                 str_stack.append(current_str)
#                 current_num = 0
#                 current_str = ""
#             elif char == ']':
#                 repeat_times = num_stack.pop()
#                 prev_str = str_stack.pop()
#                 current_str = prev_str + current_str * repeat_times
#             else:
#                 current_str += char
#
#         return current_str
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_str = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append((current_num, current_str))
                current_num = 0
                current_str = ""
            elif char == ']':
                repeat_times, prev_str = stack.pop()
                current_str = prev_str + current_str * repeat_times
            else:
                current_str += char

        return current_str


test_cases = [
    {
        "method": "decodeString",
        "s": "3[a]2[bc]",
        "expected": "aaabcbc",
        "case_id": 1,
        "description": "Basic example with multiple encoded segments"
    },
    {
        "method": "decodeString",
        "s": "3[a2[c]]",
        "expected": "accaccacc",
        "case_id": 2,
        "description": "Nested brackets example"
    },
    {
        "method": "decodeString",
        "s": "2[abc]3[cd]ef",
        "expected": "abcabccdcdcdef",
        "case_id": 3,
        "description": "Multiple segments with trailing characters"
    },
    {
        "method": "decodeString",
        "s": "abc",
        "expected": "abc",
        "case_id": 4,
        "description": "Edge case: No brackets, just letters"
    },
    {
        "method": "decodeString",
        "s": "10[a]",
        "expected": "aaaaaaaaaa",
        "case_id": 5,
        "description": "Edge case: Multi-digit number"
    },
    {
        "method": "decodeString",
        "s": "2[3[a]b]",
        "expected": "aaabaaab",
        "case_id": 6,
        "description": "Edge case: Deep nesting with multiple layers"
    },
    {
        "method": "decodeString",
        "s": "100[leetcode]",
        "expected": "leetcode" * 100,
        "case_id": 7,
        "description": "Edge case: Large repetition count"
    }
]

run_tests()
