from test.test_suite import run_tests

# 145. Binary Tree Postorder Traversal
#
# Given the `root` of a binary tree, return the postorder traversal of its nodes' values.
#
# ### Constraints:
# - The number of the nodes in the tree is in the range `[0, 100]`.
# - `-100 <= Node.val <= 100`
#
# ### Example 1:
# Input: root = [1,null,2,3]
# Output: [3,2,1]
#
# ### Example 2:
# Input: root = []
# Output: []
#
# ### Example 3:
# Input: root = [1]
# Output: [1]


from typing import *
from libs.tree import TreeNode


# LeetCode的TreeNode实现是标准的可变对象
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if not root: return []
        results = []
        self.postorder(root, results)
        return results

    def postorder(self, node: Optional[TreeNode], results: list):
        if not node: return

        self.postorder(node.left, results)
        self.postorder(node.right, results)
        results.append(node.val)


test_cases = [
    {
        "method": "postorderTraversal",
        "root": [1, None, 2, 3],
        "expected": [3, 2, 1],
        "case_id": 1,
        "description": "Standard binary tree with left null"
    },
    {
        "method": "postorderTraversal",
        "root": [],
        "expected": [],
        "case_id": 2,
        "description": "Empty tree"
    },
    {
        "method": "postorderTraversal",
        "root": [1],
        "expected": [1],
        "case_id": 3,
        "description": "Single node tree"
    },
    {
        "method": "postorderTraversal",
        "root": [1, 2, 3, 4, 5, 6, 7],
        "expected": [4, 5, 2, 6, 7, 3, 1],
        "case_id": 4,
        "description": "Complete binary tree with multiple levels"
    },
    {
        "method": "postorderTraversal",
        "root": [1, None, 2, None, 3, None, 4],
        "expected": [4, 3, 2, 1],
        "case_id": 6,
        "description": "Skewed right leaning binary tree"
    }, {
        "method": "postorderTraversal",
        "root": [1, 2, None, 3, None, 4, None],
        "expected": [4, 3, 2, 1],
        "case_id": 5,
        "description": "Skewed left leaning binary tree"
    },
    {
        "method": "postorderTraversal",
        "root": [5, 1, 4, None, None, 3, 6],
        "expected": [1, 3, 6, 4, 5],
        "case_id": 7,
        "description": "Unbalanced binary tree"
    }
]

run_tests()
