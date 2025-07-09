# 94.py
from test.test_suite import run_tests
from typing import *
from libs.tree import TreeNode
from collections import deque


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []  # 存储遍历结果
        stack = deque()  # 用deque模拟栈
        current = root  # 从根节点开始

        # 当栈不为空，或者当前节点不为空时，继续遍历
        while current or stack:
            # 一直向左子树遍历，直到最左边的节点
            while current:
                stack.append(current)  # 将当前节点压入栈
                current = current.left  # 向左子树移动

            # 取出栈顶元素，访问该节点
            current = stack.pop()  # 弹出栈顶元素
            result.append(current.val)  # 将该节点的值添加到结果中

            # 访问右子树
            current = current.right  # 向右子树移动

        return result


# def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#     result = []
#
#     def traverse(node: Optional[TreeNode]):
#         if not node:
#             return
#
#         traverse(node.left)
#
#         result.append(node.val)
#
#         traverse(node.right)
#
#     traverse(root)
#     return result


test_cases = [
    {
        "method": "inorderTraversal",
        "root": [1, None, 2, 3],
        "expected": [1, 3, 2],
        "case_id": 1,
        "description": "Standard binary tree with left None"
    },
    {
        "method": "inorderTraversal",
        "root": [],
        "expected": [],
        "case_id": 2,
        "description": "Empty tree"
    },
    {
        "method": "inorderTraversal",
        "root": [1],
        "expected": [1],
        "case_id": 3,
        "description": "Single node tree"
    },
    {
        "method": "inorderTraversal",
        "root": [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9],
        "expected": [4, 2, 6, 5, 7, 1, 3, 9, 8],
        "case_id": 4,
        "description": "LeetCode example"
    }
]
run_tests()
