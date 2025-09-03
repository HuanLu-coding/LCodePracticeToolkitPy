# 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
#
# ### Constraints:
# - 1 <= s.length <= 10^5
# - s consists of only lowercase English letters.
#
# ### Example 1:
# Input: s = "leetcode"
# Output: 0
#
# ### Example 2:
# Input: s = "loveleetcode"
# Output: 2
#
# ### Example 3:
# Input: s = "aabb"
# Output: -1

from test.test_suite import run_tests
from typing import *

#
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         hashed = {}
#         for idx, char in enumerate(s):
#             if char in hashed:
#                 hashed[char] = -1
#             else:
#                 hashed[char] = idx
#         for idx in hashed.values():
#             if idx != -1: return idx
#         return -1

# 更健壮的版本(不依赖字典有序性)
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_counts = Counter(s)
        for i, char in enumerate(s):
            if char_counts[char] == 1:
                return i

        return -1


test_cases = [
    {
        "method": "firstUniqChar",
        "s": "leetcode",
        "expected": 0,
        "case_id": 1,
        "description": "First character is unique"
    },
    {
        "method": "firstUniqChar",
        "s": "loveleetcode",
        "expected": 2,
        "case_id": 2,
        "description": "Third character is the first unique character"
    },
    {
        "method": "firstUniqChar",
        "s": "aabb",
        "expected": -1,
        "case_id": 3,
        "description": "No unique characters"
    },
    {
        "method": "firstUniqChar",
        "s": "dddccdbba",
        "expected": 8,
        "case_id": 4,
        "description": "Last character is the first unique character"
    },
    {
        "method": "firstUniqChar",
        "s": "z",
        "expected": 0,
        "case_id": 5,
        "description": "Edge case: Single character string"
    },
    {
        "method": "firstUniqChar",
        "s": "aaaaaaaaa",
        "expected": -1,
        "case_id": 6,
        "description": "Edge case: All characters are the same"
    },
    {
        "method": "firstUniqChar",
        "s": "abcdefghijklmnopqrstuvwxyz",
        "expected": 0,
        "case_id": 7,
        "description": "Edge case: All unique characters"
    }
]

run_tests()
