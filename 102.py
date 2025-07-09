# 102.py
from test.test_suite import run_tests
from typing import *
from libs.tree import TreeNode

from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            # Get number of nodes in current level
            level_size = len(queue)
            # Store values of current level
            level_values = []

            # Process all nodes in current level
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_values)

        return result


test_cases = [
    {
        "method": "levelOrder",
        "root": [3, 9, 20, None, None, 15, 7],
        "expected": [[3], [9, 20], [15, 7]],
        "case_id": 1,
        "description": "Standard binary tree with multiple levels"
    },
    {
        "method": "levelOrder",
        "root": [1],
        "expected": [[1]],
        "case_id": 2,
        "description": "Single node tree"
    },
    {
        "method": "levelOrder",
        "root": [],
        "expected": [],
        "case_id": 3,
        "description": "Empty tree"
    },
    {
        "method": "levelOrder",
        "root": [1, 2, 3, 4, 5, 6, 7],
        "expected": [[1], [2, 3], [4, 5, 6, 7]],
        "case_id": 4,
        "description": "Complete binary tree with three levels"
    },
    {
        "method": "levelOrder",
        "root": [1, None, 2, None, 3, None, 4, None, 5],
        "expected": [[1], [2], [3], [4], [5]],
        "case_id": 5,
        "description": "Right-skewed tree with increasing depth"
    },
    {
        "method": "levelOrder",
        "root": [1, 2, None, 3, None, 4, None, 5],
        "expected": [[1], [2], [3], [4], [5]],
        "case_id": 6,
        "description": "Left-skewed tree with increasing depth"
    }
]

run_tests()
