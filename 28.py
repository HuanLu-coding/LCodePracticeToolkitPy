# 28. Implement strStr()
#
# Implement the strStr() function.
#
# Given two strings haystack and needle, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Clarification:
# 	•	If needle is an empty string, return 0.
#
# Constraints:
# 	•	1 <= haystack.length <= 10^4
# 	•	0 <= needle.length <= 10^4
# 	•	haystack and needle consist of only lowercase English characters.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
# Example 3:
#
# Input: haystack = "", needle = ""
# Output: 0
#
# Example 4:
#
# Input: haystack = "mississippi", needle = "issip"
# Output: 4

from test.test_suite import run_tests


# KMP 算法 效率：O(n + m) 稳定优于其他方案的最坏情况。
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if not needle:
#             return 0
#         n, m = len(haystack), len(needle)
#         if m > n:
#             return -1
#
#         def compute_lps(needle):
#             lps = [0] * m
#             length = 0
#             i = 1
#             while i < m:
#                 if needle[i] == needle[length]:
#                     length += 1
#                     lps[i] = length
#                     i += 1
#                 else:
#                     if length != 0:
#                         length = lps[length - 1]
#                     else:
#                         lps[i] = 0
#                         i += 1
#             return lps
#
#         lps = compute_lps(needle)
#         i = j = 0
#         while i < n:
#             if haystack[i] == needle[j]:
#                 i += 1
#                 j += 1
#                 if j == m:
#                     return i - j
#             else:
#                 if j != 0:
#                     j = lps[j - 1]
#                 else:
#                     i += 1
#         return -1


# 标准暴力解
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if not needle: return 0
#
#         n, m = len(haystack), len(needle)
#         if m > n: return -1
#
#         for i in range(n):
#             if i + m <= n and haystack[i:i + m] == needle:
#                 return i
#
#         return -1

# Rabin-Karp 算法
# 核心思路： 比较两个数字（3456 vs 3325）比比较两个字符串（"ll" vs "he"）快得多！
# 把子字符串（比如 "ll"）变成一个数字。
# 在主字符串（比如 "hello"）上滑动一个窗口，每次看窗口里的小段文字，把它也变成一个数字。
# 比较这两个数字，如果一样，再仔细检查是不是真的匹配。
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        n, m = len(haystack), len(needle)
        if m > n:
            return -1

        def hash_value(s):
            val = 0
            for char in s:
                val = val * 31 + ord(char)
            return val

        needle_hash = hash_value(needle)
        for i in range(n - m + 1):
            window = haystack[i:i + m]
            if hash_value(window) == needle_hash and window == needle:
                return i
        return -1


test_cases = [
    {
        "method": "strStr",
        "haystack": "hello",
        "needle": "ll",
        "expected": 2,
        "case_id": 1
    },
    {
        "method": "strStr",
        "haystack": "aaaaa",
        "needle": "bba",
        "expected": -1,
        "case_id": 2
    },
    {
        "method": "strStr",
        "haystack": "",
        "needle": "",
        "expected": 0,
        "case_id": 3
    },
    {
        "method": "strStr",
        "haystack": "mississippi",
        "needle": "issip",
        "expected": 4,
        "case_id": 4
    },
    {
        "method": "strStr",
        "haystack": "abcde",
        "needle": "cde",
        "expected": 2,
        "case_id": 5
    },
    {
        "method": "strStr",
        "haystack": "hello",
        "needle": "ooo",  # needle比haystack长，越界
        "expected": -1,
        "case_id": 6
    },
    {
        "method": "strStr",
        "haystack": "abcde",
        "needle": "def",  # 后面部分不足以匹配整个needle
        "expected": -1,
        "case_id": 7
    },
    {
        "method": "strStr",
        "haystack": "abcde",
        "needle": "de",  # 可以匹配到，返回2
        "expected": 3,
        "case_id": 8
    },
    {
        "method": "strStr",
        "haystack": "abcdef",
        "needle": "efg",  # needle比剩余部分长，越界
        "expected": -1,
        "case_id": 9
    },
    {
        "method": "strStr",
        "haystack": "ab",
        "needle": "abc",  # needle比haystack长，越界
        "expected": -1,
        "case_id": 10
    }
]

run_tests()
