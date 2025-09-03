# 58. Length of Last Word

# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.
#
# ### Constraints:
# - `1 <= s.length <= 10^4`
# - `s` consists of only English letters and spaces ' '.
# - There will be at least one word in `s`.
#
# ### Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
#
# ### Example 2:
# Input: s = " fly me to the moon "
# Output: 4
# Explanation: The last word is "moon" with length 4.
#
# ### Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

from test.test_suite import run_tests
from typing import *


# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         return len(s.split()[-1])
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1  # 跳过末尾空格
        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length


test_cases = [
    {
        "method": "lengthOfLastWord",
        "s": "Hello World",
        "expected": 5,
        "case_id": 1,
        "description": "Basic case with two words"
    },
    {
        "method": "lengthOfLastWord",
        "s": " fly me to the moon ",
        "expected": 4,
        "case_id": 2,
        "description": "String with leading and trailing spaces"
    },
    {
        "method": "lengthOfLastWord",
        "s": "luffy is still joyboy",
        "expected": 6,
        "case_id": 3,
        "description": "Basic case with multiple words"
    },
    {
        "method": "lengthOfLastWord",
        "s": "a",
        "expected": 1,
        "case_id": 4,
        "description": "Single character string (edge case)"
    },
    {
        "method": "lengthOfLastWord",
        "s": "a ",
        "expected": 1,
        "case_id": 5,
        "description": "Single character with trailing space (edge case)"
    },
    {
        "method": "lengthOfLastWord",
        "s": " singleword",
        "expected": 10,
        "case_id": 6,
        "description": "Single word with leading spaces (edge case)"
    },
    {
        "method": "lengthOfLastWord",
        "s": "word   with   multiple   spaces ",
        "expected": 6,
        "case_id": 7,
        "description": "Multiple spaces between words and trailing spaces"
    }
]

run_tests()
