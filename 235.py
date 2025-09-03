# 235.py
from test.test_suite import run_tests

from typing import Optional
from libs.tree import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


test_cases = [
    {
        "method": "lowestCommonAncestor",
        "root": [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5],
        "p": 2,
        "q": 8,
        "expected": 6,
        "case_id": 1,
        "description": "Standard BST with LCA at root"
    },
    {
        "method": "lowestCommonAncestor",
        "root": [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5],
        "p": 2,
        "q": 4,
        "expected": 2,
        "case_id": 2,
        "description": "LCA is one of the nodes (ancestor of itself)"
    },
    {
        "method": "lowestCommonAncestor",
        "root": [2, 1],
        "p": 2,
        "q": 1,
        "expected": 2,
        "case_id": 3,
        "description": "Small tree with parent-child relationship"
    },
    {
        "method": "lowestCommonAncestor",
        "root": [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5],
        "p": 0,
        "q": 5,
        "expected": 2,
        "case_id": 4,
        "description": "LCA deeper in the tree"
    },
    {
        "method": "lowestCommonAncestor",
        "root": [20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 27, 32, 40],
        "p": 3,
        "q": 7,
        "expected": 5,
        "case_id": 5,
        "description": "Larger balanced BST with LCA in left subtree"
    },
    {
        "method": "lowestCommonAncestor",
        "root": [4, 2, 6, 1, 3, 5, 7],
        "p": 1,
        "q": 3,
        "expected": 2,
        "case_id": 6,
        "description": "Symmetric perfect binary search tree"
    }
]

run_tests()
