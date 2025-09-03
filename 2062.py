# 2062. Count Vowel Substrings of a String

# A substring is a contiguous (non-empty) sequence of characters within a string.
#
# A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.
#
# Given a string word, return the number of vowel substrings in word.
#
# ### Constraints:
# - 1 <= word.length <= 100
# - word consists of lowercase English letters only.
#
# ### Example 1:
# Input: word = "aeiouu"
# Output: 2
# Explanation: The vowel substrings of word are as follows (underlined):
# - "aeiou u"
# - "aeiouu"
#
# ### Example 2:
# Input: word = "unicornarihan"
# Output: 0
# Explanation: Not all 5 vowels are present, so there are no vowel substrings.
#
# ### Example 3:
# Input: word = "cuaieuouac"
# Output: 7
# Explanation: The vowel substrings of word are as follows (underlined):
# - "c uaieuo uac"
# - "c uaieuou ac"
# - "c uaieuoua c"
# - "cu aieuo uac"
# - "cu aieuou ac"
# - "cu aieuoua c"
# - "cua ieuoua c"

from test.test_suite import run_tests
from typing import *


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        pass


test_cases = [
    {
        "method": "countVowelSubstrings",
        "word": "aeiouu",
        "expected": 2,
        "case_id": 1,
        "description": "Simple case with all vowels and extra vowels"
    },
    {
        "method": "countVowelSubstrings",
        "word": "unicornarihan",
        "expected": 0,
        "case_id": 2,
        "description": "No vowel substring with all five vowels"
    },
    {
        "method": "countVowelSubstrings",
        "word": "cuaieuouac",
        "expected": 7,
        "case_id": 3,
        "description": "Multiple vowel substrings with all five vowels"
    },
    {
        "method": "countVowelSubstrings",
        "word": "bbaeixoubb",
        "expected": 0,
        "case_id": 4,
        "description": "Vowel substrings contain consonants, hence invalid"
    },
    {
        "method": "countVowelSubstrings",
        "word": "aeiouaeiou",
        "expected": 6,
        "case_id": 5,
        "description": "Repeated sequence of all vowels"
    },
    {
        "method": "countVowelSubstrings",
        "word": "a",
        "expected": 0,
        "case_id": 6,
        "description": "Single vowel character, not all five vowels present"
    },
    {
        "method": "countVowelSubstrings",
        "word": "aeio",
        "expected": 0,
        "case_id": 7,
        "description": "Missing one vowel, hence no valid vowel substring"
    }
]

run_tests()
