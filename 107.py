# 107. Binary Tree Level Order Traversal II
# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.
# (i.e., from left to right, level by level from leaf to root).
#
# ### Constraints:
# - The number of nodes in the tree is in the range `[0, 2000]`.
# - `-1000 <= Node.val <= 1000`
#
# ### Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]
#
# ### Example 2:
# Input: root = [1]
# Output: [[1]]
#
# ### Example 3:
# Input: root = []
# Output: []

from test.test_suite import run_tests
from typing import *
from libs.tree import TreeNode
from collections import deque


# 方法一 (先正后反):
# 最直接的想法是，不管三七二十一，先用标准的 BFS 得到一个 从上到下 的层序遍历结果
# 然后，把这个结果列表 整个反转 一下，就正好满足要求！简单粗暴有效。

#
#
#
# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:
#         if not root:
#             return []
#         queue = deque([root])  # 初始化队列
#         result = []
#
#         while queue:
#             level_size = len(queue)
#             current_level = []
#             for _ in range(level_size):
#                 node = queue.popleft()  # 弹出当前层节点
#                 current_level.append(node.val)
#                 if node.left:
#                     queue.append(node.left)  # 左子节点入队
#                 if node.right:
#                     queue.append(node.right)  # 右子节点入队
#             result.append(current_level)  # 保存当前层结果
#         return result[::-1]  # 反转结果

# 最优解: 解法二 (BFS + Prepend using deque)
# 在时间和空间复杂度上都达到了最优的 O(N)，
# 并且通过 deque.appendleft() 的技巧，巧妙地在一次遍历中就生成了题目要求的自底向上的顺序，
# 避免了解法一和解法三中额外的反转步骤。这使得它在逻辑上更直接，代码也可能更简洁（少了一步反转）。


class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        """
        解法二：BFS 层序遍历，每次将当前层结果插入到结果列表的开头。
                使用 deque 作为结果容器以实现 O(1) 的头部插入。
        """
        if not root:
            return []

        # 使用 deque 来存储最终结果，方便 O(1) 头部插入
        result_deque = deque()
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level_vals = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level_vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # 将当前层结果从左边（头部）插入 result_deque
            result_deque.appendleft(current_level_vals)

        # 将 deque 转换为 list 返回
        return list(result_deque)


# 解法三 (DFS + Reverse)
# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:
#         result = []
#
#         def dfs(node, level):
#             if not node:
#                 return
#             if level == len(result):  # 当前层未初始化
#                 result.append([])
#             result[level].append(node.val)  # 将节点值加入对应层
#             dfs(node.left, level + 1)  # 递归左子树
#             dfs(node.right, level + 1)  # 递归右子树
#
#         dfs(root, 0)
#         return result[::-1]  # 反转结果


test_cases = [
    {
        "method": "levelOrderBottom",
        "root": [3, 9, 20, None, None, 15, 7],
        "expected": [[15, 7], [9, 20], [3]],
        "case_id": 1,
        "description": "Standard binary tree"
    },
    {
        "method": "levelOrderBottom",
        "root": [1],
        "expected": [[1]],
        "case_id": 2,
        "description": "Single node tree"
    },
    {
        "method": "levelOrderBottom",
        "root": [],
        "expected": [],
        "case_id": 3,
        "description": "Empty tree"
    },
    {
        "method": "levelOrderBottom",
        "root": [1, 2, 3, 4, 5],
        "expected": [[4, 5], [2, 3], [1]],
        "case_id": 4,
        "description": "Complete binary tree with three levels"
    },
    {
        "method": "levelOrderBottom",
        "root": [1, 2, None, 3, None, 4],
        "expected": [[4], [3], [2], [1]],
        "case_id": 5,
        "description": "Left-skewed tree (edge case)"
    },
    {
        "method": "levelOrderBottom",
        "root": [1, None, 2, None, 3, None, 4],
        "expected": [[4], [3], [2], [1]],
        "case_id": 6,
        "description": "Right-skewed tree (edge case)"
    },
    {
        "method": "levelOrderBottom",
        "root": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "expected": [[8, 9, 10, 11, 12, 13, 14, 15], [4, 5, 6, 7], [2, 3], [1]],
        "case_id": 7,
        "description": "Complete binary tree with four levels (edge case)"
    }
]

run_tests()
