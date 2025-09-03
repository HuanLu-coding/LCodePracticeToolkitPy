# 155. Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# Implement the MinStack class:
# - MinStack() initializes the stack object.
# - void push(int val) pushes the element val onto the stack.
# - void pop() removes the element on the top of the stack.
# - int top() gets the top element of the stack.
# - int getMin() retrieves the minimum element in the stack.
#
# You must implement a solution with O(1) time complexity for each function.
#
# ### Constraints:
# - `-2^31 <= val <= 2^31 - 1`
# - Methods `pop`, `top` and `getMin` operations will always be called on non-empty stacks.
# - At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.
#
# ### Example 1:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# Output
# [null,null,null,null,-3,null,0,-2]
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

from test.test_suite import run_tests
from typing import *


class MinStack:
    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

test_cases = [
    {
        "method": ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
        "params": [[], [-2], [0], [-3], [], [], [], []],
        "expected": [None, None, None, None, -3, None, 0, -2],
        "case_id": 1,
        "description": "Basic operations as described in example"
    },
    {
        "method": ["MinStack", "push", "getMin", "push", "getMin", "push", "getMin", "pop", "getMin"],
        "params": [[], [-10], [], [-20], [], [-30], [], [], []],
        "expected": [None, None, -10, None, -20, None, -30, None, -20],
        "case_id": 2,
        "description": "Descending values with min tracking after pop"
    },
    {
        "method": ["MinStack", "push", "push", "push", "push", "getMin", "pop", "getMin", "pop", "getMin", "pop",
                   "getMin"],
        "params": [[], [5], [2], [3], [1], [], [], [], [], [], [], []],
        "expected": [None, None, None, None, None, 1, None, 2, None, 2, None, 5],
        "case_id": 3,
        "description": "Mixed values with consecutive pops"
    },
    {
        "method": ["MinStack", "push", "push", "push", "top", "pop", "top", "pop", "top", "pop"],
        "params": [[], [1], [2], [3], [], [], [], [], [], []],
        "expected": [None, None, None, None, 3, None, 2, None, 1, None],
        "case_id": 4,
        "description": "Edge case: Testing LIFO property with consecutive top and pop operations"
    },
    {
        "method": ["MinStack", "push", "push", "getMin", "push", "push", "getMin", "push", "getMin", "pop", "getMin"],
        "params": [[], [2147483647], [-2147483648], [], [1], [-1], [], [2147483647], [], [], []],
        "expected": [None, None, None, -2147483648, None, None, -2147483648, None, -2147483648, None, -2147483648],
        "case_id": 5,
        "description": "Edge case: Testing with integer limits (max and min values)"
    },
    {
        "method": ["MinStack", "push", "push", "push", "push", "pop", "pop", "pop", "push", "getMin", "top"],
        "params": [[], [42], [42], [42], [42], [], [], [], [10], [], []],
        "expected": [None, None, None, None, None, None, None, None, None, 10, 10],
        "case_id": 6,
        "description": "Edge case: Multiple identical values followed by push after pops"
    }
]

run_tests()
