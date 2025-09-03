# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Example 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#
# Example 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

from test.test_suite import run_tests
from typing import List, Optional
from libs.tree import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pass


test_cases = [
    {
        "method": "buildTree",
        "preorder": [3, 9, 20, 15, 7],
        "inorder": [9, 3, 15, 20, 7],
        "expected": [3, 9, 20, None, None, 15, 7],
        "case_id": 1,
        "description": "Standard binary tree with left and right subtrees"
    }, {
        "method": "buildTree",
        "preorder": [1, 2],
        "inorder": [1, 2],
        "expected": [1, None, 2],
        "case_id": 2,
        "description": "Tree with only right child"
    },
    {
        "method": "buildTree",
        "preorder": [1, 2],
        "inorder": [2, 1],
        "expected": [1, 2, None],
        "case_id": 3,
        "description": "Tree with only left child"
    },
    {
        "method": "buildTree",
        "preorder": [1],
        "inorder": [1],
        "expected": [1],
        "case_id": 4,
        "description": "Single node tree"
    },
    {
        "method": "buildTree",
        "preorder": [1, 2, 4, 5, 3, 6, 7],
        "inorder": [4, 2, 5, 1, 6, 3, 7],
        "expected": [1, 2, 3, 4, 5, 6, 7],
        "case_id": 5,
        "description": "Complete balanced binary tree"
    },
    {
        "method": "buildTree",
        "preorder": [1, 2, 3, 4, 5],
        "inorder": [5, 4, 3, 2, 1],
        "expected": [1, 2, None, 3, None, 4, None, 5, None],
        "case_id": 6,
        "description": "Left-skewed tree (edge case)"
    }, {
        "method": "buildTree",
        "preorder": [1, 2, 3, 4, 5, 6],
        "inorder": [6, 5, 4, 3, 2, 1],
        "expected": [1, 2, None, 3, None, 4, None, 5, None, 6, None],
        "case_id": 7,
        "description": "Deeply left-skewed tree (edge case)"
    }, {
        "method": "buildTree",
        "preorder": [5, 4, 3, 2, 1],
        "inorder": [1, 2, 3, 4, 5],
        "expected": [5, 4, None, 3, None, 2, None, 1, None],
        "case_id": 8,
        "description": "Right-skewed tree (edge case)"
    }
]

run_tests()
