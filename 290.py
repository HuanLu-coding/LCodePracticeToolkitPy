# 290. Word Pattern
# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
#
# ### Constraints:
# - `1 <= pattern.length <= 300`
# - `pattern` contains only lower-case English letters.
# - `1 <= s.length <= 3000`
# - `s` contains only lowercase English letters and spaces `' '`.
# - `s` does not contain any leading or trailing spaces.
# - All the words in `s` are separated by a single space.
#
# ### Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
#
# ### Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
#
# ### Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
#
from test.test_suite import run_tests
from typing import *

from collections import defaultdict

import collections  # 虽然这里没用到，但写上表示可能会用更复杂的collections类型


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        使用首次出现索引映射验证单词规律。
        :param pattern: 模式字符串
        :param s: 待匹配字符串
        :return: True 如果 s 遵循 pattern, 否则 False
        """
        words = s.split(' ')

        if len(pattern) != len(words):
            return False

        # 使用字典的 setdefault 方法存储首次出现的索引
        # 如果 key 不存在，则设置 key 的值为 default 并返回 default
        # 如果 key 存在，则返回 key 的当前值 (即首次出现的索引)
        char_first_index = {}
        word_first_index = {}

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            # 获取 char 的首次出现索引 (如果首次出现，设为当前索引 i)
            char_idx = char_first_index.setdefault(char, i)
            # 获取 word 的首次出现索引 (如果首次出现，设为当前索引 i)
            word_idx = word_first_index.setdefault(word, i)

            # 如果在当前位置 i，char 的首次出现索引与 word 的首次出现索引不同，
            # 说明映射关系被破坏了 (要么 char 之前映射了别的 word，要么 word 之前被别的 char 映射)
            if char_idx != word_idx:
                return False

        return True


test_cases = [
    {
        "method": "wordPattern",
        "pattern": "abba",
        "s": "dog cat cat dog",
        "expected": True,
        "case_id": 1,
        "description": "Basic bijection test with repeated patterns"
    },
    {
        "method": "wordPattern",
        "pattern": "abba",
        "s": "dog cat cat fish",
        "expected": False,
        "case_id": 2,
        "description": "No bijection - pattern maps to different words"
    },
    {
        "method": "wordPattern",
        "pattern": "aaaa",
        "s": "dog cat cat dog",
        "expected": False,
        "case_id": 3,
        "description": "Different length of unique elements in pattern and words"
    },
    {
        "method": "wordPattern",
        "pattern": "abba",
        "s": "dog dog dog dog",
        "expected": False,
        "case_id": 4,
        "description": "Edge case: same word for different pattern characters"
    },
    {
        "method": "wordPattern",
        "pattern": "jquery",
        "s": "jquery",
        "expected": False,
        "case_id": 5,
        "description": "Edge case: input s is not split into words correctly"
    },
    {
        "method": "wordPattern",
        "pattern": "aaa",
        "s": "aa aa aa aa",
        "expected": False,
        "case_id": 6,
        "description": "Edge case: pattern and words count mismatch"
    },
    {
        "method": "wordPattern",
        "pattern": "abc",
        "s": "b c a",
        "expected": True,
        "case_id": 7,
        "description": "Edge case: bijection in reverse order"
    },
    {
        "method": "wordPattern",
        "pattern": "abc",
        "s": "cat dog cat",
        "expected": False,
        "case_id": 8,
        "description": "Different characters mapping to same word"
    }
]

run_tests()
