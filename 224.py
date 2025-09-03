# 224. Basic Calculator

# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
#
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
#
# ### Constraints:
# - 1 <= s.length <= 3 * 10^5
# - s consists of digits, '+', '-', '(', ')', and ' '.
# - s represents a valid expression.
# - '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" are invalid).
# - '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" are valid).
# - There will be no two consecutive operators in the input.
# - Every number and running calculation will fit in a signed 32-bit integer.
#
# ### Example 1:
# Input: s = "1 + 1"
# Output: 2
#
# ### Example 2:
# Input: s = " 2-1 + 2 "
# Output: 3
#
# ### Example 3:
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23

from test.test_suite import run_tests
from typing import *
from operator import add, sub, mul


# 复杂了，其实可以直接用一个 res 累加，中间用栈保存括号前的结果和符号。
# class Solution:
#     def calculate(self, s: str) -> int:
#         stack = []
#         n = len(s)
#         for idx, s in enumerate(s):
#             if s == ')':
#                 sub_exp = []
#                 new_poped = stack.pop()
#                 while new_poped != '(' and stack:
#                     sub_exp.append(new_poped)
#                     new_poped = stack.pop()
#
#                 stack.append(self.evaluate(sub_exp))
#                 continue
#
#     def evaluate(self, opts: list(str)) -> str:
#         if len(opts) == 2:
#             return str(mul(-1, opts[1]))
#         if len(opts) == 3:
#             if opts[1] == '+':
#                 return str(add(opts[0], opts[2]))
#             else:
#                 return str(sub(opts[0], opts[2]))


# 思路整体是对的，大致步骤是：
# 	•	用栈保存遍历到的内容；
# 	•	遇到 ')'，弹出一段子表达式，计算后把结果压回栈里；
# 	•	遇到数字，要处理多位数（比如 “12” 不是两个 “1”、“2”，而是一个整体）；
# 	•	遇到符号 '+'、'-'，直接压栈。
# 问题有：
# 	1.	没处理多位数。
# 	2.	list(str) 写错了，应该是 list[str]。
# 	3.	evaluate 拿到的是逆序，需要翻转回来。

# class Solution:
#     def calculate(self, s: str) -> int:
#         stack = []
#         num = 0
#         sign = 1  # 当前符号，1表示正，-1表示负
#         result = 0
#
#         for char in s:
#             if char.isdigit():
#                 num = num * 10 + int(char)
#             elif char == '+':
#                 result += sign * num
#                 num = 0
#                 sign = 1
#             elif char == '-':
#                 result += sign * num
#                 num = 0
#                 sign = -1
#             elif char == '(':
#                 stack.append(result)
#                 stack.append(sign)
#                 result = 0
#                 sign = 1
#             elif char == ')':
#                 result += sign * num
#                 num = 0
#                 result *= stack.pop()  # 之前的符号
#                 result += stack.pop()  # 之前的结果
#             # 遇到空格就跳过
#         result += sign * num
#         return result

class Solution:
    def calculate(self, s: str) -> int:
        num_stack = []
        op_stack = []
        i = 0
        s = s.replace(' ', '')  # 移除空格

        def apply_op():
            if len(op_stack) == 0 or len(num_stack) < 2:
                return
            op = op_stack.pop()
            b = num_stack.pop()
            a = num_stack.pop()
            if op == '+':
                num_stack.append(a + b)
            elif op == '-':
                num_stack.append(a - b)

        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                num_stack.append(num)
                continue
            elif s[i] == '(':
                op_stack.append(s[i])
            elif s[i] in '+-':
                # 立即应用之前的操作，确保左到右顺序
                while op_stack and op_stack[-1] in '+-':
                    apply_op()
                op_stack.append(s[i])
            elif s[i] == ')':
                # 处理括号内所有操作
                while op_stack and op_stack[-1] != '(':
                    apply_op()
                if op_stack:  # 弹出 '('
                    op_stack.pop()
            i += 1

        # 处理剩余操作
        while op_stack:
            apply_op()

        return num_stack[0] if num_stack else 0


test_cases = [
    {
        "method": "calculate",
        "s": "1 + 1",
        "expected": 2,
        "case_id": 1,
        "description": "Simple addition"
    },
    {
        "method": "calculate",
        "s": " 2-1 + 2 ",
        "expected": 3,
        "case_id": 2,
        "description": "Mixed addition and subtraction with spaces"
    },
    {
        "method": "calculate",
        "s": "(1+(4+5+2)-3)+(6+8)",
        "expected": 23,
        "case_id": 3,
        "description": "Nested parentheses"
    },
    {
        "method": "calculate",
        "s": "- (3 + (2 - 1))",
        "expected": -4,
        "case_id": 4,
        "description": "Unary minus with nested parentheses"
    },
    {
        "method": "calculate",
        "s": "2147483647",
        "expected": 2147483647,
        "case_id": 5,
        "description": "Maximum 32-bit signed integer"
    },
    {
        "method": "calculate",
        "s": "-( -2)+4",
        "expected": 6,
        "case_id": 6,
        "description": "Double negative with unary minus"
    }
]

run_tests()
