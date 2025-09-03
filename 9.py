# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.
#
# ### Constraints:
# - -2^31 <= x <= 2^31 - 1
#
# ### Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#
# ### Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it reads 121-. Therefore it is not a palindrome.
#
# ### Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
# Follow up: Could you solve it without converting the integer to a string?
from test.test_suite import run_tests
from typing import *


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x < 10: return True
        if x % 10 == 0: return False
        reversed_x = 0
        while x > reversed_x:
            reversed_x = reversed_x * 10 + x % 10
            x = x // 10
        if x == reversed_x:
            return True
        elif x == reversed_x // 10:
            return True
        else:
            return False


test_cases = [
    {
        "method": "isPalindrome",
        "x": 121,
        "expected": True,
        "case_id": 1,
        "description": "Positive palindrome number"
    },
    {
        "method": "isPalindrome",
        "x": -121,
        "expected": False,
        "case_id": 2,
        "description": "Negative number (can't be palindrome due to negative sign)"
    },
    {
        "method": "isPalindrome",
        "x": 10,
        "expected": False,
        "case_id": 3,
        "description": "Number ending with 0 but not 0 itself (can't be palindrome)"
    },
    {
        "method": "isPalindrome",
        "x": 0,
        "expected": True,
        "case_id": 4,
        "description": "Zero (is a palindrome)"
    },
    {
        "method": "isPalindrome",
        "x": 12321,
        "expected": True,
        "case_id": 5,
        "description": "Odd length palindrome number"
    },
    {
        "method": "isPalindrome",
        "x": 1221,
        "expected": True,
        "case_id": 6,
        "description": "Even length palindrome number"
    },
    {
        "method": "isPalindrome",
        "x": 2147483647,
        "expected": False,
        "case_id": 7,
        "description": "Maximum 32-bit integer (not a palindrome)"
    },
    {
        "method": "isPalindrome",
        "x": -2147483648,
        "expected": False,
        "case_id": 8,
        "description": "Minimum 32-bit integer (not a palindrome due to negative sign)"
    }
]

run_tests()
