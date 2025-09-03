# 205. Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.
#
# ### Constraints:
# - 1 <= s.length <= 5 * 10^4
# - t.length == s.length
# - s and t consist of any valid ascii character.
#
# ### Example 1:
# Input: s = "egg", t = "add"
# Output: true
#
# ### Example 2:
# Input: s = "foo", t = "bar"
# Output: false
#
# ### Example 3:
# Input: s = "paper", t = "title"
# Output: true
from collections import Counter
from test.test_suite import run_tests
from typing import *


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_to_index_s = {}
        char_to_index_t = {}

        for i in range(len(s)):
            char_s, char_t = s[i], t[i]

            # 如果字符第一次出现，记录它的位置
            if char_s not in char_to_index_s:
                char_to_index_s[char_s] = i
            if char_t not in char_to_index_t:
                char_to_index_t[char_t] = i

            # 如果两个字符的首次出现位置不同，则它们不是同构的
            if char_to_index_s[char_s] != char_to_index_t[char_t]:
                return False

        return True


# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#
#         s_to_t = {}
#         t_to_s = {}
#
#         for i in range(len(s)):
#             char_s, char_t = s[i], t[i]
#
#             # 检查 s -> t 的映射
#             if char_s in s_to_t:
#                 if s_to_t[char_s] != char_t:
#                     return False
#             else:
#                 s_to_t[char_s] = char_t
#
#             # 检查 t -> s 的映射
#             if char_t in t_to_s:
#                 if t_to_s[char_t] != char_s:
#                     return False
#             else:
#                 t_to_s[char_t] = char_s
#
#         return True
#

test_cases = [
    {
        "method": "isIsomorphic",
        "s": "egg",
        "t": "add",
        "expected": True,
        "case_id": 1,
        "description": "Example 1: Simple isomorphic strings"
    },
    {
        "method": "isIsomorphic",
        "s": "foo",
        "t": "bar",
        "expected": False,
        "case_id": 2,
        "description": "Example 2: Non-isomorphic strings (different pattern)"
    },
    {
        "method": "isIsomorphic",
        "s": "paper",
        "t": "title",
        "expected": True,
        "case_id": 3,
        "description": "Example 3: Longer isomorphic strings"
    },
    {
        "method": "isIsomorphic",
        "s": "badc",
        "t": "baba",
        "expected": False,
        "case_id": 4,
        "description": "Different characters in s map to same character in t"
    },
    {
        "method": "isIsomorphic",
        "s": "abcdefghijklmnopqrstuvwxyz",
        "t": "abcdefghijklmnopqrstuvwxyz",
        "expected": True,
        "case_id": 5,
        "description": "Edge case: All characters map to themselves"
    },
    {
        "method": "isIsomorphic",
        "s": "a",
        "t": "b",
        "expected": True,
        "case_id": 6,
        "description": "Edge case: Single character strings"
    },
    {
        "method": "isIsomorphic",
        "s": "13",
        "t": "42",
        "expected": True,
        "case_id": 7,
        "description": "Numeric characters are also valid"
    },
    {
        "method": "isIsomorphic",
        "s": "ab",
        "t": "aa",
        "expected": False,
        "case_id": 8,
        "description": "Edge case: Multiple characters in s map to same character in t"
    }
]

run_tests()
