# 515. Find Largest Value in Each Tree Row
# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
#
# ### Constraints:
# - The number of nodes in the tree will be in the range [0, 10^4].
# - -2^31 <= Node.val <= 2^31 - 1
#
# ### Example 1:
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
# Explanation:
# The first row has only the root node with value 1, so the result is [1].
# The second row has nodes with values 3 and 2, so the largest value is 3.
# The third row has nodes with values 5, 3, and 9, so the largest value is 9.
#
# ### Example 2:
# Input: root = [1,2,3]
# Output: [1,3]
# Explanation:
# The first row has only the root node with value 1, so the result is [1].
# The second row has nodes with values 2 and 3, so the largest value is 3.
#
import math
from typing import Any

from test.test_suite import run_tests
from typing import *
from libs.tree import TreeNode
from collections import deque


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            max_val = float('-inf')

            for _ in range(level_size):
                node = queue.popleft()
                max_val = max(max_val, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(max_val)

        return result


test_cases = [
    {
        "method": "largestValues",
        "root": [1, 3, 2, 5, 3, None, 9],
        "expected": [1, 3, 9],
        "case_id": 1,
        "description": "Standard binary tree with three levels"
    },
    {
        "method": "largestValues",
        "root": [1, 2, 3],
        "expected": [1, 3],
        "case_id": 2,
        "description": "Simple binary tree with two levels"
    },
    {
        "method": "largestValues",
        "root": [],
        "expected": [],
        "case_id": 3,
        "description": "Edge case: Empty tree"
    },
    {
        "method": "largestValues",
        "root": [1],
        "expected": [1],
        "case_id": 4,
        "description": "Edge case: Single node tree"
    },
    {
        "method": "largestValues",
        "root": [1, None, 2, None, 3, None, 4, None, 5],
        "expected": [1, 2, 3, 4, 5],
        "case_id": 5,
        "description": "Edge case: Right-skewed tree"
    },
    {
        "method": "largestValues",
        "root": [-1, -2, -3, -4, -5, -6, -7],
        "expected": [-1, -2, -4],
        "case_id": 6,
        "description": "Tree with all negative values"
    },
    {
        "method": "largestValues",
        "root": [2147483647, 2147483647, 2147483647],
        "expected": [2147483647, 2147483647],
        "case_id": 7,
        "description": "Tree with maximum integer values"
    }
]

run_tests()
