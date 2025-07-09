# 144.py
from typing import *

from libs.tree import TreeNode
from test.test_suite import run_tests
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        result = deque()
        self.preorder(root, result)
        return list(result)

    def preorder(self, node: Optional[TreeNode], result: list) -> None:
        if not node:
            return
        result.append(node.val)
        self.preorder(node.left, result)
        self.preorder(node.right, result)


test_cases = [
    {
        "method": "preorderTraversal",
        "root": [1, None, 2, 3],
        "expected": [1, 2, 3],
        "case_id": 1,
        "description": "Regular case with a right-heavy binary tree"
    },
    {
        "method": "preorderTraversal",
        "root": [],
        "expected": [],
        "case_id": 2,
        "description": "Edge case with an empty tree"
    },
    {
        "method": "preorderTraversal",
        "root": [1],
        "expected": [1],
        "case_id": 3,
        "description": "Edge case with a single-node tree"
    },
    {
        "method": "preorderTraversal",
        "root": [1, 2, 3, 4, 5],
        "expected": [1, 2, 4, 5, 3],
        "case_id": 4,
        "description": "Full binary tree of height 2"
    },
    {
        "method": "preorderTraversal",
        "root": [1, 2, None, 3],
        "expected": [1, 2, 3],
        "case_id": 5,
        "description": "Left-skewed tree (edge case)"
    },
    {
        "method": "preorderTraversal",
        "root": [1, None, 2, None, 3],
        "expected": [1, 2, 3],
        "case_id": 6,
        "description": "Right-skewed tree (edge case)"
    }
]

run_tests()
