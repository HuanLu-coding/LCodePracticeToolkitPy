# 151. Reverse Words in a String

# Given an input string s, reverse the order of the words.
#
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words.
# The returned string should only have a single space separating the words. Do not include any extra spaces.
#
# ### Constraints:
# - 1 <= s.length <= 10^4
# - s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# - There is at least one word in s.
#
# ### Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"
#
# ### Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
#
# ### Example 3:
# Input: s = "a good   example"
# Output: "example good a"

from test.test_suite import run_tests
from typing import *


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(reversed(s.split())))


test_cases = [
    {
        "method": "reverseWords",
        "s": "the sky is blue",
        "expected": "blue is sky the",
        "case_id": 1,
        "description": "Basic case with multiple words"
    },
    {
        "method": "reverseWords",
        "s": "  hello world  ",
        "expected": "world hello",
        "case_id": 2,
        "description": "Leading and trailing spaces"
    },
    {
        "method": "reverseWords",
        "s": "a good   example",
        "expected": "example good a",
        "case_id": 3,
        "description": "Multiple spaces between words"
    },
    {
        "method": "reverseWords",
        "s": "single",
        "expected": "single",
        "case_id": 4,
        "description": "Single word with no spaces"
    },
    {
        "method": "reverseWords",
        "s": "    ",
        "expected": "",
        "case_id": 5,
        "description": "Only spaces (edge case)"
    },
    {
        "method": "reverseWords",
        "s": "a  b   c",
        "expected": "c b a",
        "case_id": 6,
        "description": "Multiple spaces between multiple words"
    },
    {
        "method": "reverseWords",
        "s": "  multiple   spaces  here ",
        "expected": "here spaces multiple",
        "case_id": 7,
        "description": "Leading, trailing, and multiple intermediate spaces"
    }
]

run_tests()
