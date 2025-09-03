# 38. Count and Say

# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
#
# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
# To determine the way you "say" a digit string, split it into the minimal number of groups so that each group is all the same character. Then, for each group, say the number of characters, followed by the character itself. Finally, concatenate the said groups.
#
# For example, the aggregation process for "3322251":
# "3322251" splits into "33", "222", "5", and "1".
# "33" is two 3s, so say "23".
# "222" is three 2s, so say "32".
# "5" is one 5, so say "15".
# "1" is one 1, so say "11".
# Concatenating the said groups gives "23" + "32" + "15" + "11" = "23321511".
#
# Given a positive integer n, return the nth term of the count-and-say sequence.
#
# ### Constraints:
# - `1 <= n <= 30`
#
# ### Example 1:
# Input: n = 1
# Output: "1"
# Explanation: This is the base case.
#
# ### Example 2:
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1s = "21"
# countAndSay(4) = say "21" = one 2, one 1 = "1211"

from test.test_suite import run_tests
from typing import *


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        result = "1"
        for _ in range(n - 1):
            next_result = ""
            count = 1
            for j in range(len(result)):
                if j < len(result) - 1 and result[j] == result[j + 1]:
                    count += 1
                else:
                    next_result += str(count) + result[j]
                    count = 1
            result = next_result
        return result


test_cases = [
    {
        "method": "countAndSay",
        "n": 1,
        "expected": "1",
        "case_id": 1,
        "description": "Base case n=1"
    },
    {
        "method": "countAndSay",
        "n": 2,
        "expected": "11",
        "case_id": 2,
        "description": "Count and say '1' -> one 1"
    },
    {
        "method": "countAndSay",
        "n": 3,
        "expected": "21",
        "case_id": 3,
        "description": "Count and say '11' -> two 1s"
    },
    {
        "method": "countAndSay",
        "n": 4,
        "expected": "1211",
        "case_id": 4,
        "description": "Count and say '21' -> one 2, one 1"
    },
    {
        "method": "countAndSay",
        "n": 5,
        "expected": "111221",
        "case_id": 5,
        "description": "Count and say '1211' -> one 1, one 2, two 1s"
    },
    {
        "method": "countAndSay",
        "n": 6,
        "expected": "312211",
        "case_id": 6,
        "description": "Count and say '111221' -> three 1s, two 2s, one 1"
    }
]

run_tests()
