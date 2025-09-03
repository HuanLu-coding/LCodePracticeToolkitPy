# 383. Ransom Note
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine, otherwise return false.
#
# Each letter in magazine can only be used once in ransomNote.
#
# ### Constraints:
# - 1 <= ransomNote.length, magazine.length <= 10^5
# - ransomNote and magazine consist of lowercase English letters.
#
# ### Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
#
# ### Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
#
# ### Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
from test.test_suite import run_tests
from typing import *
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt_ransomNote = Counter(ransomNote)
        for char in magazine:
            if char in cnt_ransomNote and cnt_ransomNote[char] > 0:
                cnt_ransomNote[char] -= 1

        # return all(count <= 0 for count in cnt_ransomNote.values())
        return not any(count > 0 for count in cnt_ransomNote.values())


test_cases = [
    {
        "method": "canConstruct",
        "ransomNote": "a",
        "magazine": "b",
        "expected": False,
        "case_id": 1,
        "description": "Basic case where ransomNote character is not in magazine"
    },
    {
        "method": "canConstruct",
        "ransomNote": "aa",
        "magazine": "ab",
        "expected": False,
        "case_id": 2,
        "description": "Magazine has some characters but not enough duplicates"
    },
    {
        "method": "canConstruct",
        "ransomNote": "aa",
        "magazine": "aab",
        "expected": True,
        "case_id": 3,
        "description": "Magazine has all required characters including duplicates"
    },
    {
        "method": "canConstruct",
        "ransomNote": "abcdef",
        "magazine": "abcdefghijklmnopqrstuvwxyz",
        "expected": True,
        "case_id": 4,
        "description": "Magazine contains all letters of the alphabet"
    },
    {
        "method": "canConstruct",
        "ransomNote": "aabb",
        "magazine": "aabbc",
        "expected": True,
        "case_id": 5,
        "description": "Magazine has exact characters needed plus one extra"
    },
    {
        "method": "canConstruct",
        "ransomNote": "z",
        "magazine": "a",
        "expected": False,
        "case_id": 6,
        "description": "Different single characters"
    },
    {
        "method": "canConstruct",
        "ransomNote": "fihjjjjei",
        "magazine": "hjibagacbhadfaefdjaeaebgi",
        "expected": False,
        "case_id": 7,
        "description": "Edge case: Magazine has all distinct letters but not enough duplicates"
    },
    {
        "method": "canConstruct",
        "ransomNote": "a",
        "magazine": "a",
        "expected": True,
        "case_id": 8,
        "description": "Edge case: Identical single characters"
    },
    {
        "method": "canConstruct",
        "ransomNote": "fffbfg",
        "magazine": "effjfggbffjdgbjjhhdegh",
        "expected": True,
        "case_id": 9,
        "description": "Edge case: Multiple duplicate letters in both strings"
    },
    {
        "method": "canConstruct",
        "ransomNote": "bg",
        "magazine": "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj",
        "expected": True,
        "case_id": 10,
        "description": "Magazine much longer than ransom note"
    }
]
run_tests()
