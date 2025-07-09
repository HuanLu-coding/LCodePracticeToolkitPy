# 226.py
# invert-binary-tree

from test.test_suite import run_tests

from typing import Optional

from libs.tree import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        def doInvertTree(node):
            if not node:
                return

            tmp_left = node.left
            node.left = doInvertTree(node.right)
            node.right = doInvertTree(tmp_left)
            return node

        doInvertTree(root)

        return root


# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         # Base Case: 如果当前节点为 None，则无需翻转，直接返回 None。
#         if not root:
#             return None
#
#         # 核心操作：交换当前节点的左右子节点。
#         root.left, root.right = root.right, root.left
#
#         # 递归步骤：分别对其新的左右子树进行翻转。
#         self.invertTree(root.left)
#         self.invertTree(root.right)
#
#         # 返回当前节点（其子树已被翻转）。
#         return root


test_cases = [
    {
        "method": "invertTree",
        "root": [4, 2, 7, 1, 3, 6, 9],
        "expected": [4, 7, 2, 9, 6, 3, 1],
        "case_id": 1,
        "description": "Standard balanced binary tree"
    }, {
        "method": "invertTree",
        "root": [2, 1, 3],
        "expected": [2, 3, 1],
        "case_id": 2,
        "description": "Small binary tree with three nodes"
    }, {
        "method": "invertTree",
        "root": [],
        "expected": [],
        "case_id": 3,
        "description": "Empty tree"
    }, {
        "method": "invertTree",
        "root": [1],
        "expected": [1],
        "case_id": 4,
        "description": "Single node tree"
    }, {
        "method": "invertTree",
        "root": [1, 2],
        "expected": [1, None, 2],
        "case_id": 5,
        "description": "Tree with only left child"
    }, {
        "method": "invertTree",
        "root": [1, None, 2],
        "expected": [1, 2, None],
        "case_id": 6,
        "description": "Tree with only right child"
    }, {
        "method": "invertTree",
        "root": [1, 2, 3, 4, 5, 6, 7],
        "expected": [1, 3, 2, 7, 6, 5, 4],
        "case_id": 7,
        "description": "Complete binary tree with multiple levels"
    }
]

run_tests()
