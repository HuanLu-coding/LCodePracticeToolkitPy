# 12. Integer to Roman

# Given an integer, convert it to a Roman numeral.
#
# Roman numerals are represented by seven different symbols:
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
# - I can be placed before V (5) and X (10) to make 4 and 9.
# - X can be placed before L (50) and C (100) to make 40 and 90.
# - C can be placed before D (500) and M (1000) to make 400 and 900.
#
# Given an integer, convert it to a Roman numeral.
#
# ### Constraints:
# - 1 <= num <= 3999
#
# ### Example 1:
# Input: num = 3
# Output: "III"
#
# ### Example 2:
# Input: num = 4
# Output: "IV"
#
# ### Example 3:
# Input: num = 9
# Output: "IX"
#
# ### Example 4:
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
#
# ### Example 5:
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

from test.test_suite import run_tests
from typing import *


class Solution:
    def intToRoman(self, num: int) -> str:
        value_to_roman = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        result = ""
        for value, symbol in value_to_roman:
            while num >= value:
                result += symbol
                num -= value
        return result


test_cases = [
    {
        "method": "intToRoman",
        "num": 3,
        "expected": "III",
        "case_id": 1,
        "description": "Simple case with small number"
    },
    {
        "method": "intToRoman",
        "num": 4,
        "expected": "IV",
        "case_id": 2,
        "description": "Subtractive notation for 4"
    },
    {
        "method": "intToRoman",
        "num": 9,
        "expected": "IX",
        "case_id": 3,
        "description": "Subtractive notation for 9"
    },
    {
        "method": "intToRoman",
        "num": 58,
        "expected": "LVIII",
        "case_id": 4,
        "description": "Combination of symbols without subtractive notation"
    },
    {
        "method": "intToRoman",
        "num": 1994,
        "expected": "MCMXCIV",
        "case_id": 5,
        "description": "Complex case with multiple subtractive notations"
    },
    {
        "method": "intToRoman",
        "num": 3999,
        "expected": "MMMCMXCIX",
        "case_id": 6,
        "description": "Upper boundary case"
    }
]

run_tests()
