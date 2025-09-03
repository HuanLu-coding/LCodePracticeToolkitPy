# 2351. First Letter to Appear Twice

# Given a string s consisting of lowercase English letters, return the first letter to appear twice.
#
# Note:
# - A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
# - s will contain at least one letter that appears twice.
#
# ### Constraints:
# - 2 <= s.length <= 100
# - s consists of lowercase English letters.
# - s has at least one repeated letter.
#
# ### Example 1:
# Input: s = "abccbaacz"
# Output: "c"
# Explanation:
# The letter 'a' appears on the indexes 0, 5 and 6.
# The letter 'b' appears on the indexes 1 and 4.
# The letter 'c' appears on the indexes 2, 3 and 7.
# The letter 'z' appears on the index 8.
# The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.
#
# ### Example 2:
# Input: s = "abcdd"
# Output: "d"
# Explanation:
# The only letter that appears twice is 'd' so we return 'd'.

from test.test_suite import run_tests
from typing import *


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for char in s:
            if char in seen:
                return char
            seen.add(char)


test_cases = [
    {
        "method": "repeatedCharacter",
        "s": "abccbaacz",
        "expected": "c",
        "case_id": 1,
        "description": "Multiple letters repeat; 'c' is the first to appear twice."
    },
    {
        "method": "repeatedCharacter",
        "s": "abcdd",
        "expected": "d",
        "case_id": 2,
        "description": "Only 'd' repeats."
    },
    {
        "method": "repeatedCharacter",
        "s": "aabbcc",
        "expected": "a",
        "case_id": 3,
        "description": "All letters repeat; 'a' repeats first."
    },
    {
        "method": "repeatedCharacter",
        "s": "abcdefggh",
        "expected": "g",
        "case_id": 4,
        "description": "Only 'g' repeats."
    },
    {
        "method": "repeatedCharacter",
        "s": "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy",
        "expected": "a",
        "case_id": 5,
        "description": "Long string; 'a' repeats first."
    },
    {
        "method": "repeatedCharacter",
        "s": "zyxwvutsrqponmlkjihgfedcbaaz",
        "expected": "a",
        "case_id": 6,
        "description": "Reverse alphabet with 'a' repeating."
    },
    {
        "method": "repeatedCharacter",
        "s": "abacabad",
        "expected": "a",
        "case_id": 7,
        "description": "'a' repeats multiple times; first to repeat."
    }
]

run_tests()
