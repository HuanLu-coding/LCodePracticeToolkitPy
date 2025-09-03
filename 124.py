# 124.py
from test.test_suite import run_tests

from typing import Optional
from libs.tree import TreeNode, tree_to_list


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # def maxPathSum(self, root: TreeNode) -> int:
    #     # --- 全局最大路径和，初始化为根节点值，防止全是负数遗漏 ---
    #     self.global_max_path_sum = root.val
    #
    #     # --- 定义递归函数：计算以节点为起点的最大单边路径和 ---
    #     def max_single_path_gain(node):
    #         # 边界：空节点贡献为 0
    #         if node is None:
    #             return 0
    #
    #         # 1. 递归获取左右子树的最大单边贡献，负数舍弃
    #         left_subtree_gain = max(max_single_path_gain(node.left), 0)
    #         right_subtree_gain = max(max_single_path_gain(node.right), 0)
    #
    #         # 2. 计算以当前节点为顶点的最大路径和（左+当前+右）
    #         current_node_max_path = node.val + left_subtree_gain + right_subtree_gain
    #
    #         # 3. 更新全局最大路径和
    #         self.global_max_path_sum = max(self.global_max_path_sum, current_node_max_path)
    #
    #         # 4. 返回以当前节点为起点的最大单边路径和（当前+max(左,右)）
    #         return node.val + max(left_subtree_gain, right_subtree_gain)
    #
    #     max_single_path_gain(root)
    #
    #     return self.global_max_path_sum

    # 为了避免全局变量，我们可以用元组返回每个子树的最大单边路径和与全局最大路径和。
    # 递归 + 返回元组

    def maxPathSum(self, root: TreeNode) -> int:
        def max_gain(node):
            if not node:
                return (0, float('-inf'))  # (单边最大，全局最大)

            left_single, left_global = max_gain(node.left)
            right_single, right_global = max_gain(node.right)

            # 单边最大贡献，负数舍弃
            left_single = max(left_single, 0)
            right_single = max(right_single, 0)

            # 当前节点作为顶点的最大路径和
            current_path_sum = node.val + left_single + right_single

            # 当前子树的全局最大值
            global_max = max(current_path_sum, left_global, right_global)

            # 返回以当前节点为起点的单边最大值
            single_max = node.val + max(left_single, right_single)

            return (single_max, global_max)

        _, result = max_gain(root)
        return result


# #124类似问题列表
#
# LeetCode #543 - Diameter of Binary Tree（二叉树的直径）
# 难度：Easy（但常被改编为 Hard）
# 描述：求二叉树中任意两节点间的最长路径长度。
# 与 #124 相似点：需要递归计算树的高度，同时记录全局最大值，涉及路径和的计算。
# 来源依据：LeetCode “Top Google Questions” 列表及 Reddit /r/leetcode 讨论。
# 出现公司：Google、Amazon。
# LeetCode #337 - House Robber III（打家劫舍 III）
# 难度：Medium
# 描述：在二叉树中选择不相邻节点的最大和。
# 与 #124 相似点：树上的动态规划，递归计算子树贡献，需处理全局最优解。
# 来源依据：LeetCode “Top Amazon Questions” 及 Medium 博客文章。
# 出现公司：Amazon、Meta。
# LeetCode #687 - Longest Univalue Path（最长同值路径）
# 难度：Medium
# 描述：找二叉树中最长的路径，其中所有节点值相同。
# 与 #124 相似点：递归遍历树，维护全局最大路径长度，处理单边与双边路径。
# 来源依据：LeetCode 社区讨论及 Quora 帖子。
# 出现公司：Google。
# LeetCode #236 - Lowest Common Ancestor of a Binary Tree（二叉树的最近公共祖先）
# 难度：Medium
# 描述：找到二叉树中两个节点的最近公共祖先。
# 与 #124 相似点：涉及树路径的分析，递归处理子树关系。
# 来源依据：LeetCode “Top Meta Questions” 及 Hacker News。
# 出现公司：Meta、Google。
# LeetCode #968 - Binary Tree Cameras（二叉树监控）
# 难度：Hard
# 描述：在二叉树中放置最少摄像头覆盖所有节点。
# 与 #124 相似点：树上的动态规划，递归计算子树状态，需全局优化。
# 来源依据：LeetCode 讨论区及 TeamRora 面试分析。
# 出现公司：Amazon。
# LeetCode #297 - Serialize and Deserialize Binary Tree（二叉树的序列化与反序列化）
# 难度：Hard
# 描述：将二叉树序列化为字符串并反序列化还原。
# 与 #124 相似点：深入理解树结构，递归处理节点关系。
# 来源依据：LeetCode “Top Google Questions” 及 Quora。
# 出现公司：Google、Meta。
# LeetCode #1048 - Longest String Chain（最长字符串链）
# 难度：Medium（但常与树问题结合）
# 描述：从单词列表中找出最长的递增链。
# 与 #124 相似点：动态规划思想，可改编为树形依赖问题。
# 来源依据：LeetCode “Top Amazon Questions”。
# 出现公司：Amazon。

test_cases = [
    {
        "method": "maxPathSum",
        "root": [1, 2, 3],
        "expected": 6,
        "case_id": 1,
        "description": "Standard tree with all positive nodes"
    },
    {
        "method": "maxPathSum",
        "root": [-10, 9, 20, None, None, 15, 7],
        "expected": 42,
        "case_id": 2,
        "description": "Mixed negative and positive values where the optimal path does not include the root"
    },
    {
        "method": "maxPathSum",
        "root": [5],
        "expected": 5,
        "case_id": 3,
        "description": "Edge case: Single node tree with positive value"
    },
    {
        "method": "maxPathSum",
        "root": [-3],
        "expected": -3,
        "case_id": 4,
        "description": "Edge case: Single node tree with negative value"
    },
    {
        "method": "maxPathSum",
        "root": [2, -1],
        "expected": 2,
        "case_id": 5,
        "description": "Tree with only left child where adding the negative value reduces the overall sum"
    },
    {
        "method": "maxPathSum",
        "root": [2, None, 3],
        "expected": 5,
        "case_id": 6,
        "description": "Tree with only right child"
    },
    {
        "method": "maxPathSum",
        "root": [1, 2, 3, 4, 5, 6, 7],
        "expected": 18,
        "case_id": 7,
        "description": "Complete binary tree with multiple levels; optimal path is 5 -> 2 -> 1 -> 3 -> 7"
    }
]
run_tests()
