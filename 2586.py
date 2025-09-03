from test.test_suite import run_tests

# 2586. Count the Number of Vowel Strings in Range

# You are given a **0-indexed** array of string `words` and two integers `left` and `right`.
#
# A vowel string is a string that starts with a vowel ('a', 'e', 'i', 'o', 'u') and ends with a vowel.
#
# Return the number of vowel strings in the given range [`left`, `right`] (inclusive).
#
# ### Constraints:
# - `1 <= words.length <= 1000`
# - `1 <= words[i].length <= 10`
# - `words[i]` consists of only lowercase English letters.
# - `0 <= left <= right < words.length`
#
# ### Example 1:
# Input: words = ["are","amy","u"], left = 0, right = 2
# Output: 2
# Explanation:
# - "are" starts with 'a' and ends with 'e', so it is a vowel string.
# - "amy" starts with 'a' but ends with 'y', so it is not a vowel string.
# - "u" starts with 'u' and ends with 'u', so it is a vowel string.
# The number of vowel strings in the range [0, 2] is 2.
#
# ### Example 2:
# Input: words = ["aba","bcb","ece","aa","ioi","ouu"], left = 1, right = 5
# Output: 3
# Explanation:
# - "bcb" does not start with a vowel, so it is not a vowel string.
# - "ece" starts with 'e' and ends with 'e', so it is a vowel string.
# - "aa" starts with 'a' and ends with 'a', so it is a vowel string.
# - "ioi" starts with 'i' and ends with 'i', so it is a vowel string.
# The number of vowel strings in the range [1, 5] is 3.
#
# ### Example 3:
# Input: words = ["apple","banana","cherry"], left = 1, right = 1
# Output: 0
# Explanation:
# - "banana" does not start with a vowel, so it is not a vowel string.
# The number of vowel strings in the range [1, 1] is 0.

from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        cnt = 0
        for word in words[left: right + 1]:
            if word[0] in vowels and word[-1] in vowels:
                cnt += 1
        return cnt


test_cases = [
    {
        "method": "vowelStrings",
        "words": ["are", "amy", "u"],
        "left": 0,
        "right": 2,
        "expected": 2,
        "case_id": 1,
        "description": "Basic case with vowel and non-vowel strings"
    },
    {
        "method": "vowelStrings",
        "words": ["aba", "bcb", "ece", "aa", "ioi", "ouu"],
        "left": 1,
        "right": 5,
        "expected": 4,
        "case_id": 2,
        "description": "Range in the middle of the list"
    },
    {
        "method": "vowelStrings",
        "words": ["apple", "banana", "cherry"],
        "left": 1,
        "right": 1,
        "expected": 0,
        "case_id": 3,
        "description": "Single element range with a non-vowel string"
    },
    {
        "method": "vowelStrings",
        "words": ["aeiou"],
        "left": 0,
        "right": 0,
        "expected": 1,
        "case_id": 4,
        "description": "Single element list with a vowel string of all vowels"
    },
    {
        "method": "vowelStrings",
        "words": ["a", "e", "i", "o", "u"],
        "left": 0,
        "right": 4,
        "expected": 5,
        "case_id": 5,
        "description": "List of single vowel strings"
    },
    {
        "method": "vowelStrings",
        "words": ["cat", "dog", "mouse"],
        "left": 0,
        "right": 2,
        "expected": 0,
        "case_id": 6,
        "description": "Range with no vowel strings"
    },
    {
        "method": "vowelStrings",
        "words": ["aaaaa", "eeeee", "iiiii", "ooooo", "uuuuu"],
        "left": 1,
        "right": 3,
        "expected": 3,
        "case_id": 7,
        "description": "Range with multiple identical vowel strings"
    }
]

run_tests()
