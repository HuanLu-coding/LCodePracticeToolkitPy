# 112. Path Sum
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
#
# A leaf is a node with no children.
#
# ### Constraints:
# - The number of nodes in the tree is in the range `[0, 5000]`.
# - `-1000 <= Node.val <= 1000`
# - `-1000 <= targetSum <= 1000`
#
# ### Example 1:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.
#
# ### Example 2:
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.
#
# ### Example 3:
# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.

from test.test_suite import run_tests
from typing import *
from libs.tree import TreeNode


# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False
#
#         def backtrack(node: Optional[TreeNode], sum: int) -> bool:
#             sum += node.val
#
#             if not node.left and not node.right:
#                 return sum == targetSum
#
#             left_result = False
#             if node.left:
#                 left_result = backtrack(node.left, sum)
#                 if left_result:
#                     return True
#
#             right_result = False
#             if node.right:
#                 right_result = backtrack(node.right, sum)
#                 if right_result:
#                     return True
#
#             return False
#
#         return backtrack(root, 0)


#
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def backtrack(node: Optional[TreeNode], current_sum: int) -> bool:
            # 当前路径和
            current_sum += node.val

            # 叶子节点检查
            if not node.left and not node.right:
                return current_sum == targetSum

            # 左子树递归，传递返回值
            if node.left and backtrack(node.left, current_sum):
                return True

            # 右子树递归，传递返回值
            if node.right and backtrack(node.right, current_sum):
                return True

            # 未找到路径，返回 False
            return False

        return backtrack(root, 0)


test_cases = [
    {
        "method": "hasPathSum",
        "root": [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
        "targetSum": 22,
        "expected": True,
        "case_id": 1,
        "description": "Tree with path sum equal to targetSum"
    },
    {
        "method": "hasPathSum",
        "root": [1, 2, 3],
        "targetSum": 5,
        "expected": False,
        "case_id": 2,
        "description": "Tree with no path sum equal to targetSum"
    },
    {
        "method": "hasPathSum",
        "root": [],
        "targetSum": 0,
        "expected": False,
        "case_id": 3,
        "description": "Empty tree (edge case)"
    },
    {
        "method": "hasPathSum",
        "root": [1, 2],
        "targetSum": 1,
        "expected": False,
        "case_id": 4,
        "description": "Tree with only root and left child, sum not matching targetSum"
    },
    {
        "method": "hasPathSum",
        "root": [1],
        "targetSum": 1,
        "expected": True,
        "case_id": 5,
        "description": "Tree with only root node, equal to targetSum (edge case)"
    },
    {
        "method": "hasPathSum",
        "root": [-2, -3, -1],
        "targetSum": -5,
        "expected": True,
        "case_id": 6,
        "description": "Tree with negative values"
    },
    {
        "method": "hasPathSum",
        "root": [1, -2, 3],
        "targetSum": -1,
        "expected": True,
        "case_id": 7,
        "description": "Tree with mixed positive and negative values"
    },
    {
        "method": "hasPathSum",
        "root": [0, 1, 1],
        "targetSum": 1,
        "expected": True,
        "case_id": 8,
        "description": "Tree with root value of 0 (edge case)"
    }
]

run_tests()
