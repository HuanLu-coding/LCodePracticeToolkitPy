# 103.py
from test.test_suite import run_tests

# 103. Binary Tree Zigzag Level Order Traversal

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
# (i.e., from left to right, then right to left for the next level and alternate between).
#
# ### Constraints:
# - The number of nodes in the tree is in the range [0, 2000].
# - -100 ≤ Node.val ≤ 100
#
# ### Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
#
# ### Example 2:
# Input: root = [1]
# Output: [[1]]
#
# ### Example 3:
# Input: root = []
# Output: []

from libs.tree import TreeNode
from collections import deque
from typing import *


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        results = []  # 结果列表在主方法作用域内定义和修改
        queue = deque([root])
        left_to_right = True
        # BFS 逻辑直接在主方法中展开
        while queue:
            level_size = len(queue)
            current_level = deque()
            for _ in range(level_size):
                node = queue.popleft()
                if left_to_right:
                    current_level.append(node.val)
                else:
                    current_level.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(list(current_level))
            left_to_right = not left_to_right
        return results  # 返回在同一作用域内构建的 results


test_cases = [
    {
        "method": "zigzagLevelOrder",
        "root": [3, 9, 20, None, None, 15, 7],
        "expected": [[3], [20, 9], [15, 7]],
        "case_id": 1,
        "description": "Typical binary tree with three levels in zigzag order"
    },
    {
        "method": "zigzagLevelOrder",
        "root": [1],
        "expected": [[1]],
        "case_id": 2,
        "description": "Single node tree (edge case)"
    },
    {
        "method": "zigzagLevelOrder",
        "root": [],
        "expected": [],
        "case_id": 3,
        "description": "Empty tree (edge case)"
    },
    {
        "method": "zigzagLevelOrder",
        "root": [1, 2, None, 3, None, 4],
        "expected": [[1], [2], [3], [4]],
        "case_id": 4,
        "description": "Left-skewed tree (edge case, all nodes only on left)"
    },
    {
        "method": "zigzagLevelOrder",
        "root": [1, None, 2, None, 3, None, 4],
        "expected": [[1], [2], [3], [4]],
        "case_id": 5,
        "description": "Right-skewed tree (edge case, all nodes only on right)"
    },
    {
        "method": "zigzagLevelOrder",
        "root": [1, 2, 3, 4, 5, 6, 7],
        "expected": [[1], [3, 2], [4, 5, 6, 7]],
        "case_id": 6,
        "description": "Complete binary tree with perfect zigzag structure"
    }
]

run_tests()
