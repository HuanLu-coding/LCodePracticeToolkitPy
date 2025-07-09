# 637. Average of Levels in Binary Tree
# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
# Answers within 10^-5 of the actual answer will be accepted.
#
# ### Constraints:
# - The number of nodes in the tree is in the range [1, 10^4].
# - -2^31 <= Node.val <= 2^31 - 1
#
# ### Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation:
# The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].
#
# ### Example 2:
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
#
from test.test_suite import run_tests
from typing import *
from libs.tree import TreeNode
from collections import deque


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        queue = deque([root])

        while queue:
            level_sum = 0
            level_count = len(queue)

            for _ in range(level_count):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_sum / level_count)

        return result


test_cases = [
    {
        "method": "averageOfLevels",
        "root": [3, 9, 20, None, None, 15, 7],
        "expected": [3.0, 14.5, 11.0],
        "case_id": 1,
        "description": "Standard binary tree with three levels"
    },
    {
        "method": "averageOfLevels",
        "root": [3, 9, 20, 15, 7],
        "expected": [3.0, 14.5, 11.0],
        "case_id": 2,
        "description": "Standard binary tree with different structure but same averages"
    },
    {
        "method": "averageOfLevels",
        "root": [1],
        "expected": [1.0],
        "case_id": 3,
        "description": "Edge case: Single node tree"
    },
    {
        "method": "averageOfLevels",
        "root": [1, 2, 3, 4, 5, 6, 7],
        "expected": [1.0, 2.5, 5.5],
        "case_id": 4,
        "description": "Complete binary tree"
    },
    {
        "method": "averageOfLevels",
        "root": [2147483647, 2147483647],
        "expected": [2147483647.0, 2147483647.0],
        "case_id": 5,
        "description": "Edge case: Maximum integer values"
    },
    {
        "method": "averageOfLevels",
        "root": [-2147483648, -2147483648],
        "expected": [-2147483648.0, -2147483648.0],
        "case_id": 6,
        "description": "Edge case: Minimum integer values"
    },
    {
        "method": "averageOfLevels",
        "root": [1, None, 2, None, 3, None, 4, None, 5],
        "expected": [1.0, 2.0, 3.0, 4.0, 5.0],
        "case_id": 7,
        "description": "Edge case: Right-skewed tree"
    }
]

run_tests()
