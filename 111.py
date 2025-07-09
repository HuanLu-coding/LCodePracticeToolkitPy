# 111. Minimum Depth of Binary Tree
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
#
# ### Constraints:
# - The number of nodes in the tree is in the range `[0, 10^5]`.
# - `-1000 <= Node.val <= 1000`
#
# ### Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
#
# ### Example 2:
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

from test.test_suite import run_tests
from typing import *
from libs.tree import TreeNode


# 时间复杂度
#
# BFS解法：O(n)，每个节点最多访问一次
# DFS解法：O(n)，每个节点最多访问一次
#
# 空间复杂度
#
# BFS解法：O(w)，w为树的最大宽度，最坏情况为O(n/2)≈O(n)
# DFS解法：O(h)，h为树的高度，最坏情况为O(n)，平衡树为O(log n)
# class Solution:
#     # 对于题目约束[0, 10 ^ 5]节点数：
#     #
#     # 宽树情况：BFS可能在队列中存储大量节点，接近最坏情况O(n)
#     # 深树情况：DFS递归栈可能很深，但通常小于BFS队列大小
#     #
#     # 递归风险
#     # DFS递归解法在树高接近10 ^ 5时可能面临栈溢出风险，而BFS迭代解法不存在此风险。
#     # （最优解）BFS版
#     # 对于最小深度问题，BFS通常是更优解
#     # BFS找到的第一个叶子节点就是答案，避免了不必要的遍历
#
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#         from collections import deque
#
#         if not root:
#             return 0
#         queue = deque([(root, 1)])
#         while queue:
#             node, depth = queue.popleft()
#             if not node.left and not node.right:
#                 return depth
#             if node.left:
#                 queue.append((node.left, depth + 1))
#             if node.right:
#                 queue.append((node.right, depth + 1))

# # 人类DFS版
# def minDepth(self, root: Optional[TreeNode]) -> int:
#     if not root: return 0
#     left_min_depth = self.minDepth(root.left)
#     right_min_depth = self.minDepth(root.right)
#     if left_min_depth == 0 and right_min_depth > 0:
#         return right_min_depth + 1
#     elif left_min_depth > 0 and right_min_depth == 0:
#         return left_min_depth + 1
#     else:
#         return min(left_min_depth, right_min_depth) + 1
#
# #AI另一版：
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: empty node
        if not root:
            return 0
        # Leaf node: no children
        if not root.left and not root.right:
            return 1
        # Only right child exists
        if not root.left:
            return 1 + self.minDepth(root.right)
        # Only left child exists
        if not root.right:
            return 1 + self.minDepth(root.left)
        # Both children exist
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
    # # AI的DFS版
    # def minDepth(self, root):
    #     if not root:
    #         return 0
    #
    #     # If one child is missing, we must take the path through the other child.
    #     if not root.left:
    #         return 1 + self.minDepth(root.right)
    #     if not root.right:
    #         return 1 + self.minDepth(root.left)
    #
    #     # Both children exist, return the minimum of the two paths
    #     return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


test_cases = [
    {
        "method": "minDepth",
        "root": [3, 9, 20, None, None, 15, 7],
        "expected": 2,
        "case_id": 1,
        "description": "Standard tree with minimum depth on left branch"
    },
    {
        "method": "minDepth",
        "root": [2, None, 3, None, 4, None, 5, None, 6],
        "expected": 5,
        "case_id": 2,
        "description": "Right-skewed tree with only one path"
    },
    {
        "method": "minDepth",
        "root": [],
        "expected": 0,
        "case_id": 3,
        "description": "Empty tree (edge case)"
    },
    {
        "method": "minDepth",
        "root": [1],
        "expected": 1,
        "case_id": 4,
        "description": "Single node tree (edge case)"
    },
    {
        "method": "minDepth",
        "root": [1, 2],
        "expected": 2,
        "case_id": 5,
        "description": "Tree with only left child"
    },
    {
        "method": "minDepth",
        "root": [1, None, 2],
        "expected": 2,
        "case_id": 6,
        "description": "Tree with only right child"
    },
    {
        "method": "minDepth",
        "root": [1, 2, 3, 4, 5, 6, 7],
        "expected": 3,
        "case_id": 7,
        "description": "Perfect binary tree with all levels filled"
    }
]

run_tests()
