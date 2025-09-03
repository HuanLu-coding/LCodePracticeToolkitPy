# 20.py
from test.test_suite import run_tests
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
<<<<<<< Updated upstream
        look_up = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        stack = deque()

        for char in s:
            if char in look_up:
                stack.append(look_up[char])  # 存入期望的匹配括号
            elif stack and stack[-1] == char:
                stack.pop()  # 匹配成功，出栈
            else:
                return False  # 不匹配直接返回 False

        return not stack  # 空栈返回 True，否则 False
=======
        lefts = list('([{')
        rights = list(')]}')
        lookups = dict(zip(rights, lefts))
        stack = deque()
        for _ in range(len(s)):
            char = s[_]
            if not (char in rights):
                stack.append(char)
            else:
                if not stack or stack.pop() != lookups[char]:
                    return False
        return True
>>>>>>> Stashed changes


test_cases = [
    {
        "method": "isValid",
        "s": "()",
        "expected": True,
        "case_id": 1
    },
    {
        "method": "isValid",
        "s": "()[]{}",
        "expected": True,
        "case_id": 2
    },
    {
        "method": "isValid",
        "s": "(]",
        "expected": False,
        "case_id": 3
    },
    {
        "method": "isValid",
        "s": "([)]",
        "expected": False,
        "case_id": 4
    },
    {
        "method": "isValid",
        "s": "{[]}",
        "expected": True,
        "case_id": 5
    },
    {
        "method": "isValid",
        "s": "(((((((((())))))))))",
        "expected": True,
        "case_id": 6
    }
]

run_tests()
