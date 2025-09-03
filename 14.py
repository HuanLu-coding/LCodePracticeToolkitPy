# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# ### Constraints:
# - `1 <= strs.length <= 200`
# - `0 <= strs[i].length <= 200`
# - `strs[i]` consists of only lowercase English letters.
#
# ### Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# ### Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
# ### Example 3:
# Input: strs = ["interspecies","interstellar","interstate"]
# Output: "inters"
#
# ### Example 4:
# Input: strs = ["throne","throne"]
# Output: "throne"
#
# ### Example 5:
# Input: strs = ["throne","dungeon"]
# Output: ""
#
# ### Example 6:
# Input: strs = ["prefix","prefixes","prefixation"]
# Output: "prefix"

from test.test_suite import run_tests
from typing import *


class Solution:
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     if not strs:
    #         return ""
    #     for i in range(len(strs[0])):
    #         char = strs[0][i]
    #         for string in strs[1:]:
    #             if i == len(string) or string[i] != char:
    #                 return strs[0][:i]
    #     return strs[0]


    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        min_len = min(list(map(len, strs)))
        if n == 1: return strs[0]
        if not min_len: return ''
        result = []
        for pos in range(min_len):
            temp_collection = []
            for idx in range(n):
                temp_collection.append(strs[idx][pos])
            if len(set(temp_collection)) == 1:
                result.append(temp_collection[0])
            else:
                break

        return ''.join(result)


test_cases = [
    {
        "method": "longestCommonPrefix",
        "strs": ["flower", "flow", "flight"],
        "expected": "fl",
        "case_id": 1,
        "description": "Common prefix 'fl' among all strings"
    },
    {
        "method": "longestCommonPrefix",
        "strs": ["dog", "racecar", "car"],
        "expected": "",
        "case_id": 2,
        "description": "No common prefix among the strings"
    },
    {
        "method": "longestCommonPrefix",
        "strs": ["interspecies", "interstellar", "interstate"],
        "expected": "inters",
        "case_id": 3,
        "description": "Common prefix 'inters' among the strings"
    },
    {
        "method": "longestCommonPrefix",
        "strs": ["throne", "throne"],
        "expected": "throne",
        "case_id": 4,
        "description": "Identical strings, common prefix is the string itself"
    },
    {
        "method": "longestCommonPrefix",
        "strs": ["throne", "dungeon"],
        "expected": "",
        "case_id": 5,
        "description": "No common prefix among the strings"
    },
    {
        "method": "longestCommonPrefix",
        "strs": ["prefix", "prefixes", "prefixation"],
        "expected": "prefix",
        "case_id": 6,
        "description": "Common prefix 'prefix' among the strings"
    },
    {
        "method": "longestCommonPrefix",
        "strs": ["a"],
        "expected": "a",
        "case_id": 7,
        "description": "Single string, common prefix is the string itself"
    },
    {
        "method": "longestCommonPrefix",
        "strs": ["", "b", "c"],
        "expected": "",
        "case_id": 8,
        "description": "One empty string, common prefix is empty"
    },
    {
        "method": "longestCommonPrefix",
        "strs": ["abc", "abc", "abc"],
        "expected": "abc",
        "case_id": 9,
        "description": "All strings are the same, common prefix is the string itself"
    },
    {
        "method": "longestCommonPrefix",
        "strs": ["abc", "ab", "a"],
        "expected": "a",
        "case_id": 10,
        "description": "Common prefix 'a' among the strings"
    }
]

run_tests()
