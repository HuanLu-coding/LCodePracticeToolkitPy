# 110. Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced.
#
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
#
# ### Constraints:
# - The number of nodes in the tree is in the range `[0, 5000]`.
# - `-100 <= Node.val <= 100`
#
# ### Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#
# ### Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#
# ### Example 3:
# Input: root = []
# Output: true

from test.test_suite import run_tests
from typing import *
from libs.tree import TreeNode


# 最优解: 采用自底向上的递归，一次遍历中同时完成高度计算和平衡性检查。如果发现不平衡，会立即停止相关子树的计算并向上传递信号。
# 将高度计算和平衡检查合并到一个辅助函数中，利用返回值 -1 传递平衡状态。
# 所有情况归纳为一个通用公式：
# 节点高度 = max(左子树高度, 右子树高度) + 1
# 空节点高度 = 0
#
#
# 最优解只处理了一种基本情况：if not node: return 0（空节点高度为0）
# 这个单一判断已经足够处理所有基本情况:
# 1. 叶子节点自动处理：
# 当遇到叶子节点时（即 node.left 和 node.right 都为 None）
# 左右子树高度都会返回 0（通过基本情况的判断）
# 然后计算 max(0, 0) + 1 = 1，正确返回叶子节点高度
#
# 2. 单子节点自动处理：
# 当只有一个子节点时（例如 node.left 为 None，node.right 不为 None）
# 空的那侧会返回 0
# 有节点的那侧会返回其实际高度
# 最终计算 max(0, 实际高度) + 1，得到正确结果
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self._get_height_if_balanced(root) != -1

    def _get_height_if_balanced(self, node: Optional[TreeNode]) -> int:
        """
        功能：计算以 node 为根的子树的高度，同时检查其是否平衡。
        返回值：
        - 如果子树平衡，返回其真实高度（非负整数）。
        - 如果子树不平衡（自身或其任意子孙不平衡），返回 -1。
        """
        # 基本情况：空节点高度为 0，是平衡的。
        if not node: return 0

        # 递归获取子树的高度/平衡状态
        left_height = self._get_height_if_balanced(node.left)
        # 如果子树已报告不平衡，则立即向上传递不平衡信号 (-1)
        if left_height == -1:
            return -1

        right_height = self._get_height_if_balanced(node.right)
        if right_height == -1:
            return -1

        # 检查当前节点的左右子树高度差
        if abs(left_height - right_height) > 1:
            # 当前节点不平衡，返回不平衡信号 (-1)
            return -1
        else:
            # 当前节点平衡，返回其真实高度
            return max(left_height, right_height) + 1


test_cases = [
    {
        "method": "isBalanced",
        "root": [3, 9, 20, None, None, 15, 7],
        "expected": True,
        "case_id": 1,
        "description": "Balanced binary tree"
    },
    {
        "method": "isBalanced",
        "root": [1, 2, 2, 3, 3, None, None, 4, 4],
        "expected": False,
        "case_id": 2,
        "description": "Unbalanced binary tree (deep on one side)"
    },
    {
        "method": "isBalanced",
        "root": [],
        "expected": True,
        "case_id": 3,
        "description": "Empty tree (considered balanced)"
    },
    {
        "method": "isBalanced",
        "root": [1],
        "expected": True,
        "case_id": 4,
        "description": "Single node tree (considered balanced)"
    },
    {
        "method": "isBalanced",
        "root": [1, 2, None, 3, None, 4, None, 5],
        "expected": False,
        "case_id": 5,
        "description": "Unbalanced skewed tree (left side)"
    },
    {
        "method": "isBalanced",
        "root": [1, None, 2, None, 3, None, 4, None, 5],
        "expected": False,
        "case_id": 6,
        "description": "Unbalanced skewed tree (right side)"
    },
    {
        "method": "isBalanced",
        "root": [1, 2, 2, 3, None, None, 3, 4, None, None, 4],
        "expected": False,
        "case_id": 7,
        "description": "deeper"
    }
]

run_tests()
