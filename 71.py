# 71. Simplify Path
# Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
#
# In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.
#
# The canonical path should have the following format:
# - The path starts with a single slash '/'.
# - Any two directories are separated by a single slash '/'.
# - The path does not end with a trailing '/'.
# - The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
#
# Return the simplified canonical path.
#
# ### Constraints:
# - 1 <= path.length <= 3000
# - path consists of English letters, digits, period '.', slash '/' or '_'.
# - path is a valid absolute path.
#
# ### Example 1:
# Input: path = "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory name.
#
# ### Example 2:
# Input: path = "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
#
# ### Example 3:
# Input: path = "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

from test.test_suite import run_tests
from typing import *


# from collections import deque
#
#
# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         # replace multiple `/` with single `/`:
#         stack = deque()
#         n = len(path)
#         without_multiple_slash = []
#         for i, s in enumerate(path):
#             if without_multiple_slash and without_multiple_slash[-1] == '/' and s == '/':
#                 continue
#             if s:
#                 without_multiple_slash.append(s)
#
#         str_without_multiple_slash = ''.join(without_multiple_slash)
#
#         list_without_multiple_slash = str_without_multiple_slash.split('/')
#         # print(list_without_multiple_slash)
#
#         for idx, item in enumerate(list_without_multiple_slash):
#             if not item or item == '.': # 不需要对 . 和空字符串做额外的栈操作。
#                 continue
#             if item == '..': # 实际上，栈操作只需要集中在处理 .. 时，其他情况可以简单跳过。
#                 if stack:
#                     stack.pop()
#                 else:
#                     continue
#             else:
#                 stack.append(item)
#
#         if not stack:
#             return '/'
#         result = ''
#         for item in stack:
#             result += ('/' + item) # 在 Python 中，每次字符串拼接都会创建一个新的字符串，导致了不必要的额外内存开销和性能损耗。
#         return result


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        components = path.split('/')
        # "/home//foo/".split('/') => ['', 'home', '', 'foo', '']

        for comp in components:
            if comp == '' or comp == '.':
                continue
            elif comp == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(comp)

        return '/' + '/'.join(stack)


test_cases = [
    {
        "method": "simplifyPath",
        "path": "/home/",
        "expected": "/home",
        "case_id": 1,
        "description": "Basic case with trailing slash"
    },
    {
        "method": "simplifyPath",
        "path": "/../",
        "expected": "/",
        "case_id": 2,
        "description": "Going up from root directory (no-op)"
    },
    {
        "method": "simplifyPath",
        "path": "/home//foo/",
        "expected": "/home/foo",
        "case_id": 3,
        "description": "Multiple consecutive slashes"
    },
    {
        "method": "simplifyPath",
        "path": "/a/./b/../../c/",
        "expected": "/c",
        "case_id": 4,
        "description": "Complex case with . and .. navigation"
    },
    {
        "method": "simplifyPath",
        "path": "/a/../../b/../c//.//",
        "expected": "/c",
        "case_id": 5,
        "description": "Edge case with complex navigation and redundant slashes"
    },
    {
        "method": "simplifyPath",
        "path": "/...",
        "expected": "/...",
        "case_id": 6,
        "description": "Edge case with '...' treated as directory name"
    },
    {
        "method": "simplifyPath",
        "path": "/.hidden_file",
        "expected": "/.hidden_file",
        "case_id": 7,
        "description": "Edge case with hidden file"
    },
    {
        "method": "simplifyPath",
        "path": "/a/b/c/d/./../../e/",
        "expected": "/a/b/e",
        "case_id": 8,
        "description": "Multiple directory navigation with . and .."
    }
]

run_tests()
