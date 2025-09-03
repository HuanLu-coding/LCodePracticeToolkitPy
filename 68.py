# 68. Text Justification
# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
#
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
#
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left-justified, and no extra space is inserted between words.
#
# ### Constraints:
# - `1 <= words.length <= 300`
# - `1 <= words[i].length <= 20`
# - `words[i]` consists of only English letters and symbols.
# - `1 <= maxWidth <= 100`
# - `words[i].length <= maxWidth`
#
# ### Example 1:
# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
#
# ### Example 2:
# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# Output:
# [
#    "What   must   be",
#    "acknowledgment  ",
#    "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.
#
# ### Example 3:
# Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
# Output:
# [
#    "Science  is  what we",
#    "understand      well",
#    "enough to explain to",
#    "a  computer.  Art is",
#    "everything  else  we",
#    "do                  "
# ]
from test.test_suite import run_tests
from typing import *


# class Solution:
#     def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
#         results = []
#         str_words = ' '.join(words).strip()
#         print('str_words: ', str_words)
#         n = len(str_words)
#         while n:
#             print('n: ', n)
#             print('while str_words: `', str_words, '`, len: ', len(str_words))
#             if n < maxWidth:
#                 results.append(str_words)
#                 print('if:', results)
#                 n = 0
#             elif str_words[maxWidth + 1] == ' ':
#                 results.append(str_words[0:maxWidth + 1])
#                 str_words = str_words[maxWidth + 1 + 1:]
#                 n = len(str_words)
#                 print('elif:', results)
#             else:
#                 line_end_index = str_words[0:maxWidth + 1].rfind(" ")
#                 print('line_end_index: ', line_end_index)
#                 results.append(str_words[0:line_end_index])
#                 str_words = str_words[line_end_index + 1:]
#                 n = len(str_words)
#                 print('else: ', results)
#         print('L77: ', results)
#         for idx, line in enumerate(results):
#             if idx == len(results) - 1:
#                 results[idx] = line + ' ' * (maxWidth - len(line))
#             elif line.count(' ') == 0:
#                 results[idx] = line + ' ' * (maxWidth - len(line))
#             else:
#                 slots_num = line.count(' ')
#                 space_num = maxWidth - len(line)
#                 avg_space_num = space_num // slots_num
#                 leading_space_num = space_num % slots_num
#                 new_line = ""
#                 first_space_occur_idx = line.find(' ')
#                 for i, c in enumerate(line):
#                     if i == first_space_occur_idx:
#                         new_line += ' ' * (avg_space_num + leading_space_num + 1)
#                     elif c == ' ':
#                         new_line += ' ' * (avg_space_num + 1)
#                     else:
#                         new_line += c
#
#                 results[idx] = new_line
#         print('L81: ', results)
#         return results
#
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if not words:
            return []

        result = []
        line = []  # 当前行单词列表
        line_length = 0  # 当前行单词总长度（不含空格）

        for word in words:
            # 检查加入新单词后是否超长（单词长度 + 最少空格数）
            if line_length + len(word) + len(line) > maxWidth:
                result.append(self.format_line(line, maxWidth, False))
                line = [word]
                line_length = len(word)
            else:
                line.append(word)
                line_length += len(word)

        # 处理最后一行
        if line:
            result.append(self.format_line(line, maxWidth, True))

        return result

    def format_line(self, line: List[str], maxWidth: int, is_last: bool) -> str:
        if is_last or len(line) == 1:
            # 最后一行或单单词行：左对齐
            return ' '.join(line).ljust(maxWidth)

        # 非最后一行：均匀分配空格
        total_chars = sum(len(word) for word in line)
        total_spaces = maxWidth - total_chars
        num_gaps = len(line) - 1
        spaces_per_gap = total_spaces // num_gaps
        extra_spaces = total_spaces % num_gaps

        formatted = line[0]
        for i in range(1, len(line)):
            spaces = spaces_per_gap + (1 if i <= extra_spaces else 0)
            formatted += ' ' * spaces + line[i]
        return formatted


test_cases = [
    {
        "method": "fullJustify",
        "words": ["This", "is", "an", "example", "of", "text", "justification."],
        "maxWidth": 16,
        "expected": [
            "This    is    an",
            "example  of text",
            "justification.  "
        ],
        "case_id": 1,
        "description": "Basic test case with multiple lines"
    },
    {
        "method": "fullJustify",
        "words": ["What", "must", "be", "acknowledgment", "shall", "be"],
        "maxWidth": 16,
        "expected": [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ],
        "case_id": 2,
        "description": "Test with single word line and last line with multiple words"
    },
    {
        "method": "fullJustify",
        "words": ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a",
                  "computer.", "Art", "is", "everything", "else", "we", "do"],
        "maxWidth": 20,
        "expected": [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ],
        "case_id": 3,
        "description": "Complex test with various line configurations"
    },
    {
        "method": "fullJustify",
        "words": ["a"],
        "maxWidth": 1,
        "expected": ["a"],
        "case_id": 4,
        "description": "Edge case: single word exactly matching maxWidth"
    },
    {
        "method": "fullJustify",
        "words": ["a"],
        "maxWidth": 5,
        "expected": ["a    "],
        "case_id": 5,
        "description": "Edge case: single word with padding needed"
    },
    {
        "method": "fullJustify",
        "words": ["hello", "world"],
        "maxWidth": 11,
        "expected": ["hello world"],
        "case_id": 6,
        "description": "Edge case: two words exactly matching maxWidth"
    },
    {
        "method": "fullJustify",
        "words": ["a", "b", "c", "d", "e"],
        "maxWidth": 3,
        "expected": ["a b", "c d", "e  "],
        "case_id": 7,
        "description": "Multiple lines with short words"
    }
]

run_tests()
