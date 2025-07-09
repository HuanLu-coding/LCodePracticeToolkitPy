# 257.py
from test.test_suite import run_tests
from libs.tree import TreeNode
from typing import *


# 257. Binary Tree Paths

# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.

# ### Constraints:
# - The number of nodes in the tree is in the range [0, 100].
# - -100 ≤ Node.val ≤ 100

# ### Example 1:
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

# ### Example 2:
# Input: root = [1]
# Output: ["1"]

# ### Example 3:
# Input: root = []
# Output: []


# DFS+回溯
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        if not root:
            return []

        paths = []

        def backtrack(node: TreeNode, current_path: list[str]):
            # 将当前节点值加入路径
            current_path.append(str(node.val))

            # 如果是叶子节点，记录完整路径
            if not node.left and not node.right:
                paths.append("->".join(current_path))

            # 递归遍历左子树
            if node.left:
                backtrack(node.left, current_path)

            # 递归遍历右子树
            if node.right:
                backtrack(node.right, current_path)

            # 回溯：移除当前节点，恢复状态
            current_path.pop()

        backtrack(root, [])
        return paths


#
# # Python 中字符串是不可变对象。此解法通过值传递（Pass by Value）而非引用传递，天然实现回溯效果，无需显式回溯操作。
# class Solution:
#     def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#         def dfs(node, path):
#             if not node:
#                 return
#             path += str(node.val)
#             if not node.left and not node.right:  # 叶子节点
#                 paths.append(path)
#             else:
#                 path += "->"
#                 dfs(node.left, path)
#                 dfs(node.right, path)
#
#         paths = []
#         dfs(root, "")
#         return paths
# 递归隔离性：每次递归调用传入新字符串对象，各层路径独立
#
# 自动状态回退：递归返回时，上层路径字符串未被修改（天然回溯）
#
# 叶子节点处理：直接捕获完整路径，无后续干扰
#
# 潜在缺陷
# 高空间开销：深度 h 的链状树需存储 1+2+...+h = O(h²) 的字符串
#
# 性能瓶颈：节点数 n=100 时，最坏空间 100²=10,000 字符（仍可接受，但非最优）

# BFS（使用队列）
# from collections import deque
#
#
# class Solution:
#     def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#         if not root:
#             return []
#         paths = []
#         queue = deque([(root, str(root.val))])
#         while queue:
#             node, path = queue.popleft()
#             if not node.left and not node.right:
#                 paths.append(path)
#             if node.left:
#                 queue.append((node.left, path + "->" + str(node.left.val)))
#             if node.right:
#                 queue.append((node.right, path + "->" + str(node.right.val)))
#         return paths


test_cases = [
    {
        "method": "binaryTreePaths",
        "root": [1, 2, 3, None, 5],
        "expected": ["1->2->5", "1->3"],
        "case_id": 1,
        "description": "Tree with two branches and one leaf missing"
    },
    {
        "method": "binaryTreePaths",
        "root": [1],
        "expected": ["1"],
        "case_id": 2,
        "description": "Single node tree"
    },
    {
        "method": "binaryTreePaths",
        "root": [],
        "expected": [],
        "case_id": 3,
        "description": "Empty tree (edge case)"
    },
    {
        "method": "binaryTreePaths",
        "root": [1, 2, None, 3, None, 4, None],
        "expected": ["1->2->3->4"],
        "case_id": 4,
        "description": "Left-skewed tree"
    },
    {
        "method": "binaryTreePaths",
        "root": [1, None, 2, None, 3, None, 4],
        "expected": ["1->2->3->4"],
        "case_id": 5,
        "description": "Right-skewed tree"
    },
    {
        "method": "binaryTreePaths",
        "root": [1, 2, 3, 4, 5, 6, 7],
        "expected": [
            "1->2->4",
            "1->2->5",
            "1->3->6",
            "1->3->7"
        ],
        "case_id": 6,
        "description": "Full binary tree"
    }
]

run_tests()
