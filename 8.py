# 8. String to Integer (atoi)
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
#
# The algorithm for myAtoi(string s) is as follows:
#
# 1. Read in and ignore any leading whitespace.
# 2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# 3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# 4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# 5. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -2^31 should be clamped to -2^31, and integers greater than 2^31 - 1 should be clamped to 2^31 - 1.
# 6. Return the integer as the final result.
#
# ### Constraints:
# - `0 <= s.length <= 200`
# - `s` consists of English letters (lower-case and upper-case), digits (`0-9`), `' '`, `'+'`, `'-'`, and `'.'`.
#
# ### Example 1:
# Input: s = "42"
# Output: 42
# Explanation: The underlined characters are what is read in, the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "42" ("42" is read in)
#            ^
# The parsed integer is 42.
# Since 42 is in the range [-2^31, 2^31 - 1], the final result is 42.
#
# ### Example 2:
# Input: s = "   -42"
# Output: -42
# Explanation:
# Step 1: "   -42" (leading whitespace is read and ignored)
#             ^
# Step 2: "   -42" ('-' is read, so the result should be negative)
#              ^
# Step 3: "   -42" ("42" is read in)
#                ^
# The parsed integer is -42.
# Since -42 is in the range [-2^31, 2^31 - 1], the final result is -42.
#
# ### Example 3:
# Input: s = "4193 with words"
# Output: 4193
# Explanation:
# Step 1: "4193 with words" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a space)
#              ^
# The parsed integer is 4193.
# Since 4193 is in the range [-2^31, 2^31 - 1], the final result is 4193.
from test.test_suite import run_tests
from typing import *


class Solution:
    def myAtoi(self, s: str) -> int:
        pass


test_cases = [
    {
        "method": "myAtoi",
        "s": "42",
        "expected": 42,
        "case_id": 1,
        "description": "Basic positive integer without whitespace or sign"
    },
    {
        "method": "myAtoi",
        "s": "   -42",
        "expected": -42,
        "case_id": 2,
        "description": "Negative integer with leading whitespace"
    },
    {
        "method": "myAtoi",
        "s": "4193 with words",
        "expected": 4193,
        "case_id": 3,
        "description": "Integer followed by words"
    },
    {
        "method": "myAtoi",
        "s": "words and 987",
        "expected": 0,
        "case_id": 4,
        "description": "Words before number (edge case)"
    },
    {
        "method": "myAtoi",
        "s": "-91283472332",
        "expected": -2147483648,
        "case_id": 5,
        "description": "Negative integer out of range (edge case)"
    },
    {
        "method": "myAtoi",
        "s": "3147483648",
        "expected": 2147483647,
        "case_id": 6,
        "description": "Positive integer out of range (edge case)"
    },
    {
        "method": "myAtoi",
        "s": "  +0 123",
        "expected": 0,
        "case_id": 7,
        "description": "Zero with plus sign and trailing numbers"
    },
    {
        "method": "myAtoi",
        "s": "",
        "expected": 0,
        "case_id": 8,
        "description": "Empty string (edge case)"
    },
    {
        "method": "myAtoi",
        "s": "+-12",
        "expected": 0,
        "case_id": 9,
        "description": "Invalid sign sequence (edge case)"
    }
]

run_tests()
